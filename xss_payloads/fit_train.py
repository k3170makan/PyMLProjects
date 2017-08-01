#!/usr/bin/python
import numpy
from sys import argv,exit
from data import DATA_LIB
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense,Activation,Dropout,LSTM,Flatten
from keras.callbacks import ModelCheckpoint

def build(input_shape, output_shape):
	model = Sequential()
	model.add(LSTM(256,input_shape=input_shape,return_sequences=True)) #input layer
	model.add(Dropout(0.2))
	#model.add(LSTM(256))
	#model.add(Dropout(0.2))
	model.add(Flatten())
	model.add(Dense(output_shape,activation='softmax'))
	model.compile(loss='categorical_crossentropy',optimizer='adam')

	return model
def fit(dataset, model, epochs, batch_size):
	X,Y = dataset[0],dataset[1]

	filepath="128-drop-dense_weights-improvement-{epoch:02d}-{loss:.4f}.hdf5"
	checkpoint = ModelCheckpoint(filepath,monitor='loss',verbose=1,save_best_only=True,mode='min',period=120)
	callback_list = [checkpoint]

	model.fit(X,Y,epochs=epochs,batch_size=batch_size,callbacks=callback_list)	
	return #should there be a return value here? 
def evaluate(model,dataset):
	X,Y = dataset[0],dataset[1]

	return model.evaluate(X,Y)
def predict(model,dataset):
	X,Y = dataset[0],dataset[1]

	return ""
def build_dataset(filename,sequence_length):
	raw_text = open(filename).read()
	chars = sorted(list(raw_text))
	
	char_to_int = dict((c,i) for i,c in enumerate(chars))		
	n_chars = len(raw_text)
	n_vocab = len(chars)

	seq_length = sequence_length

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
	X = numpy.reshape(dataX,(n_patterns,seq_length,1))
	X = X/float(n_vocab) #seems like a normalization of the vector weights?
	
	y = np_utils.to_categorical(dataY)


	print "[**] data set stats [**]"
	print "[*] patterns '%d'" % (n_patterns)
	print "[*] total vocab '%d' " % (n_vocab)	
	print "[*] total characters '%d' " % (n_chars)

	return X,y
if __name__=="__main__":
	
	if len(argv) < 4:
		print "Usage: ./%s [data file] [sequence length] [epochs] [batch size]" % (argv[0])
		exit(1)

	data_filename = argv[1]	
	sequence_length = int(argv[2])
	epochs = int(argv[3])
	batch_size = int(argv[4])	
	
	dataset = build_dataset(data_filename,sequence_length)
	model = build((dataset[0].shape[1],dataset[0].shape[2]),(dataset[1].shape[1]))
	fit(dataset,model,epochs,batch_size)
	#scores = evaluate(model,dataset)

