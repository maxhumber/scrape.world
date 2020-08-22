from gazpacho import Soup
import pandas as pd
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

base = "https://scrape.world/"
endpoint = "population"
url = base + endpoint

options = Options()
options.headless = True
browser = Firefox(executable_path="/usr/local/bin/geckodriver", options=options)
browser.get(url)

poplist = browser.find_element_by_id('infinite-list')

days = 365
n = 0
while n < 365:
    browser.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', poplist)
    html = browser.page_source
    soup = Soup(html)
    n = len(soup.find('ul', {'id': 'infinite-list'}).find('li'))

lis = soup.find('ul', {'id': 'infinite-list'}).find('li')

def parse_li(li):
    day, population = li.text.split(' Population ')
    population = int(population)
    day = int(day.split('Day ')[-1])
    return {'day': day, 'population': population}

population = [parse_li(li) for li in lis][:days]
