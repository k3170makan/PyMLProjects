#!/usr/bin/python
import glob
import hashlib
from time import sleep
import numpy as np
import os.path as path
from scipy import misc
from sys import exit,argv,stdout
from optparse import OptionParser
import matplotlib.pyplot as plt

import model

def visualize_data(positive_images,negative_images):

	figure = plt.figure()
	count = 0
	for i in range(positive_images.shape[0]):
		count += 1
		figure.add_subplot(2,positive_images.shape[0],count)
		plt.imshow(positive_images[i,:,:])
		plt.axis('off')
		plt.title("1")
		
		figure.add_subplot(1,negative_images.shape[0],count)	
		plt.imshow(negative_images[i,:,:])
		plt.axis('off')
		plt.title("0")
	plt.show()		

if __name__=="__main__":
	parser = OptionParser()
	parser.add_option("-w",\
							"--weights",\
							help="path to image files",\
							type="string",\
							dest="weights_path")


	parser.add_option("-i",\
							"--input_image",\
							help="path to image files",\
							type="string",\
							dest="image_path")

	options, arguments = parser.parse_args()
	image_path = options.image_path
	weights_path = options.weights_path

	#print("[*] Starting data processing ...")
	#maybe figure out multiple image types
	#print file_paths	
	images = [misc.imread(_path) for _path in [image_path]]	
	#print "[*] converting images: ",type(images),type(images[0]),"-->",
	images = np.asarray(images)
	#print images.shape	
	image_size = np.asarray([images.shape[1],images.shape[2],images.shape[3]])
	#print("[*] images size :%s" % (image_size))	
	images = images / 255.0
	n_images = images.shape[0]
	x_train = images
	
	cnn = model.PlaneCNN(shape=image_size)
	cnn.load_weights(weights=weights_path)
	print cnn.predict(x_input=x_train)[0][0]

	"""	
	N_TO_VISUALIZE = 10
	positive_example_indices = (y_train == 1)
	positive_examples = x_train[positive_example_indices,:,:]
	positive_examples = positive_examples[0:N_TO_VISUALIZE,:,:]
	

	negative_example_indices = (y_train == 0)
	negative_examples = x_train[negative_example_indices,:,:]	
	negative_examples = negative_examples[0:N_TO_VISUALIZE,:,:]

	visualize_data(positive_examples,negative_examples)
		
	"""
	
	
