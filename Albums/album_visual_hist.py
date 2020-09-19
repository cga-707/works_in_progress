import csv

import matplotlib.pyplot as plt

# Parses csv

filename = 'data/albums.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    album_name, artist_name, genre, album_length, release_year, rating =\
        [], [], [], [], [], []
    total_albums = 0
    for row in reader:
        album_name.append(row[0])
        artist_name.append(row[1])
        genre.append(row[2])
        album_length.append(int(row[3]))
        release_year.append(int(row[4]))
        rating.append(int(row[5]))
        total_albums += 1

plt.style.use('seaborn')
plt.rcdefaults()
fig, ax = plt.subplots(figsize=(15, 7.5))

print(rating)
x_c = range(24)

ax.bar(x_c, rating, width=0.8, align='edge', color=(0,0.8,0))
plt.xticks(x_c, album_name, fontsize=10, rotation=35, ha='right')
plt.title('Album Ratings')
plt.yticks(range(11))
plt.show()





