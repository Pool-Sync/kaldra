import json
from pathlib import Path

# --- Constants ---
# Construct the path to the data directory relative to this file.
# This makes the path resolution robust to where the script is run from.
DATA_PATH = Path(__file__).parent.parent / "data" / "archetypes"
LOCALES_MAP_PATH = DATA_PATH / "locales_map.json"
CULTURAL_3X48_PATH = DATA_PATH / "cultural_3x48.json"

# --- Data Loading ---

def _load_json_data():
    """
    Loads the necessary JSON files for cultural modulation.
    """
    with open(LOCALES_MAP_PATH, "r", encoding="utf-8") as f:
        locales_map = json.load(f)

    with open(CULTURAL_3X48_PATH, "r", encoding="utf-8") as f:
        cultural_weights = json.load(f)

    return locales_map, cultural_weights

# Load the data once when the module is imported
LOCALES_MAP, CULTURAL_WEIGHTS = _load_json_data()

# --- Main Function ---

def apply_kindra(delta12: list[float], locale: str) -> tuple[list[float], int]:
    """
    Applies cultural modulation to a 12-dimensional archetypal vector.

    This v0.1 implementation is a placeholder. It identifies the correct
    cultural "plan" based on the locale but does not yet apply any actual
    weighting. The `cultural_3x48.json` is loaded but not used.

    Args:
        delta12: The 12-dimensional archetypal vector.
        locale: The locale string (e.g., "pt-BR", "en") to determine the
                cultural plan. Defaults to "en" if not found.

    Returns:
        A tuple containing:
        - The modulated 12-dimensional vector (currently unmodified).
        - The integer of the cultural plan used (e.g., 3, 6, 9).
    """
    # 1. Determine the cultural plan from the locale
    # Default to 'en' if the locale is not found in the map
    culture_info = LOCALES_MAP.get(locale, LOCALES_MAP.get("en", {"plan": 3}))
    plan = culture_info["plan"]

    # 2. Select the corresponding weights (currently placeholder)
    # The key in cultural_weights is, e.g., "plan_3"
    # plan_weights = CULTURAL_WEIGHTS.get(f"plan_{plan}", [])

    # 3. Apply the modulation (v0.1 - no-op)
    # In the future, this section will multiply delta12 by the plan_weights.
    modulated_delta12 = delta12  # No modification in this version

    # 4. Return the modulated vector and the plan number
    return modulated_delta12, plan
