import json
from urllib.request import Request, urlopen
import time
from tqdm import tqdm
import pandas as pd

def post(url, data):
    data = bytes(json.dumps(data).encode("utf-8"))
    request = Request(url=url, data=data, method="POST")
    request.add_header("Content-type", "application/json; charset=UTF-8")
    with urlopen(request) as response:
        data = json.loads(response.read().decode("utf-8"))
    return data

url = "https://scrape.world/demand"

start = pd.Timestamp('today')
end = start + pd.Timedelta('7 days')
stamps = pd.date_range(start=start, end=end, freq='H')

demand = {}
for date in tqdm(stamps):
    date = date.strftime("%Y-%m-%d %H:00")
    data = {
        "date": date,
        "temperature": 21
    }
    mw = post(url, data)
    time.sleep(0.1)
    demand[date] = mw

df = pd.DataFrame(demand).T
