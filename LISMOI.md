# Outil d'Analyse des Codes Postaux Français

Script Python pour analyser et interroger une base de données CSV des codes postaux, villes et coordonnées GPS françaises.

## Fonctionnalités

- **Traitement des Données CSV**
  - Lecture et nettoyage des données depuis la base officielle des codes postaux
  - Gestion des caractères spéciaux et du formatage

- **Fonctions de Recherche**
  - Rechercher des villes par code postal
  - Rechercher des codes postaux par nom de ville
  - Rechercher des villes par latitude/longitude
  - Obtenir les coordonnées GPS d'une ville
  - Compter les villes partageant le même code postal

## Utilisation

### Prérequis
- Python 3.x
- Fichier CSV : base-officielle-codes-postaux.csv

### Fonctions Principales

```python
# Trouver les villes par code postal
TrouverCommunes(64270)  # Renvoie la liste des villes avec ce code postal

# Trouver les codes postaux d'une ville
RechercheCP("Orthez")  # Renvoie la liste des codes postaux

# Trouver les villes par latitude
TrouverMemeLatitudes(43.5, donnees)  # Renvoie les villes proches de cette latitude

# Trouver les villes par longitude
TrouverMemeLongitude(0, donnees)  # Renvoie les villes proches de cette longitude

# Obtenir les coordonnées GPS d'une ville
GPS("Orthez")  # Renvoie un tuple (latitude, longitude)

# Compter les villes avec un code postal spécifique
CompterEffectifCodePostal(64270)  # Renvoie le nombre de villes
```

### Exemple de Sortie

```
Villes avec le code postal 64270 : ['SALIES-DE-BEARN']
Coordonnées GPS de Orthez : (43.485, -0.785)
Nombre de villes ayant le code postal 64270 : 1
```

## Structure des Données
Le script utilise un fichier CSV avec les colonnes suivantes :
- code_commune_insee
- nom_de_la_commune
- code_postal
- libelle_d_acheminement
- lieux-fuisonés
- latitude
- longitude

## Gestion des Erreurs
- Gestion des données manquantes ou mal formatées
- Suggestions pour les noms de villes mal orthographiés
- Messages d'erreur appropriés pour les entrées invalides
