from parser.generate_spawn_table import generate_spawn_table
from parser.biome_loader import load_biome_tags
from parser.final_tags import final_biome_tags
from parser.pokemon_parser import parse_pokemon_spawns
from parser.tag_expander import expand_biome_tags
from parser.forge_tags import forge_tags
from parser.minecraft_biome_loader import load_minecraft_biome_tags
from parser.pokemon_biome_expander import expand_pokemon_spawns

# Caminhos
spawn_path = "data/spawning"
biome_path = "data/biomes"
mcbiomes_path = "data/mcbiomes"
forge_path = "data/worldgenbiome.html"

# Carregar dados
pokemon_data = parse_pokemon_spawns(spawn_path)
mcbiome_data = load_minecraft_biome_tags(mcbiomes_path)
forge_data = forge_tags(forge_path)

# Processar tags
tag_map = load_biome_tags(biome_path)
expanded_tag_map = expand_biome_tags(tag_map, forge_data)
final_tag_map = final_biome_tags(expanded_tag_map, mcbiome_data)

# Substituir Tags
final_data = expand_pokemon_spawns(spawn_path, final_tag_map)

# Gerar tabela de spawn
st = generate_spawn_table(final_data, output_path="pokemon_spawn_table.csv")
