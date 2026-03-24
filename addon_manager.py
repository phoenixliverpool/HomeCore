
import os
import json
from pathlib import Path

class AddonManager:
    def __init__(self, addons_dir="addons"):
        self.addons_dir = Path(addons_dir)
        self.installed_addons = {}
    
    def discover_available(self):
        """Find all available addons"""
        available = []
        for addon_path in self.addons_dir.iterdir():
            if addon_path.is_dir() and (addon_path / "manifest.json").exists():
                manifest = json.loads((addon_path / "manifest.json").read_text())
                available.append({
                    "id": addon_path.name,
                    "name": manifest.get("name", addon_path.name),
                    "description": manifest.get("description", ""),
                    "installed": addon_path.name in self.installed_addons
                })
        return available
    
    def install_addon(self, addon_id):
        """Install an addon by moving it to active"""
        addon_path = self.addons_dir / addon_id
        if addon_path.exists():
            self.installed_addons[addon_id] = {
                "path": addon_path,
                "enabled": True
            }
            return True
        return False
    
    def uninstall_addon(self, addon_id):
        """Uninstall an addon"""
        if addon_id in self.installed_addons:
            del self.installed_addons[addon_id]
            return True
        return False

# Pre-built addon manifests
PREBUILT_ADDONS = {
    "philips_hue": {
        "name": "Philips Hue",
        "description": "Control your Hue smart bulbs and bridges",
        "version": "1.0.0",
        "author": "HomeCore Team",
        "requirements": ["requests"],
        "config_flow": True
    },
    "sonoff": {
        "name": "Sonoff",
        "description": "Connect to Sonoff WiFi switches and sensors",
        "version": "1.0.0",
        "author": "HomeCore Team",
        "requirements": ["requests"],
        "config_flow": True
    },
    "mqtt": {
        "name": "MQTT Broker",
        "description": "Universal messaging for IoT devices",
        "version": "1.0.0",
        "author": "HomeCore Team",
        "requirements": ["paho-mqtt"],
        "config_flow": True
    },
    "zwave": {
        "name": "Z-Wave",
        "description": "Connect to Z-Wave mesh network devices",
        "version": "1.0.0",
        "author": "HomeCore Team",
        "requirements": ["python-openzwave"],
        "config_flow": True
    },
    "homebridge": {
        "name": "Homebridge",
        "description": "Bridge HomeKit accessories to HomeCore",
        "version": "1.0.0",
        "author": "HomeCore Team",
        "requirements": ["pyhap"],
        "config_flow": True
    }
}

def create_manifest_files(addons_dir="addons"):
    """Create manifest files for all pre-built addons"""
    addons_path = Path(addons_dir)
    addons_path.mkdir(exist_ok=True)
    for addon_id, manifest_data in PREBUILT_ADDONS.items():
        addon_path = addons_path / addon_id
        addon_path.mkdir(exist_ok=True)
        manifest_file = addon_path / "manifest.json"
        if not manifest_file.exists():  # Only create if doesn't exist
            with open(manifest_file, 'w') as f:
                json.dump(manifest_data, f, indent=2)

# Initialize the manager
addon_manager = AddonManager()

# Create initial manifests
create_manifest_files()