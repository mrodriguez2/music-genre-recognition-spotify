import os
import numpy as np
genres = ["classic", 'country', 'edm', 'flamenco', 'hiphop', 'indie', 'jazz', 'kpop', 'latin', 'metal', 'pop', 'rap', 'reggae', 'rock']

#for each genre in genres calculate the amount of files in the folder dataset/genre/

for genre in genres:
    path = 'dataset/training/' + genre + "/"
    os.chdir(path)

    temp_list = []

    for filename in os.listdir():
        if filename.endswith(".jpg"):
            temp_list.append(filename)

    np.random.shuffle(temp_list)

    delete = temp_list[2560:]

    for to_del in delete:
        os.remove(to_del)

    os.chdir("..")
    os.chdir("..")
    os.chdir("..")


