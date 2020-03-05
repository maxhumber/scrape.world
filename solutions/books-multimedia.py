from pathlib import Path
from shutil import rmtree as delete
from urllib.request import urlretrieve as download
from gazpacho import get, Soup

dir = 'media'
Path(dir).mkdir(exist_ok=True)

base = 'https://scrape.world'
url = base + '/books'
html = get(url)
soup = Soup(html)

# download images

imgs = soup.find('img')
srcs = [i.attrs['src'] for i in imgs]

for src in srcs:
    name = src.split('/')[-1]
    download(base + src, f'{dir}/{name}')

# download audio

audio = soup.find('audio').find('source').attrs['src']
name = audio.split('/')[-1]
download(base + audio, f"{dir}/{name}")

# download video

video = soup.find('video').find('source').attrs['src']
name = video.split('/')[-1]
download(base + video, f"{dir}/{name}")

# clean up

delete(dir)
