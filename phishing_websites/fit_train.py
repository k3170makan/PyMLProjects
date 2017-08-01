#!/usr/bin/python
import numpy
from data import DATA_LIB
from keras.models import Sequential
from keras.layers import Dense,Activation,Dropout
from keras.callbacks import ModelCheckpoint

def build():
	model = Sequential()
	model.add(Dense(9,input_dim=9,activation='tanh')) #input layer
	model.add(Dense(5,activation='tanh')) #hidden layer
	model.add(Dense(1,activation='softsign')) #output layer
	#could handle errors here in isolation ;)	
	model.compile(loss='logcosh',optimizer='adam',metrics=['accuracy'])
	return model
def fit(dataset, model):
	X = dataset[:,0:9] #get first 7 fields
	Y = dataset[:,9] #use 9th field as output 1 0r 0

	filepath="9-5-1_weights-improvement-{epoch:02d}-{loss:.4f}.hdf5"
	checkpoint = ModelCheckpoint(filepath,monitor='loss',verbose=1,save_best_only=True,mode='min',period=120)
	callback_list = [checkpoint]


	model.fit(X,Y,epochs=800,batch_size=100,callbacks=callback_list)	
	return #should there be a return value here? 
def evaluate(model,dataset):
	X = dataset[:,0:9]	
	Y = dataset[:,9]	
	return model.evaluate(X,Y)
def predict(model,dataset):
	X = dataset[:,0:9]
	Y = dataset[:,9]
	predictions = model.predict(X)
	rounded = [round(x[0]) for x in predictions]
	return rounded
if __name__=="__main__":
	dataset = numpy.loadtxt(DATA_LIB,delimiter=",")
	model = build()
	fit(dataset,model)
	scores = evaluate(model,dataset)
	print "[*] %s %.2f%%" % (model.metrics_names[1],scores[1]*100)	
	print "[*] output: ",predict(model,dataset)
