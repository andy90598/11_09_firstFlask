import requests
import json


def ReplayMessage(replyToken, replyMSG,text,sticker,packageID,media):
    #####################################################################
    ############################reply user###############################
    url = 'https://api.line.me/v2/bot/message/reply'
    accessToken = 'zTG6hdHrhApoeawkkdWpvspMdPq2Sc7SSztnQvIZmRiEWfamI8hFdMoRrpSoChN/ME27bdbC2nsCtchvVVfaY+CS0Tj8RQDAcqlTIq7ujZ6uAnn7UnmqxT/0X5fK4vq0UQrg9tEsTPJNlAT+JvOy4QdB04t89/1O/w1cDnyilFU='
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer '+accessToken  # Bearer後面要空一格
    }
    if sticker:
        data = {
            "replyToken": replyToken,
            "messages": [
                {
                    "type": "sticker",
                    "packageId": packageID,
                    "stickerId": sticker
                },
                {
                    "type": "image",
                    "originalContentUrl": "https://example.com/original.jpg",
                    "previewImageUrl": "https://example.com/preview.jpg"
                }
            ]
        }
    elif text == '新聞':
        data = {
            "replyToken": replyToken,
            "messages": [
                {
                    "type": "text",
                    "text": media
                },
                {
                    "type": "text",
                    "text": "輸入想找的媒體"
                },
            ]
        }
    r = requests.post(url, headers=headers, data=json.dumps(data))
    #####################################################################
    ############################reply user###############################
