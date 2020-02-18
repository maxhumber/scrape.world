from gazpacho import get, Soup

base = "http://www.scrape.world"
url = base + "/challenges"
html = get(url)
soup = Soup(html)

challenges = []
for li in soup.find("li"):
    c = base + li.find("a").attrs["href"]
    challenges.append(c)

print(challenges)
