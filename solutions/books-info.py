import time
from gazpacho import Soup
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

url = "https://scrape.world/books"

options = Options()
options.headless = True
browser = Firefox(executable_path="/usr/local/bin/geckodriver", options=options)
browser.get(url)
time.sleep(0.5)

browser.find_element_by_xpath('//*[@id="button2"]').click()
time.sleep(0.5)

html = browser.page_source
soup = Soup(html)

info = soup.find('div', {'id': 'div2'}).text

print(info)
