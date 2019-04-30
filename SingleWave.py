import wave
import struct
import numpy as np

path1=r'newmyVoiceTest.wav'
path=r'iat_wav_16k.wav'
# wr = wave.openfp("myVoiceTest.wav", mode='rb')
def SingleWave(pathInput, pathOutput="new.wav"):
  wf = wave.open(pathInput, 'rb')

  nframes = wf.getnframes()
  framerate = wf.getframerate()
  str_data = wf.readframes(nframes)
  sample_width = wf.getsampwidth()
  wf.close()
  wave_data = np.fromstring(str_data, dtype=np.short)
  print(wave_data.shape)
  wave_data.shape = (-1, 2)
  wave_data = wave_data.T
  mono_wave = (wave_data[0]+wave_data[1])/2
  print(mono_wave)

  #save wav file
  wf_mono = wave.open(pathOutput,'wb')
  wf_mono.setnchannels(1)
  wf_mono.setframerate(framerate)
  wf_mono.setsampwidth(sample_width)
  for i in mono_wave:
    data = struct.pack('<h', int(i))
    wf_mono.writeframesraw( data )
  wf_mono.close()

if __name__ == '__main__':
  SingleWave('test11.wav')
# fw = wave.openfp(path1, mode='wb')
# wr = wave.openfp("iat_wav_16k.wav", mode='rb')
# sw1 = wr.readframes(10)
# fw.setnchannels(1)
# fw.setsampwidth(wr.getsampwidth())
# fw.setframerate(wr.getframerate())
# fw.writeframes(sw1)
# wr.close()
# fw.close()


# print('---------声音信息------------')
# for item in enumerate(WAVE.getparams()):
#     print(item)
# f = wave.openfp(path1,'rb')
# params = f.getparams()
# nchannels, sampwidth, framerate, nframes = params[:4]
# print(params)