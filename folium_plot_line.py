import folium
import database
import json

def insert_base():
    
    try:
        carto_femin= folium.Map(location=[45.16667, 5.71667],zoom_start=11) 
        conn = database.create_connection()

#        cur = database.query_create_select(conn, "Select * From nom_des_voies;")
        cur = database.query_create_select(conn, "select * From nom_des_voies where geojson not like '%[[[%';")

        print("Connected to database")
        list_coord = []

        for ligne in cur:
            geojson=ligne[15]

            genre=ligne[16]
            voie_complet=ligne[1]
            Nom = str(geojson) + " , " + str(voie_complet) + " , " +str(genre)

            Nom = str(genre)
            if genre=='':
                icon = folium.Icon(color='black')
            elif genre == 'male':
                icon = folium.Icon(color='green')
            elif genre == "female":
                icon = folium.Icon(color='orange')
            else:
                icon = folium.Icon(color='red')
            if geojson!='' :
                res = json.loads(geojson)
                print(res['coordinates'][0])

                for coord in res['coordinates']:
                    print("coord1", coord[0])
                    print("coord2", coord[1])

                    tuple_coord = (coord[0], coord[1])
                    print("tuple_coord: ", tuple_coord)

                    list_coord.append(tuple_coord)

#                    folium.Marker(tuple_coord, popup=Nom, icon=icon).add_to(carto_femin)

            print("list_coord: ", list_coord)
            folium.PolyLine(list_coord, color="blue", weight=2.5, opacity=0.8).add_to(carto_femin)

        carto_femin.save(outfile='carto_femin.html')

        
        print("Printing each row")

        
    
    except Exception as e:
            print(e)
            print("Failed to read data from  table", e)
            carto_femin.save(outfile='carto_femin.html')
    finally:
            if  conn :
                print("The  connection is closed")
                return carto_femin
insert_base()
