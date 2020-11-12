import requests
import json


def ReplayMessage(replyToken, replyMSG):
    url = 'https://api.line.me/v2/bot/message/reply'
    accessToken = 'zTG6hdHrhApoeawkkdWpvspMdPq2Sc7SSztnQvIZmRiEWfamI8hFdMoRrpSoChN/ME27bdbC2nsCtchvVVfaY+CS0Tj8RQDAcqlTIq7ujZ6uAnn7UnmqxT/0X5fK4vq0UQrg9tEsTPJNlAT+JvOy4QdB04t89/1O/w1cDnyilFU='
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer '+accessToken  # Bearer後面要空一格
    }
    data = {
        "replyToken": replyToken,
        "messages": [
            {
                "type": "text",
                "text": replyMSG
            }
        ]
    }
    r = requests.post(url, headers=headers, data=json.dumps(data))
    return r
