"""
src.logging.session
===================
Logger de sesiones con naming estándar.

Crea estructura:
data/local/sessions/<SESSION_NAME>/
  - metadata.json
  - telemetry.csv
  - (opcional) events.json
"""

from pathlib import Path
from typing import Dict, Any, Optional
from datetime import datetime
import json
import csv


class SessionLogger:
    """
    Logger de sesión.
    
    Attributes:
        session_name: Nombre de la sesión (YYYYMMDD_HHMM_ROBOT_MATERIA_GRUPO)
        session_path: Path a la carpeta de sesión
        metadata: Dict con metadata de la sesión
        is_active: Si el logger está activo
    """
    
    def __init__(
        self,
        session_name: str,
        output_dir: Path,
        metadata: Optional[Dict[str, Any]] = None
    ):
        """
        Inicializa logger de sesión.
        
        Args:
            session_name: Nombre de la sesión
            output_dir: Directorio base (ej: data/local/sessions)
            metadata: Metadata opcional para la sesión
        """
        self.session_name = session_name
        self.session_path = output_dir / session_name
        self.metadata = metadata or {}
        self.is_active = False
        
        # Archivos
        self._metadata_file: Optional[Path] = None
        self._telemetry_file: Optional[Path] = None
        self._telemetry_writer: Optional[csv.DictWriter] = None
        self._telemetry_handle: Optional[Any] = None
    
    def start(self):
        """
        Inicia logging (crea directorio y archivos).
        
        Raises:
            RuntimeError: Si el logger ya está activo
            FileExistsError: Si la sesión ya existe
        """
        # TODO: Implementar
        if self.is_active:
            raise RuntimeError("Logger ya está activo")
        
        # Crear directorio
        if self.session_path.exists():
            raise FileExistsError(f"Sesión ya existe: {self.session_path}")
        
        self.session_path.mkdir(parents=True)
        
        # Crear metadata.json
        self._metadata_file = self.session_path / "metadata.json"
        self._save_metadata()
        
        # Preparar telemetry.csv (no crear aún, esperar primer log)
        self._telemetry_file = self.session_path / "telemetry.csv"
        
        self.is_active = True
        print(f"✓ Sesión iniciada: {self.session_name}")
    
    def log_telemetry(self, data: Dict[str, Any]):
        """
        Registra entrada de telemetría.
        
        Args:
            data: Dict con datos de telemetría
            
        Raises:
            RuntimeError: Si el logger no está activo
        """
        # TODO: Implementar
        if not self.is_active:
            raise RuntimeError("Logger no está activo. Llamar start() primero.")
        
        # Agregar timestamp si no existe
        if "timestamp" not in data:
            data["timestamp"] = datetime.now().isoformat()
        
        # Si es la primera vez, crear archivo con headers
        if self._telemetry_writer is None:
            self._telemetry_handle = open(self._telemetry_file, 'w', newline='')
            self._telemetry_writer = csv.DictWriter(
                self._telemetry_handle,
                fieldnames=data.keys()
            )
            self._telemetry_writer.writeheader()
        
        # Escribir fila
        self._telemetry_writer.writerow(data)
        self._telemetry_handle.flush()
    
    def stop(self):
        """
        Detiene logging y cierra archivos.
        
        Raises:
            RuntimeError: Si el logger no está activo
        """
        # TODO: Implementar
        if not self.is_active:
            raise RuntimeError("Logger no está activo")
        
        # Cerrar archivos
        if self._telemetry_handle:
            self._telemetry_handle.close()
            self._telemetry_handle = None
            self._telemetry_writer = None
        
        # Actualizar metadata con duración, etc.
        self._save_metadata()
        
        self.is_active = False
        print(f"✓ Sesión finalizada: {self.session_name}")
    
    def _save_metadata(self):
        """Guarda metadata.json"""
        if self._metadata_file:
            with open(self._metadata_file, 'w') as f:
                json.dump(self.metadata, f, indent=2)
    
    def __enter__(self):
        """Context manager support"""
        self.start()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager support"""
        self.stop()


# TODO: Agregar funciones helper
# def create_session_logger(config, materia, grupo) -> SessionLogger:
#     """Crea logger usando configuración"""
#     pass
