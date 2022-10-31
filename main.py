from flask import Flask
from flask_cors import CORS
import pymysql
import os

app = Flask(__name__)
core = CORS(app, resources={r"/*" : {"origins" : "*"}})
@app.route('/hello')
def hello_world():
    host = os.environ['DB_HOST']
    user = os.environ['DB_USER']
    passwd = os.environ['MYSQL_ROOT_PASSWORD']
    db = os.environ['DB_NAME']
    DB = pymysql.connect(host=host, user=user, db=db, password=passwd, charset="utf8mb4")
    curs = DB.cursor()
    sql = "select * from student";
    curs.execute(sql)
    rows = curs.fetchall()
    result = {"code": 200, "message": rows}
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)