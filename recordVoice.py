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
    RECORD_SECONDS = 30
    WAVE_OUTPUT_FILENAME = os.path.dirname(__file__) + '/audio/' + audio_name

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)


    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


record()
play_audio()
print(getTextFromVoice(name = "AudioResult"))