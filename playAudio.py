import pyaudio
import wave
import time
import sys
import os

def play_audio(name = None):

    if(name == None):
        name = "AudioResult"

    wf = wave.open(os.path.dirname(__file__) + "/audio/" + name + ".wav", "rb")
    p = pyaudio.PyAudio()

    def callback(in_data, frame_count, time_info, status):
        data = wf.readframes(frame_count)
        return (data, pyaudio.paContinue)

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=1,
                    rate=48100,
                    output=True,
                    stream_callback=callback)

    stream.start_stream()

    while stream.is_active():
        time.sleep(0.1)

    stream.stop_stream()
    stream.close()
    wf.close()

    p.terminate()
