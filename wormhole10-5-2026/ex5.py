prenom :str = input("Quel est ton prénom ? ")
age :int = int(input("Quel est ton âge ? "))
if age < 13:
    print(f"Bonjour {prenom}, tu es enfant.")
elif age >= 13 and age <= 17:
    print(f"Bonjour {prenom}, tu es adolescent.")
else:
    print(f"Bonjour {prenom}, tu es adulte.")