"""
Tests for Github blessed connector.
"""

from airbyte_ai_github import GithubConnector


def test_connector_creation():
    """Test creating GithubConnector instance."""
    connector = GithubConnector.create(secrets={"api_key": "test_key"})
    assert connector.connector_name == "github"
    assert connector.connector_version


def test_connector_metadata():
    """Test connector metadata."""
    assert GithubConnector.connector_name == "github"
    assert hasattr(GithubConnector, "connector_version")


def test_default_config_path():
    """Test default config path exists."""
    config_path = GithubConnector.get_default_config_path()
    assert config_path.exists()
    assert config_path.name == "connector.yaml"
