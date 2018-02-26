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
#added this so i can fiddel around with the model from one place
SEQ_LEN = 12
class PasswordLSTM:
	def __init__(self,X,y):
		#pull some configs 
		self.SEQ_LEN = SEQ_LEN
		self.X = X
		self.y = y	
		self.input_shape = (X.shape[1],X.shape[2])
		self.filepath="seq-%d-weights-improvement-{epoch:02d}-{loss:.4f}.hdf5" % (self.SEQ_LEN)
		self.epochs = 50
		self.batch_size = 50
		self.monitor = 'loss'
		self.verbose = 1
		self.save_best_only=True
		self.mode='min'
		self.checkpoint = None
		self.model = Sequential()
		self.model_built = False

	def build_model(self):
		self.model = Sequential()
		self.model.add(LSTM(512,input_shape=self.input_shape,return_sequences=True))
		self.model.add(Dropout(0.2))	
		self.model.add(LSTM(512))
		self.model.add(Dropout(0.2))

		self.model.add(Dense(self.y.shape[1],activation='softmax'))
		self.model.compile(loss='categorical_crossentropy',optimizer='adam')
		self.model_built = True
	def predict(self,x,verbose):
		return self.model.predict(x,verbose=verbose)	
	def load_weights(self,filename):
		if (self.model_built != True):
			self.build_model()	
		self.model.load_weights(filename)	
	def fit(self):
		print "[*] training model..." 
		self.checkpoint = ModelCheckpoint(filepath=self.filepath,monitor=self.monitor,verbose=self.verbose,save_best_only=self.save_best_only,mode=self.mode)
		self.model.fit(self.X,self.y,epochs=self.epochs,batch_size=self.batch_size,callbacks=[self.checkpoint])
