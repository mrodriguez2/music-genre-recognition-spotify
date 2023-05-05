import os
from pydub import AudioSegment

genres = ["classic", 'country', 'edm', 'flamenco', 'hiphop', 'indie', 'jazz', 'kpop', 'latin', 'metal', 'pop', 'rap', 'reggae', 'rock']

for genre in genres:
    path = 'dataset/' + genre + "/"
    os.chdir(path)
    audio_files = os.listdir()
    for file in audio_files:
        name, ext = os.path.splitext(file)
        if ext == ".mp3":
            sound = AudioSegment.from_mp3(file)
            sound = sound.set_channels(1)
            sound = sound.set_frame_rate(22050)
            sound.export("{0}.wav".format(name), format = "wav")
    os.chdir("..")
    os.chdir('..')