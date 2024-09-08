# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
import sys


# %%
stock = sys.argv[1]
reliance=yf.Ticker(stock)
history=reliance.history(period="5y")
df=pd.DataFrame(history)


# ARIMA Model:- 

data = list(df["Close"])



# %%
from pmdarima.arima.utils import ndiffs
d_value = ndiffs(data,test = "adf")
print("d value:", d_value)

# %%
from statsmodels.tsa.arima.model import ARIMA
from pmdarima import auto_arima

# %%
x_train= data[:-100]
x_test = data[-100:]
print(len(x_train),len(x_test))

# %%
stepwise_fit = auto_arima(data,trace=True,suppress_warnings=True, seasonal=True)
print(stepwise_fit.summary())

# %%
import statsmodels.api as sm
model = sm.tsa.arima.ARIMA(data, order=(2,1,2))
# stock_data['Monday'] = (stock_data['date'].dt.dayofweek == 0).astype(int)
# model = sm.tsa.SARIMAX(stock_data['stock_price'], exog=stock_data['Monday'], order=(p, d, q), seasonal_order=(P, D, Q, m))
# %%
model = model.fit()
model.summary()

# %%
start=len(x_train)
end=len(x_train)+len(x_test)-1
pred = model.predict(start=start,end=end)
pred

# %%
s = pd.Series(pred, index =df.index[-100:])
s


# %%
from statsmodels.graphics.tsaplots import plot_predict
plot_predict(model, start = len(data)-500, end = len(data)+10, dynamic = False);

# %%
from sklearn.metrics import mean_squared_error
np.sqrt(mean_squared_error(x_test,pred))

# %%
from sklearn.metrics import r2_score
r2_score(x_test,pred)

# %% [markdown]
# # Predicting Future values:

# %%
Close_pred = model.predict(start=end+1,end=end+3)
Close_pred

# %%
import datetime
df.index = pd.to_datetime(df.index)

# Change the index format to 'YYYY-MM-DD'
df.index = df.index.strftime('%Y-%m-%d')
df.index

# %%
last_index_date = pd.to_datetime(df.index[-1])

# Get the next 3 days from the last index date
future_dates = [last_index_date + datetime.timedelta(days=i) for i in range(1, 4)]

# Convert future dates to the desired string format 'YYYY-MM-DD'
future_dates_formatted = [date.strftime('%Y-%m-%d') for date in future_dates]

print("Next 3 Days from the Last Index Date:")
print(future_dates_formatted)

# %%
CLOSE_PREDICTION = pd.Series(Close_pred, index = future_dates_formatted)
CLOSE_PREDICTION

# %%
plt.figure(figsize=(10,6), dpi=100)
df['Close'][-200:].plot(label='Actual Stock Price', legend=True)
CLOSE_PREDICTION.plot(label='Future Predicted Price', legend=True)

# %% [markdown]
# Open

# %%
data = list(df["Open"])

# %%
d_value = ndiffs(data,test = "adf")
print("d value:", d_value)

# %%
x_train= data[:-100]
x_test = data[-100:]
print(len(x_train),len(x_test))

# %%
stepwise_fit = auto_arima(data,trace=True,suppress_warnings=True, seasonal=True)
model = sm.tsa.arima.ARIMA(data, order=(2,1,2))
model = model.fit()
start=len(x_train)
end=len(x_train)+len(x_test)-1
pred = model.predict(start=start,end=end)

# %%
np.sqrt(mean_squared_error(x_test,pred))

# %%
r2_score(x_test,pred)

# %%
Open_pred = model.predict(start=end+1,end=end+3)

# %% [markdown]
# High

# %%
data = list(df["High"])

# %%
d_value = ndiffs(data,test = "adf")
print("d value:", d_value)

# %%
x_train= data[:-100]
x_test = data[-100:]

# %%
stepwise_fit = auto_arima(data,trace=True,suppress_warnings=True, seasonal=True)
model = sm.tsa.arima.ARIMA(data, order=(2,1,2))
model = model.fit()
start=len(x_train)
end=len(x_train)+len(x_test)-1
pred = model.predict(start=start,end=end)
pred

# %%
np.sqrt(mean_squared_error(x_test,pred))

# %%
r2_score(x_test,pred)
High_pred = model.predict(start=end+1,end=end+3)
High_pred


# Low
data = list(df["Low"])

d_value = ndiffs(data,test = "adf")
print("d value:", d_value)


x_train= data[:-100]
x_test = data[-100:]

stepwise_fit = auto_arima(data,trace=True,suppress_warnings=True, seasonal=True)
model = sm.tsa.arima.ARIMA(data, order=(2,1,2))
model = model.fit()
start=len(x_train)
end=len(x_train)+len(x_test)-1
pred = model.predict(start=start,end=end)


np.sqrt(mean_squared_error(x_test,pred))

r2_score(x_test,pred)

Low_pred = model.predict(start=end+1,end=end+3)
Low_pred


data = {
    'Open': Open_pred,
    'High': High_pred,
    'Low': Low_pred,
    'Close': Close_pred
}

PREDICTION = pd.DataFrame(data, index=future_dates_formatted)
PREDICTION.index.name = 'Date'
df = pd.concat([df, PREDICTION])
df.reset_index(inplace=True) 
df

# %%
stock_name = stock.split(".")[0]
df.to_csv(f'/Users/mukeshpatel/Documents/5th SEMESTER/Python/Project/CSV/{stock_name}.csv', index=False)

# %%
import csv
import json
from datetime import datetime
import time
csv_file = f'/Users/mukeshpatel/Documents/5th SEMESTER/Python/Project/CSV/{stock_name}.csv'
json_file = f'/Users/mukeshpatel/Documents/5th SEMESTER/Python/Project/chart/public/candlestick/{stock_name}.json'

data = []

with open(csv_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    headers = next(csvreader)  # Assuming the first row contains column headers
    for row in csvreader:
        date_str = row[0].split("+")[0]
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')  
        # unix_timestamp = int(time.mktime(date_obj.timetuple()))
        open_price = round(float(row[1]),2)
        high_price = round(float(row[2]),2)
        low_price = round(float(row[3]),2)
        close_price = round(float(row[4]),2)
        
        data_point = {
            "x": date_str,
            "y": [open_price, high_price, low_price, close_price]
        }
        data.append(data_point)

with open(json_file, 'w') as jsonfile:
    json.dump(data[-100:], jsonfile, indent=2)

print("Conversion complete. JSON data saved to", json_file)