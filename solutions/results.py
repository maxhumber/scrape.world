from gazpacho import Soup
import pandas as pd
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select

url = "http://www.scrape.world/results"

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

# refetch page (just incase)

browser.get(url)

search = browser.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/label/input")
search.clear()
search.send_keys("toronto")

drop_down = Select(
    browser.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/label/select")
)
drop_down.select_by_visible_text("100")

html = browser.page_source
soup = Soup(html)
df = pd.read_html(str(soup.find("table")))[0]

print(df)
