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
    
    def __init__(self, session_path: Path):
        self.path = session_path
        self.name = session_path.name
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


def list_sessions(directory: Path) -> list[Path]:
    """
    Lista todas las sesiones en un directorio.
    
    Args:
        directory: Path al directorio de sesiones (ej: data/local/sessions)
        
    Returns:
        list[Path]: Lista de paths a sesiones
        
    Example:
        >>> sessions = list_sessions(Path("data/samples/sessions"))
        >>> for s in sessions:
        ...     print(s.name)
    """
    # TODO: Implementar
    if not directory.exists():
        return []
    
    # Buscar carpetas que contengan metadata.json
    sessions = []
    for item in directory.iterdir():
        if item.is_dir() and (item / "metadata.json").exists():
            sessions.append(item)
    
    return sorted(sessions)


# TODO: Agregar funciones de análisis básico
# def get_session_duration(session: Session) -> float:
#     """Retorna duración de la sesión en segundos"""
#     pass

# def get_session_stats(session: Session) -> Dict[str, Any]:
#     """Retorna estadísticas básicas de la sesión"""
#     pass
