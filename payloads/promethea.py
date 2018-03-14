#!/usr/bin/python
import numpy
from random import random
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils
from sys import argv
from sys import stdout
from sys import exit
import model
from model import PasswordLSTM

"""
Promethea - a mysical female half-god who walks between the real and the immateira 
	(the realm of the idealistic real) granting man kind access to this magical realm that makes anything possible.
	
	Promethea is meant to be a simple front end to making use of the LSTM stuff to plugin into other tools
	like Burp, ZapProxy, Terminal etc all you do is call this script give it a payload and it returns the autocomplete
	according to the way you trained it and the weight file you give it. 	

	class Promethea:
		def __init__(self,payload_filename, - name of file with the payloads used to train
				  weights_filename, - name of file with trained up weights in 
				  payload,          - stirng of charaters for the seed of predicition
				  nchars	    - number of characters to predict):
Fuzzing with Promethea:
	1 - payload "autocomplete" mode (here's some input that is well formed, what do you think would be a good
		way to complete this IF IT WERE a payload actually?)
	2 - blind payload generation (just spit out what you know to spit out) 

"""
class Promethea:
	def __init__(self,payload_filename,weights_filename,payload,nchars):
		self.payload_filename = payload_filename
		self.weights_filename = weights_filename

		self.prep_data(self.payload_filename,payload)	
		self.init_payload = self.payload

		self.lstm = PasswordLSTM(self.X,self.y)
		self.lstm.load_weights(weights_filename)	

		self.predict_length = nchars
	"""
		Returns next character in sequence prediction
	
		Args: 
			current_sequence (char) - sequence to predict from
		Returns:
			(char) - next character in sequence
	"""
	def predict(self):
		return self.get_next(self.init_payload)
	def get_next(self,seed):
		outstring = ""
		for i in range(self.predict_length):
			x = numpy.reshape(seed,(1,len(seed),1))
			x = x / float(self.n_vocab)
			prediction = self.lstm.predict(x,verbose=0)
			index = numpy.argmax(prediction)

			result  = self.int_to_char[index]
			outstring = outstring + result
			seed.append(index)
			seed = seed[1:len(seed)]	
	
		return outstring
	
	"""
		prep_data(data_filename,
				payload)

		Prepares the data to feed to the nextwork for prediction
		The Keras Sequential model needs a presentation of the vocab we taught it to generate from, 
		essentially it only spits out character positions in a table of all possible characters - so if you want
		her to speak payloads you need to give her that list of chars she as trained on. 
	
		Args:
			input_file (string) - list of payloads promethea was trained on (we might move over to a simpler 
			vocab reload mechanism perhaps since this is annoying)
		Returns:
			(x <list>) - x a hot encoding of the vocabulary holding initial character sequences
	"""
	def prep_data(self,data_filename,payload):
		
		seq_length = model.SEQ_LEN #need to make this SEQ_LEN an LSTM attribute rather than model level one

		raw_text = open(data_filename).read()
		self.chars = sorted(list(set(raw_text)))
		self.n_chars = len(raw_text)
		self.n_vocab = len(self.chars)
		
		self.int_to_char = dict((i,c) for i,c in enumerate(self.chars))	
		self.char_to_int = dict((c,i) for i,c in enumerate(self.chars))
		self.payload = [self.char_to_int[char] for char in payload] 	
		dataX = []
		dataY = []
		
		for i in range(self.n_chars - seq_length):
			seq_in = raw_text[i:i + seq_length]
			seq_out = raw_text[i + seq_length]
			dataX.append([self.char_to_int[char] for char in seq_in])
			dataY.append(self.char_to_int[seq_out])
					
		self.n_patterns = len(dataX)
			
		X = numpy.reshape(dataX,(self.n_patterns,seq_length,1))
		self.X = X / float(self.n_vocab)
		self.y = np_utils.to_categorical(dataY)	
		
if __name__=="__main__":
	seq_length = model.SEQ_LEN

	#ill modularize this eventually	
	if len(argv) != 5:
		print "Usage: %s [payload] [nchars] [data file] [weights filename]" % (argv[0])
		print "Example: %s 'PHPSESSIONID=' 100 awesome_polyglots.txt weights-for-generating-xss-payloads.txt" % (argv[0])
		print "Example: %s 'widget.php?username=' 100 more_polyglots.txt weights-for-generating-phpxss.txt" % (argv[0])
		exit(1)

	payload = argv[1]
	print "[*] Seed: '%s'\n" % payload
	nchars = int(argv[2])
	data_filename = argv[3]
	#generate using LSTM network
	weights_filename = argv[4]

	promethea = Promethea(data_filename,weights_filename,payload,nchars)
	print promethea.predict()
	
