import re
from gazpacho import get, Soup
import pandas as pd
import numpy as np

url = 'https://www.hockey-reference.com/leagues/NHL_2020_games.html'
html = get(url)

d = {
    'Boston Bruins': 'Boston Kodiaks',
    'Tampa Bay Lightning': 'Tampa Bay Thunder',
    'Florida Panthers': 'Florida Jaguars',
    'Toronto Maple Leafs': 'Toronto Pine Needles',
    'Montreal Canadiens': 'Montreal Quebecers',
    'Buffalo Sabres': 'Buffalo Knives',
    'Ottawa Senators': 'Ottawa Legislators',
    'Detroit Red Wings': 'Detroit Carmine Feathers',
    'Washington Capitals': 'Washington Investments',
    'Pittsburgh Penguins': 'Pittsburgh Puffins',
    'New York Islanders': 'New York Indwellers',
    'Columbus Blue Jackets': 'Columbus Navy Coats',
    'Carolina Hurricanes': 'Carolina Cyclones',
    'Philadelphia Flyers': 'Philadelphia Travellers',
    'New York Rangers': 'New York Officials',
    'New Jersey Devils': 'New Jersey Demons',
    'St. Louis Blues': 'St. Louis Doldrums',
    'Colorado Avalanche': 'Colorado Landslide',
    'Dallas Stars': 'Dallas Celebrities',
    'Nashville Predators': 'Nashville Carnivores',
    'Winnipeg Jets': 'Winnipeg Airplanes',
    'Chicago Blackhawks': 'Chicago Greyfalcons',
    'Minnesota Wild': 'Minnesota Savage',
    'Vancouver Canucks': 'Vancouver Whales',
    'Edmonton Oilers': 'Edmonton Workers',
    'Vegas Golden Knights': 'Vegas Shining Templars',
    'Arizona Coyotes': 'Arizona Dingos',
    'Calgary Flames': 'Calgary Flares',
    'San Jose Sharks': 'San Jose Charlatans',
    'Anaheim Ducks': 'Anaheim Mallards',
    'Los Angeles Kings': 'Los Angeles Monarchs'
}

pattern = re.compile(r'\b(' + '|'.join(d.keys()) + r')\b')
html = pattern.sub(lambda x: d[x.group()], html)
soup = Soup(html)
table = soup.find('table', {'id': 'games'})

df = pd.read_html(str(table))[0]
df = df.rename(columns={
    'Date': 'date',
    'Visitor': 'away',
    'Home': 'home',
    'G': 'goals_away',
    'G.1': 'goals_home',
    'Unnamed: 5': 'extra_time_loss'
})
df = df.dropna(subset=['goals_away'])
df['extra_time_loss'] = ~df['extra_time_loss'].isna()
df['extra_time_loss'] = df['extra_time_loss'].apply(int)
df['date'] = df['date'].apply(pd.to_datetime)
df['day'] = df['date'].apply(lambda x: (x - pd.Timestamp('2019-10-02')).days + 1)
df = df[['day', 'away', 'goals_away', 'home', 'goals_home', 'extra_time_loss']]
df.to_csv('data/hockey.csv', index=False)
