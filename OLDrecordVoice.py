import pyaudio
import wave
import os
import sys

path = os.path.dirname(__file__) + '/audio/' + 'RecordResult.wav'

def record_audio():
    RECORD_SECONDS = 1
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    CHUNK = 1024
   
    audio = pyaudio.PyAudio()
 
    stream = audio.open(format=FORMAT,channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
 
    print("Listening...")
 
    frames = []
 
    for i in range(int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
 
    print("Finished recording.")
 
    stream.stop_stream()
    stream.close()
    audio.terminate()
 
    waveFile = wave.open(path, 'wb')
 
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
 
    waveFile.close()
 
def read_audio():
    # function to read audio(wav) file
    with open(path, 'rb') as f:
        audio = f.read()
    return audio
       