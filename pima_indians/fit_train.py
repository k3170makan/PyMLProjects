import numpy
from data import DATA_LIB
from keras.models import Sequential
from keras.layers import Dense

def build():
	model = Sequential()
	model.add(Dense(12,input_dim='8',activation='relu')) #input layer
	model.add(Dense(8,activation='relu')) #hidden layer
	model.add(Dense(1,activation='sigmoid')) #output layer
	#could handle errors here in isolation ;)	
	model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
	return model
def fit(dataset, model):
	X = dataset[:,0:8] #get first 8 fields
	Y = dataset[:,8] #use 9th field as output 1 0r 0

	mode.fit(X,Y,epochs=150,batch_size=10)	
	return #should there be a return value here? 
def evaluate(model):
	#get the metrics on the accuracy
	return
if __name__=="__main__":
	dataset = numpy.loadtxt(DATA_LIB,delimiter=",")
	

