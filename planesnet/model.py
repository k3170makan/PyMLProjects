#!/usr/bin/python
from keras.layers import Activation,Dropout,Flatten,Dense,Conv2D,MaxPooling2D
from keras.callbacks import EarlyStopping, TensorBoard, ModelCheckpoint
from keras.models import Sequential
from datetime import datetime
import numpy as np
PATIENCE = 10
LOG_DIR_ROOT = "."

N_LAYERS = 4
MIN_NEURONS = 20
MAX_NEURONS = 120
KERNEL = (3,3)

EPOCHS = 150
BATCH_SIZE = 200

class PlaneCNN:
	def __init__(self,shape=(None),n_layers=N_LAYERS):
		self.shape = shape
		self.n_layers = n_layers	
		self.model = None
	def build(self):
		steps = np.floor(MAX_NEURONS / (self.n_layers + 1))
		neurons = np.arange(MIN_NEURONS, MAX_NEURONS, steps)
		neurons = neurons.astype(np.int32)
		
		self.model = Sequential()
		
		for i in range(0,self.n_layers):
			if i == 0:
				self.model.add(Conv2D(neurons[i],KERNEL,input_shape=(self.shape[0],self.shape[1],self.shape[2])))
			else:
				self.model.add(Conv2D(neurons[i],KERNEL))

			self.model.add(Activation('relu'))

		#max pooling layer
		self.model.add(MaxPooling2D(pool_size=(2,2)))
		self.model.add(Flatten())
		self.model.add(Dense(MAX_NEURONS))
		self.model.add(Activation('relu'))
		
		#output
		self.model.add(Dense(1))
		self.model.add(Activation('sigmoid'))	

		self.model.compile(loss="binary_crossentropy",\
						optimizer="adam",\
						metrics=["accuracy"])

	def init_logging_callbacks(self,log_dir=LOG_DIR_ROOT):

		self.checkpoint = ModelCheckpoint(filepath="%s/weights-improvement-{epoch:02d}-{loss:.4f}.hdf5" % (log_dir),\
														monitor='loss',\
														verbose=1,\
														save_best_only=True,\
														mode='min')

		self.early_stopping = EarlyStopping(monitor='loss',\
													min_delta=0,\
													patience=PATIENCE,\
													verbose=0,\
													mode='auto')	

		now = datetime.utcnow().strftime("%Y%m%d%H%M%S")	
		log_dir = "{}/run/{}".format(LOG_DIR_ROOT,now)
		self.tensorboard = TensorBoard(log_dir=log_dir,\
											write_graph=True,\
											write_images=True)
		
		self.callbacks = [self.early_stopping,\
								self.tensorboard,\
								self.checkpoint]	
	def fit(self,x,y):
		self.init_logging_callbacks()

		self.build()
		self.model.fit(x,\
							y,\
							epochs=EPOCHS,\
							batch_size=BATCH_SIZE,\
							callbacks=self.callbacks,\
							verbose=1)		

	def load_weights(self,weights=None):
		if not self.model:
			self.build()
		if weights:
			self.model.load_weights(weights)
	def predict(self,x_input=None):
		return self.model.predict(x=x_input,verbose=0)

	def evaluate(self,x_test):
		test_preds = self.model.predict(x_test)
		return np.round(test_preds)
