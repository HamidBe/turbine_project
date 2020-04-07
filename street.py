import pandas as pd
import json
import folium
from folium import FeatureGroup

import database
import numpy as np
from folium.plugins import FloatImage


# Dessine une line polygonale à partir des coordonnées GPS contenues
# dans l'objet GeoJSON
def draw_polyline(geo_json, map, color="blue", weight=5, opacity=0.6):
    data = json.loads(geo_json)
    
    if data['type'] == 'LineString':
      points = []
      for coord in data['coordinates']:
        points.append((coord[1], coord[0]))
      folium.PolyLine(points, color=color, weight=weight, opacity=opacity).add_to(map)
  
    if data['type'] == 'MultiLineString':
      for line in data['coordinates']:
        points = []
        for coord in line:
          points.append((coord[1], coord[0]))
        folium.PolyLine(points, color=color, weight=weight, opacity=opacity).add_to(map)


def draw_marker(geo_json, popup, color="green"):
    data = json.loads(geo_json)
    point = []

    for pt in data:
        point.append(pt)

    folium.Marker(
        location=[45.3311, -121.7113],
        popup=popup,
        icon=folium.Icon(color=color)
    ).add_to(map)


# Création d'une carte centrée sur Grenoble
fmap = folium.Map(location=[45.1875602, 5.7357819], tiles="OpenStreetMap", zoom_start=13.5)

# Initialisation du DataFrame df
# à partir des données du fichier CSV
#df = pd.read_csv('PLANDEVILLE_AXES-DE-VOIES_VDG_EPSG4326.json', sep = ',')

# Dessin de la rue N°67 : Avenue Jean Perrot

try:
    # La j'affiche les rues en bleu ou en rouge si l'index est pair ou impair (pour voir)
    # je vais modifier ce code pour aller chercher en base de données le sexe (male = bleu, female = rose
    conn = database.create_connection()

    cur = database.query_create_select(conn, "select genre, geojson From nom_des_voies where geojson not like '%[[[%';")

    print("Connected to database")
    list_coord = []

    for ligne in cur:
        geojson = ligne[1]
        print(geojson)
        print(geojson)
        sexe = ligne[0]

        if sexe == "masculin":
            couleur = "blue"
        elif sexe == "feminin":
            couleur = "red"
        else:
            couleur = "gray"

        draw_polyline(geojson, fmap, couleur)

    # On ajoute la légende

except Exception as e:
    print(e)

# Sauvegarde de la carte dans un fichier HTML
fmap.save("templates/street.html")



