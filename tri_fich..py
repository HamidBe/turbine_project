import csv,re
import gender_guesser.detector as gender
import string
fichier = "PLANDEVILLE_VOIES_VDG.csv"


with open(fichier) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    h=0
    for row in csv_reader:
        if line_count == 0:
         
            print(f'Nom des collonnes :-- {", ".join(row)}')
            line_count += 1
            
        else:
            champs=(f'\t{row[0]}   {row[6]} {row[7]} {row[12]} {row[17]}{row[19]} .')
            nom_voie = (f'\t  {row[1]} .')
            
            prenoms = re.sub('['+string.punctuation+']', '', nom_voie).split()
            
            
            stopwords = ['la','le','des','de','Père','point','Saint','Place',
                         'Rue','Avenue','Allée','Quai','Rond','Chemin','Passage','Cours',
                         'Boulevard','Impasse','Général','Lieutenant','Route','Cour','Galerie' ,
                        'Président','Prosper','ème','Régiment','Jardin','Champ','La','Le',
                        'et','Lys','Docteur','ter','Capitaine','Parc','Square','Stade','bis',
                         'Voie' ,'Pont','Commandant','Sainte','Colonel','Espace']
                       
            for prenom in list(prenoms): 

                if prenom in stopwords:
                     prenoms.remove(prenom)
            # gender detecter
            d = gender.Detector()
            data = d.get_gender(prenoms[0])


            # print(champs)
            # print(f'\t ID_voie:  {row[0]}.')
            # print(f'\t VOIE:  {row[1]}.')
            # print(f'\t TENENT:  {row[6]}.')
            # print(f'\t ABOUTISSANT:  {row[7]}.')
            # print(f'\t DENOM_ORIGIN:  {row[12]}.')
            # print(f'\t LIEN_EXTRENE:  {row[17]}.')
            # print(f'\t GEO_JSON:  {row[19]}.') 

            
        
            print(f'prenom :{prenoms} genre:{data}')
   
            line_count += 1
    print(f'Processed { line_count} lines.')
    


 
        
    
  
