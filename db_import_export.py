import database

def export_db():
    # on ouvre le fichier texte d'export
    fichier = open("export_donnees/nom_des_voies.txt", "w")

    # On ouvre la connexion à la base de données et on lance la requete sur la table nom_des_voies
    conn = database.create_connection()

    cur = database.query_create_select(conn, "select * from nom_des_voies where geojson not like '%[[[%' order by voie_id;")

    requete_insert = "insert into nom_des_voies(voie_id, voie_complet, voie_fantoir, voie_date_cre, voie_real, voie_officiel, tenant, aboutissant, denom_annee, dm_seance, delib_num, cote_archives, denom_origine, lien_externe, observation, geojson, genre) values("

    ligne = 0
    for row in cur:
        requete_valeurs = ""

        for i in range(1, 17):
            requete_valeurs = requete_valeurs + "'" + str(row[i]).replace("'", "''") + "', "

        requete_finale = requete_insert + str(row[0]) + ", " + requete_valeurs[0:len(requete_valeurs) - 2] + ");"
        print(requete_finale)

        fichier.write("%s\n" % (requete_finale))


    fichier.close()

    # on ouvre le fichier texte d'export
    fichier = open("export_donnees/points_interet.txt", "w")

    # On charge les points d'intérêts depuis la base de données
    cur = database.query_create_select(conn, "select * from coord_points_interets order by idtf;")

    requete_insert = "insert into coord_points_interets(idtf, titre, thématiques, periodes, types, adresse, latitude, longitude, texte_fr, texte_en, bibliographie, site_internet, credit, legende) values("

    ligne = 0
    for row in cur:
        requete_valeurs = ""

        for i in range(1, 14):
            requete_valeurs = requete_valeurs + "'" + str(row[i]).replace("'", "''") + "', "

        requete_finale = requete_insert + str(row[0]) + ", " + requete_valeurs[0:len(requete_valeurs) - 2] + ");"
        print(requete_finale)

        fichier.write("%s\n" % (requete_finale))

    fichier.close()


def import_db():
    # on ouvre le fichier texte d'export
    fichier = open("export_donnees/nom_des_voies.txt", "r")

    # On ouvre la connexion à la base de données et on lance la requete sur la table nom_des_voies
    conn = database.create_connection()

    for ligne in fichier:
        cur = database.query_create_select(conn, ligne)

    # on ouvre le fichier texte d'export
    fichier = open("export_donnees/points_interet.txt", "r")

    # On ouvre la connexion à la base de données et on lance la requete sur la table nom_des_voies
    conn = database.create_connection()

    for ligne in fichier:
        cur = database.query_create_select(conn, ligne)


export_db()
#import_db()