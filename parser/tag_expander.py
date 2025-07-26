import json
import os

def expand_biome_tags(tag_map, biome_tag_map):
    expanded_tag_map = {}

    for tag, values in tag_map.items():
        expanded_values = []

        for value in values:
            if isinstance(value, str) and value.startswith("#") and value in biome_tag_map:
                expanded_values.extend(biome_tag_map[value])
            else:
                expanded_values.append(value)

        expanded_tag_map[tag] = expanded_values

    # Criar diretório 'log' se não existir
    log_dir = os.path.join(os.getcwd(), 'log')
    os.makedirs(log_dir, exist_ok=True)

    # Caminho do log
    log_path = os.path.join(log_dir, 'expanded_tag_map.json')
    with open(log_path, 'w', encoding='utf-8') as log_file:
        json.dump(expanded_tag_map, log_file, indent=2, ensure_ascii=False)

    return expanded_tag_map
