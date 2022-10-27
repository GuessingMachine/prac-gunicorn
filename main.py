from flask import Flask
from flask_cors import CORS
import pymysql
host = "192.168.197.161"
user = "root"
db = "test"
passwd = "qwer1234"
port = 30000

app = Flask(__name__)
core = CORS(app, resources={r"/*" : {"origins" : "*"}})
@app.route('/hello')
def hello_world():
    DB = pymysql.connect(host=host, user=user, db=db, password=passwd, port=port, charset='utf8')
    curs = DB.cursor()
    sql = "select * from student";
    curs.execute(sql)
    rows = curs.fetchall()
    dic = {}
    for i in rows:
        dic[i[0]] = i[1]
    return dic

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)