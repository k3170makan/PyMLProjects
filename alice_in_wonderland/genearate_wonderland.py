#!/usr/bin/python
import numpy
from data import DATA_LIB
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils
from sys import argv
from sys import stdout
from sys import exit
if __name__=="__main__":
	#ill modularize this eventually	
	if len(argv) != 2:
		print "Usage: %s [weights filename]" % (argv[0])
		exit(1)
	data_filename = DATA_LIB+"/11-0.txt"
	raw_text = open(data_filename).read()
	raw_text = raw_text.lower()
	
	chars = sorted(list(set(raw_text)))
	n_chars = len(raw_text)
	n_vocab = len(chars)
	
	int_to_char = dict((i,c) for i,c in enumerate(chars))	
	char_to_int = dict((c,i) for i,c in enumerate(chars))
	
	print "Total Characters:", n_chars
	print "Total Vocab:", n_vocab

	seq_length = 100
	dataX = []
	dataY = []
	
	for i in range(0,n_chars - seq_length, 1):
		#selection
		seq_in = raw_text[i:i + seq_length]
		seq_out = raw_text[i + seq_length]
		#select data form, to make this more readable i should encapsulate it in methods	
		dataX.append([char_to_int[char] for char in seq_in])
		dataY.append(char_to_int[seq_out])
				
	n_patterns = len(dataX)
	print "Total Patterns:", n_patterns
	
	X = numpy.reshape(dataX,(n_patterns,seq_length,1))
	X = X / float(n_vocab)
	y = np_utils.to_categorical(dataY)	
	#generate using LSTM network
	weights_filename = argv[1]
	
	model = Sequential()
	model.add(LSTM(256,input_shape=(X.shape[1],X.shape[2])))
	model.add(Dropout(0.2))
	model.add(Dense(y.shape[1],activation='softmax'))
	model.load_weights(weights_filename)

	start = numpy.random.randint(0,len(dataX) - 1)
	pattern = dataX[start]
	seed = ''.join([int_to_char[value] for value in pattern]), " "
	print "[*] pattern:",pattern
	print "[*] Seed: ", seed
	
	for i in range(1000):
		x = numpy.reshape(pattern,(1,len(pattern),1))
		x = x / float(n_vocab)
		prediction = model.predict(x,verbose=0)
		index = numpy.argmax(prediction)
		result  = int_to_char[index]
		stdout.write(result)
		pattern.append(index)
		pattern = pattern[1:len(pattern)]	
	print "[*] done"


