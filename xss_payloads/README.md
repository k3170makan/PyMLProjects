# Generating XSS Payloads with an LSTM (PHASE 0)

Using an LSTM to learn how to generate XSS payloads like the best of them.
The purpose here is to see if there is a unique design of LSTM that suits XSS payloads better
as well as learning to adapt LSTM to the XSS injection problem.

the idea is that you train an LSTM on a sample of payloads, once you have it trained well enough
you can feed it an injection point i.e. the HTML before your injection point and it will generate
payload based on what it was trained on. i.e. 

if you give it a `<a href =` 
it should spit out something like `JavaScriPT:aLert(11111111111111111111/**/)`


## Research Phases:

* phase 0 : make the code work 
* phase 1 : develope working/trainable model aim for lowest possible loss
* phase 2 : plug this into Burp, make it free and open to piss people off 
* phase 3 : plug it into the internet and monitor for new payloads

## How to use

The project includes two scripts :

* `fit_train.py`  used to train the neural net on a set of payloads, this produces a set of weights.
* `generate.py` used to generate payloads based on a trained set of weights.  

### Training the Neural Net
In order to produce some AI that can already generate payloads based on a sample, the easiest way to do this
is to feed the password list to the `learn_passwords.py` script as follows:

```
$>./fit_train.py 
Using TensorFlow backend.
Usage: ././fit_train.py [data file] [sequence length] [epochs] [batch size]

$>./fit_train.py ./xss_payloads_50.txt 150 100 50
Using TensorFlow backend.
[**] data set stats [**]
[*] patterns '5428'
[*] total vocab '5578' 
[*] total characters '5578' 
Epoch 1/100

```

This will produce a list of weights files (used to set up the neural net from scratch if you need to use it later):

```
-rw-rw-r-- 1 k3170makan k3170makan 2463936 Jul 25 18:22 seq-100-weights-improvement-44-2.0382.hdf5
-rw-rw-r-- 1 k3170makan k3170makan 2463936 Jul 25 18:24 seq-100-weights-improvement-45-2.0002.hdf5
-rw-rw-r-- 1 k3170makan k3170makan 2463936 Jul 25 18:26 seq-100-weights-improvement-46-1.9580.hdf5
-rw-rw-r-- 1 k3170makan k3170makan 2463936 Jul 25 18:28 seq-100-weights-improvement-47-1.9290.hdf5
-rw-rw-r-- 1 k3170makan k3170makan 2463936 Jul 25 18:30 seq-100-weights-improvement-48-1.9157.hdf5
-rw-rw-r-- 1 k3170makan k3170makan 2463936 Jul 25 18:32 seq-100-weights-improvement-49-1.8796.hdf5
```

### Generating Payloads
In order to generate passwords you need to run the `generate_passwords.py` script, here's how to do that

```
TODO: [ADD GENERATE TUTOIRAL]
```
*some stderr output has been supressed, tensor flow and keras like to make a lot of noise hehe

## Dependencies

The only thing you need to get this up and running is a working python install and whatever else you need to run Keras, smoothly.
Python Keras : https://keras.io/ 


## Further Reading and Similar ideas:
* TODO: [ADD READING LIST]

