from gazpacho import get, Soup

url = "https://scrape.world/spend"
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
