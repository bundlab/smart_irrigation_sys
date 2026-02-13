# Smart Irrigation System 🌱💧

**A modular, extensible smart irrigation controller in Python**  
Decides intelligently when to water plants by combining **soil moisture levels** with **rain probability forecasts** — ideal for Raspberry Pi, ESP32, simulators, or any IoT setup.

[![Python](https://img.shields.io/badge/python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tests](https://github.com/yourusername/smart_irrigation_sys/actions/workflows/ci.yml/badge.svg)](https://github.com/yourusername/smart_irrigation_sys/actions)
<!-- Add more badges later: code coverage, PyPI version, etc. -->

## ✨ Features
- Configurable moisture & rain probability thresholds
- Simulated sensors (easy to replace with real hardware like capacitive soil sensors, DHT22, etc.)
- Dry-run / simulation mode (no hardware needed for development & testing)
- Structured logging + basic CLI interface
- Clean architecture ready for extensions:
  - Real weather APIs (OpenWeatherMap, WeatherAPI, etc.)
  - MQTT publishing/subscribing
  - GPIO control (RPi.GPIO, adafruit libraries)
  - Database storage (SQLite, InfluxDB)
  - Web dashboard (future)

## 📋 Table of Contents
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Usage Examples](#-usage-examples)
- [Configuration](#-configuration)
- [Testing](#-testing)
- [Contributing](#-contributing)
- [License](#-license)


## Project Structure
smart_irrigation_sys/                  	  # ← Root folder (repository name)
├── src/                                  # ← All source code goes here (avoids import issues)
│   └── smart_irrigation/                 # ← Actual Python package (importable name)
│       ├── __init__.py
│       ├── __main__.py                   # ← Entry point when running `python -m smart_irrigation`
│       ├── core.py                       # ← Main business logic (IrrigationSystem class)
│       ├── sensors.py                    # ← Sensor simulation / real hardware interfaces
│       ├── weather.py                    # ← Weather API integration (future)
│       ├── config.py                     # ← Configuration loading (thresholds, etc.)
│       └── utils.py                      # ← Helpers (logging setup, etc.)
├── tests/                                # ← Unit & integration tests
│   ├── __init__.py
│   ├── test_core.py
│   └── test_sensors.py
├── .github/                              # ← GitHub Actions (CI/CD)
│   └── workflows/
│       └── ci.yml                        # ← Basic tests + linting on push/PR
├── docs/                                 # ← Documentation (Sphinx or MkDocs later)
├── examples/                             # ← Example usage scripts
├── data/                                 # ← Sample data, configs, or logs (optional)
├── .gitignore
├── LICENSE
├── README.md
├── pyproject.toml                        # ← Modern configuration (replaces setup.py)
├── requirements.txt                      # ← For simple installs (optional)
└── requirements-dev.txt                  # ← Development tools (black, pytest, etc.)


## 🛠 Prerequisites
- Python 3.8+
- Git
- (Optional) Virtual environment tool: `venv`, `uv`, `poetry`, etc.


## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/smart_irrigation_sys.git
   cd smart_irrigation_sys

## ⚡ Quick Start
Run the simulation
   python -m smart_irrigation
   
[INFO] Soil moisture: 42%  |  Rain probability: 15%
[INFO] Decision: NO irrigation needed



## ▶️ Usage Examples
1. Simulate custom conditions
python -m smart_irrigation --simulate --moisture=25 --rain-prob=60

2. Run once (good for scheduled tasks)
python -m smart_irrigation --once

3. Verbose mode
python -m smart_irrigation --verbose


## ⚙️ Configuration
cp src/smart_irrigation/config.example.yaml config.yaml
Example config.yml
thresholds:
  moisture_critical: 30    # below → must water
  moisture_warning:  45
  rain_skip_probability: 40  # above → skip


## 🧪 Testing
pytest                  # run tests
pytest --cov            # with coverage
black .                 # format
ruff check --fix        # lint & fix


## 🤝 Contributing
- Fork the repo
- Create your branch (git checkout -b feature/cool-feature)
- Commit (git commit -m 'Add cool feature')
- Push (git push origin feature/cool-feature)
- Open a Pull Request
Follow black formatting & add tests where possible.


## 📄 License
- MIT License — see LICENSE for details.