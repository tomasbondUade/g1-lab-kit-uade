"""
Fixtures compartidos para tests
"""
import pytest
import tempfile
import shutil
import json
from pathlib import Path
from datetime import datetime


@pytest.fixture
def temp_dir():
    """Crea directorio temporal para tests"""
    temp = tempfile.mkdtemp()
    yield Path(temp)
    shutil.rmtree(temp)


@pytest.fixture
def sample_config(temp_dir):
    """Config YAML de ejemplo"""
    config_dir = temp_dir / "config"
    config_dir.mkdir()
    
    config_content = """robot:
  type: "g1"
  ip: "192.168.123.161"

sdk:
  timeout: 5
  reconnect: true

network:
  interface: "Ethernet"
  ip_source: "env"

telemetry:
  log_interval: 0.1

limits:
  max_velocity: 1.0
  max_torque: 50.0
  emergency_stop: true
  risk_level: 1
"""
    
    config_file = config_dir / "robot_config.yaml"
    config_file.write_text(config_content, encoding='utf-8')
    
    return config_file


@pytest.fixture
def sample_metadata():
    """Metadata JSON de ejemplo"""
    return {
        "session_name": "20260120_1430_G1_ROBOTICA_G3",
        "robot_type": "g1",
        "start_time": "2026-01-20T14:30:00",
        "end_time": "2026-01-20T15:15:00",
        "duration_seconds": 2700,
        "materia": "ROBOTICA",
        "grupo": "G3",
        "operator": "Test User",
        "risk_level": 1,
        "notes": "Test session"
    }


@pytest.fixture
def sample_session(temp_dir, sample_metadata):
    """Sesión completa de ejemplo"""
    session_name = sample_metadata["session_name"]
    session_dir = temp_dir / "data" / "local" / "sessions" / session_name
    session_dir.mkdir(parents=True)
    
    # metadata.json
    metadata_file = session_dir / "metadata.json"
    metadata_file.write_text(json.dumps(sample_metadata, indent=2), encoding='utf-8')
    
    # telemetry.csv
    telemetry_content = """timestamp,joint_0,joint_1,velocity_x,velocity_y
1705753800.0,0.1,0.2,0.01,0.02
1705753800.1,0.11,0.21,0.012,0.021
1705753800.2,0.12,0.22,0.013,0.022
"""
    telemetry_file = session_dir / "telemetry.csv"
    telemetry_file.write_text(telemetry_content, encoding='utf-8')
    
    # commands.log
    commands_content = """[2026-01-20 14:30:00] COMMAND: stand_up
[2026-01-20 14:30:05] COMMAND: move_forward
[2026-01-20 14:30:10] COMMAND: stop
"""
    commands_file = session_dir / "commands.log"
    commands_file.write_text(commands_content, encoding='utf-8')
    
    return session_dir


@pytest.fixture
def valid_session_names():
    """Nombres de sesión válidos para testing"""
    return [
        "20260120_1430_G1_ROBOTICA_G3",
        "20251215_0900_GO2_CONTROL_G1",
        "20260301_1600_G1_IA_G5",
    ]


@pytest.fixture
def invalid_session_names():
    """Nombres de sesión inválidos para testing"""
    return [
        "invalid_name",
        "20260120_G1_ROBOTICA",  # Falta hora
        "20260120_1430_INVALID_ROBOTICA_G3",  # Robot inválido
        "2026-01-20_14:30_G1_ROBOTICA_G3",  # Formato incorrecto
        "",
    ]
