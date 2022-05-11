import sounddevice 
from scipy.io.wavfile import write 
from scipy.spatial import distance

from main import Sound

cepstrumMargin = 0.06

def getVoiceTrack(fname):
    voice = Sound(fname)
    voice.calculateAll(1.3, 1.6, cepstrumMargin)
    return voice.logSpectrumLP

a = getVoiceTrack("A")
e = getVoiceTrack("E")
i = getVoiceTrack("I")
o = getVoiceTrack("O")
u = getVoiceTrack("U")
y = getVoiceTrack("Y")

# input("Press any key...")
# fs = 44100
# duration = 2
# print("Nagrywanie...")
# recording = sounddevice.rec(int(duration * fs), samplerate = fs, channels = 1)
# sounddevice.wait()
# print("Nagrywanie zakonczone")
# write("recordings/temp.wav", fs, recording)

temp = Sound("temp")
temp.calculateAll(1.3, 1.6, cepstrumMargin)
tor = temp.logSpectrumLP
temp.drawSpectrogram()

# tor = a

diffa = distance.euclidean(tor, a)
diffe = distance.euclidean(tor, e)
diffi = distance.euclidean(tor, i)
diffo = distance.euclidean(tor, o)
diffu = distance.euclidean(tor, u)
diffy = distance.euclidean(tor, y)

print(f'diffa: {diffa}')
print(f'diffe: {diffe}')
print(f'diffi: {diffi}')
print(f'diffo: {diffo}')
print(f'diffu: {diffu}')
print(f'diffy: {diffy}')
