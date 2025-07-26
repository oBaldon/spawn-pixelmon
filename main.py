from parser.biome_loader import load_biome_tags
from parser.pokemon_parser import parse_pokemon_spawns
from parser.tag_expander import expand_biome_tags
from parser.forge_tags import forge_tags

# Caminhos
spawn_path = "data/spawning"
biome_path = "data/biomes"

# Carregar dados
tag_map = load_biome_tags(biome_path)
pokemon_data = parse_pokemon_spawns(spawn_path)

forge = forge_tags()
tag_map = expand_biome_tags(tag_map, forge)
