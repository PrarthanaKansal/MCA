# -*- coding: utf-8 -*-
"""q1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wkI0b2NiSRBBOw4NKpX6vR_U_Nf_dTgN
"""

import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning) 
from google.colab import drive

drive.mount('/content/drive')

import os
import glob
trainingPath = '/content/drive/My Drive/MCAAssignment2/Dataset/training'

def dictionaryTitles(path):
    '''returns all folders in training set'''
    image_files = sorted([os.path.join(path, '', file)
                          for file in os.listdir(path)
                          ])
    return image_files
pathOfFolders = dictionaryTitles(trainingPath)


zero = {}
path = '/content/drive/My Drive/MCAAssignment2/Dataset/training/zero'
for filename in glob.glob(os.path.join(path, '*.wav')):
    zero[filename] = ""
#print(zero)

one = {}
path = '/content/drive/My Drive/MCAAssignment2/Dataset/training/one'
for filename in glob.glob(os.path.join(path, '*.wav')):
    one[filename] = ""

two = {}
path = '/content/drive/My Drive/MCAAssignment2/Dataset/training/two'
for filename in glob.glob(os.path.join(path, '*.wav')):
    two[filename] = ""

three = {}
path = '/content/drive/My Drive/MCAAssignment2/Dataset/training/three'
for filename in glob.glob(os.path.join(path, '*.wav')):
    three[filename] = ""

four = {}
path = '/content/drive/My Drive/MCAAssignment2/Dataset/training/four'
for filename in glob.glob(os.path.join(path, '*.wav')):
    four[filename] = ""

five = {}
path = '/content/drive/My Drive/MCAAssignment2/Dataset/training/five'
for filename in glob.glob(os.path.join(path, '*.wav')):
    five[filename] = ""

six = {}
path = '/content/drive/My Drive/MCAAssignment2/Dataset/training/six'
for filename in glob.glob(os.path.join(path, '*.wav')):
    six[filename] = ""

seven = {}
path = '/content/drive/My Drive/MCAAssignment2/Dataset/training/seven'
for filename in glob.glob(os.path.join(path, '*.wav')):
    seven[filename] = ""

eight = {}
path = '/content/drive/My Drive/MCAAssignment2/Dataset/training/eight'
for filename in glob.glob(os.path.join(path, '*.wav')):
    eight[filename] = ""

nine = {}
path = '/content/drive/My Drive/MCAAssignment2/Dataset/training/nine'
for filename in glob.glob(os.path.join(path, '*.wav')):
    nine[filename] = ""

import os
import glob
ValidationPath = '/content/drive/My Drive/MCAAssignment2/Dataset/validation'

def dictionaryTitles(path):
    '''returns all folders in training set'''
    image_files = sorted([os.path.join(path, '', file)
                          for file in os.listdir(path)
                          ])
    return image_files
pathOfFolders = dictionaryTitles(trainingPath)


zeroVal = {}
path = '/content/drive/My Drive/MCAAssignment2/Dataset/validation/zero'
for filename in glob.glob(os.path.join(path, '*.wav')):
    zeroVal[filename] = ""
#print(zero)

oneVal = {}
path = '/content/drive/My Drive/MCAAssignment2/Dataset/validation/one'
for filename in glob.glob(os.path.join(path, '*.wav')):
    oneVal[filename] = ""

twoVal = {}
path = '/content/drive/My Drive/MCAAssignment2/Dataset/validation/two'
for filename in glob.glob(os.path.join(path, '*.wav')):
    twoVal[filename] = ""

threeVal = {}
path = '/content/drive/My Drive/MCAAssignment2/Dataset/validation/three'
for filename in glob.glob(os.path.join(path, '*.wav')):
    threeVal[filename] = ""

fourVal = {}
path = '/content/drive/My Drive/MCAAssignment2/Dataset/validation/four'
for filename in glob.glob(os.path.join(path, '*.wav')):
    fourVal[filename] = ""

fiveVal = {}
path = '/content/drive/My Drive/MCAAssignment2/Dataset/validation/five'
for filename in glob.glob(os.path.join(path, '*.wav')):
    fiveVal[filename] = ""

sixVal = {}
path = '/content/drive/My Drive/MCAAssignment2/Dataset/validation/six'
for filename in glob.glob(os.path.join(path, '*.wav')):
    sixVal[filename] = ""

sevenVal = {}
path = '/content/drive/My Drive/MCAAssignment2/Dataset/validation/seven'
for filename in glob.glob(os.path.join(path, '*.wav')):
    sevenVal[filename] = ""

eightVal = {}
path = '/content/drive/My Drive/MCAAssignment2/Dataset/validation/eight'
for filename in glob.glob(os.path.join(path, '*.wav')):
    eightVal[filename] = ""

nineVal = {}
path = '/content/drive/My Drive/MCAAssignment2/Dataset/validation/nine'
for filename in glob.glob(os.path.join(path, '*.wav')):
    nineVal[filename] = ""

fname = "/content/drive/My Drive/MCAAssignment2/Dataset/training/zero/004ae714_nohash_0.wav"
import wave
import contextlib
ts = 0
with contextlib.closing(wave.open(fname,'r')) as f:
    frames = f.getnframes()
    rate = f.getframerate()
    duration = frames / float(rate)
    ts = duration

a = next(iter(zero))
print(a)

#MY CODE
from scipy.io import wavfile
import numpy
def getTimeSeries(fileName):
  samplerate, data = wavfile.read(fileName)
  times = np.arange(len(data))/float(samplerate)
  return times

# ts = getTimeSeries(fname)
# print(getTimeSeries(fname))

def get_xns(ts):
    mag = []
    L = len(ts)
    NyquestLimit = int(L/2)
    for i in range(NyquestLimit): # Nyquest Limit
        L  = len(ts)      
    
        ks = np.arange(0,L,1)
        temp = 1j*2
        temp = temp*np.pi
        temp = temp*ks
        temp = temp*i
        temp = temp/L
        xn = np.sum(ts*np.exp((temp))/L)

        a = np.abs(xn)
        a = a*2
        mag.append(a)
    return(mag)

# mag = get_xns(ts)

def create_spectrogram(ts,NFFT,noverlap = None):
    if noverlap is None:
        noverlap = NFFT/2
    noverlap = int(noverlap)

    a = NFFT-noverlap
    starts  = np.arange(0,len(ts),a,dtype=int)  
    starts  = starts[starts + NFFT < len(ts)]
    xns = []
    for start in starts:
        ts_window = get_xns(ts[start:start + NFFT]) 
        xns.append(ts_window)
    specX = np.array(xns).T
    spec = 10*np.log10(specX)
    return(spec)

L = 256
noverlap = 84

i=1
for key in zero:
  ts = getTimeSeries(key)
  spec = create_spectrogram(ts,L,noverlap = noverlap )
  zero[key]=spec
  print(key)
  print(i)
  i=i+1
for key in one:
  ts = getTimeSeries(key)
  spec = create_spectrogram(ts,L,noverlap = noverlap )
  one[key]=spec
  print(key)
  print(i)
  i=i+1
for key in two:
  ts = getTimeSeries(key)
  spec = create_spectrogram(ts,L,noverlap = noverlap )
  two[key]=spec
  print(key)
  print(i)
  i=i+1
for key in three:
  ts = getTimeSeries(key)
  spec = create_spectrogram(ts,L,noverlap = noverlap )
  three[key]=spec
  print(key)
  print(i)
  i=i+1
for key in four:
  ts = getTimeSeries(key)
  spec = create_spectrogram(ts,L,noverlap = noverlap )
  four[key]=spec
  print(key)
  print(i)
  i=i+1
for key in five:
  ts = getTimeSeries(key)
  spec = create_spectrogram(ts,L,noverlap = noverlap )
  five[key]=spec
  print(key)
  print(i)
  i=i+1
for key in six:
  ts = getTimeSeries(key)
  spec = create_spectrogram(ts,L,noverlap = noverlap )
  six[key]=spec
  print(key)
  print(i)
  i=i+1
for key in seven:
  ts = getTimeSeries(key)
  spec = create_spectrogram(ts,L,noverlap = noverlap )
  seven[key]=spec
  print(key)
  print(i)
  i=i+1
for key in eight:
  ts = getTimeSeries(key)
  spec = create_spectrogram(ts,L,noverlap = noverlap )
  eight[key]=spec
  print(key)
  print(i)
  i=i+1
for key in nine:
  ts = getTimeSeries(key)
  spec = create_spectrogram(ts,L,noverlap = noverlap )
  nine[key]=spec
  print(key)
  print(i)
  i=i+1

i=1
print(zeroVal)
for key in zeroVal:
  ts = getTimeSeries(key)
  spec = create_spectrogram(ts,L,noverlap = noverlap )
  zeroVal[key]=spec
  print(key)
  print(i)
  i=i+1
for key in oneVal:
  ts = getTimeSeries(key)
  spec = create_spectrogram(ts,L,noverlap = noverlap )
  oneVal[key]=spec
  print(key)
  print(i)
  i=i+1
for key in twoVal:
  ts = getTimeSeries(key)
  spec = create_spectrogram(ts,L,noverlap = noverlap )
  twoVal[key]=spec
  print(key)
  print(i)
  i=i+1
for key in threeVal:
  ts = getTimeSeries(key)
  spec = create_spectrogram(ts,L,noverlap = noverlap )
  threeVal[key]=spec
  print(key)
  print(i)
  i=i+1
for key in fourVal:
  ts = getTimeSeries(key)
  spec = create_spectrogram(ts,L,noverlap = noverlap )
  fourVal[key]=spec
  print(key)
  print(i)
  i=i+1
for key in fiveVal:
  ts = getTimeSeries(key)
  spec = create_spectrogram(ts,L,noverlap = noverlap )
  fiveVal[key]=spec
  print(key)
  print(i)
  i=i+1
for key in sixVal:
  ts = getTimeSeries(key)
  spec = create_spectrogram(ts,L,noverlap = noverlap )
  sixVal[key]=spec
  print(key)
  print(i)
  i=i+1
for key in sevenVal:
  ts = getTimeSeries(key)
  spec = create_spectrogram(ts,L,noverlap = noverlap )
  sevenVal[key]=spec
  print(key)
  print(i)
  i=i+1
for key in eightVal:
  ts = getTimeSeries(key)
  spec = create_spectrogram(ts,L,noverlap = noverlap )
  eightVal[key]=spec
  print(key)
  print(i)
  i=i+1
for key in nineVal:
  ts = getTimeSeries(key)
  spec = create_spectrogram(ts,L,noverlap = noverlap )
  nineVal[key]=spec
  print(key)
  print(i)
  i=i+1

# CODE to download dictionaries
# RUN once
import pickle
f = open("zeroVal.pkl","wb")
pickle.dump(zeroVal,f)
f.close()
f = open("oneVal.pkl","wb")
pickle.dump(oneVal,f)
f.close()
f = open("twoVal.pkl","wb")
pickle.dump(twoVal,f)
f.close()
f = open("threeVal.pkl","wb")
pickle.dump(threeVal,f)
f.close()
f = open("fourVal.pkl","wb")
pickle.dump(fourVal,f)
f.close()
f = open("fiveVal.pkl","wb")
pickle.dump(fiveVal,f)
f.close()
f = open("sixVal.pkl","wb")
pickle.dump(sixVal,f)
f.close()
f = open("sevenVal.pkl","wb")
pickle.dump(sevenVal,f)
f.close()
f = open("eightVal.pkl","wb")
pickle.dump(eightVal,f)
f.close()
f = open("nineVal.pkl","wb")
pickle.dump(nineVal,f)
f.close()

#CODE to download dictionaries
#RUN once
# import pickle
# f = open("zero.pkl","wb")
# pickle.dump(zero,f)
# f.close()
# f = open("one.pkl","wb")
# pickle.dump(one,f)
# f.close()
# f = open("two.pkl","wb")
# pickle.dump(two,f)
# f.close()
# f = open("three.pkl","wb")
# pickle.dump(three,f)
# f.close()
# f = open("four.pkl","wb")
# pickle.dump(four,f)
# f.close()
# f = open("five.pkl","wb")
# pickle.dump(five,f)
# f.close()
# f = open("six.pkl","wb")
# pickle.dump(six,f)
# f.close()
# f = open("seven.pkl","wb")
# pickle.dump(seven,f)
# f.close()
# f = open("eight.pkl","wb")
# pickle.dump(eight,f)
# f.close()
# f = open("nine.pkl","wb")
# pickle.dump(nine,f)
# f.close()

from google.colab import files

files.download('zeroVal.pkl')
files.download('oneVal.pkl')
files.download('twoVal.pkl')
files.download('threeVal.pkl')
files.download('fourVal.pkl')
files.download('fiveVal.pkl')
files.download('sixVal.pkl')
files.download('sevenVal.pkl')
files.download('eightVal.pkl')
files.download('nineVal.pkl')

import pickle
pickle_in = open("/content/drive/My Drive/zero.pkl","rb")
zero = pickle.load(pickle_in)
pickle_in = open("/content/drive/My Drive/one.pkl","rb")
one = pickle.load(pickle_in)
pickle_in = open("/content/drive/My Drive/two.pkl","rb")
two = pickle.load(pickle_in)
pickle_in = open("/content/drive/My Drive/three.pkl","rb")
three = pickle.load(pickle_in)
pickle_in = open("/content/drive/My Drive/four.pkl","rb")
four = pickle.load(pickle_in)
pickle_in = open("/content/drive/My Drive/five.pkl","rb")
five = pickle.load(pickle_in)
pickle_in = open("/content/drive/My Drive/six.pkl","rb")
six = pickle.load(pickle_in)
pickle_in = open("/content/drive/My Drive/seven.pkl","rb")
seven = pickle.load(pickle_in)
pickle_in = open("/content/drive/My Drive/eight.pkl","rb")
eight = pickle.load(pickle_in)
pickle_in = open("/content/drive/My Drive/nine.pkl","rb")
nine = pickle.load(pickle_in)

import pickle
pickle_in = open("/content/drive/My Drive/zeroVal.pkl","rb")
zeroVal = pickle.load(pickle_in)
pickle_in = open("/content/drive/My Drive/oneVal.pkl","rb")
oneVal = pickle.load(pickle_in)
pickle_in = open("/content/drive/My Drive/twoVal.pkl","rb")
twoVal = pickle.load(pickle_in)
pickle_in = open("/content/drive/My Drive/threeVal.pkl","rb")
threeVal = pickle.load(pickle_in)
pickle_in = open("/content/drive/My Drive/fourVal.pkl","rb")
fourVal = pickle.load(pickle_in)
pickle_in = open("/content/drive/My Drive/fiveVal.pkl","rb")
fiveVal = pickle.load(pickle_in)
pickle_in = open("/content/drive/My Drive/sixVal.pkl","rb")
sixVal = pickle.load(pickle_in)
pickle_in = open("/content/drive/My Drive/sevenVal.pkl","rb")
sevenVal = pickle.load(pickle_in)
pickle_in = open("/content/drive/My Drive/eightVal.pkl","rb")
eightVal = pickle.load(pickle_in)
pickle_in = open("/content/drive/My Drive/nineVal.pkl","rb")
nineVal = pickle.load(pickle_in)


def plot_spectrogram(spec,sample_rate, L,  mappable = None):
    plt.figure(figsize=(20,8))
    plt_spec = plt.imshow(spec,origin='lower')

    ## create ylim
    Nyticks = 10
    ks      = np.linspace(0,spec.shape[0],Nyticks)
    freq_Hz = ks*sample_rate/len(ts)
    freq_Hz  = [int(i) for i in freq_Hz ] 
    ksHz    = freq_Hz
    plt.yticks(ks,ksHz)
    plt.ylabel("Frequency (Hz)")

    ## create xlim
    Nxticks = 10
    ts_spec = np.linspace(0,spec.shape[1],Nxticks)
    total_ts_sec = len(ts)/sample_rate
    ts_spec_sec  = ["{:4.2f}".format(i) for i in np.linspace(0,total_ts_sec*10/len(ts),Nxticks)]
    plt.xticks(ts_spec,ts_spec_sec)
    plt.xlabel("Time (sec)")

    plt.title("Spectrogram L={} Spectrogram.shape={}".format(L,spec.shape))
    plt.colorbar(mappable,use_gridspec=True)
    plt.show()
    return(plt_spec)
# ts = getTimeSeries('/content/drive/My Drive/MCAAssignment2/Dataset/training/zero/106a6183_nohash_1.wav')
# mag = get_xns(ts)
# plot_spectrogram(zero['/content/drive/My Drive/MCAAssignment2/Dataset/training/zero/106a6183_nohash_1.wav']
#                  ,1000,L)



z=[]
for key in zero:
  z.append(zero[key].flatten())
print((len(z), len(z[0])))
z=[]
for key in one:
  z.append(one[key].flatten())
print((len(z), len(z[0])))
z=[]
for key in two:
  z.append(two[key].flatten())
print((len(z), len(z[0])))
z=[]
for key in three:
  z.append(three[key].flatten())
print((len(z), len(z[0])))
z=[]
for key in four:
  z.append(four[key].flatten())
print((len(z), len(z[0])))
z=[]
for key in five:
  z.append(five[key].flatten())
print((len(z), len(z[0])))
z=[]
for key in six:
  z.append(six[key].flatten())
print((len(z), len(z[0])))
z=[]
for key in seven:
  z.append(seven[key].flatten())
print((len(z), len(z[0])))
z=[]
for key in eight:
  z.append(eight[key].flatten())
print((len(z), len(z[0])))
z=[]
for key in nine:
  z.append(nine[key].flatten())
print((len(z), len(z[0])))

Y = ['zero','one','two','three','four','five','six','seven','eight','nine']
# Y = [0,1,2,3,4,5,6,7,8,9]
X = []

y = []
for value in zero:
  y.append(zero[value].flatten())
#y = y.flatten()
X.append(y)

y = []
for value in one:
  y.append(one[value].flatten())
X.append(y)

y = []
for value in two:
  y.append(two[value].flatten())
X.append(y)

y = []
for value in three:
  y.append(three[value].flatten())
X.append(y)

y = []
for value in four:
  y.append(four[value].flatten())
X.append(y)

y = []
for value in five:
  y.append(five[value].flatten())
X.append(y)

y = []
for value in six:
  y.append(six[value].flatten())
X.append(y)

y = []
for value in seven:
  y.append(seven[value].flatten())
X.append(y)

y = []
for value in eight:
  y.append(eight[value].flatten())
X.append(y)

y = []
for value in nine:
  y.append(nine[value].flatten())
X.append(y)

from __future__ import print_function
import math
import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt
from scipy.signal import lfilter
from scipy.fftpack.realtransforms import dct

eps = 0.00000001

def zero_crossing_rate(frame):
    """Computes zero crossing rate of frame"""
    count = len(frame)
    count_zero = np.sum(np.abs(np.diff(np.sign(frame)))) / 2
    return np.float64(count_zero) / np.float64(count - 1.0)


def energy(frame):
    return np.sum(frame ** 2) / np.float64(len(frame))


def energy_entropy(frame, n_short_blocks=10):
    frame_energy = np.sum(frame ** 2)
    frame_length = len(frame)
    sub_win_len = int(np.floor(frame_length / n_short_blocks))
    if frame_length != sub_win_len * n_short_blocks:
        frame = frame[0:sub_win_len * n_short_blocks]

    # sub_wins is of size [n_short_blocks x L]
    sub_wins = frame.reshape(sub_win_len, n_short_blocks, order='F').copy()

    s = np.sum(sub_wins ** 2, axis=0) / (frame_energy + eps)

    entropy = -np.sum(s * np.log2(s + eps))
    return entropy


""" Frequency-domain audio features """




""" Windowing and feature extraction """


def feature_extraction(signal, sampling_rate, window, step, deltas=False):
    """
    This function implements the shor-term windowing process.
    For each short-term window a set of features is extracted.
    This results to a sequence of feature vectors, stored in a np matrix.
    ARGUMENTS
        signal:         the input signal samples
        sampling_rate:  the sampling freq (in Hz)
        window:         the short-term window size (in samples)
        step:           the short-term window step (in samples)
        deltas:         (opt) True/False if delta features are to be
                        computed
    RETURNS
        features (numpy.ndarray):        contains features
                                         (n_feats x numOfShortTermWindows)
        feature_names (numpy.ndarray):   contains feature names
                                         (n_feats x numOfShortTermWindows)
    """

    window = int(window)
    step = int(step)

    # signal normalization
    signal = np.double(signal)
    signal = signal / (2.0 ** 15)
    dc_offset = signal.mean()
    signal_max = (np.abs(signal)).max()
    signal = (signal - dc_offset) / (signal_max + 0.0000000001)

    number_of_samples = len(signal)  # total number of samples
    current_position = 0
    count_fr = 0
    num_fft = int(window / 2)

    # compute the triangular filter banks used in the mfcc calculation
    #fbank, freqs = mfcc_filter_banks(sampling_rate, num_fft)

    n_total_feats = 3
    #    n_total_feats = n_time_spectral_feats + n_mfcc_feats +
    #    n_harmonic_feats

    # define list of feature names
    # feature_names = ["zcr", "energy", "energy_entropy"]
    # feature_names += ["spectral_centroid", "spectral_spread"]
    # feature_names.append("spectral_entropy")
    # feature_names.append("spectral_flux")
    # feature_names.append("spectral_rolloff")
    

    # add names for delta features:
    # if deltas:
    #     feature_names_2 = feature_names + ["delta " + f for f in feature_names]
    #     feature_names = feature_names_2

    features = []
    # for each short-term window to end of signal
    while current_position + window - 1 < number_of_samples:
        count_fr += 1
        # get current window
        x = signal[current_position:current_position + window]

        # update window position
        current_position = current_position + step

        # get fft magnitude
        fft_magnitude = abs(fft(x))

        # normalize fft
        fft_magnitude = fft_magnitude[0:num_fft]
        fft_magnitude = fft_magnitude / len(fft_magnitude)

        # keep previous fft mag (used in spectral flux)
        if count_fr == 1:
            fft_magnitude_previous = fft_magnitude.copy()
        feature_vector = np.zeros((n_total_feats, 1))

        # zero crossing rate
        feature_vector[0] = zero_crossing_rate(x)

        # short-term energy
        feature_vector[1] = energy(x)

        # short-term entropy of energy
        feature_vector[2] = energy_entropy(x)

        

        
        if not deltas:
            features.append(feature_vector)
        

        fft_magnitude_previous = fft_magnitude.copy()

    features = np.concatenate(features, 1)
    features.flatten()
    return features

trainFeatures=np.zeros((10000,3))

i=0
for key in zero:
  ts = getTimeSeries(key)
  spec = feature_extraction(ts, 1200, 256, 100, deltas=False)
  try:
    trainFeatures[i]=spec
  except:
    trainFeatures[i]=np.zeros((1,3))
    print("Problem in zero:",i)
    print(spec)
  print(i)
  i=i+1
  
for key in one:
  ts = getTimeSeries(key)
  spec = feature_extraction(ts, 1200, 256, 100, deltas=False)
  try:
    trainFeatures[i]=spec
  except:
    trainFeatures[i]=np.zeros((1,3))
    print("Problem in zero:",i)
    print(spec)
  print(i)
  i=i+1

j = 0
for key in two:
  ts = getTimeSeries(key)
  spec = feature_extraction(ts, 1200, 256, 100, deltas=False)
  try:
    trainFeatures[i]=spec
  except:
    trainFeatures[i]=np.zeros((1,3))
    print("Problem in zero:",i)
    print(spec)
  print(i)
  j = j+1
  i=i+1

j=0
for key in three:
  ts = getTimeSeries(key)
  spec = feature_extraction(ts, 1200, 256, 100, deltas=False)
  try:
    trainFeatures[i]=spec
  except:
    trainFeatures[i]=np.zeros((1,3))
    print("Problem in zero:",i)
    print(spec)
  print(i)
  j = j+1
  i=i+1

j = 0
for key in four:
  ts = getTimeSeries(key)
  spec =feature_extraction(ts, 1200, 256, 100, deltas=False)
  try:
    trainFeatures[i]=spec
  except:
    trainFeatures[i]=np.zeros((1,3))
    print("Problem in zero:",i)
    print(spec)
  print(i)
  j = j+1
  i=i+1

j = 0
for key in five:
  ts = getTimeSeries(key)
  spec = feature_extraction(ts, 1200, 256, 100, deltas=False)
  try:
    trainFeatures[i]=spec
  except:
    trainFeatures[i]=np.zeros((1,3))
    print("Problem in zero:",i)
    print(spec)
  print(i)
  j = j+1
  i=i+1

j = 0
for key in six:
  ts = getTimeSeries(key)
  spec = feature_extraction(ts, 1200, 256, 100, deltas=False)
  try:
    trainFeatures[i]=spec
  except:
    trainFeatures[i]=np.zeros((1,3))
    print("Problem in zero:",i)
    print(spec)
  print(i)
  j = j+1
  i=i+1

j = 0
for key in seven:
  ts = getTimeSeries(key)
  spec = feature_extraction(ts, 1200, 256, 100, deltas=False)
  try:
    trainFeatures[i]=spec
  except:
    trainFeatures[i]=np.zeros((1,3))
    print("Problem in zero:",i)
    print(spec)
  print(i)
  j = j+1
  i=i+1

j = 0
for key in eight:
  ts = getTimeSeries(key)
  spec = feature_extraction(ts, 1200, 256, 100, deltas=False)
  try:
    trainFeatures[i]=spec
  except:
    trainFeatures[i]=np.zeros((1,3))
    print("Problem in zero:",i)
    print(spec)
  print(i)
  j = j+1
  i=i+1

j = 0
for key in nine:
  ts = getTimeSeries(key)
  spec = feature_extraction(ts, 1200, 256, 100, deltas=False)
  try:
    trainFeatures[i]=spec
  except:
    trainFeatures[i]=np.zeros((1,3))
    print("Problem in zero:",i)
    print(spec)
  print(i)
  j = j+1
  i=i+1

ValFeatures=np.zeros((2494,3))

i=0
for key in zeroVal:
  ts = getTimeSeries(key)
  spec = feature_extraction(ts, 1200, 256, 100, deltas=False)
  try:
    ValFeatures[i]=spec
  except:
    ValFeatures[i]=trainFeatures[i]
    print(spec)
    print("Problem in zero:",i)
  print(i)
  i=i+1
for key in oneVal:
  ts = getTimeSeries(key)
  spec = feature_extraction(ts, 1200, 256, 100, deltas=False)
  try:
    ValFeatures[i]=spec
  except:
    ValFeatures[i]=trainFeatures[800+i]
    print("Problem in zero:",i)
  print(i)
  i=i+1
for key in twoVal:
  ts = getTimeSeries(key)
  spec = feature_extraction(ts, 1200, 256, 100, deltas=False)
  try:
    ValFeatures[i]=spec
  except:
    ValFeatures[i]=trainFeatures[800+i]
    print("Problem in zero:",i)
  print(i)
  i=i+1
for key in threeVal:
  ts = getTimeSeries(key)
  spec = feature_extraction(ts, 1200, 256, 100, deltas=False)
  try:
    ValFeatures[i]=spec
  except:
    ValFeatures[i]=trainFeatures[800+i]
    print("Problem in zero:",i)
  print(i)
  i=i+1
for key in fourVal:
  ts = getTimeSeries(key)
  spec =feature_extraction(ts, 1200, 256, 100, deltas=False)
  try:
    ValFeatures[i]=spec
  except:
    ValFeatures[i]=trainFeatures[800+i]
    print("Problem in zero:",i)
  print(i)
  i=i+1
for key in fiveVal:
  ts = getTimeSeries(key)
  spec = feature_extraction(ts, 1200, 256, 100, deltas=False)
  try:
    ValFeatures[i]=spec
  except:
    ValFeatures[i]=trainFeatures[800+i]
    print("Problem in zero:",i)
  print(i)
  i=i+1
for key in sixVal:
  ts = getTimeSeries(key)
  spec = feature_extraction(ts, 1200, 256, 100, deltas=False)
  try:
    ValFeatures[i]=spec
  except:
    ValFeatures[i]=trainFeatures[800+i]
    print("Problem in zero:",i)
  print(i)
  i=i+1
for key in sevenVal:
  ts = getTimeSeries(key)
  spec = feature_extraction(ts, 1200, 256, 100, deltas=False)
  try:
    ValFeatures[i]=spec
  except:
    ValFeatures[i]=trainFeatures[800+i]
    print("Problem in zero:",i)
  print(i)
  i=i+1
for key in eightVal:
  ts = getTimeSeries(key)
  spec = feature_extraction(ts, 1200, 256, 100, deltas=False)
  try:
    ValFeatures[i]=spec
  except:
    ValFeatures[i]=trainFeatures[800+i]
    print("Problem in zero:",i)
  print(i)
  i=i+1
for key in nineVal:
  ts = getTimeSeries(key)
  spec = feature_extraction(ts, 1200, 256, 100, deltas=False)
  try:
    ValFeatures[i]=spec
  except:
    ValFeatures[i]=trainFeatures[800+i]
    print("Problem in zero:",i)
  print(i)
  i=i+1

y=[]
for i in range(1000):
  y.append(0)
for i in range(1000):
  y.append(1)
for i in range(1000):
  y.append(2)
for i in range(1000):
  y.append(3)
for i in range(1000):
  y.append(4)
for i in range(1000):
  y.append(5)
for i in range(1000):
  y.append(6)
for i in range(1000):
  y.append(7)
for i in range(1000):
  y.append(8)
for i in range(1000):
  y.append(9)

# for i in range(10000):
#   if (len(trainFeatures[i]))!= 3:
#     print(i)
print(trainFeatures.shape)
from sklearn import svm
clf = svm.SVC()
clf.fit(trainFeatures, y)

clf.predict(ValFeatures)