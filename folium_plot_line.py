import folium

gpx_file = open('path_to_gpx_file.gpx', 'r')

points = [5.73188935696086;5.1853088153218]

ave_lat = sum(p[0] for p in points)/len(points)
ave_lon = sum(p[1] for p in points)/len(points)

# Load map centred on average coordinates
my_map = folium.Map(location=[ave_lat, ave_lon], zoom_start=14)

#add a markers
for each in points:
    folium.Marker(each).add_to(my_map)

#fadd lines
folium.PolyLine(points, color="red", weight=2.5, opacity=1).add_to(my_map)

# Save map
my_map.save("./gpx_berlin_withmarker.html")