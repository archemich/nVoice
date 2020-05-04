import pyaudio
import wave
import os
from playAudio import play_audio
from TextFromVoice import getTextFromVoice
from TextFromVoice import getVoiceFromText

def record(audio_name = None):

    if(audio_name == None):
        audio_name = 'AudioResult.wav'

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 16 #max 30 sec

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)


    frames = []

    for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    with wave.open(os.path.dirname(__file__) + '/audio/' + audio_name, 'wb') as f:
        f.setnchannels(CHANNELS)
        f.setsampwidth(p.get_sample_size(FORMAT))
        f.setframerate(RATE)
        f.writeframes(b''.join(frames))