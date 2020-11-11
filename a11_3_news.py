import requests
import json
from bs4 import BeautifulSoup
def news():
    r=requests.get('https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFZxYUdjU0JYcG9MVlJYR2dKVVZ5Z0FQAQ?hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant')
    soup=BeautifulSoup(r.text,'html.parser')
    data=soup.select('.VDXfz+h3')
    link=soup.select('.VDXfz')
    data2=soup.select('H3 ~ .QmrVtf.RD0gLb.kybdz>.SVJrMe>a')
    b={}
    c={'headNews':[]}

    for i in range (len(data)):
        # print(data2[i].text," ",data[i].text)
        if b.get(data2[i].text)==None:
            b[data2[i].text]={
                'title':[],
                'link':[]
            }
        b[data2[i].text]['title'].append(data[i].text)
        b[data2[i].text]['link'].append('https://news.google.com/'+link[i].get('href')[2:])
    c['headNews'].append(b)
    return c
    # str1=json.dumps(b,indent=4,ensure_ascii=False)
    # return str1
    # f=open('./json/text.json','w',encoding='UTF-8')
    # f.write(str1)
    # f.close()

# str1=json.dumps(a,indent=4,ensure_ascii=False)
# f=open('./json/news.json','w',encoding='UTF-8')
# f.write(str1)
# f.close()
# for i in a.keys():
#     print(i)
#     for j in a[i]:
#         print(j)
#     print('--------------------')


# data=soup.select('.VDXfz +h3')
# data2 = soup.select('.SVJrMe > a')
# for i in range(len(data)):
#     print(data2[i].text," ",data[i].text)
#     print("")