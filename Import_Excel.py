from xlrd import open_workbook
import database

# On crée le dictionnaire correspondant à la base de données
ligne_excel = {}

def ouvre_fichier_excel_voies():

    # On ouvre le fichier Exceln
    book = open_workbook('PLANDEVILLE_VOIES.xls',on_demand=True)
    book = open_workbook('./Donnees/Doc_Villes/PLANDEVILLE_VOIES_VDG.xls',on_demand=True)

    worksheet = book.sheet_by_name('Feuille1')

    # text:'VOIE_ID'
    # text:'VOIE_COMPLET'
    # text:'VOIE_FANTOIR'
    # text:'VOIE_DATECRE'
    # text:'VOIE_REAL'
    # text:'VOIE_OFFICIEL'
    # text:'TENANT'
    # text:'ABOUTISSANT'
    # text:'DENOM_ANNEE'
    # text:'DM_SEANCE'
    # text:'DELIB_NUM'
    # text:'COTE_ARCHIVES'
    # text:'DENOM_ORIGINE'
    # text:'DENOM_N_MOINS_1'
    # text:'DENOM_N_MOINS_1_ANNEE'
    # text:'DENOM_N_MOINS_2'
    # text:'DENOM_N_MOINS_2_ANNEE'
    # text:'LIEN_EXTERNE'
    # text:'OBSERVATIONS'
    # text:'GeoJSON'

    requete_insert = "insert into nom_des_voies (voie_id, voie_complet, voie_fantoir, voie_date_cre, voie_real, voie_officiel, tenant, aboutissant, denom_annee, dm_seance, delib_num, cote_archives, denom_origine, lien_externe, observation, geojson, genre) values("
    requete_valeurs = ""

    # On crée la connexion à la base de données
    conn = database.create_connection()

    # On crée les tables si elles n'existent pas encore
    database.create_tables(conn)

    num_rows = worksheet.nrows - 1
    curr_row = 0
    while curr_row < num_rows:
        curr_row += 1
        row = worksheet.row(curr_row)

        requete = ""

        ligne_en_cours = ""
        voie_id = row[0].value
        voie_complet = str(row[1].value).replace("'", "''")
        voie_fantoir = str(row[2].value).replace("'", "''")
        voie_date_cre = str(row[3].value).replace("'", "''")
        voie_real = str(row[5].value).replace("'", "''")
        voie_officiel = str(row[5].value).replace("'", "''")
        tenant = str(row[6].value).replace("'", "''")
        aboutissant = str(row[7].value).replace("'", "''")
        denom_annee = str(row[8].value).replace("'", "''")
        dm_seance = str(row[9].value).replace("'", "''")
        delib_num = str(row[10].value).replace("'", "''")
        cote_archives = str(row[11].value).replace("'", "''")
        denom_origine = str(row[12].value).replace("'", "''")
        lien_externe = str(row[17].value).replace("'", "''")
        observation = str(row[18].value).replace("'", "''")
        geojson = str(row[19].value).replace("'", "''")

        if voie_real == 'oui':
            voie_real = 'true'
            voie_officiel = 'true'
        else:
            voie_real = 'false'
            voie_officiel = 'false'

        if denom_annee == '':
            denom_annee = 2000

        if delib_num == '':
            delib_num = 0


        print(denom_annee)
        print(tenant)

        requete = requete_insert + str(voie_id) + ", '"
        requete = requete + str(voie_complet) + "', '"
        requete = requete + str(voie_fantoir) + "', '"
        requete = requete + str(voie_date_cre) + "', '"
        requete = requete + str(voie_real) + "', "
        requete = requete + str(voie_officiel) + ", '"
        requete = requete + str(tenant) + "', '"
        requete = requete + str(aboutissant) + "', '"
        requete = requete + str(denom_annee)[0:4] + "', '"
        print("requete1: ", requete)

        requete = requete + str(dm_seance) + "', '"
        requete = requete + str(delib_num) + "', '"
        requete = requete + str(cote_archives) + "', '"
        requete = requete + str(denom_origine) + "', '"
        requete = requete + str(lien_externe) + "', '"
        requete = requete + str(observation) + "', '"
        requete = requete + str(geojson) + "', '');"
        print("requete2: ", requete)
        try:
            database.query_create_select(conn, requete)
        except Exception as e:
            print(e)

    book.release_resources()
    del book

def ouvre_fichier_excel_monuments():
    # On ouvre le fichier Exceln
    book = open_workbook('./Donnees/Doc_Villes/PATRIMOINE_VDG.xls', on_demand=True)

    worksheet = book.sheet_by_name('Feuille1')

    requete_insert = "insert into coord_points_interets(idtf, titre, thématiques, periodes, types, adresse, latitude, longitude, texte_fr, Texte_en, bibliographie, site_internet, credit, legende) values("
    requete_valeurs = ""

    # On crée la connexion à la base de données
    conn = database.create_connection()

    # On crée les tables si elles n'existent pas encore
    database.create_tables(conn)

    num_rows = worksheet.nrows - 1
    curr_row = 0
    while curr_row < num_rows:
        curr_row += 1
        row = worksheet.row(curr_row)

        # idtf, titre, thématiques, periodes, types, adresse, latitude, longitude, texte_fr, Texte_en, bibliographie, site_internet, credit, legende


        idtf = row[0].value
        titre = str(row[1].value).replace("'", "''").replace("’", "’’")
        thematiques = str(row[2].value).replace("'", "''")
        periodes = str(row[3].value).replace("'", "''")
        types = str(row[4].value).replace("'", "''")
        adresse  = str(row[5].value).replace("'", "''")
        latitude = str(row[6].value).replace("'", "''")
        longitude = str(row[7].value).replace("'", "''")
        texte_fr = str(row[8].value).replace("'", "''")
        texte_en = str(row[9].value).replace("'", "''")
        bibliographie = str(row[10].value).replace("'", "''")
        site_internet = str(row[11].value).replace("'", "''")
        credit = str(row[12].value).replace("'", "''")
        legende = str(row[13].value).replace("'", "''")

        print("idtf: ", idtf)
        print("titre: ", titre)
        print("thematiques: ", thematiques)
        print("periodes: ", periodes)
        print("types: ", types)
        print("adresse: ", adresse)
        print("latitude: ", latitude)
        print("longitude: ", longitude)
        print("texte_fr: ", texte_fr)
        print("texte_en: ", texte_en)
        print("bibliographie: ", bibliographie)
        print("site_internet: ", site_internet)
        print("credit: ", credit)
        print("legende: ", legende)

        requete = requete_insert + str(idtf) + ", '"
        requete = requete + str(titre) + "', '"
        requete = requete + str(thematiques) + "', '"
        requete = requete + str(periodes) + "', '"
        requete = requete + str(types) + "', '"
        requete = requete + str(adresse) + "', "
        requete = requete + str(latitude) + ", "
        requete = requete + str(longitude) + ", '"
        requete = requete + str(texte_fr) + "', '"
        requete = requete + str(texte_en) + "', '"
        requete = requete + str(bibliographie) + "', '"
        requete = requete + str(site_internet) + "', '"
        requete = requete + str(credit) + "', '"
        requete = requete + str(legende) + "');"


        print(requete)

        try:
            database.query_create_select(conn, requete)
        except Exception as e:
            print(e)


#ouvre_fichier_excel_voies()
ouvre_fichier_excel_monuments()