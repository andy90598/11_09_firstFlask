from flask import Flask, request, render_template
from Module.a11_3_news import news
import requests
from Module.replyMessage import ReplayMessage as rmsg
from Module.PSS import Pss
app = Flask(__name__)  # 這段是一定要打的


@app.route('/', methods=['POST', 'GET'])  # 這段是路徑
def hello_world():
    if request.method == 'POST':
        message = request.get_json().get('events')[0]  # 存對方送進來的資料
        replyToken = message.get('replyToken')  # 存token
        text = message.get('message').get('text')  # 存text
        sticker = message.get('message').get('stickerId')
        packageID = message.get('message').get('packageId')
        a = news()
        replyMSG = text
        newstitle = ''
        media = ''
        # 媒體
        for i in a['headNews'][0]:
            media = media+i+'\n'
        # 標題
        if text in a['headNews'][0].keys():
            for i in range(len(a['headNews'][0][text]['title'])):
                newstitle = newstitle+a['headNews'][0][text]['title'][i]+'\n' + \
                    a['headNews'][0][text]['link'][i] + \
                    '\n'+'------------------------'+'\n'
            replyMSG = newstitle       
        fist = ['剪刀', '石頭', '布']
        if text in fist:
            Pss(text,fist)# 猜拳
        rmsg(replyToken, replyMSG, text, sticker, packageID, media)
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
    app.run(host='127.0.0.1', port=5000)
