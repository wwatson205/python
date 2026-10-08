etudiant: dict = {
    "prenom": "Sarah",
    "age": 21,
    "notes": [14, 16, 12]
}
print(f"{etudiant['prenom']} a {etudiant['age']} ans")
etudiant["ville"] = "Paris"
moyenne : float = sum(etudiant["notes"]) / len(etudiant["notes"])
print(f"La moyenne des notes de l'étudiant est {moyenne}")
for key in etudiant:
    print(f"{key}: {etudiant[key]}")