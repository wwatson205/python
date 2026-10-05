dividende : int = int(input("Entrez le dividende : "))
diviseur : int = int(input("Entrez le diviseur : "))
if diviseur == 0:
    print("Erreur : Il faut saisir un diviseur différent de zéro.")
else:
    division : float = dividende / diviseur
    print(f"Le résultat de la division est : {division}")
