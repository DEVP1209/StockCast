import requests
from bs4 import BeautifulSoup
import time
import socket
import csv
def scrape_stock_data():
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

    curr_time = time.strftime("%H:%M:%S", t)
    nsechange = soup.find('div',{'id':'sp_ch_prch'}).get_text(strip=True)
    return curr_time, price , nsechange

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"  
port = 12345  
s.connect((host, port))

while True:
    time_data, price_data, price_change_data = scrape_stock_data()

    data_to_send = f"{time_data}|{price_data}|{price_change_data}\n"
    s.sendall(data_to_send.encode())
    print(data_to_send)
    time.sleep(5)  
