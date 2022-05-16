import folium
import pandas as pd

my_map = folium.Map(
    location=[59.421849,17.822131],
    zoom_start=125
)

cities = pd.read_csv('allCars.csv', nrows=6)
for _, city in cities.iterrows():
    print(city)
    folium.Marker(
        location=[city['latitude'], city['longtitude']],
        popup=city['arac']
    ).add_to(my_map)
my_map.save('example1.html')
