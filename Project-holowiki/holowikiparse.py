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
    if 'Debuted as' in toadd or 'Mococo' in toadd:
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

nottidy.iloc[73, 1] = 'Fuwawa and Mococo Abyssgard'
print(nottidy[70:])

keep = []
for index, row in nottidy.iterrows():
    if 'HOLOSTARS' in row['gen']:
        continue
    else:
        keep.append(row)

tidy = pd.DataFrame(keep, columns=nottidy.columns)
print(tidy)