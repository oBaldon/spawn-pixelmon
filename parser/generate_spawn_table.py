import os
import pandas as pd
import json

def generate_spawn_table(expanded_data: dict, output_path: str = "pokemon_spawn_table.csv"):
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)

    rows = []

    for file_name, data in expanded_data.items():
        spawn_infos = data.get("spawnInfos", [])

        for entry in spawn_infos:
            row = {}

            # Nome
            spec = entry.get("spec", ".BUG")
            row["Name"] = spec.replace("species:", "") if isinstance(spec, str) else "ANY"

            row["minLevel"] = entry.get("minLevel", "ANY")
            row["maxLevel"] = entry.get("maxLevel", "ANY")

            # Condição
            condition = entry.get("condition", {})
            times = condition.get("times", "ANY")
            row["Times"] = ", ".join(times) if isinstance(times, list) else times

            # LocationTypes (tudo de stringLocationTypes)
            location_types = entry.get("stringLocationTypes", [])
            row["LocationTypes"] = ", ".join(location_types) if location_types else "NONE"

            # Biomes
            biomes = (
                condition.get("biomes")
                or condition.get("stringBiomes")
                or entry.get("stringBiomes")
                or "ANY"
            )
            row["Biome"] = ", ".join(biomes) if isinstance(biomes, list) else biomes

            # AntiBiomes
            anticondition = entry.get("anticondition", {})
            antibiomes = (
                anticondition.get("biomes")
                or anticondition.get("stringBiomes")
                or "NONE"
            )
            row["AntiBiome"] = ", ".join(antibiomes) if isinstance(antibiomes, list) else antibiomes

            # Rarity
            row["Rarity"] = entry.get("rarity", entry.get("Rarity", "ANY"))

            rows.append(row)

    # Definir a ordem das colunas
    column_order = ["Name", "minLevel", "maxLevel", "Times", "LocationTypes", "Biome", "AntiBiome", "Rarity"]
    df = pd.DataFrame(rows)[column_order]
    df.sort_values(by="Name", inplace=True)
    df.to_csv(output_path, index=False, encoding='utf-8-sig')
    print(f"[✓] Tabela gerada com {len(df)} linhas em: {output_path}")

    # Gerar JSON
    json_data = {}

    for _, row in df.iterrows():
        name = str(row["Name"]).strip().lower()
        entry = {
            "minLevel": row["minLevel"],
            "maxLevel": row["maxLevel"],
            "Times": row["Times"],
            "LocationTypes": row["LocationTypes"],
            "Biome": row["Biome"],
            "AntiBiome": row["AntiBiome"],
            "Rarity": row["Rarity"]
        }

        if name not in json_data:
            json_data[name] = []

        json_data[name].append(entry)

    os.makedirs("log", exist_ok=True)
    json_output_path = os.path.join("log", "spawns.json")
    with open(json_output_path, "w", encoding="utf-8") as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)
    print(f"[✓] Arquivo JSON gerado com {len(json_data)} Pokémon em: {json_output_path}")
    
    return df
