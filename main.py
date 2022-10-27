from flask import Flask
from flask_cors import CORS
import pymysql

app = Flask(__name__)
core = CORS(app, resources={r"/*" : {"origins" : "*"}})
@app.route('/hello')
def hello_world():
    host = "mysql-svc"
    user = "root"
    db = "test"
    passwd = "qwer1234"
    DB = pymysql.connect(host=host, user=user, db=db, password=passwd, charset='utf8')
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