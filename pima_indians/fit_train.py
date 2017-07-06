#!/usr/bin/python
import numpy
from data import DATA_LIB
from keras.models import Sequential
from keras.layers import Dense

def build():
	model = Sequential()
	model.add(Dense(12,input_dim=8,activation='relu')) #input layer
	model.add(Dense(8,activation='relu')) #hidden layer
	model.add(Dense(1,activation='sigmoid')) #output layer
	#could handle errors here in isolation ;)	
	model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
	return model
def fit(dataset, model):
	X = dataset[:,0:8] #get first 8 fields
	Y = dataset[:,8] #use 9th field as output 1 0r 0

	model.fit(X,Y,epochs=150,batch_size=10)	
	return #should there be a return value here? 
def evaluate(model,dataset):
	X = dataset[:,0:8]	
	Y = dataset[:,8]	
	return model.evaluate(X,Y)
def predict(model,dataset):
	X = dataset[:,0:8]
	Y = dataset[:,8]
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

