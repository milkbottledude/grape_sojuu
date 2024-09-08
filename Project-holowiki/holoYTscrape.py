import pandas as pd
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
csvfile_path = r"C:\Users\Yu Zen\Documents\Coding\grape_soju\Project-holowiki\tidy_fanwiki.csv"

table = pd.read_csv(r"C:\Users\Yu Zen\Documents\Coding\grape_soju\Project-holowiki\tidy_fanwiki.csv")
print(table)
driver_service = Service(executable_path=r"C:\Users\Yu Zen\Documents\Coding\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)

subs = []
vids = []
def getYT2(url):
    driver.get(url)
    driver.implicitly_wait(10) # if your device or internet is slow, try this. Otherwise, its optional
    try:
        lines = driver.find_elements(By.CSS_SELECTOR, "span[dir='auto'][role='text'][class='yt-core-attributed-string yt-content-metadata-view-model-wiz__metadata-text yt-core-attributed-string--white-space-pre-wrap yt-core-attributed-string--link-inherit-color']")
        for line in lines:
            info = line.text
            print(info)
            if 'subscribers' in info:
                subs.append(info)
            elif 'videos' in info:
                vids.append(info)
            
    except Exception as e:
        print(f"Error: {e}")
    

for url in table['channel_url']:
    getYT2(url)
driver.quit()

# getYT2('https://www.youtube.com/@HoshimachiSuisei')


table['Subs'] = subs
table['vids'] = vids
table.to_csv(csvfile_path, mode='w', header=True, index=False)