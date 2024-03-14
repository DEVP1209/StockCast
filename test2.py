from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import csv

# Set up the Chrome driver
options = Options()
options.headless = False  # Set to True to run in headless mode

service = Service('/usr/local/bin/chromedriver')  # Replace with the path to your chromedriver executable
driver = webdriver.Chrome(service=service, options=options)

while True:
    url = "https://www.nseindia.com/get-quotes/equity?symbol=TCS"
    try:
        # Open the URL
        driver.get(url)
        
        # Wait for the page to load (you can adjust the sleep time as needed)
        time.sleep(5)
        
        # Find and print the stock data
        name = driver.find_element(By.CSS_SELECTOR, '.nav-item.nav-link.active').text
        price = driver.find_element(By.ID, 'quoteLtp').text
        nsechange = driver.find_elements(By.ID, 'priceInfoStatus')[0].find_elements(By.TAG_NAME, 'span')
        change = nsechange[0].text
        percent = nsechange[1].text
        
        current_time = time.strftime("%H:%M:%S")
        print(current_time, name, price, change, percent)
        
        with open(f'{name}_data.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            
            # Append new data to CSV
            writer.writerow([name, price, change, percent, current_time])
        
    except Exception as e:
        print(f"An error occurred: {e}")

    time.sleep(2)

# Close the browser
driver.quit()
