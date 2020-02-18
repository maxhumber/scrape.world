from gazpacho import get, Soup

url = "http://www.scrape.world"
html = get(url)
soup = Soup(html)

hidden = soup.find("p")[3].text

print(hidden)
