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


nottidy = pd.DataFrame(columns=['emblem', 'name', 'date', 'gen'])
row = []

reset = 0
for dongxi in data:
    if reset == 4:
        row = pd.DataFrame([row], columns=nottidy.columns)
        nottidy = pd.concat([nottidy, row], ignore_index=True)
        row = []
        row.append(dongxi)
        reset = 1
    else:
        row.append(dongxi)
        reset += 1

print(nottidy[70:])