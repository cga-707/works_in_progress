import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structures of the data
filename = 'data_2/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']
data_title = all_eq_data["metadata"]["title"]

mags, lons, lats, hover_text = [], [], [], []
for eq_dict in all_eq_dicts:
    title = eq_dict['properties']['title']
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_text.append(title)

# Map the earthquakes
data = [{'type': 'scattergeo',
         'lon': lons,
         'lat': lats,
         'text': hover_text,
         'marker': {
             'size': [3*mag for mag in mags],
             'color': mags,
             'colorscale': 'Reds',
             'colorbar': {'title': 'Magnitude'}
         }
}]
my_layout =  Layout(title=data_title)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')