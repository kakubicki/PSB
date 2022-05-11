import sounddevice 
from scipy.io.wavfile import write 

fs = 44100
duration = 2
print("Nagrywanie...")
recording = sounddevice.rec(int(duration * fs), samplerate = fs, channels = 1)
sounddevice.wait()
print("Nagrywanie zakonczone")

write("NowyPlik.wav", fs, recording) #zmienic nazwe podczas nagrywania