"""
src.replay.loader
=================
Carga sesiones grabadas desde data/samples/ o data/local/.

Funciones principales:
- load_session(path): Carga sesión completa
- load_metadata(path): Carga solo metadata
- load_telemetry(path): Carga solo telemetría
- list_sessions(dir): Lista sesiones disponibles
"""

from pathlib import Path
from typing import Dict, Any, Optional
import pandas as pd
import json


class Session:
    """
    Representa una sesión grabada.
    
    Atributos:
        path: Path a la sesión
        metadata: Dict con metadata.json
        telemetry: DataFrame con telemetry.csv
        name: Nombre de la sesión
    """
    
    def __init__(self, session_path):
        # Aceptar tanto Path como str
        self.path = Path(session_path) if not isinstance(session_path, Path) else session_path
        self.name = self.path.name
        self.metadata: Optional[Dict] = None
        self.telemetry: Optional[pd.DataFrame] = None
    
    def load_metadata(self):
        """Carga metadata.json"""
        # TODO: Implementar
        metadata_file = self.path / "metadata.json"
        if metadata_file.exists():
            with open(metadata_file, 'r') as f:
                self.metadata = json.load(f)
        else:
            raise FileNotFoundError(f"metadata.json no encontrado en {self.path}")
    
    def load_telemetry(self):
        """Carga telemetry.csv"""
        # TODO: Implementar
        telemetry_file = self.path / "telemetry.csv"
        if telemetry_file.exists():
            self.telemetry = pd.read_csv(telemetry_file)
        else:
            raise FileNotFoundError(f"telemetry.csv no encontrado en {self.path}")
    
    def load_all(self):
        """Carga metadata y telemetría"""
        self.load_metadata()
        self.load_telemetry()
    
    def get_metadata(self) -> Dict[str, Any]:
        """Retorna metadata (carga si no está cargada)"""
        if self.metadata is None:
            self.load_metadata()
        return self.metadata
    
    def get_telemetry(self) -> pd.DataFrame:
        """Retorna telemetría (carga si no está cargada)"""
        if self.telemetry is None:
            self.load_telemetry()
        return self.telemetry
    
    def get_commands(self) -> list[Dict[str, Any]]:
        """Lee y retorna comandos desde commands.log"""
        commands_file = self.path / "commands.log"
        if not commands_file.exists():
            return []
        
        commands = []
        with open(commands_file, 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    parts = line.split(' - ', 2)
                    if len(parts) >= 2:
                        commands.append({
                            'timestamp': parts[0],
                            'event': parts[1],
                            'details': parts[2] if len(parts) > 2 else ''
                        })
                except Exception:
                    continue
        return commands
    
    def duration(self) -> Optional[float]:
        """Calcula duración de la sesión en minutos"""
        metadata = self.get_metadata()
        if 'duration_minutes' in metadata:
            return metadata['duration_minutes']
        return None
    
    def __repr__(self):
        return f"Session(name={self.name}, path={self.path})"


def load_session(session_path: Path) -> Session:
    """
    Carga sesión completa.
    
    Args:
        session_path: Path a la carpeta de sesión
        
    Returns:
        Session: Objeto de sesión cargado
        
    Example:
        >>> session = load_session(Path("data/samples/sessions/example_session"))
        >>> print(session.metadata)
        >>> print(session.telemetry.head())
    """
    # TODO: Implementar
    session = Session(session_path)
    session.load_all()
    return session


def list_sessions(directory: Path, robot_type: Optional[str] = None) -> list[Path]:
    """
    Lista todas las sesiones en un directorio.
    
    Args:
        directory: Path al directorio de sesiones (ej: data/local/sessions)
        robot_type: Filtrar por tipo de robot ('g1' o 'go2'), None para todos
        
    Returns:
        list[Path]: Lista de paths a sesiones
        
    Example:
        >>> sessions = list_sessions(Path("data/samples/sessions"))
        >>> go2_sessions = list_sessions(Path("data/samples/sessions"), robot_type="go2")
    """
    if not directory.exists():
        return []
    
    # Buscar carpetas que contengan metadata.json
    sessions = []
    for item in directory.iterdir():
        if item.is_dir() and (item / "metadata.json").exists():
            # Filtrar por robot_type si se especifica
            if robot_type:
                try:
                    with open(item / "metadata.json", 'r') as f:
                        metadata = json.load(f)
                    if metadata.get('robot_type', '').lower() != robot_type.lower():
                        continue
                except Exception:
                    continue
            sessions.append(item)
    
    return sorted(sessions)


# TODO: Agregar funciones de análisis básico
# def get_session_duration(session: Session) -> float:
#     """Retorna duración de la sesión en segundos"""
#     pass

# def get_session_stats(session: Session) -> Dict[str, Any]:
#     """Retorna estadísticas básicas de la sesión"""
#     pass
