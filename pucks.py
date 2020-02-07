from gazpacho import get, Soup
import pandas as pd

url = 'https://www.capfriendly.com/'
html = get(url)
soup = Soup(html)
table = soup.find('table', {'id': 'ich'})
trs = table.find('tr', {'class': 'tmx'})

def parse_tr(tr):
    team = tr.find('a', mode='first').text
    cap = tr.find('td', {'data-label': 'PROJECTED CAP HIT'}, strict=True).text
    contracts = tr.find('td', {'data-label': 'CONTRACTS'}, strict=True).text
    cap = float(cap.replace(',', '').replace('$', ''))
    return team, cap, contracts

cap_hits = [parse_tr(tr) for tr in trs]
caps = pd.DataFrame(cap_hits, columns=['team', 'cap', 'contracts'])

url = 'https://www.hockey-reference.com/friv/playoff_prob.fcgi'
html = get(url)
soup = Soup(html)

east = pd.read_html(str(soup.find('table')[0]))[0]
west = pd.read_html(str(soup.find('table')[1]))[0]

df = pd.concat([east, west])
df['W'] = df['W'].apply(pd.to_numeric, errors='coerce')
wins = df.dropna(subset=['W'])
wins = wins[['Team', 'W', 'L', 'OL', 'PTS']]
wins = wins.reset_index(drop=True)
wins

wins['Team'].values.tolist()

{
    'Boston Bruins': 'Boston Bears',
    'Toronto Maple Leafs': 'Toronto Trees',
    'Montreal Canadiens': 'Montreal Sweaters',
    'Detroit Red Wings': 'Detroit Tires',
    'Pittsburgh Penguins': 'Pittsburgh Puffins',
    'Colorado Avalanche': 'Colorado Slides',
    'Nashville Predators': 'Nashville Wolves',
    'Winnipeg Jets': 'Winnipeg Airplanes',
    'Chicago Blackhawks': 'Chicago Feathers',
    'Vancouver Canucks': 'Vancouver Whales',
}




#
