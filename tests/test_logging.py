"""
Tests para src/logging/session.py
"""
import pytest
from pathlib import Path
import sys
import json
import time

# Agregar src al path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from src.logging.session import SessionLogger


class TestSessionLogger:
    """Tests para clase SessionLogger"""
    
    def test_logger_creation(self, temp_dir):
        """Test crear SessionLogger"""
        logger = SessionLogger(
            session_name="20260120_1430_G1_ROBOTICA_G3",
            output_dir=temp_dir,
            robot_type="g1"
        )
        
        assert logger.session_name == "20260120_1430_G1_ROBOTICA_G3"
        assert logger.robot_type == "g1"
        assert logger.output_dir == temp_dir
    
    def test_logger_context_manager(self, temp_dir):
        """Test usar SessionLogger como context manager"""
        with SessionLogger(
            session_name="20260120_1430_G1_ROBOTICA_G3",
            output_dir=temp_dir,
            robot_type="g1"
        ) as logger:
            assert logger is not None
            assert logger.is_active()
        
        # Después del context, debe estar cerrado
        assert not logger.is_active()
    
    def test_logger_creates_directory(self, temp_dir):
        """Test que SessionLogger crea el directorio de sesión"""
        session_name = "20260120_1430_G1_ROBOTICA_G3"
        
        with SessionLogger(session_name, temp_dir, "g1") as logger:
            pass
        
        session_dir = temp_dir / session_name
        assert session_dir.exists()
        assert session_dir.is_dir()
    
    def test_logger_creates_metadata(self, temp_dir):
        """Test que crea metadata.json"""
        session_name = "20260120_1430_G1_ROBOTICA_G3"
        
        with SessionLogger(session_name, temp_dir, "g1") as logger:
            pass
        
        metadata_file = temp_dir / session_name / "metadata.json"
        assert metadata_file.exists()
        
        with open(metadata_file) as f:
            metadata = json.load(f)
        
        assert metadata["session_name"] == session_name
        assert metadata["robot_type"] == "g1"
        assert "start_time" in metadata


class TestLogTelemetry:
    """Tests para log_telemetry"""
    
    def test_log_telemetry_single(self, temp_dir):
        """Test loguear telemetría única"""
        with SessionLogger("20260120_1430_G1_ROBOTICA_G3", temp_dir, "g1") as logger:
            logger.log_telemetry({
                "timestamp": time.time(),
                "joint_0": 0.1,
                "joint_1": 0.2
            })
        
        telemetry_file = temp_dir / "20260120_1430_G1_ROBOTICA_G3" / "telemetry.csv"
        assert telemetry_file.exists()
        
        content = telemetry_file.read_text(encoding='utf-8')
        assert "timestamp" in content
        assert "joint_0" in content
    
    def test_log_telemetry_multiple(self, temp_dir):
        """Test loguear múltiples telemetrías"""
        with SessionLogger("20260120_1430_G1_ROBOTICA_G3", temp_dir, "g1") as logger:
            for i in range(5):
                logger.log_telemetry({
                    "timestamp": time.time(),
                    "value": i * 0.1
                })
        
        telemetry_file = temp_dir / "20260120_1430_G1_ROBOTICA_G3" / "telemetry.csv"
        content = telemetry_file.read_text(encoding='utf-8')
        
        # Debe tener header + 5 líneas
        lines = content.strip().split('\n')
        assert len(lines) == 6  # header + 5 datos


class TestLogCommand:
    """Tests para log_command"""
    
    def test_log_command_single(self, temp_dir):
        """Test loguear comando único"""
        with SessionLogger("20260120_1430_G1_ROBOTICA_G3", temp_dir, "g1") as logger:
            logger.log_command("stand_up")
        
        commands_file = temp_dir / "20260120_1430_G1_ROBOTICA_G3" / "commands.log"
        assert commands_file.exists()
        
        content = commands_file.read_text(encoding='utf-8')
        assert "stand_up" in content
    
    def test_log_command_multiple(self, temp_dir):
        """Test loguear múltiples comandos"""
        with SessionLogger("20260120_1430_G1_ROBOTICA_G3", temp_dir, "g1") as logger:
            logger.log_command("stand_up")
            logger.log_command("move_forward")
            logger.log_command("stop")
        
        commands_file = temp_dir / "20260120_1430_G1_ROBOTICA_G3" / "commands.log"
        content = commands_file.read_text(encoding='utf-8')
        
        assert "stand_up" in content
        assert "move_forward" in content
        assert "stop" in content


class TestLogEvent:
    """Tests para log_event"""
    
    def test_log_event_info(self, temp_dir):
        """Test loguear evento INFO"""
        with SessionLogger("20260120_1430_G1_ROBOTICA_G3", temp_dir, "g1") as logger:
            logger.log_event("Test event", level="INFO")
        
        events_file = temp_dir / "20260120_1430_G1_ROBOTICA_G3" / "events.log"
        content = events_file.read_text(encoding='utf-8')
        
        assert "INFO" in content
        assert "Test event" in content
    
    def test_log_event_warning(self, temp_dir):
        """Test loguear evento WARNING"""
        with SessionLogger("20260120_1430_G1_ROBOTICA_G3", temp_dir, "g1") as logger:
            logger.log_event("Warning message", level="WARNING")
        
        events_file = temp_dir / "20260120_1430_G1_ROBOTICA_G3" / "events.log"
        content = events_file.read_text(encoding='utf-8')
        
        assert "WARNING" in content
        assert "Warning message" in content
    
    def test_log_event_error(self, temp_dir):
        """Test loguear evento ERROR"""
        with SessionLogger("20260120_1430_G1_ROBOTICA_G3", temp_dir, "g1") as logger:
            logger.log_event("Error message", level="ERROR")
        
        events_file = temp_dir / "20260120_1430_G1_ROBOTICA_G3" / "events.log"
        content = events_file.read_text(encoding='utf-8')
        
        assert "ERROR" in content
        assert "Error message" in content


class TestSessionLoggerEdgeCases:
    """Tests de casos edge"""
    
    def test_logger_without_context_manager(self, temp_dir):
        """Test usar logger sin context manager"""
        logger = SessionLogger("20260120_1430_G1_ROBOTICA_G3", temp_dir, "g1")
        logger.start()
        logger.log_command("test")
        logger.close()
        
        # Debe funcionar igual
        session_dir = temp_dir / "20260120_1430_G1_ROBOTICA_G3"
        assert session_dir.exists()
    
    def test_logger_double_start(self, temp_dir):
        """Test iniciar logger dos veces"""
        logger = SessionLogger("20260120_1430_G1_ROBOTICA_G3", temp_dir, "g1")
        logger.start()
        
        # Segundo start no debería causar error
        logger.start()
        
        logger.close()
    
    def test_logger_log_after_close(self, temp_dir):
        """Test loguear después de cerrar"""
        logger = SessionLogger("20260120_1430_G1_ROBOTICA_G3", temp_dir, "g1")
        logger.start()
        logger.close()
        
        # Intentar loguear después de cerrar
        with pytest.raises((ValueError, RuntimeError)):
            logger.log_command("test")
    
    def test_logger_invalid_session_name(self, temp_dir):
        """Test con nombre de sesión inválido"""
        with pytest.raises(ValueError):
            SessionLogger("invalid_name", temp_dir, "g1")
