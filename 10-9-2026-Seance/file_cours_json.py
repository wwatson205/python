import json 
#"r" pour lire le fichier
#"w" pour écrire dans le fichier
#"a" pour ajouter du contenu à la fin du fichier
def read_json(path) -> list: #fonction qui permet de lire le fichier json
    file = open(path, "r")
    data : list = json.load(file)
    return data

def write_json(path): #fonction qui permet d'ecrire un contact en fonction du chemin 
    data = read_json(path)

    new_contact: dict = {}

    nom: str = input("Entrez le nom du contact : ")
    prenom: str = input("Entrez le prénom du contact : ")
    tel: str = input("Numéro du contact ? ")

    new_contact["nom"] = nom
    new_contact["prenom"] = prenom
    new_contact["telephone"] = tel
    
    data.append(new_contact)
    
    file_out = open(path, "w",encoding="utf-8")
    json.dump(data,file_out)
    return data