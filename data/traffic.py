import datetime
import math
import random

def time_to_seconds(x):
    hs = x.hour * 60 * 60
    ms = x.minute * 60
    ss = x.second
    return hs + ms + ss

def generate_traffic(timestamp):
    x = time_to_seconds(timestamp)
    seconds_in_day = 24*60*60
    y = 30 + 25 * math.cos(2*math.pi*x / seconds_in_day)
    y += random.normalvariate(0, 8)
    y = max(0, y)
    return y

def decompose_minutes(minutes):
    hour = minutes // 60
    minute = minutes % 60
    return hour, minute

def simulate_time(minutes):
    hour, minute = decompose_minutes(minutes)
    today = datetime.date.today()
    return datetime.datetime(today.year, today.month, today.day, hour, minute)

generate_traffic(datetime.datetime.now())

x = range(1440)
y = [generate_traffic(simulate_time(i)) for i in x]

import matplotlib.pyplot as plt
%matplotlib inline

plt.scatter(x, y)




#
