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
* 
"""
if __name__=="__main__":
	seq_length = model.SEQ_LEN

	#ill modularize this eventually	
	if len(argv) != 3:
		print "Usage: %s [data file] [weights filename]" % (argv[0])
		exit(1)
	data_filename = argv[1]

	raw_text = open(data_filename).read()
	#raw_text = raw_text.lower() <--- removed lower conversion! accidentally left that in form alice in wonder land 0_o
	
	chars = sorted(list(set(raw_text)))
	n_chars = len(raw_text)
	n_vocab = len(chars)
	
	int_to_char = dict((i,c) for i,c in enumerate(chars))	
	char_to_int = dict((c,i) for i,c in enumerate(chars))
	
	print "[*] Total Characters:", n_chars
	print "[*] Total Vocab:", n_vocab

	dataX = []
	dataY = []
	
	for i in range(n_chars - seq_length):
		#selection
		seq_in = raw_text[i:i + seq_length]
		seq_out = raw_text[i + seq_length]
		#select data form, to make this more readable i should encapsulate it in methods	
		dataX.append([char_to_int[char] for char in seq_in])
		dataY.append(char_to_int[seq_out])
				
	n_patterns = len(dataX)
	print "[*] Total Patterns:", n_patterns
	
	X = numpy.reshape(dataX,(n_patterns,seq_length,1))
	X = X / float(n_vocab)
	y = np_utils.to_categorical(dataY)	

	#generate using LSTM network
	weights_filename = argv[2]

	model = PasswordLSTM(X,y)
	model.load_weights(weights_filename)	
		
	start = numpy.random.randint(0,len(dataX) - 1)
	pattern = dataX[start]
	seed = ''.join([int_to_char[value] for value in pattern]), " "
	print "[*] Seed: '%s'\n" % seed[0]
	outstring = ""	
	for i in range(5000):


		x = numpy.reshape(pattern,(1,len(pattern),1))
		x = x / float(n_vocab)
		prediction = model.predict(x,verbose=0)
		index = numpy.argmax(prediction)
		result  = int_to_char[index]

		outstring = outstring + result
		#stdout.write("%s" % result)		
		pattern.append(index)
		pattern = pattern[1:len(pattern)]	

		if len(outstring) >= 200:
			start = numpy.random.randint(0,len(dataX) - 1)
			pattern = dataX[start]
			stdout.write("%s\n" % outstring)
			outstring = ""
	print "\n[*] done"
