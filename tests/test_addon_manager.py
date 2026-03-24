import pytest
import json
import tempfile
import shutil
from pathlib import Path
from addon_manager import AddonManager, PREBUILT_ADDONS, create_manifest_files


class TestAddonManager:
    """Tests for the AddonManager class"""

    @pytest.fixture
    def temp_addons_dir(self):
        """Create a temporary addons directory for testing"""
        temp_dir = tempfile.mkdtemp()
        yield Path(temp_dir)
        shutil.rmtree(temp_dir)

    @pytest.fixture
    def manager(self, temp_addons_dir):
        """Create an AddonManager instance with temporary directory"""
        return AddonManager(addons_dir=temp_addons_dir)

    def test_init(self, temp_addons_dir):
        """Test AddonManager initialization"""
        manager = AddonManager(addons_dir=temp_addons_dir)
        assert manager.addons_dir == temp_addons_dir
        assert manager.installed_addons == {}

    def test_discover_available_empty(self, manager):
        """Test discovering addons when directory is empty"""
        available = manager.discover_available()
        assert available == []

    def test_discover_available_with_addon(self, manager, temp_addons_dir):
        """Test discovering addons when addons exist"""
        # Create a test addon with manifest
        addon_path = temp_addons_dir / "test_addon"
        addon_path.mkdir()
        manifest = {
            "name": "Test Addon",
            "description": "A test addon",
            "version": "1.0.0"
        }
        (addon_path / "manifest.json").write_text(json.dumps(manifest))

        available = manager.discover_available()
        
        assert len(available) == 1
        assert available[0]["id"] == "test_addon"
        assert available[0]["name"] == "Test Addon"
        assert available[0]["description"] == "A test addon"
        assert available[0]["installed"] is False

    def test_discover_available_without_manifest(self, manager, temp_addons_dir):
        """Test that directories without manifest.json are ignored"""
        # Create a directory without manifest
        (temp_addons_dir / "no_manifest").mkdir()
        
        available = manager.discover_available()
        assert available == []

    def test_install_addon_success(self, manager, temp_addons_dir):
        """Test installing an addon successfully"""
        # Create a test addon
        addon_path = temp_addons_dir / "test_addon"
        addon_path.mkdir()
        (addon_path / "manifest.json").write_text(json.dumps({"name": "Test"}))

        result = manager.install_addon("test_addon")
        
        assert result is True
        assert "test_addon" in manager.installed_addons
        assert manager.installed_addons["test_addon"]["path"] == addon_path
        assert manager.installed_addons["test_addon"]["enabled"] is True

    def test_install_addon_not_exists(self, manager):
        """Test installing a non-existent addon"""
        result = manager.install_addon("nonexistent")
        assert result is False
        assert manager.installed_addons == {}

    def test_uninstall_addon_success(self, manager, temp_addons_dir):
        """Test uninstalling an addon"""
        # First install an addon
        addon_path = temp_addons_dir / "test_addon"
        addon_path.mkdir()
        (addon_path / "manifest.json").write_text(json.dumps({"name": "Test"}))
        manager.install_addon("test_addon")

        result = manager.uninstall_addon("test_addon")
        
        assert result is True
        assert "test_addon" not in manager.installed_addons

    def test_uninstall_addon_not_installed(self, manager):
        """Test uninstalling an addon that's not installed"""
        result = manager.uninstall_addon("nonexistent")
        assert result is False

    def test_discover_shows_installed_status(self, manager, temp_addons_dir):
        """Test that discover_available shows correct installed status"""
        # Create and install an addon
        addon_path = temp_addons_dir / "test_addon"
        addon_path.mkdir()
        (addon_path / "manifest.json").write_text(json.dumps({"name": "Test"}))
        manager.install_addon("test_addon")

        available = manager.discover_available()
        
        assert len(available) == 1
        assert available[0]["installed"] is True


class TestPrebuiltAddons:
    """Tests for PREBUILT_ADDONS configuration"""

    def test_prebuilt_addons_structure(self):
        """Test that PREBUILT_ADDONS has correct structure"""
        required_keys = {"name", "description", "version", "author", "requirements", "config_flow"}
        
        for addon_id, manifest in PREBUILT_ADDONS.items():
            for key in required_keys:
                assert key in manifest, f"Missing key '{key}' in addon '{addon_id}'"

    def test_prebuilt_addons_count(self):
        """Test that we have expected pre-built addons"""
        expected_addons = {"philips_hue", "sonoff", "mqtt", "zwave", "homebridge"}
        assert set(PREBUILT_ADDONS.keys()) == expected_addons

    def test_prebuilt_addon_versions(self):
        """Test that all addons have version strings"""
        for addon_id, manifest in PREBUILT_ADDONS.items():
            assert isinstance(manifest["version"], str)
            assert len(manifest["version"]) > 0

    def test_prebuilt_addon_requirements(self):
        """Test that requirements are lists"""
        for addon_id, manifest in PREBUILT_ADDONS.items():
            assert isinstance(manifest["requirements"], list)


class TestCreateManifestFiles:
    """Tests for create_manifest_files function"""

    @pytest.fixture
    def temp_addons_dir(self):
        """Create a temporary addons directory"""
        temp_dir = tempfile.mkdtemp()
        yield Path(temp_dir)
        shutil.rmtree(temp_dir)

    def test_create_manifest_files(self, temp_addons_dir):
        """Test that manifest files are created"""
        # Run the function with temp directory
        create_manifest_files(addons_dir=temp_addons_dir)

        # Check that manifest files were created
        for addon_id in PREBUILT_ADDONS.keys():
            manifest_path = temp_addons_dir / addon_id / "manifest.json"
            assert manifest_path.exists(), f"Manifest not created for {addon_id}"
            
            # Verify manifest content
            manifest = json.loads(manifest_path.read_text())
            assert manifest["name"] == PREBUILT_ADDONS[addon_id]["name"]

    def test_create_manifest_files_doesnt_overwrite(self, temp_addons_dir):
        """Test that existing manifests are not overwritten"""
        # Create a custom manifest first
        custom_addon_path = temp_addons_dir / "philips_hue"
        custom_addon_path.mkdir(parents=True)
        custom_manifest = {"name": "Custom Name", "custom": True}
        (custom_addon_path / "manifest.json").write_text(json.dumps(custom_manifest))

        # Run the function
        create_manifest_files(addons_dir=temp_addons_dir)

        # Verify custom manifest is preserved
        manifest = json.loads((custom_addon_path / "manifest.json").read_text())
        assert manifest["name"] == "Custom Name"
        assert manifest["custom"] is True
