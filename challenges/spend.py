from gazpacho import get, Soup

url = "http://www.scrape.world/spend"
html = get(url)
soup = Soup(html)

trs = soup.find("tr", {"class": "tmx"})

def parse_tr(tr):
    team = tr.find("td", {"data-label": "TEAM"}).text
    spend = float(
        tr.find("td", {"data-label": "TODAYS CAP HIT"}).text.replace(",", "")[1:]
    )
    return team, spend

spend = [parse_tr(tr) for tr in trs]

print(spend)

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
