import csv
import json
import os
from dotenv import load_dotenv

def get_json_paths(data, path=""):
    paths = []
    if isinstance(data, dict):
        for key, value in data.items():
            if "User has updated this ticket" in str(value):
                paths.append(f"{path}.{key}")
            paths.extend(get_json_paths(value, f"{path}.{key}"))
    elif isinstance(data, list):
        for index, item in enumerate(data):
            paths.extend(get_json_paths(item, f"{path}[{index}]"))
    return paths

def get_value_at_path(data, path):
    components = path.replace("[", ".").replace("]", "").split(".")
    if components[0] == "":
        components.pop(0)
    value = data
    try:
        for component in components:
            if component.isdigit():
                value = value[int(component)]
            else:
                value = value[component]
    except (KeyError, IndexError):
        value = None
    return value

# Charger les variables d'environnement à partir du fichier .env
load_dotenv('.env')

# Récupérer les valeurs des variables d'environnement
zendeskExportFilename = os.getenv('ZENDESK_EXPORT_FILENAME')
zendeskExportFilenameRepaired = os.getenv('ZENDESK_EXPORT_FILENAME_REPAIRED')
search = os.getenv('SEARCH')
search2 = os.getenv('SEARCH2')

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
    if search in element_str or search2 in element_str:
        # L'élément contient l'une des deux chaînes recherchées, ne rien faire
        pass
    else:
        # L'élément ne contient ni la première chaîne ni la deuxième chaîne, l'ajouter à la liste filtrée
        filtered_data.append(element)

# Écrire le JSON filtré dans un fichier
with open(zendeskExportFilenameRepaired, 'w') as f:
    json.dump(filtered_data, f)
    
# Écrire les éléments filtrés dans un fichier CSV avec une nouvelle ligne pour chaque élément 
with open('resultat.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['URL', 'ID', 'Name', 'Email', "Note", "UserHas"])  # En-tête du fichier CSV

    # Écrire chaque élément dans une nouvelle ligne du fichier CSV
    for element in filtered_data:
        element_id = element["id"]
        url = "https://jobberssas.zendesk.com/agent/tickets/" + str(element_id)
        name = element["submitter"]["name"]
        email = element["submitter"]["email"]
        note = int(element["custom_fields"][6]["value"])
        true_note = 0
        if note > 10:
            true_note = 5
        if note >= 0 and note <= 5:
            true_note = note
        if note > 5 and note < 10:
            true_note = note / 2
        if note == 10:
            true_note = 5
        
        
        date = "Manually updated"
        user_has_updated = "User has updated this ticket" in json.dumps(element)
        if user_has_updated:
            paths = get_json_paths(element)
            path = paths[1].replace("body", "created_at")
            date = get_value_at_path(element, path)
        else:
            date = element["metric_set"]["updated_at"] + " (not sure ?)"
        
        writer.writerow([url, element_id, name, email, true_note, date])
