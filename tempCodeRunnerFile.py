import matplotlib.pyplot as plt
from datetime import datetime

time_data_list = ["15:33:11","15:33:12","15:33:13","15:33:14"]
price_data_list = [414.32,415.60,416,418]

time_data_list_dt = [datetime.strptime(time_str, '%H:%M:%S') for time_str in time_data_list]
print (time_data_list_dt)
plt.plot(time_data_list_dt, price_data_list, label='Price')
# plt.plot(time_data_list_dt, price_change_data_list, label='Price Change')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
plt.title('Real-Time Stock Price')
plt.gcf().autofmt_xdate()  # Auto-format the x-axis date
plt.show()