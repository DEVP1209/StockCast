import matplotlib.pyplot as plt
import socket
from datetime import datetime
import time
from matplotlib.animation import FuncAnimation
MAX_DATA_POINTS = 50
time_data_list = []
price_data_list = []
# price_change_data_list = []

# Function to update the plot
def update_plot():
    plt.clf()
    time_data_list_dt = [datetime.strptime(time_str, '%H:%M:%S') for time_str in time_data_list[-MAX_DATA_POINTS:]]
    plt.plot(time_data_list_dt, price_data_list[-MAX_DATA_POINTS:], label='Price')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.legend()
    plt.title('Real-Time Stock Price')
    plt.gcf().autofmt_xdate()  # Auto-format the x-axis date
    ani = FuncAnimation(plt.gcf(), update_plot, interval=1000) 
    plt.show()  


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"  # Replace this with the IP address of the machine running the scraping program
port = 12345  # Replace this with the same port number used in the scraping program
s.bind((host, port))
s.listen()

conn, addr = s.accept()
print(f"Connection from {addr} established.")

while (True):
    data = conn.recv(1024).decode()
    if not data:
        break
    # Process the received data
    time_data, price_data, price_change_data = data.strip().split('|')
    print(time_data,price_data)
    # Append data to the lists
    time_data_list.append(time_data)

    # Step 1: Remove commas from the string
    price_float = price_data.replace(',', '')

    # Step 2: Convert the string to a float
    price_data = float(price_float)
    price_data_list.append(float(price_data))
    # price_change_data_list.append(float(price_change_data))

    # Update the plot
    update_plot()
    time.sleep(5)

conn.close()
