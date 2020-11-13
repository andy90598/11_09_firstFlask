from flask import Flask, request, render_template
from Module.NewsTitle import NewsTopic
from Module.replyMessage import ReplayMessage as rmsg
from Module.PSS import Pss
from Module.a113news import news
from Module.RentHouse import Rent
import requests
import atexit

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

app = Flask(__name__)  # 這段是一定要打的


def print_date_time():
    r = requests.get('https://andy-flask.herokuapp.com/')
    print(r.text)


scheduler = BackgroundScheduler()
scheduler.add_job(
    func=print_date_time,
    trigger=IntervalTrigger(minutes=20),
)
scheduler.start()
# atexit.register(lambda: scheduler.shutdown())


@app.route('/', methods=['POST', 'GET'])  # 這段是路徑
def hello_world():
    if request.method == 'POST':
        message = request.get_json().get('events')[0]  # 存對方送進來的資料
        replyToken = message.get('replyToken')  # 存token
        text = message.get('message').get('text')  # 存text
        rent_flex=''
        media = ''


        list_media = []
        a = news()
        for i in a['headNews'][0]:
            list_media.append(i)

        fist = ['剪刀', '石頭', '布']
        if text in fist:
            text = Pss(text, fist)  # 猜拳
        if text == '新聞':
            a = news()
            media = NewsTopic(text,a)
        elif text in list_media:
            a = news()
            text = NewsTopic(text, a)
        elif text =='591':
            rent_flex=Rent()
            
            



########################排程器########################
        # scheduler = BackgroundScheduler()
        # scheduler.start()
        # scheduler.add_job(
        #     func=print_date_time,
        #     trigger=IntervalTrigger(seconds=3),
        #     replace_existing=True)
        # atexit.register(lambda: scheduler.shutdown())
########################排程器########################

        rmsg(replyToken, message, text,media,rent_flex)
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

    app.run(host='127.0.0.1', port=5000, debug=True)
