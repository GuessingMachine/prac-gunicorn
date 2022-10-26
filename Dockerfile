FROM    python
ADD     ./main.py /main.py
ADD     ./wsgi.py /wsgi.py
ADD     ./requirements.txt /requirements.txt
RUN     pip install -r /requirements.txt
EXPOSE  8000
CMD     "gunicorn", "wsgi.app", "--bind", "0.0.0.0:8000"