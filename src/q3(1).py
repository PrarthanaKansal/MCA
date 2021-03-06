# -*- coding: utf-8 -*-
"""q3(1).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wJ8QvOgINSYdyS6JLPCBvdvatADWKirq
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

import IPython.display as ipd
a = next(iter(zero))
print(a)
ts = getTimeSeries(a)
# ipd.Audio(ts, rate=5000)
bck = "/content/drive/My Drive/MCAAssignment2/Dataset/_background_noise_/doing_the_dishes.wav"
ts2 = getTimeSeries(bck)
if(ts.shape[0]>ts2.shape[0]):
  ts3 = ts[0:ts2.shape[0]]+0.005*ts2
else:
  ts3 = ts + 0.005*ts2[0:ts.shape[0]]
# ts3 = ts + 0.005*ts2
ipd.Audio(ts3, rate=5000)

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

def zero_crossing_rate(frame):
    """Computes zero crossing rate of frame"""
    count = len(frame)
    count_zero = np.sum(np.abs(np.diff(np.sign(frame)))) / 2
    return np.float64(count_zero) / np.float64(count - 1.0)


def energy(frame):
    """Computes signal energy of frame"""
    return np.sum(frame ** 2) / np.float64(len(frame))


def energy_entropy(frame, n_short_blocks=10):
    """Computes entropy of energy"""
    # total frame energy
    frame_energy = np.sum(frame ** 2)
    frame_length = len(frame)
    sub_win_len = int(np.floor(frame_length / n_short_blocks))
    if frame_length != sub_win_len * n_short_blocks:
        frame = frame[0:sub_win_len * n_short_blocks]

    # sub_wins is of size [n_short_blocks x L]
    sub_wins = frame.reshape(sub_win_len, n_short_blocks, order='F').copy()

    # Compute normalized sub-frame energies:
    s = np.sum(sub_wins ** 2, axis=0) / (frame_energy + eps)

    # Compute entropy of the normalized sub-frame energies:
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
result = clf.predict(ValFeatures)
print(getAccuracy(result))

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

def get_xns(ts):
    '''
    Compute Fourier coefficients only up to the Nyquest Limit Xn, n=1,...,L/2
    and multiply the absolute value of the Fourier coefficients by 2, 
    to account for the symetry of the Fourier coefficients above the Nyquest Limit. 
    '''
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
    '''
          ts: original time series
        NFFT: The number of data points used in each block for the DFT.
          Fs: the number of points sampled per second, so called sample_rate
    noverlap: The number of points of overlap between blocks. The default value is 128. 
    '''
    if noverlap is None:
        noverlap = NFFT/2
    noverlap = int(noverlap)

    a = NFFT-noverlap
    starts  = np.arange(0,len(ts),a,dtype=int)
    # remove any window with less than NFFT sample size
    starts  = starts[starts + NFFT < len(ts)]
    xns = []
    for start in starts:
        # short term discrete fourier transform
        ts_window = get_xns(ts[start:start + NFFT]) 
        xns.append(ts_window)
    specX = np.array(xns).T
    # rescale the absolute value of the spectrogram as rescaling is standard
    spec = 10*np.log10(specX)
    #assert spec.shape[1] == len(starts) 
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

# CODE to download dictionaries
# RUN once
import pickle
f = open("zeroNoise.pkl","wb")
pickle.dump(zero,f)
f.close()
f = open("oneNoise.pkl","wb")
pickle.dump(one,f)
f.close()
f = open("twoNoise.pkl","wb")
pickle.dump(two,f)
f.close()
f = open("threeNoise.pkl","wb")
pickle.dump(three,f)
f.close()
f = open("fourNoise.pkl","wb")
pickle.dump(four,f)
f.close()
f = open("fiveNoise.pkl","wb")
pickle.dump(five,f)
f.close()
f = open("sixNoise.pkl","wb")
pickle.dump(six,f)
f.close()
f = open("sevenNoise.pkl","wb")
pickle.dump(seven,f)
f.close()
f = open("eightNoise.pkl","wb")
pickle.dump(eight,f)
f.close()
f = open("nineNoise.pkl","wb")
pickle.dump(nine,f)
f.close()

from google.colab import files

files.download('zeroNoise.pkl')
files.download('oneNoise.pkl')
files.download('twoNoise.pkl')
files.download('threeNoise.pkl')
files.download('fourNoise.pkl')
files.download('fiveNoise.pkl')
files.download('sixNoise.pkl')
files.download('sevenNoise.pkl')
files.download('eightNoise.pkl')
files.download('nineNoise.pkl')

import pickle
pickle_in = open("/content/drive/My Drive/zeroNoise.pkl","rb")
zero = pickle.load(pickle_in)
pickle_in = open("/content/drive/My Drive/oneNoise.pkl","rb")
one = pickle.load(pickle_in)
pickle_in = open("/content/drive/My Drive/twoNoise.pkl","rb")
two = pickle.load(pickle_in)
pickle_in = open("/content/drive/My Drive/threeNoise.pkl","rb")
three = pickle.load(pickle_in)
pickle_in = open("/content/drive/My Drive/fourNoise.pkl","rb")
four = pickle.load(pickle_in)
pickle_in = open("/content/drive/My Drive/fiveNoise.pkl","rb")
five = pickle.load(pickle_in)
pickle_in = open("/content/drive/My Drive/sixNoise.pkl","rb")
six = pickle.load(pickle_in)
pickle_in = open("/content/drive/My Drive/sevenNoise.pkl","rb")
seven = pickle.load(pickle_in)
pickle_in = open("/content/drive/My Drive/eightNoise.pkl","rb")
eight = pickle.load(pickle_in)
pickle_in = open("/content/drive/My Drive/nineNoise.pkl","rb")
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
    """Computes signal energy of frame"""
    return np.sum(frame ** 2) / np.float64(len(frame))


def energy_entropy(frame, n_short_blocks=10):
    """Computes entropy of energy"""
    # total frame energy
    frame_energy = np.sum(frame ** 2)
    frame_length = len(frame)
    sub_win_len = int(np.floor(frame_length / n_short_blocks))
    if frame_length != sub_win_len * n_short_blocks:
        frame = frame[0:sub_win_len * n_short_blocks]

    # sub_wins is of size [n_short_blocks x L]
    sub_wins = frame.reshape(sub_win_len, n_short_blocks, order='F').copy()

    # Compute normalized sub-frame energies:
    s = np.sum(sub_wins ** 2, axis=0) / (frame_energy + eps)

    # Compute entropy of the normalized sub-frame energies:
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
from sklearn import svm
clf = svm.SVC()
result= clf.fit(trainFeatures, y)