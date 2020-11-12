import requests
import json


def ReplayMessage(replyToken, message, text,media):
    url = 'https://api.line.me/v2/bot/message/reply'
    accessToken = 'zTG6hdHrhApoeawkkdWpvspMdPq2Sc7SSztnQvIZmRiEWfamI8hFdMoRrpSoChN/ME27bdbC2nsCtchvVVfaY+CS0Tj8RQDAcqlTIq7ujZ6uAnn7UnmqxT/0X5fK4vq0UQrg9tEsTPJNlAT+JvOy4QdB04t89/1O/w1cDnyilFU='
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer '+accessToken  # Bearer後面要空一格
    }
    if message.get('message').get('stickerId'):
        data = {
            "replyToken": replyToken,
            "messages": [
                {
                    "type": "sticker",
                    "packageId": message.get('message').get('packageId'),
                    "stickerId": message.get('message').get('stickerId')
                },
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
    elif text == '卡片':
        data={
            "type": "flex",
            "altText": "this is a flex message",
            "contents": {
                "type": "bubble",
                "header": {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {
                            "type": "text",
                            "text": "NEWS DIGEST",
                            "weight": "bold",
                            "size": "sm",
                            "color": "#AAAAAA",
                            "contents": []
                        }
                    ]
                },
                "hero": {
                    "type": "image",
                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_4_news.png",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover",
                    "action": {
                        "type": "uri",
                        "label": "Action",
                        "uri": "https://linecorp.com/"
                    }
                },
                "body": {
                    "type": "box",
                    "layout": "horizontal",
                    "spacing": "md",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "flex": 1,
                            "contents": [
                                {
                                    "type": "image",
                                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/02_1_news_thumbnail_1.png",
                                    "gravity": "bottom",
                                    "size": "sm",
                                    "aspectRatio": "4:3",
                                    "aspectMode": "cover"
                                },
                                {
                                    "type": "image",
                                    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/02_1_news_thumbnail_2.png",
                                    "margin": "md",
                                    "size": "sm",
                                    "aspectRatio": "4:3",
                                    "aspectMode": "cover"
                                }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "flex": 2,
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "7 Things to Know for Today",
                                    "size": "xs",
                                    "flex": 1,
                                    "gravity": "top",
                                    "contents": []
                                },
                                {
                                    "type": "separator"
                                },
                                {
                                    "type": "text",
                                    "text": "Hay fever goes wild",
                                    "size": "xs",
                                    "flex": 2,
                                    "gravity": "center",
                                    "contents": []
                                },
                                {
                                    "type": "separator"
                                },
                                {
                                    "type": "text",
                                    "text": "LINE Pay Begins Barcode Payment Service",
                                    "size": "xs",
                                    "flex": 2,
                                    "gravity": "center",
                                    "contents": []
                                },
                                {
                                    "type": "separator"
                                },
                                {
                                    "type": "text",
                                    "text": "LINE Adds LINE Wallet",
                                    "size": "xs",
                                    "flex": 1,
                                    "gravity": "bottom",
                                    "contents": []
                                }
                            ]
                        }
                    ]
                },
                "footer": {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {
                            "type": "button",
                            "action": {
                                "type": "uri",
                                "label": "More",
                                "uri": "https://linecorp.com"
                            }
                        }
                    ]
                }
            }
        }
    else:
        data = {
            "replyToken": replyToken,
            "messages": [
                {
                    "type": "text",
                    "text": text
                },
            ]
        }
    r = requests.post(url, headers=headers, data=json.dumps(data))
    return r
