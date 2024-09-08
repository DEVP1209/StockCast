import requests
from bs4 import BeautifulSoup
import json
import random
url = 'https://economictimes.indiatimes.com/markets'  # Replace with the URL of the website you want to scrape

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

anchor_tags = soup.find_all('a', string=lambda string: string and len(string) > 35)
anchor_data = []

for anchor in anchor_tags:
    href = anchor.get('href')
    text = anchor.text
    anchor_data.append({
        'text': text,
        'link': href
    })
random.shuffle(anchor_data)
with open('/Users/mukeshpatel/Documents/5th SEMESTER/Python/Project/chart/public/news.json', 'w') as json_file:
    json.dump(anchor_data, json_file, indent=4)
