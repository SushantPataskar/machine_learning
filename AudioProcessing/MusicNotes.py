from pydub import AudioSegment
AudioSegment.converter = r"C:\Program Files\ffmpeg-2022-12-25-git-eeb280f351-full_build\bin\ffmpeg.exe"
audio=AudioSegment.from_mp3('a1a.mp3')


import numpy as np
import sounddevice as sd
import time


saregama0=[130.81,146.83,164.81,174.61,196.00,220.00,246.94,261.63]
saregama1=[261.63,293.66,329.63,349.23,392.00,440.00,493.88,523.25]
saregama2=[523.25,587.33,659.25,698.46,783.99,880.00,987.77,1046.50]
abc=[C4,D4,E4,F4,G4,A4,B4,C5]
happy_birthday=[A4, A4, 0, B4, A4, D4,Db4,A4, A4, 0, B4, A4 ,E4, D4]
twinkle_twinkle=[C4,C4,G4,G4,A4,A4,G4,F4,F4,E4,E4,D4,D4,C4,G4,G4,F4,F4,E4,E4,D4,G4,G4,F4,F4,E4,E4,D4,C4,G4,G4,A4,G4,F4,F4,E4,E4,D4,C4]
tum_hi_ho=[F4,Ab4,C5,Db5,Ab4,Bb4,G4, F4,Ab4,C5,Db5,Ab4,Bb4,G4, F4,Ab4,C5,Db5,Ab4,Bb4,G4, F4,Ab4,C5,Db5,Ab4,Bb4,G4]

C4=261.63
Db4=277.18
D4=293.66
Eb4=311.13
E4=329.63
F4=349.23
Gb4=369.99
G4=392.00
Ab4=415.30
A4=440.00
Bb4=466.16
B4=493.88
C5=523.25
Db5=554.37
D5=587.33
Eb5=622.25
E5=659.25
F5=698.46
Gb5=739.99
G5=783.99
Ab5=830.61
A5=880.00
Bb5=932.33
B5=987.77
C6=1046.50


for freq_hz in saregama1:
    each_sample_number=np.arange(duration*sps)
    waveform=np.cos(2*np.pi*each_sample_number*freq_hz/sps)
    waveform_quiet=waveform*atten
    sd.play(waveform_quiet,sps)
    time.sleep(1)