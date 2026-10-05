prenom : str = "Alex"
age : int = 19
taille : float = 1.72
if age < 18:
    est_majeur = False
else : 
    est_majeur = True

print(f" {prenom} a {age} ans et mesure {taille}m et est {"majeur" if est_majeur == True else "mineur"}")