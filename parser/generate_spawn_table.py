import os
import pandas as pd

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
    return df
