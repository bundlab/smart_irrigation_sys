import logging
import random


class IrrigationSystem:
    def __init__(
        self,
        soil_moisture_threshold: float = 30.0,
        rain_probability_threshold: float = 0.5,
    ):
        self.soil_moisture_threshold = soil_moisture_threshold
        self.rain_probability_threshold = rain_probability_threshold
        self.logger = logging.getLogger(__name__)

    def get_soil_moisture(self) -> float:
        """Simulate or read real soil moisture (0-100%)"""
        return random.uniform(0, 100)  # Replace with real sensor later

    def get_rain_probability(self) -> float:
        """Simulate or fetch real rain probability (0.0-1.0)"""
        return random.uniform(0, 1)  # Replace with OpenWeatherMap API later

    def irrigate(self, dry_run: bool = False):
        if dry_run:
            self.logger.info("[DRY RUN] Would irrigate now...")
        else:
            self.logger.info("Starting irrigation... 🌧️💧")
            # TODO: Add real pump/valve control (RPi.GPIO, relay, etc.)
            self.logger.info("Irrigation completed ✅")

    def check_and_irrigate(self, dry_run: bool = False):
        moisture = self.get_soil_moisture()
        rain_prob = self.get_rain_probability()

        self.logger.info(f"Soil moisture: {moisture:.1f}% | Rain prob: {rain_prob:.1%}")

        if (
            moisture < self.soil_moisture_threshold
            and rain_prob < self.rain_probability_threshold
        ):
            self.irrigate(dry_run=dry_run)
        else:
            self.logger.info("No irrigation needed today 🌱")
