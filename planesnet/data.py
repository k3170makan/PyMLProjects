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
	parser.add_option("-e",\
							"--extension",\
							help="file extension",\
							type="string",\
							dest="file_extension")	
	parser.add_option("-p",\
							"--path",\
							help="path to image files",\
							type="string",\
							dest="file_path")

	options, arguments = parser.parse_args()
	file_extension = options.file_extension
	file_path = options.file_path
	print("[*] Starting data processing ...")
	#maybe figure out multiple image types
	file_paths = glob.glob(path.join(file_path,\
												"*.%s" % (file_extension)))
	file_paths = file_paths[:len(file_paths)/2]
	#print file_paths	
	images = [misc.imread(_path) for _path in file_paths]	
	print "[*] converting images: ",type(images),type(images[0]),"-->",
	images = np.asarray(images)
	print images.shape	
	image_size = np.asarray([images.shape[1],images.shape[2],images.shape[3]])
	print("[*] images size :%s" % (image_size))	

	images = images / 255.0
	
	n_images = images.shape[0]
	labels = np.zeros(n_images)
	for i in range(n_images):
		#print "[{0}]{1}\r".format([i],file_paths[i])
		filename = path.basename(file_paths[i])
		labels[i] = int(filename[0]) #this is because the images are marked with 1s and 0s in the file names
	print ("[*] labels ->",type(labels))
	TRAIN_TEST_SPLIT = 0.9
	
	split_index = int(TRAIN_TEST_SPLIT * n_images)

	shuffled_indices = np.random.permutation(n_images)
	
	train_indices = shuffled_indices[0:split_index]
	test_indices = shuffled_indices[split_index:]
	
	x_train = images[train_indices,:,:]
	y_train = labels[train_indices]
	
	x_test = images[test_indices,:,:]
	y_test = labels[test_indices]
	
	print ("[*]	network input : %s %s [%s]" % (type(x_train),type(x_train[0]),x_test.shape))
	cnn = model.PlaneCNN(shape=image_size)
	cnn.fit(x_train,y_train)	

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
	
	
