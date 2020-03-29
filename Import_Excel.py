from xlrd import open_workbook

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

    num_rows = worksheet.nrows - 1
    curr_row = 0
    while curr_row < num_rows:
        curr_row += 1
        row = worksheet.row(curr_row)

        requete = ""

        ligne_en_cours = ""
        voie_id = str(row[0].value)
        voie_complet = str(row[1].value)
        voie_fantoir = str(row[2].value)
        voie_date_cre = str(row[3].value)
        voie_real = str(row[5].value)
        voie_officiel = str(row[6].value)
        tenant = str(row[7].value)
        aboutissant = str(row[8].value)
        denom_annee = str(row[9].value)
        dm_seance = str(row[10].value)
        delib_num = str(row[11].value)
        cote_archives = str(row[12].value)
        denom_origine = str(row[13].value)
        lien_externe = str(row[18].value)
        observation = str(row[19].value)
        geojson = str(row[20].value)

        requete = requete_insert + voie_id + ", '" + voie_complet + "', " + voie_fantoir + "', " + voie_date_cre + ", " + voie_real + ", " + voie_officiel + ", '" + tenant + "', '" + aboutissant + "', '" + denom_annee + "', '" + dm_seance + "', " + delib_num + ", " + cote_archives + ", '" + denom_origine + "', " + lien_externe + "', '" + observation + "', '" + geojson +"');"

        print(requete)

    book.release_resources()
    del book

ouvre_fichier_excel()