import json
import os
from dotenv import load_dotenv

# Charger les variables d'environnement à partir du fichier .env
load_dotenv('.env')

# Récupérer les valeurs des variables d'environnement
zendeskExportFilename = os.getenv('ZENDESK_EXPORT_FILENAME')
zendeskExportFilenameRepaired = os.getenv('ZENDESK_EXPORT_FILENAME_REPAIRED')

# Ouvrir le fichier contenant la liste de JSON
with open(zendeskExportFilename) as f:
    lines = f.readlines()

# Ajouter les caractères pour former un tableau JSON
formatted_data = '[' + ','.join(lines).rstrip('\n') + ']'

# Analyser le tableau JSON en une structure de données Python
data = json.loads(formatted_data)

# Parcourir les éléments du tableau JSON
for element in data:
    # Faire quelque chose avec chaque élément
    print(element)

# Écrire le tableau JSON dans un fichier
with open(zendeskExportFilenameRepaired, 'w') as f:
    json.dump(data, f)
