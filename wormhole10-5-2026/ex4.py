notes: list[int] = [8, 12, 17, 5, 10, 16, 19, 3]
admis : int = 0
for i in range(len(notes)):
    if notes[i] >= 16:
        print(f"Tu as eu {notes[i]} à l'examen, tu es admis avec félicitations !")
        admis += 1
    elif notes[i] >= 10   and notes[i] < 16:
        print(f"Tu as eu {notes[i]} à l'examen, tu es admis !")
        admis += 1
    else:
        print(f"Tu as eu {notes[i]} à l'examen, tu es recalé !")
print(f"Nombre d'étudiants admis : {admis}")
    
    