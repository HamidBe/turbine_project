from collections import Counter
import requests
from bs4 import BeautifulSoup


def check_genre(nom):

    liste_nom_nmasculin = ["né", "français", "italien", "espagnol", "allemand", "commandant", "mort", "pilote", "fondateur", "homme", "général", "officier", "il", "comte", "roi", "acteur"]
    liste_nom_feminin = ["née", "italienne", "espagnole", "allemande", "fondatrice", "femme", "française", "morte", "dédédée", "parisienne", "fille", "actrice", "elle", "reine", "comtesse"]

    params = {}

    url = "https://www.google.com/search"

    params["q"] = nom
    r = requests.get(url, params=params)
    resultat_soup = BeautifulSoup(r.content, 'html.parser')

    resultat_split = resultat_soup.get_text().lower().split()
    c = Counter(resultat_split)
    somme_masc = sum([c[word] for word in liste_nom_nmasculin])
    somme_femi = sum([c[word] for word in liste_nom_feminin])

    pourcentage = somme_masc/(somme_femi + somme_masc)*100

    if pourcentage > 50:
        retour = "masculin"
    else:
        retour = "feminin"

    return retour