import os
import json

def expand_biomes(biome_list, tag_map):
    expanded = []
    for biome in biome_list:
        if biome.startswith("#") and biome in tag_map:
            expanded.extend(tag_map[biome])
        else:
            expanded.append(biome)
    return expanded

def expand_pokemon_spawns(spawn_folder, final_tag_map):
    combined_spawns = {}

    for root, _, files in os.walk(spawn_folder):
        for file in sorted(files):
            if file.endswith(".json"):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    try:
                        data = json.load(f)
                        if isinstance(data, dict) and "spawnInfos" in data:
                            for info in data["spawnInfos"]:
                                # Condições normais
                                condition = info.get("condition", {})
                                if "biomes" in condition:
                                    condition["biomes"] = expand_biomes(condition["biomes"], final_tag_map)
                                if "stringBiomes" in condition:
                                    condition["stringBiomes"] = expand_biomes(condition["stringBiomes"], final_tag_map)

                                # Anti-condições
                                anticond = info.get("anticondition", {})
                                if "biomes" in anticond:
                                    anticond["biomes"] = expand_biomes(anticond["biomes"], final_tag_map)
                                if "stringBiomes" in anticond:
                                    anticond["stringBiomes"] = expand_biomes(anticond["stringBiomes"], final_tag_map)

                            combined_spawns[file.replace(".json", "")] = data
                        else:
                            print(f"[IGNORADO] {file} não possui 'spawnInfos'")
                    except Exception as e:
                        print(f"[ERRO] ao processar {file}: {e}")

    os.makedirs("log", exist_ok=True)
    output_path = os.path.join("log", "final_data.json")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(combined_spawns, f, indent=2, ensure_ascii=False)

    return combined_spawns
