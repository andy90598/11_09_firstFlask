from flask import Flask,request,render_template
from a11_3_news import news
import requests
import json

app = Flask(__name__) #這段是一定要打的
c=[]
@app.route('/',methods=['POST','GET']) #這段是路徑
def hello_world():
    if request.method=='POST':
        message = request.get_json().get('events')[0] #存對方送進來的資料
        print(message)
        replyToken=message.get('replyToken') #存token
        text=message.get('message').get('text') #存text
        sticker=message.get('message').get('stickerId')
        packageID=message.get('message').get('packageId')
        print('replay token=',replyToken)
        print('text=',text)
        a=news()
        if text in a.keys():
            for i in  a[text]:
                c=c.append(i)
                text=c
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
        else:
            data={
                "replyToken":replyToken,
                "messages":[
                    {
                        "type":"text",
                        "text":text
                    },
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