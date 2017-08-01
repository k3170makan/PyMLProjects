# Classifying Phishing Websties (Tutorial)

The following python script uses a simple 3 layer densely connected neural net in
order to determine if a given url sample is most probably for a phishing site. 

The example here is merely just a cool example of how to use a neural net for cool
infosec stuff. As well as a little Neural net "hello world" for keras. 

# Training Neural Net 

In order to train the neural net all you need to do is run 
```
$>./fit_train.py 
Using TensorFlow backend.
Epoch 1/800
1353/1353 [==============================] - 0s - loss: 0.4188 - acc: 0.0761     
Epoch 2/800
1353/1353 [==============================] - 0s - loss: 0.3700 - acc: 0.0761     
Epoch 3/800
1353/1353 [==============================] - 0s - loss: 0.3294 - acc: 0.0761     
Epoch 4/800
1353/1353 [==============================] - 0s - loss: 0.3001 - acc: 0.0761     
Epoch 5/800
1353/1353 [==============================] - 0s - loss: 0.2792 - acc: 0.0761     

```

if done correctly it should produce a set of weights files that look like this:

```
-rw-rw-r-- 1 k3170makan k3170makan 22976 Jul 28 16:42 9-5-1_weights-improvement-119-0.1050.hdf5
-rw-rw-r-- 1 k3170makan k3170makan 22976 Jul 28 16:42 9-5-1_weights-improvement-239-0.0913.hdf5
-rw-rw-r-- 1 k3170makan k3170makan 22976 Jul 28 16:42 9-5-1_weights-improvement-359-0.0860.hdf5
-rw-rw-r-- 1 k3170makan k3170makan 22976 Jul 28 16:42 9-5-1_weights-improvement-479-0.0835.hdf5
-rw-rw-r-- 1 k3170makan k3170makan 22976 Jul 28 16:42 9-5-1_weights-improvement-599-0.0803.hdf5
-rw-rw-r-- 1 k3170makan k3170makan 22976 Jul 28 16:43 9-5-1_weights-improvement-719-0.0791.hdf5

```
# Reading and References
* https://archive.ics.uci.edu/ml/datasets/Website+Phishing  
