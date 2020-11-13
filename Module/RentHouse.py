import requests
import json
from bs4 import BeautifulSoup


def Rent(text):
    cityId = {"台北市": "1", "基隆市": "2", "新北市": "3", "新竹市": "4", "新竹縣": "5", "桃園市": "6", "苗栗縣": "7", "台中市": "8", "彰化縣": "10", "南投縣": "11", "嘉義市": "12",
              "嘉義縣": "13", "雲林縣": "14", "台南市": "15", "高雄市": "17", "屏東縣": "19", "宜蘭縣": "21", "花蓮縣": "23", "台東縣": "22", "金門縣": "25", "澎湖縣": "24", "連江縣": "26"}
    if len(text.split(' '))==2: 
        cityName = text.split(' ')[1].replace('臺', '台')
    else:
        cityName=''

    if cityId.get(cityName) != None:
        cookies={
            'urlJumpIp':cityId.get(cityName)
        }
        url = 'https://rent.591.com.tw/?kind=0&region='+cityId.get(cityName)

        r = requests.get(url,cookies=cookies)
        soup = BeautifulSoup(r.text, 'html.parser')
        houseCards = soup.select('.listInfo')

        carousel = {
            "type": "carousel",
            "contents": []
        }

        count = 0
        for houseInfo in houseCards:
            imgurl = houseInfo.select('.imageBox img')[0].get('data-original')
            titleArea = houseInfo.select('.infoContent>h3>a')[0]
            title = titleArea.text
            infoUrl = 'https:'+titleArea.get('href')
            bubble = {
                "type": "bubble",
                        "direction": "ltr",
                        "header": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": title,
                                    "align": "center",
                                    "gravity": "center",
                                    "wrap": True,
                                    "contents": []
                                }
                            ]
                        },
                "hero": {
                            "type": "image",
                            "url": imgurl,
                            "size": "full",
                            "aspectRatio": "1.51:1",
                            "aspectMode": "fit"
                        },
                "footer": {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "button",
                                    "action": {
                                        "type": "uri",
                                        "label": "查看詳情",
                                        "uri": infoUrl
                                    },
                                    "color": "#43DE2BFF",
                                    "margin": "xs",
                                    "style": "link"
                                }
                            ]
                        }
            }

            if count <= 11:
                carousel['contents'].append(bubble)
            else:
                break
            count += 1

        flex_box = {
            "type": "flex",
            "altText": "this is a flex message",
            "contents": carousel
        }
        data = json.dumps(carousel, ensure_ascii=False, indent=4)
        f = open('house.json', 'w', encoding='utf-8')
        f.write(data)
        f.close
        return flex_box
    else:
        return ''
