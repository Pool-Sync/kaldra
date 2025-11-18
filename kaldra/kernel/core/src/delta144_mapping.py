import json
from pathlib import Path

# --- Constants and Data Loading ---
DATA_PATH = Path(__file__).parent.parent / "data" / "archetypes"
DELTA144_GRID_PATH = DATA_PATH / "delta144_grid.json"

def _load_delta144_grid():
    """
    Loads the delta144 grid and creates a lookup map for efficient access.
    The map keys are the Jungian archetype names (e.g., "Inocente").
    """
    with open(DELTA144_GRID_PATH, "r", encoding="utf-8") as f:
        grid_data = json.load(f)

    # Create a dictionary for O(1) average time complexity lookups
    return {item["jung"]: item for item in grid_data}

DELTA144_MAP = _load_delta144_grid()

# --- Main Function ---

def map_to_delta144(archetype_name: str) -> dict:
    """
    Maps a dominant archetype name to its corresponding entry in the Δ144 grid.

    This function looks up the archetype name in the pre-loaded Δ144 data.
    If a match is found, it returns the complete data object for that entry.
    If not found, it returns a default dictionary with a "desconhecido" stage.

    Args:
        archetype_name: The name of the Jungian archetype to look up.

    Returns:
        A dictionary containing the Δ144 grid information for the archetype.
    """
    # Find the corresponding entry in the map
    result = DELTA144_MAP.get(archetype_name)

    if result:
        return result

    # If the archetype name is not found, return a default fallback structure
    return {
        "id": None,
        "jung": archetype_name,
        "hero_stage": "desconhecido",
        "description": ""
    }
