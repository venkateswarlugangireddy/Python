import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elv = list(data["ELEV"])
map = folium.Map(location=[32,-90], zoom_start=6, tiles="Mapbox bright")

def color_producer(elevation):
    if elevation <= 1000:
        return "green"
    elif elevation > 1000 and elevation <= 2000:
        return "orange"
    else:
        return "red"

fg = folium.FeatureGroup(name="My Map")

for lat, lon, elv in zip(lat,lon, elv):
    fg.add_child(folium.CircleMarker(location=[lat, lon], popup=str(elv), radius=6, color=color_producer(elv)))

#for coordinates in [[38.2, -99.1], [38.5, -99.4]]:
#    fg.add_child(folium.Marker(location=coordinates, popup="Hi I am a Marker", icon=folium.Icon(color="green")))
#fg.add_child(folium.Marker(location=[38.0, -99.2], popup="Hi I am a Marker", icon=folium.Icon(color="red")))
map.add_child(fg)
map.save("map1.html")