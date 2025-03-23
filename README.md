# French Postal Code Analysis Tool

A Python script for analyzing and querying French postal codes, cities, and their GPS coordinates from a CSV database.

## Features

- **CSV Data Processing**
  - Clean and load data from official French postal code database
  - Handle special characters and formatting

- **Search Functions**
  - Find cities by postal code
  - Find postal codes by city name
  - Search cities by latitude/longitude
  - Get GPS coordinates for any city
  - Count cities sharing the same postal code

## Usage

### Prerequisites
- Python 3.x
- CSV file: `base-officielle-codes-postaux.csv`

### Main Functions

```python
# Find cities by postal code
TrouverCommunes(64270)  # Returns list of cities with this postal code

# Find postal codes for a city
RechercheCP("Orthez")  # Returns list of postal codes

# Find cities by latitude
TrouverMemeLatitudes(43.5, donnees)  # Returns cities near this latitude

# Find cities by longitude
TrouverMemeLongitude(0, donnees)  # Returns cities near this longitude

# Get GPS coordinates for a city
GPS("Orthez")  # Returns (latitude, longitude) tuple

# Count cities with specific postal code
CompterEffectifCodePostal(64270)  # Returns number of cities
```

### Example Output

```
Cities with postal code 64270: ['SALIES-DE-BEARN']
GPS coordinates of Orthez: (43.485, -0.785)
Number of cities with postal code 64270: 1
```

## Data Structure
The script expects a CSV file with the following columns:
- code_commune_insee
- nom_de_la_commune
- code_postal
- libelle_d_acheminement
- lieux-fuisonés
- latitude
- longitude

## Error Handling
- Handles missing or malformed data
- Provides suggestions for misspelled city names
- Returns appropriate error messages for invalid inputs
