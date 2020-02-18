from urllib.request import urlretrieve
from gazpacho import Soup
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

url = "https://www.goodreads.com/review/list/16626766"

options = Options()
options.headless = True
browser = Firefox(executable_path="/usr/local/bin/geckodriver", options=options)
browser.get(url)

html = browser.page_source
soup = Soup(html)

trs = soup.find("tr", {"class": "bookalike"})
tr = trs[0]
tr.find("a")
image_source = tr.find("img").attrs["src"]




##

url = "http://127.0.0.1:5000/books"

html = get(url)
soup = Soup(html)
images = soup.find("img")
paths = [i.attrs["src"] for i in images]

path = paths[0]

base_url = "http://127.0.0.1:5000"
for i, path in enumerate(paths):
    extension = path.split(".")[-1]
    url = base_url + path
    urlretrieve(url, f"{i}.{extension}")


#
