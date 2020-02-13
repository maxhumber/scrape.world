import re

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

def replace(file='caps'):
    pattern = re.compile(r'\b(' + '|'.join(d.keys()) + r')\b')
    with open(f'templates/{file}.html', 'r') as f:
        s = f.read()
    s = pattern.sub(lambda x: d[x.group()], s)
    with open(f'templates/{file}.html', 'w') as f:
        f.write(s)
