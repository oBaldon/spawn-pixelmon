import os
import json

def expand_recursively(value, mcbiome_data, seen):
    """Expande recursivamente uma tag do Minecraft"""
    if value in seen:
        return []

    if isinstance(value, str) and value.startswith("#") and value in mcbiome_data:
        seen.add(value)
        result = []
        for subvalue in mcbiome_data[value]:
            result.extend(expand_recursively(subvalue, mcbiome_data, seen))
        return result
    else:
        return [value]

def final_biome_tags(expanded_tag_map, mcbiome_data):
    """
    Expande todas as tags restantes (#minecraft:...) recursivamente
    """
    final_map = {}

    for tag, values in expanded_tag_map.items():
        final_values = []
        seen_values = set()

        for value in values:
            expanded = expand_recursively(value, mcbiome_data, seen=set())
            for val in expanded:
                if val not in seen_values:
                    final_values.append(val)
                    seen_values.add(val)

        final_map[tag] = final_values

    # Log
    os.makedirs("log", exist_ok=True)
    log_path = os.path.join("log", "final_tag_map.json")
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump(final_map, f, indent=2, ensure_ascii=False)

    return final_map
