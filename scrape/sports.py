from gazpacho import Soup
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

url = "http://www.scrape.world/spend"

options = Options()
options.headless = True
browser = Firefox(executable_path="/usr/local/bin/geckodriver", options=options)
browser.get(url)

username = browser.find_element_by_id("username")
username.clear()
username.send_keys("admin")

password = browser.find_element_by_name("password")
password.clear()
password.send_keys("admin")

browser.find_element_by_xpath("/html/body/div/div/form/div/input[3]").click()

html = browser.page_source
soup = Soup(html)

trs = soup.find("tr", {"class": "tmx"})


def parse_tr(tr):
    team = tr.find("td", {"data-label": "TEAM"}).text
    spend = float(
        tr.find("td", {"data-label": "TODAYS CAP HIT"}).text.replace(",", "")[1:]
    )
    return team, spend


spend = [parse_tr(tr) for tr in trs]

url = "http://www.scrape.world/season"
browser.get(url)

tables = pd.read_html(browser.page_source)
east = tables[0]
west = tables[1]
df = pd.concat([east, west], axis=0)
df["W"] = df["W"].apply(pd.to_numeric, errors="coerce")
df = df.dropna(subset=["W"])
df = df[["Team", "W"]]
df = df.rename(columns={"Team": "team", "W": "wins"})
df
