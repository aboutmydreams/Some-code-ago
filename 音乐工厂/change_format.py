from pydub import AudioSegment
song = AudioSegment.from_mp3("cat.mp3")
song.export('cat.wav',format = 'wav')