from getToken import getIAMToken
from PcmToWav import convert
import soundfile as sf
import urllib.request
import os
import requests
import json

OATH_TOKEN = "AgAAAAAsX9JLAATuwQCGu0TMUU2kl2oyjf2vlD4"
FOLDER_ID = "b1g888iudohmdqgobtgp"
IAM_TOKEN = getIAMToken(OATH_TOKEN)


#Распознавание голоса
#getTextFromVoice(<Название файла(должен находиться в audio)>)
def getTextFromVoice(name = None):

    if(name == None):
        with open(os.path.dirname(__file__) + "/audio/testvoice.ogg", "rb") as f:
            data = f.read()
    else:
        #конвертация с wav в ogg
        test, samplerate = sf.read(os.path.dirname(__file__) + "/audio/" + name + '.wav')
        sf.write(os.path.dirname(__file__) + "/audio/" + name + '.ogg', test, samplerate)

        #считывание
        with open(os.path.dirname(__file__) + "/audio/" + name + '.ogg', "rb") as f:
            data = f.read()

    params = "&".join([
        "topic=general",
        "folderId=%s" % FOLDER_ID,
        "lang=ru-RU"
    ])

    url = urllib.request.Request("https://stt.api.cloud.yandex.net/speech/v1/stt:recognize?%s" % params, data=data)
    url.add_header("Authorization", "Bearer %s" % IAM_TOKEN)

    responseData = urllib.request.urlopen(url).read().decode('UTF-8')
    decodedData = json.loads(responseData)

    if decodedData.get("error_code") is None:
        return decodedData.get("result")
    else:
        return "Повторите запрос"


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
# getVoiceFromText(<текст>, <название аудиофайла с синтезированным голосом>, <промежуточный файл(не рекомендуется менять)>)
def getVoiceFromText(text = "Это тест ало ало", audio_name = 'AudioResult', name = 'output.pcm'):
    with open(os.path.dirname(__file__) + '/workfiles/' + name, "wb") as f:
        for audio_content in getVoiceToBin(text):
            f.write(audio_content)

    convert(os.path.dirname(__file__) + '/workfiles/' + name, os.path.dirname(__file__) + '/audio/' + audio_name + '.wav')
