FROM python:3.7

ADD traffic.py /

RUN pip install pandas psycopg2-binary schedule SQLAlchemy

CMD [ "python", "./traffic.py" ]
