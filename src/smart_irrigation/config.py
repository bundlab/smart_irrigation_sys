from pathlib import Path
import json

DEFAULT_CONFIG = {
    "thresholds": {
        "soil_moisture": 30.0,
        "rain_probability": 0.5
    }
}

def load_config() -> dict:
    config_path = Path.home() / ".smart_irrigation" / "config.json"
    if config_path.exists():
        with config_path.open() as f:
            return json.load(f)
    return DEFAULT_CONFIG