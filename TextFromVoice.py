from getToken import getIAMToken
from PcmToWav import convert

import os
import requests


OATH_TOKEN = "AgAAAAAVsAZxAATuwU7C3SKJhUrotg4wfAwpELE"
FOLDER_ID = "b1gn5u1km3uptg8mrs39"
IAM_TOKEN = getIAMToken(OATH_TOKEN)


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
