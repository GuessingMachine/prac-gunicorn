From flask import Flask

app = Flask(__name__)
@app.route('/')
def hello_world():
    result = {"code" : 200, "message" : "Hello World!"}
   	return result

if __name__ == '__main__':
    app.run()