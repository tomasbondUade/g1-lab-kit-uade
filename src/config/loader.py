"""
src.config.loader
=================
Carga configuración desde .env y archivos YAML.

Funciones principales:
- load_config(): Carga configuración completa
- load_env(): Carga solo variables de entorno
- load_yaml(file): Carga archivo YAML específico
- validate_config(config): Valida configuración
"""

from pathlib import Path
from typing import Dict, Any, Optional
import os
from dotenv import load_dotenv
import yaml


class Config:
    """
    Clase de configuración del Lab Kit.
    
    Atributos:
        data_mode: "replay" o "live"
        robot_type: "g1" o "go2" (lowercase)
        robot_ip: IP del robot (solo live)
        session_name: Nombre de sesión actual
        project_root: Path a la raíz del proyecto
    """
    
    def __init__(self):
        self.data_mode: str = "replay"
        self.robot_type: str = "g1"
        self.robot_ip: Optional[str] = None
        self.session_name: Optional[str] = None
        self.project_root: Path = Path(__file__).parent.parent.parent
        
        # Directorios
        self.data_dir_local: Path = self.project_root / "data" / "local"
        self.data_dir_samples: Path = self.project_root / "data" / "samples"
        self.config_dir: Path = self.project_root / "config"
        
        # Configuraciones YAML (cargadas on-demand)
        self._robot_config: Optional[Dict] = None
        self._network_config: Optional[Dict] = None
        self._limits_config: Optional[Dict] = None
    
    def __repr__(self):
        return (f"Config(data_mode={self.data_mode}, "
                f"robot_type={self.robot_type}, "
                f"robot_ip={self.robot_ip})")


def load_config() -> Config:
    """
    Carga configuración completa desde .env y YAML.
    
    Returns:
        Config: Objeto de configuración
        
    Example:
        >>> config = load_config()
        >>> print(config.data_mode)
        'replay'
    """
    # TODO: Implementar carga completa
    # 1. Cargar .env
    # 2. Crear objeto Config
    # 3. Poblar desde variables de entorno
    # 4. Validar
    
    config = Config()
    
    # Cargar .env
    env_path = config.project_root / ".env"
    if env_path.exists():
        load_dotenv(env_path)
    
    # Cargar variables de entorno
    config.data_mode = os.getenv("DATA_MODE", "replay")
    config.robot_type = os.getenv("ROBOT_TYPE", "G1")
    config.robot_ip = os.getenv("ROBOT_IP")
    config.session_name = os.getenv("SESSION_NAME")
    
    return config


def load_yaml(yaml_path: Path) -> Dict[str, Any]:
    """
    Carga archivo YAML.
    
    Args:
        yaml_path: Path al archivo YAML
        
    Returns:
        Dict con contenido del YAML
        
    Raises:
        FileNotFoundError: Si el archivo no existe
        yaml.YAMLError: Si hay error de parseo
    """
    # TODO: Implementar carga con manejo de errores
    if not yaml_path.exists():
        raise FileNotFoundError(f"Archivo YAML no encontrado: {yaml_path}")
    
    with open(yaml_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def validate_config(config: Config) -> bool:
    """
    Valida configuración.
    
    Args:
        config: Objeto Config a validar
        
    Returns:
        bool: True si válido, False si no
        
    Raises:
        ValueError: Si hay errores críticos
    """
    # TODO: Implementar validaciones
    # - data_mode in ["replay", "live"]
    # - robot_type in ["G1", "GO2"]
    # - Si live, robot_ip debe existir
    # - Verificar que existan directorios necesarios
    
    if config.data_mode not in ["replay", "live"]:
        raise ValueError(f"data_mode inválido: {config.data_mode}")
    
    if config.robot_type not in ["G1", "GO2"]:
        raise ValueError(f"robot_type inválido: {config.robot_type}")
    
    if config.data_mode == "live" and not config.robot_ip:
        raise ValueError("robot_ip requerido para modo live")
    
    return True


# TODO: Agregar funciones helper
# def get_robot_config(config: Config) -> Dict:
#     """Carga robot_config.yaml"""
#     pass

# def get_network_config(config: Config) -> Dict:
#     """Carga network.yaml"""
#     pass

# def get_limits_config(config: Config) -> Dict:
#     """Carga limits.yaml"""
#     pass
