import os
import json

def load_minecraft_biome_tags(mcbiomes_folder="data/mcbiomes"):
    """
    Lê arquivos JSON da pasta `mcbiomes` e retorna um dicionário com tags
    no formato #minecraft:tag_name → [bioma1, bioma2, ...]
    """
    tag_map = {}

    for root, _, files in os.walk(mcbiomes_folder):
        files = sorted([f for f in files if f.endswith(".json")])

        for file in files:
            tag_name = f"#minecraft:{file.replace('.json', '')}"
            path = os.path.join(root, file)

            with open(path, encoding='utf-8') as f:
                data = json.load(f)
                values = data.get("values", [])
                tag_map[tag_name] = values

    # Criar log
    log_dir = "log"
    os.makedirs(log_dir, exist_ok=True)
    log_path = os.path.join(log_dir, "minecraft_tag_map.json")

    with open(log_path, "w", encoding="utf-8") as f:
        json.dump(tag_map, f, indent=2, ensure_ascii=False)
        
    return tag_map
