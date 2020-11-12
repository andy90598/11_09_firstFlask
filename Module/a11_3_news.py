import requests
import json
from bs4 import BeautifulSoup
def news():
    r=requests.get('https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFZxYUdjU0JYcG9MVlJYR2dKVVZ5Z0FQAQ?hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant')
    soup=BeautifulSoup(r.text,'html.parser')
    data=soup.select('.VDXfz+h3')
    link=soup.select('.VDXfz+h3>a')
    data2=soup.select('H3 ~ .QmrVtf.RD0gLb.kybdz>.SVJrMe>a')
    b={}
    c={'headNews':[]}

    for i in range (len(data)):
        if b.get(data2[i].text)==None:
            b[data2[i].text]={
                'title':[],
                'link':[]
            }
        b[data2[i].text]['title'].append(data[i].text)
        b[data2[i].text]['link'].append('https://news.google.com/'+link[i].get('href')[2:])
    c['headNews'].append(b)
    return c
# a=news()
# newstitle=''
# for i in range(len(a['headNews'][0]['新頭殼']['title'])) :
#     newstitle=newstitle+a['headNews'][0]['新頭殼']['title'][i]+'\n'+a['headNews'][0]['新頭殼']['link'][i]+'\n'+'------------------------'+'\n'
# print(newstitle)
# str1=json.dumps(a,indent=4,ensure_ascii=False)
# f=open('./json/news.json','w',encoding='UTF-8')
# f.write(str1)
# f.close()
