contacts: list[dict] = []
nb_contacts : int = int(input("Combien de contacts voulez-vous ajouter ? "))
for i in range(nb_contacts):
    contact = {}
    contact["nom"] = input(f"Entrez le nom du contact numéro {i+1} : ")
    contact["numero"] = input(f"Entrez le numéro de téléphone du contact {i+1} : ")
    contacts.append(contact)
for contact in contacts:
    print(f" {contact['nom']} : {contact['numero']}")
print(f"Le total de contacts enregistrés est : {nb_contacts}")


bonus :str = input("Quel contact voulez vous afficher ? ")
if bonus in [contact["nom"]]:
             for contact in contacts:
                    if contact["nom"] == bonus:
                        print(f"Le contact {bonus} a pour numéro de téléphone : {contact['numero']}")
                    elif contact["nom"] != bonus:
                        print(f"Contact introuvable")