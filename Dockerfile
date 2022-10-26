FROM    python:3.6.8
ADD     ./main.py /main.py
ADD     ./wsgi.py /wsgi.py
ADD     ./requirements.txt /requirements.txt
RUN     pip3 install -r /requirements.txt
EXPOSE  8000
CMD     "gunicorn", "wsgi.app", "--bind", "0.0.0.0:8000"