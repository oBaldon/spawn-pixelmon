
# 🧬 Pixelmon Spawn Parser

A powerful tool to parse, expand, and visualize Pokémon spawn data from Pixelmon JSON configurations. Designed to help developers, server owners, and modders understand spawn rules by biome, time, rarity, and other conditions.

## 📦 Features

- ✅ Parses all spawn `.json` files from Pixelmon.
- 🔍 Expands biome tags recursively using custom `final_tag_map`.
- 🗺 Merges Forge biome tags and Minecraft vanilla biome groups.
- 📊 Generates a clean CSV table with spawn data.
- 🧠 Handles edge cases like `anticondition`, `stringBiomes`, and time-based spawns.
- 💾 Outputs a unified JSON and CSV file for easy use and inspection.

## 📂 Project Structure

```
spawn-pixelmon/
├── data/
│   ├── biomes/             # Pixelmon biome tag files
│   ├── mcbiomes/           # Vanilla/Minecraft biome group definitions
│   └── spawning/           # Raw Pokémon spawn files
├── log/                    # Intermediate outputs (tag maps, expansions, etc.)
├── parser/                 # All parsing and data processing modules
├── worldgenbiome.html      # HTML from Forge containing tag mappings
├── main.py                 # Entry point for the full pipeline
└── pokemon_spawn_table.csv # Final output table
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/oBaldon/spawn-pixelmon.git
cd spawn-pixelmon
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
```

### 3. Install dependencies

Make sure to extract the `data.zip` file into the project root so the `data/` folder is created properly.
```bash
pip install -r requirements.txt
unzip data.zip -d .
```

### 4. Run the parser

```bash
python main.py
```

Output files will be saved as:

- 🧾 `log/final_tag_map.json` → Expanded biome mapping
- 🧬 `log/final_data.json` → Pokémon spawns with resolved biomes
- 📊 `pokemon_spawn_table.csv` → Table of all spawn rules

## 🛠 Technologies Used

- Python 3.10+
- BeautifulSoup (HTML parsing)
- Pandas (data manipulation and CSV export)
- JSON handling and recursive tag processing

## 📘 Example Use Case

Want to know where **Larvitar** spawns and under what conditions?

Run the tool and search for "Larvitar" in the generated `pokemon_spawn_table.csv` — it will show:
- Min/Max level
- Time of day
- Biomes
- Anti-biomes
- Spawn rarity

## 🤝 Contributing

Pull requests are welcome! If you'd like to improve biome handling, tag expansions, or performance, feel free to open an issue or PR.

### Suggested Improvements

Here are a few ideas to help improve the project:

- 📦 **Refactor File and Class Names**: Ensure file and class names follow consistent naming conventions and better reflect their responsibilities (e.g., rename `final_tags.py` to something more descriptive like `tag_merger.py`).
- 🧪 **Add Tests**: Implement automated tests for core functions such as tag expansion, biome parsing, and spawn merging to ensure correctness.
- 📝 **Log Review**: Improve or expand logging to help debug biome mismatches and verify that the final spawn table is complete and accurate.
- 📊 **Validate Final Table Output**: Add validation logic to check for missing or duplicated Pokémon entries in the final spawn table.
- 📁 **Folder Structure**: Consider organizing the `parser` folder into submodules (e.g., `loaders/`, `transformers/`, `exporters/`) for better modularity.

Feel free to suggest additional features, improvements, or bug fixes via Issues or PRs.

## 📄 License

MIT License © 2025 Douglas Baldon

---

Made with ❤️ for the Pixelmon community.