import database


def mise_a_jour_genre(fichier):
    # Initialisation du DataFrame df
    # à partir des données du fichier CSV
    # file = open('home/hb/PROJET/turbine_prjt/turbine_project/Donnees/fichiers avec genre/1.csv', "r")
    file = open(fichier, "r")
    # utiliser readlines pour lire toutes les lignes du fichier
    # La variable "lignes" est une liste contenant toutes les lignes du fichier
    lines = file.readlines()
    # fermez le fichier après avoir lu les lignes
    file.close()
    # Itérer sur les lignes

    conn = database.create_connection()

    for line in lines:
        # if line.find("genre")<0:
        pos_voie_id = line.find("VOIE_ID")
        pos_2points = line.find(":", pos_voie_id)
        pos_virgule = line.find(",", pos_2points)

        pos_genre = line.find("genre\":")
        pos_accolade = line.find("}}", pos_genre + 8)

        print(line)
        print(pos_voie_id, pos_2points, pos_virgule, pos_genre, pos_accolade)
        index = line[pos_2points + 1:pos_virgule]
        genre_str = line[pos_genre + 8: pos_accolade - 1]
        voie_id_str = line[pos_voie_id + 9: pos_virgule]
        print("voie_id_str: ", voie_id_str)
        print(genre_str)

        requete = "Update nom_des_voies set genre = '" + genre_str + "' where voie_id = " + voie_id_str + ";"
        print(requete)
        try:
            database.query_create_select(conn, requete)
        except:
            print("Erreur")


def sauve_base_de_donnes():
    conn = database.create_connection()
    requete = "Select * From nom_des_voies;"
    requete = "Select voie_id, voie_complet, voie_fantoir, voie_date_cre, voie_real, voie_officiel, tenant, aboutissant, denom_annee, dm_seance, delib_num, cote_archives, denom_origine, lien_externe, observation, geojson, genre From nom_des_voies order by voie_id;"

    try:
        cur = database.query_create_select(conn, requete)
        print("apres query")

# voie_id, voie_complet, voie_fantoir, voie_date_cre, voie_real, voie_officiel, tenant, aboutissant, denom_annee, dm_seance, delib_num, cote_archives, denom_origine, lien_externe, observation, geojson, genre
        fichier = open("sauvegarde_base_de_donnees.txt", "w")

        for row in cur:
            print(row[0])
            ligne_fichier = ""
            print("Début: ")
            for j in range(0, 17):
                print(row[j])
                ligne_fichier = ligne_fichier + ";" + str(row[j])

            print(ligne_fichier)
            fichier.write(ligne_fichier[1:] + "\n")

        fichier.close()


    except Exception as inst:
        print(type(inst))  # the exception instance
        print(inst.args)  # arguments stored in .args


#mise_a_jour_genre('/home/hb/PROJET/turbine_prjt/turbine_project/Donnees/fichiers avec genre/1.csv')
#mise_a_jour_genre('/home/hb/PROJET/turbine_prjt/turbine_project/Donnees/fichiers avec genre/2.csv')
#mise_a_jour_genre('/home/hb/PROJET/turbine_prjt/turbine_project/Donnees/fichiers avec genre/3.csv')
#mise_a_jour_genre('/home/hb/PROJET/turbine_prjt/turbine_project/Donnees/fichiers avec genre/4.csv')

sauve_base_de_donnes()