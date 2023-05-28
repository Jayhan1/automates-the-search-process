import requests

def retrieve_scientist_info(scientist_name):
    url = f"https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json&language=ar&search={scientist_name}"
    response = requests.get(url)
    data = response.json()

    if 'search' in data:
        search_results = data['search']

        if search_results:
            result = search_results[0]
            scientist_id = result['id']
            url = f"https://www.wikidata.org/wiki/Special:EntityData/{scientist_id}.json"
            response = requests.get(url)
            data = response.json()

            if 'entities' in data and scientist_id in data['entities']:
                scientist_data = data['entities']
                labels = scientist_data[scientist_id]['labels']
                descriptions = scientist_data[scientist_id]['descriptions']
                scientist_info = {
                    "Scientist": labels.get('ar', {}).get('value', scientist_name),
                    "Brief description": descriptions.get('ar', {}).get('value', "N/A"),
                    "Field of study": [],
                    "Place of birth": []
                }

                if 'claims' in scientist_data[scientist_id]:
                    claims = scientist_data[scientist_id]['claims']
                    if 'P101' in claims:
                        for claim in claims['P101']:
                            if 'mainsnak' in claim and 'datavalue' in claim['mainsnak']:
                                field_id = claim['mainsnak']['datavalue']['value']['id']
                                field_label, field_description = retrieve_entity_info(field_id)
                                scientist_info['Field of study'].append((field_label, field_description))

                    if 'P19' in claims:
                        for claim in claims['P19']:
                            if 'mainsnak' in claim and 'datavalue' in claim['mainsnak']:
                                place_id = claim['mainsnak']['datavalue']['value']['id']
                                place_label, place_description = retrieve_entity_info(place_id)
                                scientist_info['Place of birth'].append((place_label, place_description))

                return scientist_info

    return None

def retrieve_entity_info(entity_id):
    url = f"https://www.wikidata.org/wiki/Special:EntityData/{entity_id}.json"
    response = requests.get(url)
    data = response.json()

    if 'entities' in data and entity_id in data['entities']:
        entity_data = data['entities'][entity_id]
        label = entity_data['labels'].get('ar', {}).get('value', entity_data['labels'].get('en', {}).get(''))
        description = entity_data['descriptions'].get('ar', {}).get('value', entity_data['descriptions'].get('en', {}).get(''))
        return label, description

    return "", ""

scientist_name = input("Enter the scientist's name: ")
scientist_info = retrieve_scientist_info(scientist_name)

if scientist_info:
    print(f"Scientist: {scientist_info['Scientist']}")
    print(f"Brief description: {scientist_info['Brief description']}")
    
    print("Field of study:")
    for field in scientist_info['Field of study']:
        print(f"- {field[0]}: {field[1]}")

    print("Place of birth:")
    for place in scientist_info['Place of birth']:
        print(f"- {place[0]}: {place[1]}")
else:
    print("Unable to retrieve information for the scientist.")
