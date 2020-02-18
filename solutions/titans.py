from gazpacho import get, Soup

url = "http://www.scrape.world/titans"

html = get(url)
soup = Soup(html)

titans = soup.find("b")[1:]
titans = [t.find("a").text for t in titans]

print(titans)
