import json
import os
from dotenv import load_dotenv

# Charger les variables d'environnement à partir du fichier .env
load_dotenv('.env')

# Récupérer les valeurs des variables d'environnement
zendeskExportFilename = os.getenv('ZENDESK_EXPORT_FILENAME')
zendeskExportFilenameRepaired = os.getenv('ZENDESK_EXPORT_FILENAME_REPAIRED')
search = os.getenv('SEARCH')

# Ouvrir le fichier contenant la liste de JSON
with open(zendeskExportFilename) as f:
    lines = f.readlines()

# Ajouter les caractères pour former un tableau JSON
formatted_data = '[' + ','.join(lines).rstrip('\n') + ']'

# Analyser le tableau JSON en une structure de données Python
data = json.loads(formatted_data)

# Liste pour stocker les éléments sans la chaîne recherchée
filtered_data = []

# Parcourir les éléments du JSON
for element in data:
    # Convertir l'élément en chaîne de caractères
    element_str = json.dumps(element)
    
    # Vérifier si la chaîne recherchée est présente dans l'élément
    if search in element_str:
        # L'élément contient la chaîne recherchée, ne rien faire
        pass
    else:
        # L'élément ne contient pas la chaîne recherchée, l'ajouter à la liste filtrée
        filtered_data.append(element)

# Écrire le JSON filtré dans un fichier
with open(zendeskExportFilenameRepaired, 'w') as f:
    json.dump(filtered_data, f)
