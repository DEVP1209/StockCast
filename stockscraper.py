import requests
from bs4 import BeautifulSoup
import time
import csv
while True:

    url = "https://www.moneycontrol.com/india/stockpricequote/auto-lcvshcvs/tatamotors/TM03"
    r = requests.get(url)
    t = time.localtime()
    soup = BeautifulSoup(r.text,'html.parser')
    name = soup.find('div',{'id':'stockName'}).find_all('h1')[0].text
    input_tag = soup.find('input',{'id':'nsespotval'})
    if input_tag:
        price = input_tag["value"]
    else:
        print("Input tag not found.")

    nsechange = soup.find('div',{'class':'nsechange'}).text.split(' ')[0]
    print(time.strftime("%H:%M:%S", t),name, price , nsechange)
    with open(f'{name}_data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        # Append new data to CSV
        writer.writerow([name, price, nsechange,time.strftime('%Y-%m-%d %H:%M:%S')])
    time.sleep(2)