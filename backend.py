from flask import Flask,request,render_template
from a11_3_news import news
import requests
import json
import random

app = Flask(__name__) #這段是一定要打的

@app.route('/',methods=['POST','GET']) #這段是路徑
def hello_world():
    if request.method=='POST':        
        message = request.get_json().get('events')[0] #存對方送進來的資料
        replyToken=message.get('replyToken') #存token
        text=message.get('message').get('text') #存text
        sticker=message.get('message').get('stickerId')
        packageID=message.get('message').get('packageId')
        a=news()
        replyMSG=text
        newstitle=''
        media=''
        for i in a['headNews'][0]:
            media=media+i+'\n'
        if text in a['headNews'][0].keys():
            for i in range(len(a['headNews'][0][text]['title'])) :
                newstitle=newstitle+a['headNews'][0][text]['title'][i]+'\n'+a['headNews'][0][text]['link'][i]+'\n'+'------------------------'+'\n'
            replyMSG=newstitle
        fist = ['剪刀','石頭','布']
        if text in fist:
                ai = random.randint(0,2)
                player = fist.index(text)
                if ai == player :
                    replyMSG="電腦出"+fist[ai]+"，平手"
                elif (ai== 0 and player==1) or (ai == 1 and player == 2) or (ai == 2 and player == 0):
                    replyMSG="電腦出"+fist[ai]+"，你獲勝"
                else: 
                    replyMSG="電腦出"+fist[ai]+"，你輸了"
        # for i in a.keys():
        #     print(i)
        #     for j in a[i]:
        #         print(j)
        #     print('--------------------')
        #####################################################################
        ############################reply user###############################
        url='https://api.line.me/v2/bot/message/reply'
        accessToken='zTG6hdHrhApoeawkkdWpvspMdPq2Sc7SSztnQvIZmRiEWfamI8hFdMoRrpSoChN/ME27bdbC2nsCtchvVVfaY+CS0Tj8RQDAcqlTIq7ujZ6uAnn7UnmqxT/0X5fK4vq0UQrg9tEsTPJNlAT+JvOy4QdB04t89/1O/w1cDnyilFU='
        headers={
            'Content-Type':'application/json',
            'Authorization':'Bearer '+accessToken #Bearer後面要空一格
        }
        if sticker:
            data={
                "replyToken":replyToken,
                "messages":[
                    {
                        "type": "sticker",
                        "packageId": packageID,
                        "stickerId": sticker
                    },
                ]
            }
        elif text=='新聞':
            data={
                "replyToken":replyToken,
                "messages":[
                    {
                        "type":"text",
                        "text":media
                    },
                    {
                        "type":"text",
                        "text":"輸入想找的媒體"
                    },
                ]
            }       
        else:
            data={
                "replyToken":replyToken,
                "messages":[
                    {
                        "type":"text",
                        "text":replyMSG
                    }
                ]
            }
        r=requests.post(url,headers=headers,data=json.dumps(data))
        #####################################################################
        ############################reply user###############################
        return "POST"
    else:
        return "GET"

# @app.route('/flask',methods=['POST','GET']) #增加POST GET
# def hello_world2():
#     if request.method=='POST':
#         return "POST"
#     else:
#         title="first_template"
#         Info=[
#             {
#             'name':'andy',
#             'sex':'male'
#             },
#             {
#             'name':'jack',
#             'sex':'male'
#             },{
#             'name':'cardy',
#             'sex':'female'
#             },
#         ]
#         return render_template('hello.html',Info=Info,title=title)

# @app.route('/headnews',methods=['POST','GET'])
# def get_news():
#     news()
#     return news()

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000)