import pytest
from fastapi.testclient import TestClient
from main import app


@pytest.fixture
def client():
    """Create a test client for the FastAPI app"""
    return TestClient(app)


class TestMainRoutes:
    """Tests for main.py FastAPI routes"""

    def test_root_endpoint(self, client):
        """Test the root endpoint returns correct response"""
        response = client.get("/")
        
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "HomeCore Online"
        assert data["version"] == "0.1"

    def test_light_toggle_endpoint(self, client):
        """Test the light toggle endpoint"""
        response = client.get("/light/toggle")
        
        assert response.status_code == 200
        data = response.json()
        assert data["action"] == "toggled"
        assert data["device"] == "Living Room Light"

    def test_root_endpoint_method_not_allowed(self, client):
        """Test that root endpoint doesn't accept POST"""
        response = client.post("/")
        assert response.status_code == 405

    def test_light_toggle_method_not_allowed(self, client):
        """Test that light toggle doesn't accept POST"""
        response = client.post("/light/toggle")
        assert response.status_code == 405

    def test_nonexistent_route(self, client):
        """Test that nonexistent routes return 404"""
        response = client.get("/nonexistent")
        assert response.status_code == 404


class TestAppConfiguration:
    """Tests for FastAPI app configuration"""

    def test_app_title(self):
        """Test that the app has the correct title"""
        assert app.title == "HomeCore"
