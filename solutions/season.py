from gazpacho import Soup
import pandas as pd
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

url = "https://scrape.world/season"

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

html = browser.page_source
soup = Soup(html)

tables = pd.read_html(browser.page_source)
east = tables[0]
west = tables[1]
df = pd.concat([east, west], axis=0)
df["W"] = df["W"].apply(pd.to_numeric, errors="coerce")
df = df.dropna(subset=["W"])
df = df[["Team", "W"]]
df = df.rename(columns={"Team": "team", "W": "wins"})
df = df.sort_values("wins", ascending=False)

print(df)
