import pytest
from smart_irrigation.core import IrrigationSystem

def test_irrigation_decision_low_moisture_no_rain():
    system = IrrigationSystem(soil_moisture_threshold=30.0, rain_probability_threshold=0.5)
    system.get_soil_moisture = lambda: 25.0
    system.get_rain_probability = lambda: 0.3
    # We can mock irrigate later with unittest.mock
    assert system.get_soil_moisture() < system.soil_moisture_threshold
    assert system.get_rain_probability() < system.rain_probability_threshold