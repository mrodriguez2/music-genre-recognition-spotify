import os
import time
import shutil
import librosa
import numpy as np
import matplotlib.pyplot as plt

def generate_spectogram_for_g(g):
  j = 0
  print(g)
  for filename in os.listdir("files"):
    if filename.endswith(".wav") and g in filename:
      start_time = time.time()
      song  =  os.path.join("files", filename)
      j = j+1

      x, sr = librosa.load(song, sr = None)
      X = librosa.stft(x)
      Xdb = librosa.amplitude_to_db(abs(X))
      librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='log')
      plt.axis('off')

      #check if song file exists
      if os.path.isfile(filename.replace(".wav", ".jpg")):
        continue
      else:
        print("saved {}".format(filename))
        plt.savefig(os.path.join("files", filename.replace(".wav", ".jpg")), bbox_inches='tight')
        plt.cla()
        print("--- %s seconds ---" % (time.time() - start_time))


genres = ["classic", 'country', 'edm', 'flamenco', 'hiphop', 'indie', 'jazz', 'kpop', 'latin', 'metal', 'pop', 'rap', 'reggae', 'rock']

#We will use 3200 samples per class, split into 80% training, 10% validation, and 10% testing
samples = 1000
validation_split = 0.1
testing_split = 0.1
training_split = 0.8

path = '9_sec_dataset'
os.chdir(path)

for genre in genres:
  print('Processing ' + genre)

  temp_list = []

  for filename in os.listdir(genre):
    if filename.endswith(".jpg"):
      temp_list.append(filename)

  #randomly shuffle elements in temp_list
  np.random.shuffle(temp_list)

  validation = temp_list[:int(samples * validation_split)]
  testing = temp_list[int(samples * validation_split) : int(samples * validation_split + samples * testing_split)]
  training = temp_list[int(samples * validation_split + samples * testing_split) : int(samples * validation_split + samples * testing_split + samples * training_split)]

  for image in validation:
    shutil.move(os.path.join(genre, image), os.path.join("validation", genre, image))
  for image in testing:
    shutil.move(os.path.join(genre, image), os.path.join("testing", genre, image))
  for image in training:
    shutil.move(os.path.join(genre, image), os.path.join("training", genre, image))