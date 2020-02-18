from gazpacho import Soup
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

url = "http://scrape.world/books"

options = Options()
options.headless = True
browser = Firefox(executable_path="/usr/local/bin/geckodriver", options=options)
browser.get(url)

browser.find_element_by_xpath('//*[@id="button2"]').click()

html = browser.page_source
soup = Soup(html)

info = soup.find('div', {'id': 'div2'}).text

print(info)
