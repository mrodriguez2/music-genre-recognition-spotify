import os
from pydub import AudioSegment

genres = ["classic", 'country', 'edm', 'flamenco', 'hiphop', 'indie', 'jazz', 'kpop', 'latin', 'metal', 'pop', 'rap', 'reggae', 'rock']

for genre in genres:
    print('Processing ' + genre)
    path = '9_sec_dataset/' + genre + "/"
    os.chdir(path)
    audio_files = os.listdir()

    audio_files = [x for x in audio_files if x.endswith(".wav")]

    for file in audio_files:
        name, ext = os.path.splitext(file)
        parts = name.split("_")
        try:
            if int(parts[1]) % 3 == 0:
                sound1 = AudioSegment.from_wav(parts[0] + "_" + parts[1] + ".wav")
                sound2 = AudioSegment.from_wav(parts[0] + "_" + str(int(parts[1]) + 1) + ".wav")
                sound3 = AudioSegment.from_wav(parts[0] + "_" + str(int(parts[1]) + 2) + ".wav")
                combined_sounds = sound1 + sound2 + sound3 
                combined_sounds.export("joined_" + str(name) + ".wav", format = "wav")
        except:
            print("no hay mas")
    
    os.chdir("..")
    os.chdir('..')

        




