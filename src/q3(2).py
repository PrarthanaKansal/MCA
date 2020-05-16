# -*- coding: utf-8 -*-
"""q3(2).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JIK8jUY6Cf2C-KPVPQyBdLG-obrqMbrD
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

#MY CODE
from scipy.io import wavfile
import random 
import numpy
import librosa
import IPython.display as ipd
# a = next(iter(zero))
# data = librosa.core.load(a)[0]
# # ipd.Audio(data, rate=16000)
# bck = "/content/drive/My Drive/MCAAssignment2/Dataset/_background_noise_/doing_the_dishes.wav"
# wn = librosa.core.load(bck)[0]
# # ipd.Audio(wn, rate=16000)
# if(data.shape[0]>wn.shape[0]):
#   data_wn = data[0:wn.shape[0]]+0.005*wn
# else:
#   data_wn = data + 0.005*wn[0:data.shape[0]]
# ipd.Audio(data_wn, rate=16000)


def gettimeSeries(fileName):
  
  data = librosa.core.load(fileName)[0]
  samplerate, dataTemp = wavfile.read(fileName)
  x = random.randint(1,3)
  if x==1:
    bck = "/content/drive/My Drive/MCAAssignment2/Dataset/_background_noise_/doing_the_dishes.wav"
  elif x==2:
    bck = "/content/drive/My Drive/MCAAssignment2/Dataset/_background_noise_/dude_miaowing.wav"
  elif x ==3:
    bck = "/content/drive/My Drive/MCAAssignment2/Dataset/_background_noise_/exercise_bike.wav"
  wn = librosa.core.load(bck)[0]

  if(data.shape[0]>wn.shape[0]):
    data_wn = data[0:wn.shape[0]]+0.005*wn
  else:
    data_wn = data + 0.005*wn[0:data.shape[0]]

  #samplerate, data = wavfile.read(data_wn)
  ts = np.arange(len(data_wn))/float(samplerate)
  
  
  return ts

def getTimeSeries(fileName):
  samplerate, data = wavfile.read(fileName)
  ts = np.arange(len(data))/float(samplerate)
  x = random.randint(1,3)
  if x==1:
    bck = "/content/drive/My Drive/MCAAssignment2/Dataset/_background_noise_/doing_the_dishes.wav"
  elif x==2:
    bck = "/content/drive/My Drive/MCAAssignment2/Dataset/_background_noise_/dude_miaowing.wav"
  elif x ==3:
    bck = "/content/drive/My Drive/MCAAssignment2/Dataset/_background_noise_/exercise_bike.wav"
  samplerate, data = wavfile.read(bck)
  ts2 = np.arange(len(data))/float(samplerate)
  if(ts.shape[0]>ts2.shape[0]):
    ts3 = ts[0:ts2.shape[0]]+0.005*ts2
  else:
    ts3 = ts + 0.005*ts2[0:ts.shape[0]]
  return ts3

# ts = getTimeSeries(fname)
# print(getTimeSeries(fname))

def mfcc_filter_banks(sampling_rate, num_fft, lowfreq=133.33, linc=200 / 3,
                      logsc=1.0711703, num_lin_filt=13, num_log_filt=27):
    """
    Computes the triangular filterbank for MFCC computation 
    (used in the stFeatureExtraction function before the stMFCC function call)
    This function is taken from the scikits.talkbox library (MIT Licence):
    https://pypi.python.org/pypi/scikits.talkbox
    """


    # Total number of filters
    var = num_lin_filt #Linear Filters
    var2 = num_log_filt #Log Filters
    varFin = var + var2 #Sum of filters
    num_filt_total = varFin # Total filters variable

    # Compute frequency points of the triangle:
    a = num_filt_total + 2
    frequencies = np.zeros(a)

    b = np.arrange(num_lin_filt)
    c = b*linc
    d = lowfreq + c
    frequencies[:num_lin_filt] = d

    temp = num_lin_filt - 1
    temp2 = num_log_filt + 3
    frequencies[num_lin_filt:] = frequencies[temp] * logsc ** \
                                 np.arange(1, temp2)
    heights = 2. / (frequencies[2:] - frequencies[0:-2])

    # Compute filterbank coeff (in fft domain, in bins)
    fbank = np.zeros((var+var2, num_fft))
    nfreqs = np.arange(num_fft) / (1. * num_fft) * sampling_rate

    for i in range(var+var2):
        low_freqs = frequencies[i]

        forCent = i+1
        cent_freqs = frequencies[forCent]

        forHigh = i+2
        high_freqs = frequencies[forHigh]

        u =  low_freqs * num_fft
        floor1 = u/sampling_rate
        v = cent_freqs * num_fft
        floor2 = v / sampling_rate
        lid = np.arange(np.floor(floor1) + 1,
                        np.floor(floor2) + 1,
                        dtype=np.int)
        
        difference = cent_freqs - low_freqs
        lslope = heights[i] / (difference)

        u = cent_freqs * num_fft
        floor1 = u / sampling_rate
        v = high_freqs * num_fft
        floor2 = v/ sampling_rate
        rid = np.arange(np.floor( floor1) + 1,
                        np.floor( floor2) + 1,
                        dtype=np.int)
        
        difference = high_freqs - cent_freqs
        rslope = heights[i] / (difference)
        
        try:
          a = nfreqs[lid]
          a = a - low_freqs
          fbank[i][lid] = lslope * (a)

          b = high_freqs
          fbank[i][rid] = rslope * (high_freqs - nfreqs[rid])
        except:
          continue
        

    return fbank, frequencies



def mfcc(fft_magnitude, fbank, num_mfcc_feats):
    """
    Computes the MFCCs of a frame, given the fft mag
    ARGUMENTS:
        fft_magnitude:  fft magnitude abs(FFT)
        fbank:          filter bank (see mfccInitFilterBanks)
    RETURN
        ceps:           MFCCs (13 element vector)
    Note:    MFCC calculation is, in general, taken from the 
             scikits.talkbox library (MIT Licence),
    #    with a small number of modifications to make it more 
         compact and suitable for the pyAudioAnalysis Lib
    """
    mspec = np.log10(np.dot(fft_magnitude, fbank.T) + eps)
    ceps = dct(mspec, type=2, norm='ortho', axis=-1)[:num_mfcc_feats]
    return ceps

from scipy.fftpack import fft
from scipy.signal import lfilter
from scipy.fftpack.realtransforms import dct

eps = 0.00000001
def feature_extraction(signal, sampling_rate, window, step, deltas=True):
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
    fbank, freqs = mfcc_filter_banks(sampling_rate, num_fft)

    # n_time_spectral_feats = 8
    # n_harmonic_feats = 0
    n_mfcc_feats = 13
    # n_chroma_feats = 13
    n_total_feats = 13
    #    n_total_feats = n_time_spectral_feats + n_mfcc_feats +
    #    n_harmonic_feats

    # define list of feature names
    feature_names=[]
    # feature_names = ["zcr", "energy", "energy_entropy"]
    # feature_names += ["spectral_centroid", "spectral_spread"]
    # feature_names.append("spectral_entropy")
    # feature_names.append("spectral_flux")
    # feature_names.append("spectral_rolloff")
    feature_names += ["mfcc_{0:d}".format(mfcc_i)
                       for mfcc_i in range(1, n_mfcc_feats + 1)]
    # feature_names += ["chroma_{0:d}".format(chroma_i)
    #                   for chroma_i in range(1, n_chroma_feats)]
    # feature_names.append("chroma_std")

    # # add names for delta features:
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

        # # zero crossing rate
        # feature_vector[0] = zero_crossing_rate(x)

        # # short-term energy
        # feature_vector[1] = energy(x)

        # # short-term entropy of energy
        # feature_vector[2] = energy_entropy(x)

        # # sp centroid/spread
        # [feature_vector[3], feature_vector[4]] = \
        #     spectral_centroid_spread(fft_magnitude,
        #                              sampling_rate)

        # # spectral entropy
        # feature_vector[5] = \
        #     spectral_entropy(fft_magnitude)

        # spectral flux
        # feature_vector[6] = \
        #     spectral_flux(fft_magnitude,
        #                   fft_magnitude_previous)

        # # spectral rolloff
        # feature_vector[7] = \
        #     spectral_rolloff(fft_magnitude, 0.90)

        # MFCCs
        mffc_feats_end =  n_mfcc_feats
        feature_vector[0:mffc_feats_end, 0] = mfcc(fft_magnitude, fbank, n_mfcc_feats).copy()

        # chroma features
        # chroma_names, chroma_feature_matrix = \
        #     chroma_features(fft_magnitude, sampling_rate, num_fft)
        # chroma_features_end = n_time_spectral_feats + n_mfcc_feats + \
        #                       n_chroma_feats - 1
        # feature_vector[mffc_feats_end:chroma_features_end] = \
        #     chroma_feature_matrix
        # feature_vector[chroma_features_end] = chroma_feature_matrix.std()
        # if not deltas:
        features.append(feature_vector)
        # else:
        #     # delta features
        #     if count_fr > 1:
        #         delta = feature_vector - feature_vector_prev
        #         feature_vector_2 = np.concatenate((feature_vector, delta))
        #     else:
        #         feature_vector_2 = np.concatenate((feature_vector,
        #                                            np.zeros(feature_vector.
        #                                                     shape)))
        #     feature_vector_prev = feature_vector
        #     features.append(feature_vector_2)

        fft_magnitude_previous = fft_magnitude.copy()

    # features = np.concatenate(features, 1)
    return features

import librosa
import IPython.display as ipd
a = next(iter(zero))
data = librosa.core.load(a)[0]
# ipd.Audio(data, rate=16000)
bck = "/content/drive/My Drive/MCAAssignment2/Dataset/_background_noise_/doing_the_dishes.wav"
wn = librosa.core.load(bck)[0]
# ipd.Audio(wn, rate=16000)
if(data.shape[0]>wn.shape[0]):
  data_wn = data[0:wn.shape[0]]+0.005*wn
else:
  data_wn = data + 0.005*wn[0:data.shape[0]]
ipd.Audio(data_wn, rate=16000)

i=1
for key in zero:
  ts = getTimeSeries(key)
  spec = feature_extraction(ts,1200,256,100)
  zero[key]=spec
  print(key)
  print(i)
  i=i+1
for key in one:
  ts = getTimeSeries(key)
  spec = feature_extraction(ts,1200,256,100)
  one[key]=spec
  print(key)
  print(i)
  i=i+1
for key in two:
  ts = getTimeSeries(key)
  spec = feature_extraction(ts,1200,256,100)
  two[key]=spec
  print(key)
  print(i)
  i=i+1
for key in three:
  ts = getTimeSeries(key)
  spec = feature_extraction(ts,1200,256,100)
  three[key]=spec
  print(key)
  print(i)
  i=i+1
for key in four:
  ts = getTimeSeries(key)
  spec = feature_extraction(ts,1200,256,100)
  four[key]=spec
  print(key)
  print(i)
  i=i+1
for key in five:
  ts = getTimeSeries(key)
  spec = feature_extraction(ts,1200,256,100)
  five[key]=spec
  print(key)
  print(i)
  i=i+1
for key in six:
  ts = getTimeSeries(key)
  spec = feature_extraction(ts,1200,256,100)
  six[key]=spec
  print(key)
  print(i)
  i=i+1
for key in seven:
  ts = getTimeSeries(key)
  spec = feature_extraction(ts,1200,256,100)
  seven[key]=spec
  print(key)
  print(i)
  i=i+1
for key in eight:
  ts = getTimeSeries(key)
  spec = feature_extraction(ts,1200,256,100)
  eight[key]=spec
  print(key)
  print(i)
  i=i+1
for key in nine:
  ts = getTimeSeries(key)
  spec = feature_extraction(ts,1200,256,100)
  nine[key]=spec
  print(key)
  print(i)
  i=i+1

# # CODE to download dictionaries
# # RUN once
# import pickle
# f = open("zeroNoiseMFCC.pkl","wb")
# pickle.dump(zero,f)
# f.close()
# f = open("oneNoiseMFCC.pkl","wb")
# pickle.dump(one,f)
# f.close()
# f = open("twoNoiseMFCC.pkl","wb")
# pickle.dump(two,f)
# f.close()
# f = open("threeNoiseMFCC.pkl","wb")
# pickle.dump(three,f)
# f.close()
# f = open("fourNoiseMFCC.pkl","wb")
# pickle.dump(four,f)
# f.close()
# f = open("fiveNoiseMFCC.pkl","wb")
# pickle.dump(five,f)
# f.close()
# f = open("sixNoiseMFCC.pkl","wb")
# pickle.dump(six,f)
# f.close()
# f = open("sevenNoiseMFCC.pkl","wb")
# pickle.dump(seven,f)
# f.close()
# f = open("eightNoiseMFCC.pkl","wb")
# pickle.dump(eight,f)
# f.close()
# f = open("nineNoiseMFCC.pkl","wb")
# pickle.dump(nine,f)
# f.close()

from google.colab import files

# files.download('zeroNoiseMFCC.pkl')
# files.download('oneNoiseMFCC.pkl')
# files.download('twoNoiseMFCC.pkl')
# files.download('threeNoiseMFCC.pkl')
# files.download('fourNoiseMFCC.pkl')
# files.download('fiveNoiseMFCC.pkl')
# files.download('sixNoiseMFCC.pkl')
# files.download('sevenNoiseMFCC.pkl')
# files.download('eightNoiseMFCC.pkl')
# files.download('nineNoiseMFCC.pkl')

import pickle
pickle_in = open("/content/drive/My Drive/zeroNoiseMFCC.pkl","rb")
zero = pickle.load(pickle_in)
pickle_in = open("/content/drive/My Drive/oneNoiseMFCC.pkl","rb")
one = pickle.load(pickle_in)
pickle_in = open("/content/drive/My Drive/twoNoiseMFCC.pkl","rb")
two = pickle.load(pickle_in)
pickle_in = open("/content/drive/My Drive/threeNoiseMFCC.pkl","rb")
three = pickle.load(pickle_in)
pickle_in = open("/content/drive/My Drive/fourNoiseMFCC.pkl","rb")
four = pickle.load(pickle_in)
pickle_in = open("/content/drive/My Drive/fiveNoiseMFCC.pkl","rb")
five = pickle.load(pickle_in)
pickle_in = open("/content/drive/My Drive/sixNoiseMFCC.pkl","rb")
six = pickle.load(pickle_in)
pickle_in = open("/content/drive/My Drive/sevenNoiseMFCC.pkl","rb")
seven = pickle.load(pickle_in)
pickle_in = open("/content/drive/My Drive/eightMFCC.pkl","rb")
eight = pickle.load(pickle_in)
pickle_in = open("/content/drive/My Drive/nineNoiseMFCC.pkl","rb")
nine = pickle.load(pickle_in)

import pickle
pickle_in = open("/content/drive/My Drive/zeroMFCCVal.pkl","rb")
zeroVal = pickle.load(pickle_in)
pickle_in = open("/content/drive/My Drive/oneMFCCVal.pkl","rb")
oneVal = pickle.load(pickle_in)
pickle_in = open("/content/drive/My Drive/twoMFCCVal.pkl","rb")
twoVal = pickle.load(pickle_in)
pickle_in = open("/content/drive/My Drive/threeMFCCVal.pkl","rb")
threeVal = pickle.load(pickle_in)
pickle_in = open("/content/drive/My Drive/fourMFCCVal.pkl","rb")
fourVal = pickle.load(pickle_in)
pickle_in = open("/content/drive/My Drive/fiveMFCCVal.pkl","rb")
fiveVal = pickle.load(pickle_in)
pickle_in = open("/content/drive/My Drive/sixMFCCVal.pkl","rb")
sixVal = pickle.load(pickle_in)
pickle_in = open("/content/drive/My Drive/sevenMFCCVal.pkl","rb")
sevenVal = pickle.load(pickle_in)
pickle_in = open("/content/drive/My Drive/eightMFCCVal.pkl","rb")
eightVal = pickle.load(pickle_in)
pickle_in = open("/content/drive/My Drive/nineMFCCVal.pkl","rb")
nineVal = pickle.load(pickle_in)

x = np.zeros((10000,767))

i=0
for key in zero:
  x[i]=np.asarray(zero[key]).flatten()[0:767]
  
  i=i+1
for key in one:
  try:
    x[i]=np.asarray(one[key]).flatten()[0:767]
  except:
    x[i]= np.zeros((1,65))
    print(i)

  i=i+1
for key in two:
  try:
    x[i]=np.asarray(two[key]).flatten()[0:767]
  except:
    x[i]= np.zeros((1,65))
    print(i)

  i=i+1
for key in three:
  try:
    x[i]=np.asarray(three[key]).flatten()[0:767]
  except:
    x[i]= np.zeros((1,65))
    print(i)

  i=i+1
for key in four:
  try:
    x[i]=np.asarray(four[key]).flatten()[0:767]
  except:
    x[i]= np.zeros((1,65))
    print(i)

  i=i+1
for key in five:
  try:
    x[i]=np.asarray(five[key]).flatten()[0:767]
  except:
    x[i]= np.zeros((1,65))
    print(i)

  i=i+1
for key in six:
  try:
    x[i]=np.asarray(six[key]).flatten()[0:767]
  except:
    x[i]= np.zeros((1,65))
    print(i)

  i=i+1
for key in seven:
  try:
    x[i]=np.asarray(seven[key]).flatten()[0:767]
  except:
    x[i]= np.zeros((1,65))
    print(i)

  i=i+1
for key in eight:
  try:
    x[i]=np.asarray(eight[key]).flatten()[0:767]
  except:
    x[i]= np.zeros((1,65))
    print(i)

  i=i+1
for key in nine:
  try:
    x[i]=np.asarray(nine[key]).flatten()[0:767]
  except:
    x[i]= np.zeros((1,65))
    print(i)

  i=i+1

### X dim = 10000,65

xVal = np.zeros((2494,767))

i=0
for key in zeroVal:
  # try:
  xVal[i]=np.asarray(zeroVal[key]).flatten()[0:767]
  # except:
  #   x[i]= np.zeros((1,65))
  #   print(i)
  i=i+1
for key in oneVal:
  try:
    xVal[i]=np.asarray(oneVal[key]).flatten()[0:767]
  except:
    xVal[i]= np.zeros((1,65))
    print(i)

  i=i+1
for key in twoVal:
  try:
    xVal[i]=np.asarray(twoVal[key]).flatten()[0:767]
  except:
    x[i]= np.zeros((1,65))
    print(i)

  i=i+1
for key in threeVal:
  try:
    xVal[i]=np.asarray(threeVal[key]).flatten()[0:767]
  except:
    x[i]= np.zeros((1,65))
    print(i)

  i=i+1
for key in fourVal:
  try:
    xVal[i]=np.asarray(fourVal[key]).flatten()[0:767]
  except:
    x[i]= np.zeros((1,65))
    print(i)

  i=i+1
for key in fiveVal:
  try:
    xVal[i]=np.asarray(fiveVal[key]).flatten()[0:767]
  except:
    x[i]= np.zeros((1,65))
    print(i)

  i=i+1
for key in sixVal:
  try:
    xVal[i]=np.asarray(sixVal[key]).flatten()[0:767]
  except:
    x[i]= np.zeros((1,65))
    print(i)

  i=i+1
for key in sevenVal:
  try:
    xVal[i]=np.asarray(sevenVal[key]).flatten()[0:767]
  except:
    x[i]= np.zeros((1,65))
    print(i)

  i=i+1
for key in eightVal:
  try:
    xVal[i]=np.asarray(eightVal[key]).flatten()[0:767]
  except:
    x[i]= np.zeros((1,65))
    print(i)

  i=i+1
for key in nineVal:
  try:
    xVal[i]=np.asarray(nineVal[key]).flatten()[0:767]
  except:
    x[i]= np.zeros((1,65))
    print(i)

  i=i+1

### X dim = 10000,65

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

from sklearn import svm
clf = svm.SVC()
clf.fit(x, y)
result = clf.predict(xVal)
print(getAccuracy(result))
print(getPrecision(result))

def getAccuracy(result):
  count = 0
  for i in range(260):
    if result[i]==0:
      count+=1
  for i in range(230):
    if result[i]==1:
      count+=1
  for i in range(236):
    if result[i]==2:
      count+=1
  for i in range(248):
    if result[i]==3:
      count+=1
  for i in range(280):
    if result[i]==4:
      count+=1
  for i in range(242):
    if result[i]==5:
      count+=1
  for i in range(262):
    if result[i]==6:
      count+=1
  for i in range(263):
    if result[i]==7:
      count+=1
  for i in range(243):
    if result[i]==0:
      count+=1
  for i in range(230):
    if result[i]==9:
      count+=1
  accuracy = float(float(count)/float(2494))
  return accuracy*100

def getPrecision(result):
    truePositives = getAccuracy(result)*float(24.94)
    count = 0
    for i in range(260):
      if result[i]!=0:
        count+=1
    for i in range(230):
      if result[i]!=1:
        count+=1
    for i in range(236):
      if result[i]!=2:
        count+=1
    for i in range(248):
      if result[i]!=3:
        count+=1
    for i in range(280):
      if result[i]!=4:
        count+=1
    for i in range(242):
      if result[i]!=5:
        count+=1
    for i in range(262):
      if result[i]!=6:
        count+=1
    for i in range(263):
      if result[i]!=7:
        count+=1
    for i in range(243):
      if result[i]!=0:
        count+=1
    for i in range(230):
      if result[i]!=9:
        count+=1
    falseNeg = count
    prec = truePositives/(truePositives+falseNeg)
    return prec