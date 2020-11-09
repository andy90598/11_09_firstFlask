from flask import Flask,request
from a11_3_news import news
app = Flask(__name__) #這段是一定要打的

@app.route('/abc') #這段是路徑
def hello_world():
    return 'hello'

@app.route('/',methods=['POST','GET']) #增加POST GET
def hello_world2():
    if request.method=='POST':
        return "POST"
    else:
        news()
        return news()
if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000)