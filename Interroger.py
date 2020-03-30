import requests
from unidecode import unidecode

listeAppellations = ["Bernard lavilliers","Kevin Schwantz","Michel Platini","Zinédine Zidane"]
output = open("/home/laurent/git/turbine_project/appellation2wikipedia_rapport.txt", "w")
output.write("appellation \t Nb reponses \t forme preferee \t toutes reponses \n")
for appellation in listeAppellations:
    url = "https://fr.wikipedia.org/w/api.php?action=opensearch&search=" + appellation + "&limit=10&namespace=0&format=json"
    url = "http://domybiblio.net/search/search_api.php?type_search=subject&q=" + appellation + "&type_doc=all&period=&pageID=1&wp=true&idref=true&loc=true"
    #resultats = etree.parse(url)
    jsonfile = requests.get(url)
    print(jsonfile.json())
    listeTitres = jsonfile.json()[1]
    NbReponses = len(listeTitres)
    listeURL = jsonfile.json()[3]
    forme_preferee = []
    toutes_reponses = []
    i = 0
    for el in listeTitres:
         TITRE = unidecode(el.upper())
         if (TITRE == appellation):
             forme_preferee.append(unidecode(el))
             forme_preferee.append(listeURL[i])
         else:
             toutes_reponses.append(unidecode(el) + ";" + listeURL[i])
         i = i+1

    output.write(appellation + "\t" + str(NbReponses) + "\t" + "|".join(forme_preferee) + "\t" +  "|".join(toutes_reponses) + "\n")