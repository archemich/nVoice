import requests
import json

#get IAM_TOKEN
def getIAMToken(OATH_TOKEN):

    data = "{\"yandexPassportOauthToken\":\"%s\"}" % OATH_TOKEN
    request = requests.post('https://iam.api.cloud.yandex.net/iam/v1/tokens', data=data)
    IAM_TOKEN = request.json()["iamToken"]

    return IAM_TOKEN
