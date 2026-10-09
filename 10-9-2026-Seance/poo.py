class Animal():

    def __init__(self):
        print("Init")


    def parler(self) -> None:
        print("L'animal a parlé")


class Chien(Animal):
    def __init__(self):
        super().__init__()

    def parler(self):
        super().parler()
        print("Il wouf")




#animal : Animal = Animal()
#animal.parler()

dog: Chien = Chien()
dog.parler()