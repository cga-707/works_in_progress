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
        album_length.append(row[3])
        release_year.append(row[4])
        rating.append(row[5])
        total_albums += 1

# Gets the representation of genres in these albums and puts them in a dict
genre_count = dict()

for item in genre:
    genre_count[item] = genre.count(item)

genre_makeup = list()
for item in genre_count.keys():
    value =  (genre_count[item] / total_albums) * 100
    genre_makeup.append(value)

plt.style.use('seaborn')
fig, ax = plt.subplots(figsize=(15, 7.5))

labels = genre_count.keys()
sizes = genre_makeup
explode = (0.1, 0, 0, 0)

ax.set_title("Genre Breakdown", fontsize=18, fontweight=1000, loc='left')
ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
       shadow=True, startangle=90)
ax.axis('equal')

plt.show()





