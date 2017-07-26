# Generating Passwords with an LSTM 

This project is for training an AI to learn the statistical patterns in how people construct passwords and use them
to generate an infinite amount of the same "kind" of passwords. This is a potentially very successful way to guess
passwords since people often employ password "schemes" when choosing an easy to remember password. 

## How to use
The project includes two scripts 

* `learn_passwords.py`  used to train the neural net on a set of passwords, this produces a set of weights.
* `generate_passwords.py` used to generate passwords based on a trained set of weights.  

### Training the Neural Net
In order to produce some AI that can already generate passwords based on a sample, the easiest way to do this
is to feed the password list to the `learn_passwords.py` script as follows:
```

$>./learn_passwords.py 
Using TensorFlow backend.
Usage: ./learn_passwords.py [password list]

$>./learn_passwords.py passwords_random_medium.txt 
Using TensorFlow backend.
['\n', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '}', '~', '\x82', '\x84', '\x85', '\x88', '\x91', '\x95', '\x96', '\xa0', '\xa1', '\xa3', '\xac', '\xb0', '\xb2', '\xb4', '\xb6', '\xb8', '\xb9', '\xbc', '\xc2', '\xc3', '\xe0', '\xe1', '\xe2']
[*] Total Characters: 244242
[*] Total Vocab: 92

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

### Generating Passwords
In order to generate passwords you need to run the `generate_passwords.py` script, here's how to do that:

```
$>./generate_passwords.py 
Using TensorFlow backend.
Usage: ./generate_passwords.py [data file] [weights filename]

$>./generate_passwords.py passwords_1000.txt seq-100-weights-improvement-49-1.8796.hdf5 
Using TensorFlow backend.
[*] Total Characters: 7784
[*] Total Vocab: 38
[*] Total Patterns: 7684
[*] Seed:  tiful
mylove
angela
poohbear
patrick
iloveme
sakura
adrian
alexander
destiny
christian
121212
```
*some stderr output has been supressed, tensor flow and keras like to make a lot of noise hehe
