from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
core = CORS(app, resources={r"/*" : {"origins" : "*"}})
@app.route('/hello')
def hello_world():
    result = {"code" : 200, "message" : "Hello World!"}
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)