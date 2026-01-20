"""
src.utils.naming
================
Convenciones de naming para sesiones y archivos.

Estándar: YYYYMMDD_HHMM_ROBOT_MATERIA_GRUPO
Ejemplo: 20260120_1030_G1_Prog1_G3
"""

from datetime import datetime
from typing import Optional, Dict
import re


def generate_session_name(
    robot_type: str,
    materia: str,
    grupo: str,
    timestamp: Optional[datetime] = None
) -> str:
    """
    Genera nombre de sesión estándar.
    
    Args:
        robot_type: "G1" o "GO2"
        materia: Nombre de la materia (ej: "Prog1", "Robotica")
        grupo: Nombre del grupo (ej: "G3", "Equipo1")
        timestamp: Timestamp opcional (usa actual si no se provee)
        
    Returns:
        str: Nombre de sesión (YYYYMMDD_HHMM_ROBOT_MATERIA_GRUPO)
        
    Example:
        >>> generate_session_name("G1", "Prog1", "G3")
        '20260120_1030_G1_Prog1_G3'
    """
    # TODO: Implementar generación
    if timestamp is None:
        timestamp = datetime.now()
    
    date_str = timestamp.strftime("%Y%m%d")
    time_str = timestamp.strftime("%H%M")
    
    # Sanitizar nombres (sin espacios ni caracteres especiales)
    robot_clean = robot_type.upper()
    materia_clean = materia.replace(" ", "")
    grupo_clean = grupo.replace(" ", "")
    
    return f"{date_str}_{time_str}_{robot_clean}_{materia_clean}_{grupo_clean}"


def parse_session_name(session_name: str) -> Dict[str, str]:
    """
    Parsea nombre de sesión estándar.
    
    Args:
        session_name: Nombre de sesión a parsear
        
    Returns:
        Dict con componentes: date, time, robot, materia, grupo
        
    Raises:
        ValueError: Si el nombre no sigue el formato estándar
        
    Example:
        >>> parse_session_name("20260120_1030_G1_Prog1_G3")
        {'date': '20260120', 'time': '1030', 'robot': 'G1', 
         'materia': 'Prog1', 'grupo': 'G3'}
    """
    # TODO: Implementar parseo con regex
    pattern = r"^(\d{8})_(\d{4})_([A-Z0-9]+)_([A-Za-z0-9]+)_([A-Za-z0-9]+)$"
    match = re.match(pattern, session_name)
    
    if not match:
        raise ValueError(f"Nombre de sesión inválido: {session_name}")
    
    return {
        "date": match.group(1),
        "time": match.group(2),
        "robot": match.group(3),
        "materia": match.group(4),
        "grupo": match.group(5)
    }


def validate_session_name(session_name: str) -> bool:
    """
    Valida que un nombre de sesión siga el formato estándar.
    
    Args:
        session_name: Nombre a validar
        
    Returns:
        bool: True si válido, False si no
    """
    try:
        parse_session_name(session_name)
        return True
    except ValueError:
        return False


# TODO: Agregar más utilidades de naming
# def sanitize_filename(filename: str) -> str:
#     """Sanitiza nombre de archivo (remueve caracteres inválidos)"""
#     pass

# def generate_log_filename(session_name: str, extension: str = "csv") -> str:
#     """Genera nombre de archivo de log"""
#     pass
