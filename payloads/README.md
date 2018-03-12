# Generating XSS Payloads from Polyglot Files using Deep Learning

## How to use
The project includes two scripts

* `learn_payloads.py`  used to train the neural net on a set of payloads, this produces a set of weights.
* `generate_payloads.py` used to generate payloads based on a trained set of weights.  

### Training the Neural Net
In order to get the net to spit out payloads that look "polyglotty" enough (according to the structural set up I have) all you need to do is run the `learn_payloads.py` script and it will sweep up all the strings you have in a given file and try to learn the rules used to generate them so it can produce more like that.

Here's how its done:
```
keth@keithbook:~/pymlprojects_main/PyMLProjects/payloads/jhaddix/seq-12/run2$ ../../../learn_payloads.py ../../data/jhaddix.txt 
Using TensorFlow backend.
['\t', '\n', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '}', '~', '\x80', '\x82', '\x85', '\x86', '\x89', '\x8e', '\x8f', '\x90', '\x92', '\x93', '\x98', '\x9d', '\xa2', '\xaf', '\xbc', '\xbd', '\xbe', '\xc2', '\xc3', '\xe2']
[*] Total Characters: 36896
[*] Total Vocab: 116
[*] Total Patterns: 36884
12 1
116
[*] training model...
Epoch 1/50
2018-03-12 21:00:06.275223: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX AVX2 FMA
 3450/36884 [=>............................] - ETA: 8:11 - loss: 4.1146^[c
 3500/36884 [=>............................] - ETA: 8:10 - loss: 4.1133
 3550/36884 [=>............................] - ETA: 8:09 - loss: 4.1095

```

This will produce a list of weights files (used to set up the neural net from scratch if you need to use it later):

```
-rw-rw-r-- 1 keth keth 38566192 Feb 26 22:48 seq-12-weights-improvement-01-3.8815.hdf5
-rw-rw-r-- 1 keth keth 38566192 Feb 26 22:54 seq-12-weights-improvement-02-3.4597.hdf5
-rw-rw-r-- 1 keth keth 38566192 Feb 26 23:00 seq-12-weights-improvement-03-3.0045.hdf5
-rw-rw-r-- 1 keth keth 38566192 Feb 26 23:06 seq-12-weights-improvement-04-2.6040.hdf5
...
-rw-rw-r-- 1 keth keth 38566192 Feb 27 00:17 seq-12-weights-improvement-19-0.5382.hdf5
-rw-rw-r-- 1 keth keth 38566192 Feb 27 00:20 seq-12-weights-improvement-20-0.5177.hdf5

```

### Generating Payloads
In order to generate payloads you need to run the `generate_payloads.py` script, it takes in the original data file you used to train the net and a weight configuration you'd like to use (try choosing one with a low enough weight to satisfy your payload generatio nneeds) here's how to do that:

```
keth@keithbook:~/pymlprojects_main/PyMLProjects/payloads/jhaddix/seq-12$ ../../generate_payloads.py ../data/jhaddix.txt seq-12-weights-improvement-50-0.3361.hdf5 
Using TensorFlow backend.
[*] Total Characters: 36896
[*] Total Vocab: 116
[*] Total Patterns: 36884
2018-03-12 21:10:21.244253: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX AVX2 FMA
[*] Seed: 'e?\/onerror '

= alert(1)???
<svg><script ?>alert(1)
<input talue="``onmouseover=alert(1)"></dire <dtr sac tooreo=alert(1)"></dire <dtr sac tooreo=alert(1)"></dire <dtr sac tooreo=alert(1)"></dire <dtr sac tooreo=al
e="x:">
<--`<img/src=` onerror=alert(1)>/script>">script> document.getElementById(%div2").innerHTML;</script>
<script> document.getElementById(%div2").innerHTML;</script>
<script> document.getElementB
TML=innerHTML</script>

```
*some stderr output has been supressed, tensor flow and keras like to make a lot of noise hehe

## Dependencies

The only thing you need to get this up and running is a working python install and whatever else you need to run Keras, smoothly.
Python Keras : https://keras.io/ 


Further Reading and Similar ideas:
*  http://www.ieeeconfpublishing.org/cpir/UploadedFiles/ver11.0.pdf 
*  http://machinelearningmastery.com/text-generation-lstm-recurrent-neural-networks-python-keras/ 
*  https://0day.work/using-neural-networks-for-password-cracking/ 
