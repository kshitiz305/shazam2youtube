import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
driver = webdriver.Chrome(ChromeDriverManager().install())

with open("shazamlibrary.csv") as f:
    lines= f.readlines()

links = [href for line in lines for href in line.split(",") if href.startswith("https://www.shazam.com")]
# Make a request to the URL
url = "https://www.shazam.com/track/468202549/t=re-ishq-mein"
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

try:
    link = soup.find("div", {"class": "video-container"}).get("data-href")
except:
    print('Error in getting youtube link')