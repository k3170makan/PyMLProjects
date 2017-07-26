#!/usr/bin/python
from data import DATA_LIB
import numpy
from sys import argv
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils
SEQ_LEN = 100
if __name__=="__main__":
	#load the raw ascii text
	filename = argv[1]
	raw_text = open(filename).read()
	raw_text = raw_text.lower()
	
	chars = sorted(list(set(raw_text)))
	print chars
	char_to_int = dict((c,i) for i,c in enumerate(chars))
	
	n_chars = len(raw_text)
	n_vocab = len(chars)
	print "[*] Total Characters:", n_chars
	print "[*] Total Vocab:", n_vocab

	seq_length = SEQ_LEN
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
	print "[*] Total Patterns:", n_patterns

	X = numpy.reshape(dataX,(n_patterns,seq_length,1))
	X = X/float(n_vocab) #seems like a normalization of the vector weights?
	
	y = np_utils.to_categorical(dataY)

	print X.shape[1],X.shape[2]
	print y.shape[1]
	model = Sequential()
	model.add(LSTM(256,input_shape=(X.shape[1],X.shape[2]),return_sequences=True))
	model.add(Dropout(0.2))
	model.add(LSTM(256))
	model.add(Dropout(0.2))
	model.add(Dense(y.shape[1],activation='softmax'))
	model.compile(loss='categorical_crossentropy',optimizer='adam')

	filepath="seq-%d-weights-improvement-{epoch:02d}-{loss:.4f}.hdf5" % (SEQ_LEN)
	checkpoint = ModelCheckpoint(filepath,monitor='loss',verbose=1,save_best_only=True,mode='min')
	callback_list = [checkpoint]
	#fit the model
	print "[*] training model..." 
	model.fit(X,y,epochs=50, batch_size=50,callbacks=callback_list) 	
