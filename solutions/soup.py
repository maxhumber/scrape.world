from gazpacho import get, Soup

url = "http://www.scrape.world/soup"
html = get(url)
soup = Soup(html)

fos = soup.find('div', {'class': 'section-speech'})

links = []
for a in fos.find("a"):
    try:
        link = a.attrs["href"]
        links.append(link)
    except AttributeError:
        pass

links = [l for l in links if "wikipedia.org" in l]

print(links)
