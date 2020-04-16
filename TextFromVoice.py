from getToken import getIAMToken
import urllib.request
import json

OATH_TOKEN = "AgAAAAAsX9JLAATuwQCGu0TMUU2kl2oyjf2vlD4"
FOLDER_ID = "b1g888iudohmdqgobtgp"
IAM_TOKEN = getIAMToken(OATH_TOKEN)

def getTextFromVoice(data = None):

    if(data == None):
        with open("testvoice.ogg", "rb") as f:
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