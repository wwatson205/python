import json


# ==============================
# CLASSE PERSONNAGE
# ==============================

class Personnage:
    def __init__(self, nom, points_de_vie, force):
        self.nom = nom
        self.points_de_vie = points_de_vie
        self.pv_max = points_de_vie
        self.force = force

    def est_vivant(self):
        return self.points_de_vie > 0

    def subir_degats(self, degats):
        self.points_de_vie = max(
            0, self.points_de_vie - degats
        )

    def attaquer(self, cible):
        if not self.est_vivant():
            return f"{self.nom} ne peut plus attaquer."

        if not cible.est_vivant():
            return f"{cible.nom} est deja vaincu."

        degats = self.force
        cible.subir_degats(degats)

        return (
            f"{self.nom} attaque {cible.nom} "
            f"et inflige {degats} degats !"
        )

    def to_dict(self):
        return {
            "type": "Personnage",
            "nom": self.nom,
            "points_de_vie": self.points_de_vie,
            "pv_max": self.pv_max,
            "force": self.force
        }


# ==============================
# CLASSE HEROS
# ==============================

class Heros(Personnage):
    def __init__(self, nom, points_de_vie, force, mana):
        super().__init__(nom, points_de_vie, force)
        self.mana = mana
        self.mana_max = mana

    def competence_speciale(self, cible):
        if not self.est_vivant():
            return "Tu ne peux plus attaquer."

        if not cible.est_vivant():
            return f"{cible.nom} est deja vaincu."

        if self.mana < 10:
            return "Pas assez de mana ! Il faut 10 mana."

        degats = self.force * 2
        cible.subir_degats(degats)
        self.mana -= 10

        return (
            f"{self.nom} lance une attaque speciale ! "
            f"{degats} degats infliges a {cible.nom}."
        )

    def to_dict(self):
        d = super().to_dict()
        d["type"] = "Heros"
        d["mana"] = self.mana
        d["mana_max"] = self.mana_max
        return d


# ==============================
# CLASSE MONSTRE
# ==============================

class Monstre(Personnage):
    def __init__(
        self, nom, points_de_vie, force,
        niveau_de_danger, butin
    ):
        super().__init__(nom, points_de_vie, force)
        self.niveau_de_danger = niveau_de_danger
        self.butin = butin

    def attaquer(self, cible):
        if not self.est_vivant():
            return f"{self.nom} est vaincu."

        if not cible.est_vivant():
            return f"{cible.nom} est deja vaincu."

        degats = self.force * self.niveau_de_danger
        cible.subir_degats(degats)

        return (
            f"{self.nom} riposte et inflige "
            f"{degats} degats a {cible.nom} !"
        )

    def to_dict(self):
        d = super().to_dict()
        d["type"] = "Monstre"
        d["niveau_de_danger"] = self.niveau_de_danger
        d["butin"] = self.butin
        return d


# ==============================
# CLASSE PARTIE
# ==============================

class Partie:
    def __init__(self):
        self.heros = Heros("Lancelot", 40, 10, 25)
        self.monstre = Monstre(
            "Gobelin", 40, 5, 2, "10 pieces d'or"
        )
        self.historique = []
        self.terminee = False

    def afficher_personnages(self):
        h = self.heros
        m = self.monstre

        print("\n" + "=" * 42)
        print("          CHRONIQUES DE LANCELOT")
        print("=" * 42)

        print(f"\n[HERO] {h.nom}")
        print(f"PV    : {h.points_de_vie}/{h.pv_max}")
        print(f"Force : {h.force}")
        print(f"Mana  : {h.mana}/{h.mana_max}")

        print("\n[ENNEMI] " + m.nom)
        print(f"PV     : {m.points_de_vie}/{m.pv_max}")
        print(f"Force  : {m.force}")
        print(f"Danger : x{m.niveau_de_danger}")
        print(f"Butin  : {m.butin}")

        print("=" * 42)

    def ajouter_message(self, message):
        self.historique.append(message)
        print("\n> " + message)

    def verifier_fin(self):
        if not self.monstre.est_vivant():
            self.terminee = True
            self.ajouter_message(
                f"VICTOIRE ! {self.heros.nom} a gagne !"
            )
            self.ajouter_message(
                f"Butin obtenu : {self.monstre.butin}"
            )
            return True

        if not self.heros.est_vivant():
            self.terminee = True
            self.ajouter_message(
                f"DEFAITE ! {self.heros.nom} est vaincu."
            )
            return True

        return False

    def tour_monstre(self):
        if self.verifier_fin():
            return

        message = self.monstre.attaquer(self.heros)
        self.ajouter_message(message)
        self.verifier_fin()

    def tour_heros(self, speciale=False):
        if self.terminee:
            return

        if speciale:
            message = self.heros.competence_speciale(
                self.monstre
            )
        else:
            message = self.heros.attaquer(self.monstre)

        self.ajouter_message(message)

        # Une attaque invalide ne consomme pas le tour.
        if (
            message.startswith("Pas assez")
            or message.startswith("Tu ne peux")
        ):
            return

        if self.verifier_fin():
            return

        self.tour_monstre()

    def sauvegarder(self):
        chemin = input(
            "Nom du fichier (exemple : partie.json) : "
        ).strip()

        if not chemin:
            print("Nom de fichier invalide.")
            return

        if not chemin.endswith(".json"):
            chemin += ".json"

        donnees = {
            "heros": self.heros.to_dict(),
            "monstre": self.monstre.to_dict(),
            "historique": self.historique,
            "terminee": self.terminee
        }

        try:
            with open(chemin, "w", encoding="utf-8") as f:
                json.dump(
                    donnees, f,
                    ensure_ascii=False, indent=4
                )
            print("Partie sauvegardee !")
        except OSError as erreur:
            print("Erreur de sauvegarde :", erreur)

    @staticmethod
    def personnage_depuis_dict(d):
        if d["type"] == "Heros":
            p = Heros(
                d["nom"], d["points_de_vie"],
                d["force"], d["mana"]
            )
            p.mana_max = d.get("mana_max", d["mana"])
        elif d["type"] == "Monstre":
            p = Monstre(
                d["nom"], d["points_de_vie"],
                d["force"], d["niveau_de_danger"],
                d["butin"]
            )
        else:
            p = Personnage(
                d["nom"], d["points_de_vie"], d["force"]
            )

        p.pv_max = d.get("pv_max", d["points_de_vie"])
        return p

    @classmethod
    def charger(cls):
        chemin = input(
            "Nom du fichier a charger (partie.json) : "
        ).strip()

        if not chemin:
            print("Nom de fichier invalide.")
            return None

        try:
            with open(chemin, "r", encoding="utf-8") as f:
                d = json.load(f)

            partie = cls()
            partie.heros = cls.personnage_depuis_dict(d["heros"])
            partie.monstre = cls.personnage_depuis_dict(d["monstre"])
            partie.historique = d.get("historique", [])
            partie.terminee = d.get("terminee", False)

            print("Partie chargee !")
            return partie

        except (OSError, json.JSONDecodeError, KeyError,
                TypeError, ValueError) as erreur:
            print("Impossible de charger :", erreur)
            return None


# ==============================
# LANCEMENT DU JEU
# ==============================

def lancer_jeu():
    print("==========================================")
    print("       LES CHRONIQUES DE LANCELOT")
    print("==========================================")
    print("1. Nouvelle partie")
    print("2. Charger une partie")

    while True:
        choix = input("\nTon choix : ").strip()

        if choix == "1":
            partie = Partie()
            break

        elif choix == "2":
            partie = Partie.charger()
            if partie is not None:
                break
            print("Reessaie ou choisis une nouvelle partie.")
        else:
            print("Choisis 1 ou 2.")

    while True:
        partie.afficher_personnages()

        if partie.terminee:
            print("\nCombat termine !")
            print("1. Nouvelle partie")
            print("2. Quitter")

            choix = input("Ton choix : ").strip()

            if choix == "1":
                partie = Partie()
                continue
            elif choix == "2":
                print("Merci d'avoir joue !")
                break
            else:
                print("Choix invalide.")
                continue

        print("\n1. Attaque normale")
        print("2. Attaque speciale (10 mana)")
        print("3. Afficher l'historique")
        print("4. Sauvegarder")
        print("5. Quitter")

        choix = input("\nQue fais-tu ? ").strip()

        if choix == "1":
            partie.tour_heros()

        elif choix == "2":
            partie.tour_heros(speciale=True)

        elif choix == "3":
            print("\n--- HISTORIQUE ---")
            if not partie.historique:
                print("Aucune action pour le moment.")
            else:
                for message in partie.historique:
                    print("- " + message)

        elif choix == "4":
            partie.sauvegarder()

        elif choix == "5":
            print("A bientot, aventurier !")
            break

        else:
            print("Choix invalide.")


if __name__ == "__main__":
    lancer_jeu()