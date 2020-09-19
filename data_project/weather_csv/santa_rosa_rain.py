import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/santa_rosa_weather.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for index, name in enumerate(header_row):
        print(index, name)

# Gets dates and rain fall
    dates, rain_fall = [], []
    for row in reader:
        current_date = datetime.strptime(row[5], '%Y-%m-%d')
        rain = row[6]

        dates.append(current_date)
        rain_fall.append(rain)

# Visualize the data
plt.style.use('seaborn')
fig, ax = plt.subplots(figsize=(15, 7.5))
ax.plot(dates, rain_fall, c='blue')
plt.title('Rain in Santa Rosa', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Rainfall (mm)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
