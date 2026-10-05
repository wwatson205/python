notes : list[int] = [12, 8, 15, 19, 6, 14]
print(f"Nombre de notes : {len(notes)}")
print(f"Note maximale : {max(notes)}")
print(f"Note minimale : {min(notes)}")
sum(notes)
moyenne : float = sum(notes) / len(notes)
print(f"Moyenne : {moyenne}")
notes.append(17)
print(f"Notes : {notes}")
