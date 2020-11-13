import requests
import json
from bs4 import BeautifulSoup
def Rent():
    url = 'https://rent.591.com.tw/?kind=0&region=8'
    r = requests.get(url)
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
