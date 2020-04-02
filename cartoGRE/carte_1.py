import folium
import pandas
import csv
import requests


c= folium.Map(location=[45.1875602, 5.7357819], zoom_start=10)
folium.Marker([45.1875602, 5.7357819], popup="Grenoble").add_to(c)
c.save('maCarte.html')

url="http://home/hb/PROJET/turbine_prjt/turbine_project/PLANDEVILLE_VOIES_VDG.csv"

csvfile = requests.get(url)

csvfile = csvfile.content.decode('utf-8')

fichier = pandas.read_csv("PLANDEVILLE_VOIES_VDG.csv",
          delimiter= ";",
          usecols = ["VOIE_COMPLET","TENANT","ABOUTISSANT","GeoJSON"])
		