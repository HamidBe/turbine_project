import folium
import database
import pandas as pd
import json

# on charge la base de données centrée sur Grenoble
m = folium.Map(location=[45.1875602, 5.7357819], tiles="OpenStreetMap", zoom_start=13.5)
folium.raster_layers.TileLayer('Open Street Map').add_to(m)
folium.raster_layers.TileLayer('Stamen Terrain').add_to(m)
folium.raster_layers.TileLayer('Stamen Toner').add_to(m)
folium.raster_layers.TileLayer('Stamen Watercolor').add_to(m)
folium.raster_layers.TileLayer('CartoDB Positron').add_to(m)
folium.raster_layers.TileLayer('CartoDB Dark_Matter').add_to(m)
conn = database.create_connection()
# On crée la connexion à  la base de données
conn = database.create_connection()

# On charge les points d'intérêts depuis la base de données
cur = database.query_create_select(conn, "select * from coord_points_interets;")

# On crée la dataframe contenant les données
# Element 6 et 7 du curseur: coordonnées du point

latitude = []
longitude = []
texte = []

for ligne in cur:
    latitude.append(ligne[7])
    longitude.append(ligne[6])
    texte.append(ligne[8])

# Maintenant on construit le dataframe pour la fonction folium.Marker

data = pd.DataFrame({
    'lat': latitude,
    'lon': longitude,
    'name': texte
})

# On crée le groupe "Points d'Intérêt"
group0 = folium.FeatureGroup(name='<span style=\\"color: red;\\">Points d&apos;Intéret</span>')

# Maintenant on associe les points d'intérêt à la carte
for i in range(0, len(data)):
#    folium.CircleMarker(([data.iloc[i]['lon'], data.iloc[i]['lat']]), color='red', radius=2).add_to(group0)
    folium.Marker([data.iloc[i]['lon'], data.iloc[i]['lat']], popup=data.iloc[i]['name'][0:160]).add_to(group0)

group0.add_to(m)

group1 = folium.FeatureGroup(name='<span style=\\"color: red;\\">Routes Féminines</span>')

# On va chercher les données ne base concernant les rues dont le nom est féminin
cur = database.query_create_select(conn, "select genre, geojson From nom_des_voies where geojson not like '%[[[%' and genre = 'feminin';")

for ligne in cur:
    geojson = ligne[1]

    couleur = "red" # On affiche les rues dont le nom est féminin
    data = json.loads(geojson)

    if data['type'] == 'LineString':
        points = []

        for coord in data['coordinates']:
            points.append((coord[1], coord[0]))

            folium.PolyLine(points, color='red', weight=5, opacity=0.6).add_to(group1)

    if data['type'] == 'MultiLineString':
        for line in data['coordinates']:
            points = []
            for coord in line:
                points.append((coord[1], coord[0]))

            folium.PolyLine(points, color='red', weight=5, opacity=0.6).add_to(group1)

group1.add_to(m)

group2 = folium.FeatureGroup(name='<span style=\\"color: blue;\\">Routes Masculines</span>')


# On va maintenant chercher les données ne base concernant les rues dont le nom est masculin
cur = database.query_create_select(conn, "select genre, geojson From nom_des_voies where geojson not like '%[[[%' and genre = 'masculin';")

for ligne in cur:
    geojson = ligne[1]

    couleur = "blue" # On affiche les rues dont le nom est masculin
    data = json.loads(geojson)

    if data['type'] == 'LineString':
        points = []

        for coord in data['coordinates']:
            points.append((coord[1], coord[0]))

            folium.PolyLine(points, color='blue', weight=5, opacity=0.6).add_to(group2)

    if data['type'] == 'MultiLineString':
        for line in data['coordinates']:
            points = []
            for coord in line:
                points.append((coord[1], coord[0]))

            folium.PolyLine(points, color='blue', weight=5, opacity=0.6).add_to(group2)

group2.add_to(m)

#folium.map.LayerControl('topleft', collapsed=False).add_to(m)
folium.LayerControl().add_to(m) 
m.save("templates/street.html")