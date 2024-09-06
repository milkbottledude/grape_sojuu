import pandas as pd
from bs4 import BeautifulSoup
import csv
import requests
import emoji

url = 'https://hololive.wiki/wiki/Members'
page = requests.get(url)
page_content = page.content

soup = BeautifulSoup(page_content, 'html.parser')
content = soup.find('tbody')
all = content.find_all('td')

data = []
for line in all:
    toadd = str(line.get_text())
    if 'Debuted as' in toadd:
        continue
    else:
        data.append(toadd[:-1])


