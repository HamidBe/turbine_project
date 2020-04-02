import wikipediaapi
import json

from urllib.request import urlopen


url = "https://gender-api.com/get?name=elizabeth&key=UHpbZEfqcJwXBQzXwV"
response = urlopen(url)
decoded = response.read().decode('utf-8')
data = json.loads(decoded)
print( "Gender: " + data["gender"]); #Gender: male


wiki_wiki = wikipediaapi.Wikipedia('fr')

page_py = wiki_wiki.page('Georges Sand')


print("Page - Exists: %s" % page_py.exists())
#print(page_py.sections)

def print_sections(sections, compteur1, compteur2, level=0):
    for s in sections:
       # print("%s: %s - %s" % ("*" * (level + 1), s.title, s.text))
        print_sections(s.sections, compteur1, compteur2, level + 1)

        if "elle " in s.text:
        #    print("elle trouvé")
            compteur2 += 1

        elif "il " in s.text:
       #     print("il trouvé")
            compteur1 += 1

        elif "née " in s.text:
      #      print("né trouvé")
            compteur2 += 1
        elif "Homme" in s.text:
     #       print("Homme trouvé")
            compteur1 += 1
        elif "homme" in s.text:
    #        print("homme trouvé")
            compteur1 += 1
        elif "Femme" in s.text:
   #         print("Femme trouvé")
            compteur2 += 1
        elif "femme" in s.text:
   #        print("femme trouvé")
           compteur2 += 1

cpt_elle = 0
cpt_il = 0


print_sections(page_py.sections, cpt_il, cpt_elle, 0)

print("Femmes trouvées: ", cpt_elle)
print("Hommes trouvées: ", cpt_il)

myKey = "insert your server key here"
url = "https://gender-api.com/get?key=" + myKey + "&name=kevin"
url = "https://gender-api.com/get?name=elizabeth&key=UHpbZEfqcJwXBQzXwV"
url = "https://gender-api.com/get?split=jacques%20chirac&key=UHpbZEfqcJwXBQzXwV"
response = urlopen(url)
decoded = response.read().decode('utf-8')
data = json.loads(decoded)
print( "Gender: " + data["gender"]); #Gender: male
print("Certitude: ", data["accuracy"])
