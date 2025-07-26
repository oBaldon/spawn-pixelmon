import os
import json
from bs4 import BeautifulSoup

def forge_tags(html_path="data/worldgenbiome.html"):
    # Criar pasta de log se necessário
    log_dir = "log"
    os.makedirs(log_dir, exist_ok=True)
    json_output_path = os.path.join(log_dir, "biomes_tags.json")

    # Ler o HTML
    with open(html_path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")

    # Extrair dados
    biome_tags = {}
    for li in soup.find("ul").find_all("li", recursive=False):
        tag_code = li.find("code")
        if not tag_code:
            continue

        tag_name = f"#{tag_code.text}"
        sublist = li.find("ul")
        biomes = [code.text for code in sublist.find_all("code")] if sublist else []

        biome_tags[tag_name] = biomes

    # Salvar log
    with open(json_output_path, "w", encoding="utf-8") as f:
        json.dump(biome_tags, f, indent=4, ensure_ascii=False)

    return biome_tags
