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

def dmd_ajt_contact(): # fonction qui demande à l'utilisateur si il veut ajouter un contact 
    choix: str = input("voulez vous ajoutez un contact(oui/non)")
    if choix == "oui":
        write_json("./contacts.json")
    else:
        return print("Aucun contact ajouté")


def find_contact(): #fonction qui permet de trouver un contact via son prenom ou nom
    data = read_json("./contacts.json")
    recherche = input("Contact a rechercher: ")
    resultats = []

    for contact in data:
        if recherche.lower() == contact["nom"].lower() or recherche.lower() == contact["prenom"].lower():
            resultats.append(contact)

    if resultats != []:
        for contact in resultats:
            print(f"Voici le contact {contact['nom']} {contact['prenom']} avec comme numero {contact['telephone']}")
    else:
        print("Aucun contact trouvé")


    for contact in data:
        if recherche.lower() == contact["nom"].lower() or recherche.lower() == contact["prenom"].lower():
            print(f"Voici le contact {contact['nom']} {contact['prenom']} avec comme numero {contact['telephone']}")
            break
        else:
             print("Aucun contact trouvé")








dmd_ajt_contact()
find_contact()




