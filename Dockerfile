FROM    python:3.6.8
ADD     ./main.py /main.py
ADD     ./wsgi.py /wsgi.py
RUN     pip install --upgrade pip && pip install flask gunicorn flask_cors pymysql cryptography
EXPOSE  8000
CMD    gunicorn wsgi:app --bind 0.0.0.0:8000