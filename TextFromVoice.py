from getToken import getIAMToken
from PcmToWav import convert
from playAudio import play_audio

import speech_recognition as sr
import soundfile as sf
import urllib.request

import os
import requests
import json

OATH_TOKEN = "AgAAAAAsX9JLAATuwQCGu0TMUU2kl2oyjf2vlD4"
FOLDER_ID = "b1g888iudohmdqgobtgp"
IAM_TOKEN = getIAMToken(OATH_TOKEN)


#Распознавание голоса
def RecordRecognizeVoice():
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as first:
        print("Говорите...")
        r.adjust_for_ambient_noise(first, duration=1)
        audio = r.listen(first)
    try:
        answer = r.recognize_google(audio, language="ru-RU").lower()
    except sr.UnknownValueError:
        getVoiceFromText("Простите, я не рассл+ышала.")
        play_audio()
        RecordRecognizeVoice()

    return answer


def getVoiceToBin(text):
    url = 'https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize'

    headers = {
        'Authorization': 'Bearer ' + IAM_TOKEN,
    }

    data = {
        "text": text,
        "lang": "ru-RU",
        "speed": 1,
        "voice": "alena",
        "emotion": "good",
        'folderId': FOLDER_ID,
        'format': 'lpcm'
    }

    with requests.post(url, headers=headers, data=data, stream=True) as resp:
        if resp.status_code != 200:
            raise RuntimeError("Invalid response received: code: %d, message: %s" % (resp.status_code, resp.text))

        for chunk in resp.iter_content(chunk_size=None):
            yield chunk

#Синтез голоса
#getVoiceFromText(<текст>, <название аудиофайла с синтезированным голосом>, <промежуточный файл(не рекомендуется менять)>)
def getVoiceFromText(text = "Это тест ало ало", audio_name = 'AudioResult', name = 'output.pcm'):
    with open(os.path.dirname(__file__) + '/workfiles/' + name, "wb" ) as f:
        for audio_content in getVoiceToBin(text):
            f.write(audio_content)

    convert(os.path.dirname(__file__) + '/workfiles/' + name, os.path.dirname(__file__) + '/audio/' + audio_name + '.wav')

