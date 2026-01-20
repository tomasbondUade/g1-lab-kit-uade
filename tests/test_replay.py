"""
Tests para src/replay/loader.py
"""
import pytest
from pathlib import Path
import sys
import json

# Agregar src al path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from replay.loader import Session, load_session, list_sessions


class TestSession:
    """Tests para clase Session"""
    
    def test_session_creation(self, sample_session):
        """Test crear Session desde directorio"""
        session = Session(sample_session)
        
        assert session.name == sample_session.name
        assert session.path == sample_session
        assert session.metadata is not None
    
    def test_session_get_metadata(self, sample_session):
        """Test obtener metadata"""
        session = Session(sample_session)
        metadata = session.get_metadata()
        
        assert metadata["robot_type"] == "g1"
        assert "session_name" in metadata
        assert "start_time" in metadata
    
    def test_session_get_telemetry(self, sample_session):
        """Test obtener telemetría como DataFrame"""
        session = Session(sample_session)
        df = session.get_telemetry()
        
        assert df is not None
        assert len(df) > 0
        assert "timestamp" in df.columns
    
    def test_session_get_commands(self, sample_session):
        """Test obtener comandos"""
        session = Session(sample_session)
        commands = session.get_commands()
        
        assert isinstance(commands, list)
        assert len(commands) > 0
    
    def test_session_duration(self, sample_session):
        """Test obtener duración"""
        session = Session(sample_session)
        duration = session.duration()
        
        assert duration == 2700  # 45 minutos
    
    def test_session_invalid_path(self):
        """Test Session con path inválido"""
        with pytest.raises((FileNotFoundError, ValueError)):
            Session(Path("path_inexistente"))


class TestLoadSession:
    """Tests para función load_session"""
    
    def test_load_session_success(self, sample_session):
        """Test cargar sesión exitosamente"""
        session = load_session(sample_session)
        
        assert session is not None
        assert session.name == sample_session.name
    
    def test_load_session_from_string(self, sample_session):
        """Test cargar sesión desde string path"""
        session = load_session(str(sample_session))
        
        assert session is not None
    
    def test_load_session_invalid(self):
        """Test cargar sesión inválida"""
        with pytest.raises((FileNotFoundError, ValueError)):
            load_session("path_inexistente")
    
    def test_load_session_missing_metadata(self, temp_dir):
        """Test cargar sesión sin metadata.json"""
        session_dir = temp_dir / "incomplete_session"
        session_dir.mkdir()
        
        with pytest.raises((FileNotFoundError, ValueError)):
            load_session(session_dir)


class TestListSessions:
    """Tests para función list_sessions"""
    
    def test_list_sessions_single(self, sample_session):
        """Test listar sesiones con una sesión"""
        data_dir = sample_session.parent.parent.parent
        sessions = list_sessions(data_dir)
        
        assert isinstance(sessions, list)
        assert len(sessions) >= 1
    
    def test_list_sessions_multiple(self, temp_dir, sample_metadata):
        """Test listar múltiples sesiones"""
        sessions_dir = temp_dir / "data" / "local" / "sessions"
        sessions_dir.mkdir(parents=True)
        
        # Crear 3 sesiones
        for i in range(3):
            session_dir = sessions_dir / f"20260120_14{30+i}_G1_ROBOTICA_G{i+1}"
            session_dir.mkdir()
            
            metadata = sample_metadata.copy()
            metadata["session_name"] = session_dir.name
            
            metadata_file = session_dir / "metadata.json"
            metadata_file.write_text(json.dumps(metadata), encoding='utf-8')
        
        sessions = list_sessions(temp_dir)
        assert len(sessions) >= 3
    
    def test_list_sessions_empty_dir(self, temp_dir):
        """Test listar sesiones en directorio vacío"""
        sessions = list_sessions(temp_dir)
        
        assert isinstance(sessions, list)
        assert len(sessions) == 0
    
    def test_list_sessions_filter_robot(self, temp_dir, sample_metadata):
        """Test listar sesiones filtradas por robot"""
        sessions_dir = temp_dir / "data" / "local" / "sessions"
        sessions_dir.mkdir(parents=True)
        
        # Crear sesiones G1 y GO2
        for robot in ["G1", "GO2"]:
            session_dir = sessions_dir / f"20260120_1430_{robot}_ROBOTICA_G1"
            session_dir.mkdir()
            
            metadata = sample_metadata.copy()
            metadata["robot_type"] = robot.lower()
            metadata["session_name"] = session_dir.name
            
            metadata_file = session_dir / "metadata.json"
            metadata_file.write_text(json.dumps(metadata), encoding='utf-8')
        
        # Listar solo G1
        sessions_g1 = list_sessions(temp_dir, robot_type="g1")
        assert len(sessions_g1) >= 1
        assert all(s.metadata["robot_type"] == "g1" for s in sessions_g1)


class TestSessionEdgeCases:
    """Tests de casos edge"""
    
    def test_session_empty_telemetry(self, temp_dir, sample_metadata):
        """Test sesión con telemetry.csv vacío"""
        session_dir = temp_dir / "empty_telemetry"
        session_dir.mkdir()
        
        metadata_file = session_dir / "metadata.json"
        metadata_file.write_text(json.dumps(sample_metadata), encoding='utf-8')
        
        telemetry_file = session_dir / "telemetry.csv"
        telemetry_file.write_text("", encoding='utf-8')
        
        session = Session(session_dir)
        df = session.get_telemetry()
        
        # Puede ser None o DataFrame vacío
        assert df is None or len(df) == 0
    
    def test_session_malformed_json(self, temp_dir):
        """Test sesión con metadata.json malformado"""
        session_dir = temp_dir / "bad_json"
        session_dir.mkdir()
        
        metadata_file = session_dir / "metadata.json"
        metadata_file.write_text("{invalid json", encoding='utf-8')
        
        with pytest.raises(Exception):
            Session(session_dir)
