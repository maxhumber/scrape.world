from gazpacho import get, Soup

url = "https://scrape.world"
html = get(url)
soup = Soup(html)

hidden = soup.find("p")[3].text

print(hidden)
