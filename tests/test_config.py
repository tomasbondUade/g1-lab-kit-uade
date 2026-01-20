"""
Tests para src/config/loader.py
"""
import pytest
from pathlib import Path
import sys

# Agregar src al path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from config.loader import Config, load_config, validate_config


class TestConfig:
    """Tests para clase Config"""
    
    def test_config_creation(self, sample_config):
        """Test crear Config desde archivo"""
        config = Config(sample_config)
        
        assert config.robot_type == "g1"
        assert config.robot_ip == "192.168.123.161"
        assert config.sdk_timeout == 5
        assert config.sdk_reconnect == True
    
    def test_config_invalid_file(self):
        """Test Config con archivo inexistente"""
        with pytest.raises(FileNotFoundError):
            Config("archivo_inexistente.yaml")
    
    def test_config_get_value(self, sample_config):
        """Test obtener valores anidados"""
        config = Config(sample_config)
        
        assert config.get("robot.type") == "g1"
        assert config.get("sdk.timeout") == 5
        assert config.get("telemetry.log_interval") == 0.1
    
    def test_config_get_default(self, sample_config):
        """Test get con valor default"""
        config = Config(sample_config)
        
        assert config.get("no.existe", "default") == "default"
    
    def test_config_to_dict(self, sample_config):
        """Test convertir Config a dict"""
        config = Config(sample_config)
        data = config.to_dict()
        
        assert isinstance(data, dict)
        assert "robot" in data
        assert data["robot"]["type"] == "g1"


class TestLoadConfig:
    """Tests para función load_config"""
    
    def test_load_config_success(self, sample_config):
        """Test cargar config exitosamente"""
        config = load_config(sample_config)
        
        assert config is not None
        assert config.robot_type == "g1"
    
    def test_load_config_from_string(self, sample_config):
        """Test cargar config desde string path"""
        config = load_config(str(sample_config))
        
        assert config is not None
        assert config.robot_type == "g1"
    
    def test_load_config_invalid(self):
        """Test cargar config inválido"""
        with pytest.raises(FileNotFoundError):
            load_config("no_existe.yaml")


class TestValidateConfig:
    """Tests para función validate_config"""
    
    def test_validate_valid_config(self, sample_config):
        """Test validar config válido"""
        config = load_config(sample_config)
        is_valid, errors = validate_config(config)
        
        assert is_valid == True
        assert len(errors) == 0
    
    def test_validate_missing_robot_type(self, temp_dir):
        """Test validar config sin robot.type"""
        invalid_config = temp_dir / "invalid.yaml"
        invalid_config.write_text("sdk:\n  timeout: 5\n", encoding='utf-8')
        
        config = load_config(invalid_config)
        is_valid, errors = validate_config(config)
        
        assert is_valid == False
        assert any("robot.type" in error for error in errors)
    
    def test_validate_invalid_robot_type(self, temp_dir):
        """Test validar config con robot.type inválido"""
        invalid_config = temp_dir / "invalid.yaml"
        invalid_config.write_text("robot:\n  type: 'invalid_robot'\n", encoding='utf-8')
        
        config = load_config(invalid_config)
        is_valid, errors = validate_config(config)
        
        assert is_valid == False
        assert any("robot type" in error.lower() for error in errors)


class TestConfigEdgeCases:
    """Tests de casos edge"""
    
    def test_config_empty_file(self, temp_dir):
        """Test config con archivo vacío"""
        empty_file = temp_dir / "empty.yaml"
        empty_file.write_text("", encoding='utf-8')
        
        with pytest.raises(Exception):  # Puede ser ValueError o similar
            load_config(empty_file)
    
    def test_config_malformed_yaml(self, temp_dir):
        """Test config con YAML malformado"""
        bad_yaml = temp_dir / "bad.yaml"
        bad_yaml.write_text("robot:\n  type: g1\n    invalid indent", encoding='utf-8')
        
        with pytest.raises(Exception):
            load_config(bad_yaml)
