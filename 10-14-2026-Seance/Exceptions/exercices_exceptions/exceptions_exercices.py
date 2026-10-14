#Exercice 1: Conversion de types basique


def str_to_int(text):


    try:
        texte = int(text)
    except ValueError as e:

        print(f"Le texte que vous avez saisi de ne peut pas se convertir en entier")
        return 0
    
    else:
        return (f"La conversion a réussie :  {text}")

print(str_to_int("42"))
print(str_to_int("abc"))
print(str_to_int("-15"))



#Exercice 2: Accès à une liste


def safe_list_access(lst, index):


    try:
        nb = lst [index]

    except IndexError as e:

        print(f"L'index {index} est en dehors de la liste")
        return None
    
    else:
        return(f"L'élément {nb} a été récupérer en sécurité")

numbers = [10, 20, 30, 40]
print(safe_list_access(numbers,0))
print(safe_list_access(numbers, 10))



#Exercice 3: Gestion de fichier


def read_file(filename):

    file = None
    try:
        file = open(filename, "r")
        contenu = file.read()
    except FileNotFoundError as e:
        print(f"Une erreur{e}")

    except IOError as i:
        print(f"Le logiciel n'a pas pu lire ou écrire des données, erreur : {i} ")
        return None
    
    else:
        print("Tout va bien")
        return contenu

    finally:
        if file is not None:
            file.close()
            print(f"Le fichier est fermé")
    



print(read_file("fichier_existant.txt"))
print(read_file("fichier_inexistant.txt"))