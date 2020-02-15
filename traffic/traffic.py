import datetime
import math
import os
import random
import time

import pandas as pd
import psycopg2 # pip install psycopg2-binary
import schedule # pip install schedule
from sqlalchemy import create_engine # pip install SQLAlchemy

SCRAPE_PASSWORD = os.environ.get('SCRAPE_PASSWORD')
SCRAPE_PASSWORD = 'scrape-the-world-42'

ENGINE = create_engine(f'postgresql+psycopg2://postgres:{SCRAPE_PASSWORD}@165.22.239.165/postgres')

def now():
    return datetime.datetime.now()

def time_to_seconds(x):
    hs = x.hour * 60 * 60
    ms = x.minute * 60
    ss = x.second
    return hs + ms + ss

def generate_traffic(timestamp=None):
    if not timestamp:
        timestamp = now()
    x = time_to_seconds(timestamp)
    seconds_in_day = 24*60*60
    y = 30 + 25 * math.cos(2*math.pi*x / seconds_in_day)
    y += random.normalvariate(0, 8)
    y = max(0, y)
    y = int(round(y))
    return y

def decompose_minutes(minutes):
    hour = minutes // 60
    minute = minutes % 60
    return hour, minute

def simulate_time(minutes, day=None):
    hour, minute = decompose_minutes(minutes)
    today = datetime.date.today()
    year, month = today.year, today.month
    if not day:
        day = today.day
    return datetime.datetime(year, month, day, hour, minute)

def seed_database():
con = ENGINE.connect()
cur = ENGINE.cursor()
pd.read_sql('drop table visits', con)
x = range(0, 1440, 5)
t = [simulate_time(xi, 13) for xi in x]
y = [generate_traffic(ti) for ti in t]
df = pd.DataFrame({'date': t, 'traffic': y})
df.to_sql('visits', con, index=False, if_exists='replace')
con.close()

def traffic_to_database():
    con = ENGINE.connect()
    t = now()
    y = generate_traffic(t)
    df = pd.DataFrame({'date': [t], 'traffic': [y]})
    df.to_sql('visits', con, index=False, if_exists='append')
    con.close()


con = ENGINE.connect()
pd.read_sql('select * from visits', con).tail()
con.close()


if __name__ == '__main__':
    schedule.every().minute.do(traffic_to_database)
    while True:
        schedule.run_pending()
