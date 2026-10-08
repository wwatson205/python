import json 
#"r" pour lire le fichier
#"w" pour écrire dans le fichier
#"a" pour ajouter du contenu à la fin du fichier
file = open("contact.json", "r")
data : list = json.load(file)

new_contact = {
    "nom" : "PIGNON",
    "prenom" : "Jean",
    "adresse" : "1 rue de la paix",
    "telephone" : "0600000000"
}
data.append(new_contact)

