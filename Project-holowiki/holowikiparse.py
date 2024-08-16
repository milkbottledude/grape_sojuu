import pandas as pd
from bs4 import BeautifulSoup
import csv
import requests

url = 'https://en.wikipedia.org/wiki/Hololive_Production'
page = requests.get(url)
page_content = page.content

soup = BeautifulSoup(page_content, 'html.parser')
content = soup.find('div', class_='mw-content-ltr mw-parser-output')
all_gens_all_mems = content.find_all('div')
Hololive = content.find_all('div', class_='mw-heading mw-heading3')[3].find('h3').get_text()
branchestext = content.find_all('div', class_='mw-heading mw-heading4')[1:-4]
brunches = []
for branchtext in branchestext:
    brunches.append(branchtext.find('h4').get_text().replace(' ', '_').replace('(', '').replace(')', ''))
print(brunches)

Hololive_Japan = []
Hololive_DEV_IS = []
Hololive_Indonesia = []
Hololive_English = []

# for gen in all_gens_wmems:
#     member = gen.find_all('li')
#     for mem in member:
#         mem.find('a')   


all_divs = soup.select('div')
target_divs = [div for div in all_divs if not div.attrs and div.contents][:-13]
gen_sum = []
for div in target_divs:
    try:
        gen_sum.append(div.find('b').get_text())
    except:
        continue

for i in gen_sum[:7]:
    Hololive_Japan.append(i)
Hololive_DEV_IS.append(gen_sum[8])
for i in gen_sum[9:11]:
    Hololive_Indonesia.append(i)
for i in gen_sum[12:]:
    Hololive_English.append(i)
print(Hololive_English)


# headingcontent = content.find_all('div', class_='mw-heading mw-heading4')



