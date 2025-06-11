import numpy as np
import pandas as pd

df = pd.read_csv("./data/taxi_fare_data.csv", quoting=3)

pickup_datetime = df['pickup_datetime'] 

year_date = []
time = []

for data in pickup_datetime :
    year_, time_ = data.split(' ')
    year_date.append(year_)
    time.append(time_)

years = []
months = []
days = []

for data in year_date:
    y,m,d=data.split('-')
    years.append(int(y))
    months.append(int(m))
    days.append(int(d))

hours = [int(i.split(':')[0])for i in time]

print(years[:10])
print(months[:10])
print(days[:10])
print(hours[:10])