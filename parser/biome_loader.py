import json
import os

def load_biome_tags(biome_folder):
    tag_map = {}

    for root, _, files in os.walk(biome_folder):
        files = sorted([file for file in files if file.endswith('.json')])  # Ordenação alfabética

        for file in files:
            path = os.path.join(root, file)
            tag = f"#pixelmon:spawning/{file.replace('.json', '')}"

            with open(path, encoding='utf-8') as f:
                data = json.load(f)
                raw_values = data.get("values", [])

                # Converter todos os valores em strings
                parsed_values = []
                for value in raw_values:
                    if isinstance(value, str):
                        parsed_values.append(value)
                    elif isinstance(value, dict) and "id" in value:
                        parsed_values.append(value["id"])

                tag_map[tag] = parsed_values

    # Criar diretório 'log' se não existir
    log_dir = os.path.join(os.getcwd(), 'log')
    os.makedirs(log_dir, exist_ok=True)

    # Caminho do log
    log_path = os.path.join(log_dir, 'tag_map.json')
    with open(log_path, 'w', encoding='utf-8') as log_file:
        json.dump(tag_map, log_file, indent=2, ensure_ascii=False)

    return tag_map
