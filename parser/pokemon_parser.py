import json
import os

def parse_pokemon_spawns(spawn_folder):
    pokemon_data = []

    for root, dirs, files in os.walk(spawn_folder):
        dirs.sort()  # Ordena as pastas
        files = sorted([f for f in files if f.endswith('.json')])  # Ordena os arquivos

        for file in files:
            path = os.path.join(root, file)

            with open(path, encoding='utf-8') as f:
                data = json.load(f)
                for info in data.get("spawnInfos", []):
                    spec = info.get("spec", "UNKNOWN").replace("species:", "")
                    spawn_type = ", ".join(info.get("stringLocationTypes", ["ANY"]))
                    min_level = info.get("minLevel", "ANY")
                    max_level = info.get("maxLevel", "ANY")
                    time = ", ".join(info.get("condition", {}).get("times", ["ANY"]))
                    rarity = info.get("rarity", "ANY")
                    biomes = info.get("condition", {}).get("biomes", [])
                    anti_biomes = info.get("anticondition", {}).get("biomes", [])
                    max_y = info.get("condition", {}).get("maxY", "ANY")

                    pokemon_data.append({
                        "Pokemon": spec,
                        "Location Type": spawn_type,
                        "Min Level": min_level,
                        "Max Level": max_level,
                        "Time": time,
                        "Rarity": rarity,
                        "Biomes": biomes,
                        "Anti Biomes": anti_biomes,
                        "MaxY": max_y
                    })

    # Salvar JSON
    os.makedirs("log", exist_ok=True)
    with open("log/pokemon_data.json", "w", encoding="utf-8") as f:
        json.dump(pokemon_data, f, indent=2, ensure_ascii=False)

    return pokemon_data
