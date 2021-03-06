import requests
import json


def ReplayMessage(replyToken, message, text, media,rent_flex):
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
        print('media=',media)
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
        data = {
            "replyToken": replyToken,
            "messages": [
                {
                    "type": "flex",
                    "altText": "this is a flex message",
                    "contents": {
                        "type": "bubble",
                        "hero": {
                            "type": "image",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_5_carousel.png",
                            "size": "full",
                            "aspectRatio": "20:13",
                            "aspectMode": "cover"
                        },
                        "body": {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "Arm Chair, White",
                                    "weight": "bold",
                                    "size": "xl",
                                    "wrap": True,
                                    "contents": []
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "$49",
                                            "weight": "bold",
                                            "size": "xl",
                                            "flex": 0,
                                            "wrap": True,
                                            "contents": []
                                        },
                                        {
                                            "type": "text",
                                            "text": ".99",
                                            "weight": "bold",
                                            "size": "sm",
                                            "flex": 0,
                                            "wrap": True,
                                            "contents": []
                                        }
                                    ]
                                }
                            ]
                        },
                        "footer": {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "button",
                                    "action": {
                                        "type": "uri",
                                        "label": "Add to Cart",
                                        "uri": "https://linecorp.com"
                                    },
                                    "style": "primary"
                                },
                                {
                                    "type": "button",
                                    "action": {
                                        "type": "uri",
                                        "label": "Add to wishlist",
                                        "uri": "https://linecorp.com"
                                    }
                                }
                            ]
                        }
                    }

                }
            ]
        }
    elif text.find('租屋') != -1:
        data = {
            "replyToken": replyToken,
            "messages": [
                rent_flex
            ]
        }
    else:
        data = {
            "replyToken": replyToken,
            "messages": [
                {
                    "type": "text",
                    "text": text
                },
                {
                    "type": "text",
                    "text": "輸入媒體名稱查看當日頭條 ex'新頭殼'"
                },
                {
                    "type": "text",
                    "text": "輸入 '租屋 縣市名' 查看租屋資訊 ex'租屋 台中市'"
                },
                {
                    "type": "text",
                    "text": "輸入 '新聞' 查看新聞標題"
                },
                {
                    "type": "text",
                    "text": "輸入剪刀石頭布 猜拳"
                },
            ]
        }
    print(json.dumps(data))
    r = requests.post(url, headers=headers, data=json.dumps(data))

    return r
