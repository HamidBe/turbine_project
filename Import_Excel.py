from xlrd import open_workbook
import database

# On crée le dictionnaire correspondant à la base de données
ligne_excel = {}

def ouvre_fichier_excel():

    # On ouvre le fichier Exceln
    book = open_workbook('PLANDEVILLE_VOIES_VDG.xls',on_demand=True)

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

    requete_insert = "insert into nom_des_voies (voie_id, voie_complet, voie_fantoir, voie_date_cre, voie_real, voie_officiel, tenant, aboutissant, denom_annee, dm_seance, delib_num, cote_archives, denom_origine, lien_externe, observation, geojson) values("
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

        print("voie_id: ", voie_id)
        print("voie_complet: ", voie_complet)
        print("voie_fantoir: ", voie_fantoir)
        print("voie_date_cre: ", voie_date_cre)
        print("voie_real: ", voie_real)
        print("voie_officiel: ", voie_officiel)
        print("tenant: ", tenant)
        print("aboutissant: ", aboutissant)
        print("denom_annee: ", denom_annee)
        print("dm_seance: ", dm_seance)
        print("delib_num: ", delib_num)
        print("cote_archives: ", cote_archives)
        print("denom_origine: ", denom_origine)
        print("lien_externe: ", lien_externe)
        print("observation: ", observation)
        print("geojson: ", geojson)

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
        requete = requete + str(geojson) + "');"
        print("requete2: ", requete)
        database.query_create_select(conn, requete)

    book.release_resources()
    del book

ouvre_fichier_excel()