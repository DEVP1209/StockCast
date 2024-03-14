import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
import csv
while True:

    url = "https://www.moneycontrol.com/indian-indices/nifty-bank-23.html"
    r = requests.get(url)
    t = time.localtime()
    soup = BeautifulSoup(r.text,'html.parser')
    name = soup.find('div',{'class':'indices_namntab clearfix'}).find_all('h1')[0].text
    input_tag = soup.find('input',{'id':'spotValue'})
    if input_tag:
        price = input_tag["value"]
    else:
        print("Input tag not found.")

    nsechange = soup.find('div',{'id':'sp_ch_prch'}).get_text(strip=True)
    print(time.strftime("%H:%M:%S", t),name, price , nsechange)
    with open('nifty_bank_data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        
        # Append new data to CSV
        writer.writerow([name, price, nsechange,time.strftime('%Y-%m-%d %H:%M:%S')])
    
    time.sleep(2)