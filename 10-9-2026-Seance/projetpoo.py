import json
class Personnage:
    """Un personnage générique : nom, points de vie, force d'attaque."""

    def __init__(self, nom, points_de_vie, force):
        self.nom = nom
        self.points_de_vie = points_de_vie
        self.force = force


    def est_vivant(self):
        return self.points_de_vie > 0


    def subir_degats(self, degats):
        # TODO : diminue self.points_de_vie de `degats`, sans jamais descendre sous 0
        self.points_de_vie -= degats
        if self.points_de_vie < 0:
            self.points_de_vie = 0
        self.points_de_vie = self.points_de_vie


    def attaquer(self, cible : "Personnage"):
        # TODO : applique self.force en dégâts à `cible` (via subir_degats),
        if not cible.est_vivant():
            return (f"{cible.nom} est deja vaincu")
        degats = self.force
        cible.subir_degats(degats)
        # puis RETOURNE (return, pas print) un message du type :
        # "Aldric attaque Gobelin et lui infline 8 degats (Gobelin : 12 PV restants)"
        return (f"{self.nom} attaque {cible.nom} et lui inflige {degats}dégats ({cible.nom}: {cible.points_de_vie} PV restants)")


    def to_dict(self):
        return {
            "type": "Personnage",
            "nom" : self.nom,
            "points_de_vie": self.points_de_vie,
            "force": self.force,
        }


    def sauvegarder(self,path):
        file = open(path, "a", encoding="utf-8")
        json.dump(self.to_dict(),file)


    def __repr__(self):
        return (f"{self.nom} : {self.points_de_vie} PV")










class Heros(Personnage):


    def __init__(self,nom, points_de_vie, force, mana):
        super().__init__(nom, points_de_vie, force)
        self.mana = mana


    def competence_speciale(self,cible : "Personnage"):
        degats = self.force
        cible.subir_degats(degats * 2)
        self.mana -= 10
        if self.mana < 0:
            print (f"Plus de points de mana")
            self.mana = 0
            
        else:
            self.mana = self.mana           
        return (f"{self.nom} attaque {cible.nom} et lui inflige {degats *2 } dégats et lui reste {self.mana} de mana({cible.nom}: {cible.points_de_vie} PV restants)")


    def to_dict(self):    
        dico : dict = super().to_dict()
        dico["type"]= "Heros"
        dico["mana"]= self.mana
        return dico










class Monstre(Personnage):


    def __init__(self,nom, points_de_vie, force, niveau_de_danger,butin):
        super().__init__(nom, points_de_vie, force)
        self.niveau_de_danger = niveau_de_danger
        self.butin = butin


    def attaquer(self, cible : "Personnage"):
        # TODO : applique self.force en dégâts à `cible` (via subir_degats),
        degats = self.force * self.niveau_de_danger
        cible.subir_degats(degats)    
        # puis RETOURNE (return, pas print) un message du type :
        # "Aldric attaque Gobelin et lui infline 8 degats (Gobelin : 12 PV restants)"
        return (f"{self.nom} attaque {cible.nom} et lui inflige {degats}dégats ({cible.nom}: {cible.points_de_vie} PV restants)")


    def to_dict(self):
        dico : dict = super().to_dict()
        dico["type"] = "Monstre"
        dico["niveau_de_danger"] = self.niveau_de_danger
        dico["butin"]= self.butin
        return dico





def charger_personnage(path):
    file =  open(path, "r", encoding="utf-8")
    dico= json.load(file)

    if dico["type"] == "Heros":
        return Heros(
            dico["nom"],
            dico["points_de_vie"],
            dico["force"],
            dico["mana"]
        )

    elif dico["type"] == "Monstre":
        return Monstre(
            dico["nom"],
            dico["points_de_vie"],
            dico["force"],
            dico["niveau_de_danger"],
            dico["butin"]
        )

    elif dico["type"] == "Personnage":
        return Personnage(
            dico["nom"],
            dico["points_de_vie"],
            dico["force"]
        )

    else:
        return(f"Il n'existe pas de type de personnage de la sorte {dico['type']}")




class Partie:
    def __init__(self):
        self.personnages = []
        self.historique = []   # liste de messages, dans l'ordre chronologique



    def ajouter_personnage(self,personnage):
        self.personnages.append(personnage)


    def combat(self,attaquant, defenseur):
        atq = attaquant.attaquer(defenseur)
        self.historique.append(atq)
        if not defenseur.est_vivant():
            msg_dft = (f"{defenseur.nom} est mort")
            self.historique.append(msg_dft)
        else :
            msg_atq = (f"{attaquant.nom} a attaqué {defenseur.nom}")
            self.historique.append(msg_atq)

    def sauvegarder(self,path):
        









# petit_gobelin = Personnage("Gobelin", 20, 5)
# aldric = Personnage("Aldric", 30, 8)
# print(aldric.attaquer(petit_gobelin))
# print(petit_gobelin.attaquer(aldric))
# print(petit_gobelin)
# print(aldric)
lancelot = Heros("Lancelot", 40, 10, mana=25)
# william = Heros("William",40,10, mana = 25)
gobelin = Monstre("Gobelin", 100, 5, niveau_de_danger=2, butin="10 pièces d'or")

# print(gobelin.attaquer(lancelot))             # degats = 5 * 2 = 10
# print(lancelot.competence_speciale(gobelin))  # degats = 10 * 2 = 20, mana 25 -> 15
# print(lancelot.competence_speciale(gobelin))  # mana 15 -> 5, encore possible
# print(lancelot.competence_speciale(gobelin))  # mana 5 < 10, message d'echec

# lancelot.sauvegarder("dict_perso.json")
# lancelot_recharge = charger_personnage("dict_perso.json")
# print(lancelot_recharge)
# print(lancelot_recharge.mana)


partie = Partie()
partie.ajouter_personnage(lancelot)
partie.ajouter_personnage(gobelin)

partie.combat(lancelot, gobelin)
partie.combat(gobelin, lancelot)
