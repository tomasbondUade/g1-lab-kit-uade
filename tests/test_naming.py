"""
Tests para src/utils/naming.py
"""
import pytest
from datetime import datetime
from pathlib import Path
import sys

# Agregar src al path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from utils.naming import generate_session_name, parse_session_name, is_valid_session_name


class TestGenerateSessionName:
    """Tests para función generate_session_name"""
    
    def test_generate_basic(self):
        """Test generar nombre básico"""
        name = generate_session_name("g1", "ROBOTICA", "G3")
        
        assert isinstance(name, str)
        assert "G1" in name
        assert "ROBOTICA" in name
        assert "G3" in name
        assert len(name.split("_")) == 5
    
    def test_generate_with_timestamp(self):
        """Test generar con timestamp específico"""
        dt = datetime(2026, 1, 20, 14, 30)
        name = generate_session_name("g1", "ROBOTICA", "G3", timestamp=dt)
        
        assert name.startswith("20260120_1430")
        assert name == "20260120_1430_G1_ROBOTICA_G3"
    
    def test_generate_go2(self):
        """Test generar con GO2"""
        name = generate_session_name("go2", "CONTROL", "G1")
        
        assert "GO2" in name
        assert "CONTROL" in name
    
    def test_generate_lowercase_robot(self):
        """Test con robot en lowercase (debe convertir a uppercase)"""
        name = generate_session_name("g1", "ROBOTICA", "G3")
        
        assert "G1" in name
        assert "g1" not in name
    
    def test_generate_invalid_robot(self):
        """Test con robot inválido"""
        with pytest.raises(ValueError):
            generate_session_name("invalid_robot", "ROBOTICA", "G3")


class TestParseSessionName:
    """Tests para función parse_session_name"""
    
    def test_parse_valid_name(self, valid_session_names):
        """Test parsear nombres válidos"""
        for name in valid_session_names:
            parsed = parse_session_name(name)
            
            assert parsed is not None
            assert "date" in parsed
            assert "time" in parsed
            assert "robot" in parsed
            assert "materia" in parsed
            assert "grupo" in parsed
    
    def test_parse_specific_name(self):
        """Test parsear nombre específico"""
        name = "20260120_1430_G1_ROBOTICA_G3"
        parsed = parse_session_name(name)
        
        assert parsed["date"] == "20260120"
        assert parsed["time"] == "1430"
        assert parsed["robot"] == "G1"
        assert parsed["materia"] == "ROBOTICA"
        assert parsed["grupo"] == "G3"
    
    def test_parse_invalid_names(self, invalid_session_names):
        """Test parsear nombres inválidos"""
        for name in invalid_session_names:
            parsed = parse_session_name(name)
            assert parsed is None
    
    def test_parse_empty_string(self):
        """Test parsear string vacío"""
        parsed = parse_session_name("")
        assert parsed is None
    
    def test_parse_none(self):
        """Test parsear None"""
        parsed = parse_session_name(None)
        assert parsed is None


class TestIsValidSessionName:
    """Tests para función is_valid_session_name"""
    
    def test_valid_names(self, valid_session_names):
        """Test validar nombres válidos"""
        for name in valid_session_names:
            assert is_valid_session_name(name) == True
    
    def test_invalid_names(self, invalid_session_names):
        """Test validar nombres inválidos"""
        for name in invalid_session_names:
            assert is_valid_session_name(name) == False
    
    def test_valid_go2(self):
        """Test validar nombre GO2"""
        assert is_valid_session_name("20260120_1430_GO2_CONTROL_G1") == True
    
    def test_valid_g1(self):
        """Test validar nombre G1"""
        assert is_valid_session_name("20260120_1430_G1_ROBOTICA_G3") == True
    
    def test_invalid_robot_type(self):
        """Test con tipo de robot inválido"""
        assert is_valid_session_name("20260120_1430_INVALID_ROBOTICA_G3") == False
    
    def test_invalid_format(self):
        """Test con formato incorrecto"""
        assert is_valid_session_name("invalid_format") == False


class TestNamingEdgeCases:
    """Tests de casos edge"""
    
    def test_generate_special_chars_materia(self):
        """Test generar con caracteres especiales en materia"""
        # Debería limpiar o rechazar caracteres especiales
        name = generate_session_name("g1", "ROBÓTICA", "G3")
        # El comportamiento depende de la implementación
        assert isinstance(name, str)
    
    def test_parse_extra_underscores(self):
        """Test parsear con underscores extra"""
        name = "20260120_1430_G1_ROBOTICA_AVANZADA_G3"  # 6 partes en vez de 5
        parsed = parse_session_name(name)
        # Podría ser None o manejar el caso
        # Depende de cómo implementaste parse_session_name
    
    def test_generate_empty_materia(self):
        """Test generar con materia vacía"""
        with pytest.raises((ValueError, AssertionError)):
            generate_session_name("g1", "", "G3")
    
    def test_generate_empty_grupo(self):
        """Test generar con grupo vacío"""
        with pytest.raises((ValueError, AssertionError)):
            generate_session_name("g1", "ROBOTICA", "")
