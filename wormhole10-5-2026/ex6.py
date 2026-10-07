contacts: list[dict] = []
nb_contacts : int = int(input("Combien de contacts voulez-vous ajouter ? "))
for i in range(nb_contacts):
    contact : dict = {}
    contact["nom"] = input(f"Entrez le nom du contact numéro {i+1} : ")
    contact["numero"] = input(f"Entrez le numéro de téléphone du contact {i+1} : ")
    contacts.append(contact)
for contact in contacts:
    print(f" {contact['nom']} : {contact['numero']}")
print(f"Le total de contacts enregistrés est : {nb_contacts}")

display : int = int(input("Voulez-vous afficher un contact en particulier ?"))
for contact in contacts:
    if contact['nom'].lower() == display.lower():
        print(f"Le contact {contact['nom']} a pour numéro : {contact['numero']}")
        break
    else:
        print(f"Le contact {display} n'existe pas dans la liste.")