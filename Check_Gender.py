import database
import gender_guesser.detector as gender
import scrap_google as sc


def select_en_base():
    debug = 2
    conn = database.create_connection()

    cur = database.query_create_select(conn, "Select * From nom_des_voies;")

    stopwords = ['la', 'le', 'des', 'de', 'Père', 'point', 'Saint', 'Place',
                 'Rue', 'Avenue', 'Allée', 'Quai', 'Rond', 'Chemin', 'Passage', 'Cours',
                 'Boulevard', 'Impasse', 'Général', 'Lieutenant', 'Route', 'Cour', 'Galerie',
                 'Président', 'Prosper', 'ème', 'Régiment', 'Jardin', 'Champ', 'La', 'Le',
                 'et', 'Lys', 'Docteur', 'ter', 'Capitaine', 'Parc', 'Square', 'Stade', 'bis',
                 'Voie', 'Pont', 'Commandant', 'Sainte', 'Colonel', 'Espace']

    for ligne in cur:
        try:
            if debug == 1:
                print(ligne[0], ligne[1])
            prenom = ligne[1].split(" ")[1]
            if prenom in stopwords:
                prenom = ligne[1].split(" ")[2]
                if prenom in stopwords:
                    prenom = ligne[1].split(" ")[3]

            nom = ligne[1].split(" ")[2]
            if debug == 1:
                print(prenom, nom)
            d = sc.check_genre(prenom)
#            data = d.get_gender(prenom)
            if debug == 1:
                print(f'prenom :{prenom} genre:{d}')

            # Mise à jour du genre en base données
            requete = "update nom_des_voies set genre = '" + d + "' Where voie_id = " + str(ligne[0]) + ";"
            try:
                database.query_create_select(conn, requete)
            except:
                print("Erreur")

            if debug == 1:
                print(requete)

        except IndexError:
            print("Juste un nom dans la rue")
            print(ligne[1])
            d = gender.Detector()
            data = d.get_gender(prenom)
            if debug == 2:
                print(f'prenom :{prenom} genre:{data}')

            # Mise à jour du genre en base données
            requete = "update nom_des_voies set genre = '" + data + "' Where voie_id = " + str(ligne[0]) + ";"


select_en_base()