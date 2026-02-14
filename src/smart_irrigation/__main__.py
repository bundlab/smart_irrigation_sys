import argparse
import logging
from smart_irrigation.core import IrrigationSystem
from smart_irrigation.config import load_config


def main():
    parser = argparse.ArgumentParser(description="Smart Irrigation System CLI")
    parser.add_argument(
        "--dry-run", action="store_true", help="Simulate without actual irrigation"
    )
    parser.add_argument(
        "--days", type=int, default=7, help="Number of days to simulate"
    )
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )

    config = load_config()
    system = IrrigationSystem(
        soil_moisture_threshold=config["thresholds"]["soil_moisture"],
        rain_probability_threshold=config["thresholds"]["rain_probability"],
    )

    for day in range(1, args.days + 1):
        logging.info(f"Day {day:02d}")
        system.check_and_irrigate(dry_run=args.dry_run)


if __name__ == "__main__":
    main()
