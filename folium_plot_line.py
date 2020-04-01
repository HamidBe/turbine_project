import folium
import database
def insert_base():
    
    try:
        carto_femin= folium.Map(location=[45.16667, 5.71667],zoom_start=11) 
        conn = database.create_connection()

        cur = database.query_create_select(conn, "Select * From nom_des_voies;")

        print("Connected to database")

        for ligne in cur:
            
                geojson=ligne[15]
                
                genre=ligne[16]
                voie_complet=ligne[1]
                Nom = str( geojson) + " , " + str( voie_complet) + " , " +str (genre)
                #print(Nom)
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
                    folium.Marker(geojson,popup=Nom, icon=icon).add_to(carto_femin)
            
        carto_femin.save(outfile='carto_femin.html')

        
        print("Printing each row")

        
    
    except Exception as e:
            print(e)
            print("Failed to read data from  table", e)
    finally:
            if  conn :
                print("The  connection is closed")
                return carto_femin
insert_base()
     