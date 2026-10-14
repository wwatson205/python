# les exceptions peremettent de :

#capturer les erreurs au lieu de laisser le programme planter,
#reagir intelligemment,
#nettoyer les ressources, 
#continuer l'éxecution

a = 5
b = 0
try :
    c = a/b # la ligne qui peut génerer un crash, ZeroDivisionError: division by zero
except ZeroDivisionError as e:
    print(f"Une erreur : {e}")

#AUTRE EXEMPLE

a = 7
b = 0
try :
    c = int("abc") #La ligne qui peut génerer un crash, ValueError: invalid literal for int() with base 10: 'abc'
except ValueError as e:
    print(f"Une erreur : {e}")

#On peut utiliser un else qui sera utilisé comme un else dans une condition if


try :
    c = int("1") #La ligne qui peut génerer un crash, ValueError: invalid literal for int() with base 10: 'abc'
except ValueError as e:
    print(f"Une erreur : {e}")
else: 
    print("Tout va bien")

#On peut utiliser un finally qui executera la commande quoiqu'il arrive.


file = None
try:
    file = open("./save001.json", "r")
except FileNotFoundError as e:
    print(f"Une erreur{e}")
else:
    print("Tout va bien")
finally:
    if file is not None:
        file.close()



