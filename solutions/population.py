# TODO

from gazpacho import Soup
import pandas as pd
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

# TODO
base = "https://scrape.world/"
base = "http://localhost:5000/"
endpoint = "population"
url = base + endpoint

options = Options()
options.headless = True
browser = Firefox(executable_path="/usr/local/bin/geckodriver", options=options)
browser.get(url)



# username

username = browser.find_element_by_id("username")
username.clear()
username.send_keys("admin")

# password

password = browser.find_element_by_name("password")
password.clear()
password.send_keys("admin")

# submit

browser.find_element_by_xpath("/html/body/div/div/form/div/input[3]").click()
