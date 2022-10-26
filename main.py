From flask import Flask # 서버 구현을 위한 flask import

app = Flask(__name__)


@app.route('/')
def hello_world():
    result = {"code" : 200, "message" : "Hello World!"}
   	return result

if __name__ == '__main__':
    app.run()