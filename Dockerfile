FROM    python:3.6.8
ADD     ./main.py /main.py
ADD     ./wsgi.py /wsgi.py
RUN     pip install --upgrade pip && pip install flask && pip install gunicorn
EXPOSE  8000
CMD     "/usr/local/bin/gunicorn", "wsgi.app", "--bind", "0.0.0.0:8000"