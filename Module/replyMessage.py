import requests
import json


def ReplayMessage(replyToken, message, text, media):
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
        data = {
            "type": "flex",
            "altText": "this is a flex message",
            "contents": {
                "type": "carousel",
                "contents": [
                    {
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
                    },
                    {
                        "type": "bubble",
                        "hero": {
                            "type": "image",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_6_carousel.png",
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
                                    "text": "Metal Desk Lamp",
                                    "weight": "bold",
                                    "size": "xl",
                                    "wrap": True,
                                    "contents": []
                                },
                                {
                                    "type": "box",
                                    "layout": "baseline",
                                    "flex": 1,
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "$11",
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
                                },
                                {
                                    "type": "text",
                                    "text": "Temporarily out of stock",
                                    "size": "xxs",
                                    "color": "#FF5551",
                                    "flex": 0,
                                    "margin": "md",
                                    "wrap": True,
                                    "contents": []
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
                                    "flex": 2,
                                    "color": "#AAAAAA",
                                    "style": "primary"
                                },
                                {
                                    "type": "button",
                                    "action": {
                                        "type": "uri",
                                        "label": "Add to wish list",
                                        "uri": "https://linecorp.com"
                                    }
                                }
                            ]
                        }
                    },
                    {
                        "type": "bubble",
                        "body": {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "button",
                                    "action": {
                                        "type": "uri",
                                        "label": "See more",
                                        "uri": "https://linecorp.com"
                                    },
                                    "flex": 1,
                                    "gravity": "center"
                                }
                            ]
                        }
                    }
                ]
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
