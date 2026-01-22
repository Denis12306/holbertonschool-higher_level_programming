#!/usr/bin/python3
"""
EXERCICE PYTHON - LE MONDE MAGIQUE DE HARRY POTTER

Dans cet exercice, vous allez manipuler des structures de données Python
(listes, dictionnaires et tuples) pour créer et gérer différents aspects
du monde magique de Harry Potter.
"""

# PARTIE 1: MANIPULATION DE LISTES
# --------------------------------

# Voici une liste des élèves de Poudlard
eleves_poudlard = ["Harry Potter", "Hermione Granger", "Ron Weasley", "Drago Malfoy",
                  "Neville Londubat", "Luna Lovegood", "Ginny Weasley", "Cho Chang"]

# TODO: Ajoutez "Cedric Diggory" à la liste des élèves

eleves_poudlard.append("Cedric Diggory")
print(eleves_poudlard)

# TODO: Supprimez "Drago Malfoy" de la liste

eleves_poudlard.remove("Drago Malfoy")
print(eleves_poudlard)

# TODO: Affichez les 3 premiers élèves de la liste

print(eleves_poudlard[:3])

# TODO: Triez la liste des élèves par ordre alphabétique et affichez-la

print(sorted(eleves_poudlard))

# PARTIE 2: MANIPULATION DE DICTIONNAIRES
# --------------------------------------

# Voici un dictionnaire qui associe les élèves à leur maison
maisons = {
    "Harry Potter": "Gryffondor",
    "Hermione Granger": "Gryffondor",
    "Ron Weasley": "Gryffondor",
    "Draco Malfoy": "Serpentard",
    "Luna Lovegood": "Serdaigle",
    "Cho Chang": "Serdaigle",
    "Cedric Diggory": "Poufsouffle",
    "Neville Londubat": "Gryffondor"
}

# TODO: Ajoutez Ginny Weasley à la maison Gryffondor

maisons["Ginny Weasley"] = "Gryffondor"
print(maisons)

# TODO: Créez un dictionnaire comptant le nombre d'élèves par maison
# Résultat attendu: {"Gryffondor": 5, "Serpentard": 1, "Serdaigle": 2, "Poufsouffle": 1}

nb_eleves = {}

for maison in maisons.values():
    if maison in nb_eleves:
        nb_eleves[maison] += 1
    else:
        nb_eleves[maison] = 1

print(nb_eleves)

# TODO: Affichez tous les élèves de Gryffondor

for eleve, maison in maisons.items():
    if maison == "Gryffondor":
        print(eleve)


# PARTIE 3: MANIPULATION DE TUPLES
# -------------------------------

# Les sorts sont représentés par des tuples (nom_du_sort, effet, difficulté)
# La difficulté est notée de 1 (facile) à 5 (très difficile)
sorts = [
    ("Wingardium Leviosa", "Fait léviter des objets", 2),
    ("Expelliarmus", "Désarme l'adversaire", 3),
    ("Expecto Patronum", "Repousse les Détraqueurs", 5),
    ("Accio", "Attire un objet vers le lanceur", 2),
    ("Avada Kedavra", "Sort mortel impardonnable", 5)
]

# TODO: Créez une liste contenant uniquement les noms des sorts

for idx in sorts:
    print(idx[0])

# TODO: Créez une liste des sorts faciles (difficulté <= 2)

for idx in sorts:
    if idx[2] <= 2:
        print(idx)

# TODO: Triez les sorts par niveau de difficulté (du plus facile au plus difficile)

sorts_tries = sorted(sorts, key=lambda x: x[2])
print(sorts_tries)


# PARTIE 4: COMBINAISON DES STRUCTURES
# ----------------------------------

# Dictionnaire associant des personnages à leurs caractéristiques
# Format: {"nom": (âge, "rôle", ["compétence1", "compétence2", ...])}
personnages = {
    "Albus Dumbledore": (115, "Directeur", ["Métamorphose", "Sortilèges", "Duel"]),
    "Severus Rogue": (38, "Professeur", ["Potions", "Occlumancie", "Sortilèges"]),
    "Minerva McGonagall": (70, "Professeur", ["Métamorphose", "Duel"]),
    "Rubeus Hagrid": (65, "Garde-chasse", ["Créatures magiques"])
}

# TODO: Ajoutez une nouvelle compétence "Transplanage" à Albus Dumbledore

personnages["Albus Dumbledore"][2].append("Transplanage")
print(personnages)

# TODO: Créez une liste de tous les professeurs

professeurs = []
for nom, infos in personnages.items():
    poste = infos[1]
    if poste == "Professeur":
        professeurs.append(nom)
print(professeurs)

# TODO: Créez un dictionnaire qui compte le nombre de personnages maîtrisant chaque compétence
# Résultat attendu: {"Métamorphose": 2, "Sortilèges": 2, "Duel": 2, "Potions": 1, ...}

Master_skill= {}


# DÉFI BONUS: LE TOURNOI DES TROIS SORCIERS
# ----------------------------------------

champions = [
    {"nom": "Harry Potter", "école": "Poudlard", "scores": [8, 7, 9]},
    {"nom": "Cedric Diggory", "école": "Poudlard", "scores": [7, 8, 6]},
    {"nom": "Viktor Krum", "école": "Durmstrang", "scores": [9, 6, 8]},
    {"nom": "Fleur Delacour", "école": "Beauxbâtons", "scores": [6, 9, 7]}
]

# TODO: Calculez le score total de chaque champion et déterminez le vainqueur du tournoi


# TODO: Créez un dictionnaire qui indique le score moyen obtenu par chaque école
