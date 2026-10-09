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
        degats = self.force
        cible.subir_degats(degats)

        
        # puis RETOURNE (return, pas print) un message du type :
        # "Aldric attaque Gobelin et lui infline 8 degats (Gobelin : 12 PV restants)"
        return (f"{self.nom} attaque {cible.nom} et lui inflige {degats}dégats ({cible.nom}: {cible.points_de_vie} PV restants)")
        

        

    def __repr__(self):
        return (f"{self.nom} : {self.points_de_vie} PV")





gobelin = Personnage("Gobelin", 20, 5)
aldric = Personnage("Aldric", 30, 8)
print(aldric.attaquer(gobelin))
print(gobelin)
    