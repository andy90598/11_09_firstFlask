from flask import Flask,request,render_template
from a11_3_news import news
app = Flask(__name__) #這段是一定要打的

@app.route('/',methods=['POST','GET']) #這段是路徑
def hello_world():
    if request.method=='POST':
        data = request.get_json()
        print(data)
        print('replay token=',data['events'][0]['replyToken'])
        print('text=',data['events'][0]['message']['text'])
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