#Programme 180 (Code postal/Insee csv) --> Version GPT
def LectureFichier(chemin):
    """Lecture et nettoyage des données depuis un fichier CSV"""
    # Ouvre le fichier et lit toutes les lignes
    with open(chemin, "r", encoding="utf-8") as fichier:
        donnees = fichier.readlines()

    # Traitement des descripteurs (en-têtes)
    descripteurs = donnees[0].rstrip("\n").split(",")
    # Nettoyage des descripteurs
    descripteurs = [d.replace('"', '').strip() for d in descripteurs]

    # Traitement des données
    tab = []
    for i in range(1, len(donnees)):  # Parcourt les lignes de données
        # Sépare et nettoie chaque ligne
        ligne = donnees[i].rstrip("\n").split(",")
        # Nettoyage des valeurs
        ligne = [col.replace('"', '').strip() for col in ligne]
        tab.append(ligne)

    return descripteurs, tab

# Test de la fonction
descripteurs, donnees = LectureFichier('base-officielle-codes-postaux.csv')

def AfficherDescripteurs():
    """Affiche les descripteurs"""
    for descripteur in descripteurs:
        print(descripteur)

AfficherDescripteurs()


def TrouverCommunes(CP):
    """Entrée : un code postal (type int)
    Sortie : la liste des la liste des villes (type str) qui ont ce code postal"""
    res=[]
    for commune in donnees:
        if commune[2]==str(CP):
            res.append(commune[1])
    if res==[]:
        res="Aucune commune n'a ce code postal"
    return res


print(TrouverCommunes(64270))


def RechercheCP(ville):
    """Entrée : une ville (type str)
    Sortie : liste des codes postaux de la ville (type list)"""
    res = []  # Liste des codes postaux trouvés
    suggestions = []  # Liste des villes similaires

    for commune in donnees:
        if commune[1] == ville.upper():
            res.append(int(commune[2]))  # Ajout du CP sous forme d'entier
        elif ville.upper() in commune[1]:  # Recherche partielle
            suggestions.append(commune[1])

    if not res:  # Si aucun CP trouvé
        if suggestions:
            return f"Aucune ville exacte trouvée. Vouliez-vous dire : {', '.join(suggestions)} ?"
        return "Aucune ville trouvée. Avez-vous bien marqué le nom de la ville ?"

    return res  # Retourne la liste des codes postaux trouvés

print(RechercheCP("Orthez"))
print("----------------------")

def TrouverMemeLatitudes(latitude, donnees):
    """Entrée : une latitude (type float)
    Sortie : la liste des villes (type str) qui ont cette latitude"""
    res = []
    for commune in donnees:
        try:
            if commune[5] and commune[1] not in res:  # Index 5 est la latitude
                lat = float(commune[5])
                if latitude-0.01 <= lat <= latitude+0.01:  # Compare avec la latitude entrée
                        res.append(commune[1])
        except (ValueError, IndexError):
            continue
    
    return res if res else "Aucune ville n'a cette latitude"

# Test avec une latitude spécifique
test_latitude = 43.5
print(f"Villes avec une latitude proche de {test_latitude}:\n")
print(TrouverMemeLatitudes(test_latitude, donnees))
print("----------------------")


# Trouver les villes qui ont la même longitude
def TrouverMemeLongitude(longitude, donnees):
    """Entrée : une longitude (type float)
    Sortie : la liste des villes (type str) qui ont cette longitude"""
    res = []
    for commune in donnees:
        try:
            if commune[5] and commune[1] not in res:  # Index 5 est la longitude
                lat = float(commune[6])
                if longitude-0.01 <= lat <= longitude+0.01:  # Compare avec la longitude entrée
                        res.append(commune[1])
        except (ValueError, IndexError):
            continue
    
    return res if res else "Aucune ville n'a cette longitude"

# Test avec une longitude spécifique
test_longitude = 0
print(f"Villes avec une longitude proche de {test_longitude}:\n")
print(TrouverMemeLongitude(test_longitude, donnees))
print("----------------------")


# Chercher les coordonnées d'une ville
def GPS(ville):
    """Entrée : une ville (type str)
    Sortie : les coordonnées GPS de la ville (type tuple)"""
    for commune in donnees:
        if commune[1] == ville.upper():
            return float(commune[5]), float(commune[6])
    return "Ville introuvable"

print("Coordonnées GPS de Orthez:")
print(GPS("Orthez"))
print("----------------------")

#Compter le nombre de villes ayant un code postal spécifique
def CompterEffectifCodePostal(CodePostal):
    """Compte le nombre de villes ayant ce code postal"""
    NbVilles = TrouverCommunes(CodePostal)
    return len(NbVilles)

test_postal=64270
print(f"Nombre de villes ayant {test_postal} comme code postal : {CompterEffectifCodePostal(test_postal)}")