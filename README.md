# HomeCore

## Project Overview

HomeCore is a modular smart home automation hub built with Python. It provides a unified platform for managing IoT devices and integrations through a plugin-based addon system.

**Core Components:**
- **FastAPI Backend** (`main.py`): REST API server running on `localhost:8000`
- **Streamlit Dashboard** (`Dashboard.py`): Web-based UI for device control and addon management
- **Addon System** (`addon_manager.py`): Plugin architecture for extending functionality with smart home integrations

**Supported Integrations (Pre-built Addons):**
- Philips Hue - Smart lighting control
- Sonoff - WiFi switches and sensors
- MQTT Broker - Universal IoT messaging
- Z-Wave - Mesh network devices
- Homebridge - HomeKit compatibility

**Architecture:**
```
HomeCore/
├── main.py           # FastAPI REST API
├── Dashboard.py      # Streamlit UI
├── addon_manager.py  # Plugin management system
├── addons/           # Addon modules with manifest.json
└── tests/            # Pytest test suite
```

## Building and Running

### Prerequisites
- Python 3.10+
- Virtual environment recommended (`venv/`)

### Installation
```bash
pip install -r requirements.txt
```

### Running the FastAPI Server
```bash
python main.py
# or
uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```

### Running the Streamlit Dashboard
```bash
streamlit run Dashboard.py
```

### Running Tests
```bash
pytest
# or with verbose output
pytest -v
```

## Development Conventions

### Code Style
- Python with type hints where applicable
- Classes use docstrings for public methods
- Test files follow `test_*.py` naming convention

### Testing Practices
- Uses `pytest` with fixtures for setup/teardown
- Test classes group related tests (e.g., `TestAddonManager`, `TestMainRoutes`)
- Temporary directories used for filesystem tests
- Test coverage includes success, failure, and edge cases

### Addon Development
Addons are directories under `addons/` containing a `manifest.json`:
```json
{
  "name": "Addon Name",
  "description": "Description",
  "version": "1.0.0",
  "author": "Author",
  "requirements": ["dependency1", "dependency2"],
  "config_flow": true
}
```

### Project Philosophy
> "My hub. My rules." - Local-first, user-controlled smart home automation.
