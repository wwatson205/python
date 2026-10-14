"""
CORRECTION - Exercices POO : Personnage, Heros, Monstre (RPG)

Ce fichier contient une correction propre et commentée de tous les exercices.
Niveau : Débutant/Intermédiaire
"""

import json


# ============================================================================
# PARTIE A : Classe Personnage de base
# ============================================================================

class Personnage:
    """Un personnage générique : nom, points de vie, force d'attaque."""

    def __init__(self, nom: str, points_de_vie: int, force: int):
        """Initialise un personnage.

        Args:
            nom (str): Le nom du personnage
            points_de_vie (int): Les points de vie initiaux
            force (int): La force d'attaque
        """
        self.nom = nom
        self.points_de_vie = points_de_vie
        self.force = force

    def est_vivant(self):
        """Retourne True si le personnage a au moins 1 PV, False sinon."""
        return self.points_de_vie > 0

    def subir_degats(self, degats: int):
        """Réduit les points de vie du personnage.

        Les PV ne descendent jamais sous 0 (grâce à max()).

        Args:
            degats (int): Le nombre de dégâts infligés
        """
        self.points_de_vie = max(self.points_de_vie - degats, 0)

    def attaquer(self, cible: "Personnage") -> str:
        """Attaque une cible et retourne un message de combat.

        Cette méthode :
        1. Applique self.force en dégâts à la cible
        2. Retourne un message du combat (très important pour l'historique)

        Args:
            cible (Personnage): Le personnage à attaquer

        Returns:
            str: Message du type "Aldric attaque Gobelin et lui inflige 8 dégâts..."
        """
        # On applique les dégâts à la cible via sa méthode subir_degats
        cible.subir_degats(self.force)

        # On retourne un message (pas print !) pour pouvoir l'ajouter à l'historique
        return f"{self.nom} attaque {cible.nom} et lui inflige {self.force} dégâts ({cible.nom}: {cible.points_de_vie} PV restant)"

    def to_dict(self) -> dict:
        """Convertit le personnage en dictionnaire pour sauvegarder en JSON.

        La clé 'type' permet de reconstruire le bon type d'objet à la lecture.

        Returns:
            dict: Dictionnaire avec type, nom, points_de_vie, force
        """
        return {
            "type": "Personnage",
            "nom": self.nom,
            "points_de_vie": self.points_de_vie,
            "force": self.force
        }

    def sauvegarder(self, chemin: str):
        """Sauvegarde le personnage dans un fichier JSON.

        Args:
            chemin (str): Le chemin du fichier (ex: "personnage.json")
        """
        data = self.to_dict()

        # Ouvrir le fichier en mode écriture et y mettre le dictionnaire
        with open(chemin, 'w', encoding='utf-8') as fichier:
            json.dump(data, fichier, indent=2, ensure_ascii=False)

    def __repr__(self) -> str:
        """Retourne une représentation lisible du personnage.

        Utilisée quand on print l'objet.

        Returns:
            str: Chaîne du type "Aldric (30 PV | 8 Force)"
        """
        return f"{self.nom} ({self.points_de_vie} PV | {self.force} Force)"


# ============================================================================
# PARTIE B : Héritage - Classe Heros
# ============================================================================

class Heros(Personnage):
    """Un héros hérite de Personnage et ajoute la magie avec le mana."""

    def __init__(self, nom: str, points_de_vie: int, force: int, mana: int):
        """Initialise un héros.

        Args:
            nom (str): Le nom du héros
            points_de_vie (int): Les points de vie initiaux
            force (int): La force d'attaque
            mana (int): Les points de mana pour les capacités spéciales
        """
        # On appelle le constructeur parent pour initialiser les attributs communs
        super().__init__(nom, points_de_vie, force)

        # On ajoute l'attribut spécifique au héros
        self.mana = mana

    def competence_speciale(self, cible: Personnage) -> str:
        """Lance une attaque spéciale qui coûte 10 mana et inflige 2x la force.

        Args:
            cible (Personnage): La cible de l'attaque

        Returns:
            str: Message du résultat (succès ou échec/mana manquant)
        """
        # Vérifier qu'on a assez de mana (10 points minimum)
        if self.mana >= 10:
            # Déduire 10 mana (attention : bug courant = self.mana -= self.mana !)
            self.mana -= 10

            # Infliger 2x la force en dégâts
            degats = 2 * self.force
            cible.subir_degats(degats)

            # Retourner le message d'attaque
            return f"{self.nom} lance une attaque spéciale sur {cible.nom} et lui inflige {degats} dégâts ({cible.nom}: {cible.points_de_vie} PV restant)"
        else:
            # Pas assez de mana
            return f"Impossible de lancer un sort. Mana manquant. ({self.mana}/10)"

    def to_dict(self) -> dict:
        """Convertit le héros en dictionnaire.

        On réutilise le to_dict() du parent pour ne pas recopier les attributs.
        """
        # Appeler le to_dict() parent
        donnees = super().to_dict()

        # Remplacer le type par "Heros"
        donnees['type'] = "Heros"

        # Ajouter l'attribut spécifique du héros
        donnees['mana'] = self.mana

        return donnees

    def __repr__(self) -> str:
        """Représentation lisible du héros avec mana affiché."""
        return f"{self.nom} ({self.points_de_vie} PV | {self.force} Force | {self.mana} PM)"


# ============================================================================
# PARTIE B : Héritage - Classe Monstre
# ============================================================================

class Monstre(Personnage):
    """Un monstre hérite de Personnage et ajoute un niveau de danger et du butin."""

    def __init__(self, nom: str, points_de_vie: int, force: int,
                 niveau_de_danger: int, butin: str):
        """Initialise un monstre.

        Args:
            nom (str): Le nom du monstre
            points_de_vie (int): Les points de vie initiaux
            force (int): La force d'attaque de base
            niveau_de_danger (int): Multiplicateur de dégâts
            butin (str): Description du butin (ex: "10 pièces d'or")
        """
        # Appeler le constructeur parent
        super().__init__(nom, points_de_vie, force)

        # Ajouter les attributs spécifiques au monstre
        self.niveau_de_danger = niveau_de_danger
        self.butin = butin

    def attaquer(self, cible: Personnage) -> str:
        """Overriding : un monstre inflige force * niveau_de_danger en dégâts.

        C'est un exemple de polymorphisme : on réutilise la même interface
        (la méthode attaquer) mais avec un comportement différent.

        Args:
            cible (Personnage): La cible de l'attaque

        Returns:
            str: Message du combat
        """
        # Calculer les dégâts : force * niveau_de_danger
        degats = self.force * self.niveau_de_danger

        # Appliquer les dégâts
        cible.subir_degats(degats)

        # Retourner le message (noter : on affiche les dégâts réels)
        return f"{self.nom} attaque {cible.nom} et lui inflige {degats} dégâts ({cible.nom}: {cible.points_de_vie} PV restant)"

    def to_dict(self) -> dict:
        """Convertit le monstre en dictionnaire."""
        donnees = super().to_dict()
        donnees['type'] = "Monstre"
        donnees['niveau_de_danger'] = self.niveau_de_danger
        donnees['butin'] = self.butin
        return donnees

    def __repr__(self) -> str:
        """Représentation lisible du monstre avec danger affiché."""
        return f"{self.nom} ({self.points_de_vie} PV | {self.force} Force | Danger: {self.niveau_de_danger} | Butin: {self.butin})"


# ============================================================================
# PARTIE C : Charger un personnage depuis JSON
# ============================================================================

def charger_personnage(chemin: str) -> Personnage:
    """Relit un fichier JSON et reconstruit le bon type de personnage.

    On utilise la clé 'type' pour savoir quel constructeur appeler.

    Args:
        chemin (str): Chemin du fichier JSON

    Returns:
        Personnage: L'objet reconstruit (Personnage, Heros ou Monstre)
    """
    # Lire le fichier JSON
    with open(chemin, 'r', encoding='utf-8') as fichier:
        donnees = json.load(fichier)

    # Selon le type, appeler le bon constructeur
    # Pattern : match/case (Python 3.10+)
    match donnees['type']:
        case "Personnage":
            return Personnage(
                nom=donnees['nom'],
                points_de_vie=donnees['points_de_vie'],
                force=donnees['force']
            )

        case "Heros":
            return Heros(
                nom=donnees['nom'],
                points_de_vie=donnees['points_de_vie'],
                force=donnees['force'],
                mana=donnees['mana']
            )

        case "Monstre":
            return Monstre(
                nom=donnees['nom'],
                points_de_vie=donnees['points_de_vie'],
                force=donnees['force'],
                niveau_de_danger=donnees['niveau_de_danger'],
                butin=donnees['butin']
            )

        case _:
            # Type inconnu
            raise ValueError(f"Type de personnage inconnu: {donnees['type']}")


# ============================================================================
# PARTIE D : Gérer une partie avec historique
# ============================================================================

class Partie:
    """Représente une partie de jeu avec personnages et historique des combats."""

    def __init__(self):
        """Initialise une partie vide."""
        self.personnages = []      # Liste des personnages en jeu
        self.historique = []       # Liste des messages de combat

    def ajouter_personnage(self, personnage: Personnage):
        """Ajoute un personnage à la partie.

        Args:
            personnage (Personnage): Le personnage à ajouter
        """
        self.personnages.append(personnage)

    def combat(self, attaquant: Personnage, defenseur: Personnage):
        """Lance un combat entre deux personnages.

        1. Appelle la méthode attaquer de l'attaquant
        2. Ajoute le message à l'historique
        3. Si le défenseur est vaincu, ajoute un message de victoire

        Args:
            attaquant (Personnage): Celui qui attaque
            defenseur (Personnage): Celui qui reçoit l'attaque
        """
        # Faire attaquer et récupérer le message
        message_attaque = attaquant.attaquer(defenseur)

        # Ajouter à l'historique
        self.historique.append(message_attaque)

        # Vérifier si le défenseur est vaincu
        if not defenseur.est_vivant():
            message_victoire = f"💀 {defenseur.nom} est vaincu !"
            self.historique.append(message_victoire)

    def sauvegarder(self, chemin: str):
        """Sauvegarde la partie complète en JSON.

        Sauvegarde l'historique et la liste des personnages.

        Args:
            chemin (str): Chemin du fichier JSON
        """
        # Créer le dictionnaire de la partie
        donnees = {
            "historique": self.historique,
            "personnages": [p.to_dict() for p in self.personnages]
        }

        # Sauvegarder dans le fichier
        with open(chemin, 'w', encoding='utf-8') as fichier:
            json.dump(donnees, fichier, indent=2, ensure_ascii=False)


def charger_partie(chemin: str) -> Partie:
    """Charge une partie complète depuis un fichier JSON.

    Bonus : fonction facultative de la partie D.

    Args:
        chemin (str): Chemin du fichier JSON

    Returns:
        Partie: La partie complète avec personnages et historique
    """
    with open(chemin, 'r', encoding='utf-8') as fichier:
        donnees = json.load(fichier)

    # Créer une partie vide
    partie = Partie()

    # Ajouter l'historique
    partie.historique = donnees.get("historique", [])

    # Reconstruire chaque personnage en créant temporairement un fichier JSON
    for p_dict in donnees.get("personnages", []):
        # Créer un fichier temporaire pour charger avec charger_personnage
        temp_file = "__temp_load__.json"
        with open(temp_file, 'w', encoding='utf-8') as f:
            json.dump(p_dict, f)

        # Charger le personnage
        personnage = charger_personnage(temp_file)
        partie.ajouter_personnage(personnage)

        # Supprimer le fichier temporaire
        import os
        os.remove(temp_file)

    return partie


# ============================================================================
# TESTS - Partie A
# ============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("TESTS - PARTIE A : Classe Personnage")
    print("=" * 70)

    gobelin = Personnage("Gobelin", 20, 5)
    aldric = Personnage("Aldric", 30, 8)

    print(f"\nAzantage initial :")
    print(f"  {aldric}")
    print(f"  {gobelin}")

    print(f"\nAldric attaque Gobelin :")
    message = aldric.attaquer(gobelin)
    print(f"  {message}")
    print(f"  État actuel: {gobelin}")

    print(f"\nGobelin contre-attaque :")
    message = gobelin.attaquer(aldric)
    print(f"  {message}")
    print(f"  État actuel: {aldric}")


    # ========================================================================
    # TESTS - Partie B
    # ========================================================================
    print("\n" + "=" * 70)
    print("TESTS - PARTIE B : Héritage (Heros et Monstre)")
    print("=" * 70)

    lancelot = Heros("Lancelot", 40, 10, mana=25)
    gobelin_fort = Monstre("Gobelin", 20, 5, niveau_de_danger=2, butin="10 pièces d'or")

    print(f"\nÉtat initial :")
    print(f"  {lancelot}")
    print(f"  {gobelin_fort}")

    print(f"\nMonstre attaque (dégâts = 5 * 2 = 10) :")
    msg = gobelin_fort.attaquer(lancelot)
    print(f"  {msg}")

    print(f"\nHéros lance attaque spéciale (2 * 10 = 20 dégâts, coûte 10 mana) :")
    msg = lancelot.competence_speciale(gobelin_fort)
    print(f"  {msg}")
    print(f"  Mana restant: {lancelot.mana}")

    print(f"\nDeuxième attaque spéciale (mana 15 -> 5) :")
    msg = lancelot.competence_speciale(gobelin_fort)
    print(f"  {msg}")
    print(f"  Mana restant: {lancelot.mana}")

    print(f"\nTroisième attaque (mana 5 < 10, échoue) :")
    msg = lancelot.competence_speciale(gobelin_fort)
    print(f"  {msg}")
    print(f"  Gobelin toujours: {gobelin_fort.est_vivant()}")


    # ========================================================================
    # TESTS - Partie C
    # ========================================================================
    print("\n" + "=" * 70)
    print("TESTS - PARTIE C : Sauvegarder et charger en JSON")
    print("=" * 70)

    print(f"\nSauvegarde de Lancelot...")
    lancelot.sauvegarder("lancelot.json")

    print(f"Rechargement depuis JSON...")
    lancelot_recharge = charger_personnage("lancelot.json")
    print(f"  Objet recharger: {lancelot_recharge}")
    print(f"  Mana: {lancelot_recharge.mana}")
    print(f"  Type: {type(lancelot_recharge).__name__}")


    # ========================================================================
    # TESTS - Partie D
    # ========================================================================
    print("\n" + "=" * 70)
    print("TESTS - PARTIE D : Classe Partie avec historique")
    print("=" * 70)

    # Créer une nouvelle partie
    partie = Partie()

    # Ajouter les combattants
    heros = Heros("Lancelot", 50, 12, mana=30)
    ennemi = Monstre("Orc", 35, 7, niveau_de_danger=3, butin="20 pièces d'or")

    partie.ajouter_personnage(heros)
    partie.ajouter_personnage(ennemi)

    print(f"\nCombat entre {heros.nom} et {ennemi.nom} :")

    # Tour 1 : Heros attaque
    partie.combat(heros, ennemi)

    # Tour 2 : Orc contre-attaque
    partie.combat(ennemi, heros)

    # Tour 3 : Heros compétence spéciale
    partie.combat(heros, ennemi)

    print(f"\nHistorique du combat :")
    for i, evenement in enumerate(partie.historique, 1):
        print(f"  {i}. {evenement}")

    print(f"\nSauvegarde de la partie...")
    partie.sauvegarder("partie.json")

    print(f"\nRechargement de la partie...")
    partie_recharge = charger_partie("partie.json")
    print(f"Personnages rechargés: {len(partie_recharge.personnages)}")
    print(f"Événements: {len(partie_recharge.historique)}")
    print(f"Premier événement: {partie_recharge.historique[0]}")


    print("\n" + "=" * 70)
    print("✅ Tous les tests sont terminés !")
    print("=" * 70)
