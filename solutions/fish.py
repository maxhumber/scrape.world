import re
from textwrap import indent
from urllib.request import urlopen
from gazpacho import get, Soup
from PIL import Image # pip install pillow
import pytesseract # pip install pytesseract

base = 'http://scrape.world'
url = base + '/fish'
html = get(url)
soup = Soup(html)

imgs = soup.find('img')[1:]
paths = [i.attrs['src'] for i in imgs]

images = []
for path in paths:
    url = base + path
    im = Image.open(urlopen(url))
    images.append(im)

text = ''
for image in images:
    i2t = pytesseract.image_to_string(image)
    text += i2t

pattern = re.compile('(?<![.!?\’\”\'])\n')
text = re.sub(pattern, ' ', text)
text = indent(text, '\t')

print(text)
