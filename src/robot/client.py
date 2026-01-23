"""
src.robot.client
================
Wrapper limpio del Unitree SDK para simplificar operaciones comunes.

Clase principal: RobotClient
"""

import os
import time
from typing import Optional, Callable
from pathlib import Path

# Configurar CycloneDDS para evitar error de log en Windows
os.environ['CYCLONEDDS_URI'] = '<CycloneDDS><Domain><Id>0</Id></Domain><Tracing><Verbosity>none</Verbosity></Tracing></CycloneDDS>'

from unitree_sdk2py.core.channel import ChannelSubscriber, ChannelFactoryInitialize
from unitree_sdk2py.idl.default import unitree_go_msg_dds__SportModeState_
from unitree_sdk2py.idl.unitree_go.msg.dds_ import SportModeState_
from unitree_sdk2py.go2.sport.sport_client import SportClient


class RobotClient:
    """
    Cliente simplificado para robot Unitree Go2.
    
    Encapsula la inicialización del SDK, conexión y comandos básicos.
    
    Example:
        >>> from src.robot import RobotClient
        >>> 
        >>> # Crear y conectar
        >>> robot = RobotClient()
        >>> robot.connect()
        >>> 
        >>> # Enviar comandos
        >>> robot.stand_up()
        >>> time.sleep(2)
        >>> robot.damp()
        >>> 
        >>> # Desconectar
        >>> robot.disconnect()
    """
    
    def __init__(self, timeout: float = 5.0):
        """
        Inicializa el cliente del robot.
        
        Args:
            timeout: Timeout para comandos en segundos (default: 5.0)
        """
        self.timeout = timeout
        self.sport_client: Optional[SportClient] = None
        self.telemetry_subscriber: Optional[ChannelSubscriber] = None
        self.is_connected = False
        self._last_state: Optional[SportModeState_] = None
        
    def connect(self, use_broadcast: bool = True, robot_ip: Optional[str] = None) -> bool:
        """
        Conecta con el robot.
        
        Args:
            use_broadcast: Si True, usa broadcast (recomendado). Si False, usa IP específica.
            robot_ip: IP del robot (solo si use_broadcast=False)
            
        Returns:
            bool: True si la conexión fue exitosa
            
        Example:
            >>> robot = RobotClient()
            >>> robot.connect()  # Usa broadcast
            >>> # o
            >>> robot.connect(use_broadcast=False, robot_ip="192.168.123.18")
        """
        try:
            # Inicializar canal de comunicación
            if use_broadcast:
                ChannelFactoryInitialize(0)
            else:
                if not robot_ip:
                    raise ValueError("robot_ip requerido cuando use_broadcast=False")
                ChannelFactoryInitialize(0, robot_ip)
            
            # Crear cliente deportivo
            self.sport_client = SportClient()
            self.sport_client.SetTimeout(self.timeout)
            self.sport_client.Init()
            
            self.is_connected = True
            return True
            
        except Exception as e:
            print(f"Error al conectar: {e}")
            self.is_connected = False
            return False
    
    def disconnect(self):
        """Desconecta del robot y limpia recursos."""
        self.is_connected = False
        self.sport_client = None
        self.telemetry_subscriber = None
    
    def _ensure_connected(self):
        """Verifica que haya conexión activa."""
        if not self.is_connected or not self.sport_client:
            raise RuntimeError("Robot no conectado. Llama a connect() primero.")
    
    # ==================== Comandos básicos ====================
    
    def stand_up(self) -> bool:
        """
        Hace que el robot se pare.
        
        Returns:
            bool: True si el comando fue exitoso
        """
        self._ensure_connected()
        try:
            self.sport_client.StandUp()
            return True
        except Exception as e:
            print(f"Error en stand_up: {e}")
            return False
    
    def stand_down(self) -> bool:
        """
        Hace que el robot se agache.
        
        Returns:
            bool: True si el comando fue exitoso
        """
        self._ensure_connected()
        try:
            self.sport_client.StandDown()
            return True
        except Exception as e:
            print(f"Error en stand_down: {e}")
            return False
    
    def damp(self) -> bool:
        """
        Pone el robot en modo relajado (parada segura).
        
        Returns:
            bool: True si el comando fue exitoso
        """
        self._ensure_connected()
        try:
            self.sport_client.Damp()
            return True
        except Exception as e:
            print(f"Error en damp: {e}")
            return False
    
    def move(self, vx: float = 0.0, vy: float = 0.0, vyaw: float = 0.0) -> bool:
        """
        Mueve el robot con velocidades específicas.
        
        Args:
            vx: Velocidad adelante/atrás (m/s)
            vy: Velocidad lateral (m/s)
            vyaw: Velocidad angular (rad/s)
            
        Returns:
            bool: True si el comando fue exitoso
            
        Example:
            >>> robot.move(vx=0.3, vy=0.0, vyaw=0.0)  # Avanzar
            >>> robot.move(vx=0.0, vy=0.0, vyaw=0.5)  # Rotar
        """
        self._ensure_connected()
        try:
            self.sport_client.Move(vx, vy, vyaw)
            return True
        except Exception as e:
            print(f"Error en move: {e}")
            return False
    
    def stop_move(self) -> bool:
        """
        Detiene el movimiento del robot.
        
        Returns:
            bool: True si el comando fue exitoso
        """
        return self.move(0.0, 0.0, 0.0)
    
    # ==================== Telemetría ====================
    
    def subscribe_telemetry(self, callback: Optional[Callable[[SportModeState_], None]] = None):
        """
        Suscribe a la telemetría del robot.
        
        Args:
            callback: Función que se llama con cada mensaje de telemetría.
                     Si no se provee, guarda en self._last_state
                     
        Example:
            >>> def my_handler(msg):
            ...     print(f"Posición: {msg.position}")
            >>> 
            >>> robot.subscribe_telemetry(my_handler)
        """
        self._ensure_connected()
        
        def default_handler(msg: SportModeState_):
            self._last_state = msg
            if callback:
                callback(msg)
        
        self.telemetry_subscriber = ChannelSubscriber("rt/sportmodestate", SportModeState_)
        self.telemetry_subscriber.Init(default_handler, 10)
    
    def get_last_state(self) -> Optional[SportModeState_]:
        """
        Retorna el último estado de telemetría recibido.
        
        Returns:
            SportModeState_ o None si no hay datos
            
        Note:
            Requiere haber llamado a subscribe_telemetry() primero
        """
        return self._last_state
    
    def wait_for_telemetry(self, timeout: float = 5.0) -> Optional[SportModeState_]:
        """
        Espera hasta recibir telemetría.
        
        Args:
            timeout: Tiempo máximo de espera en segundos
            
        Returns:
            SportModeState_ o None si timeout
        """
        if not self.telemetry_subscriber:
            self.subscribe_telemetry()
        
        start_time = time.time()
        while time.time() - start_time < timeout:
            if self._last_state is not None:
                return self._last_state
            time.sleep(0.1)
        
        return None
    
    # ==================== Utilidades ====================
    
    def __enter__(self):
        """Context manager: with RobotClient() as robot: ..."""
        self.connect()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager: cleanup automático"""
        self.disconnect()
    
    def __repr__(self):
        status = "conectado" if self.is_connected else "desconectado"
        return f"RobotClient(status={status}, timeout={self.timeout})"


# ==================== Funciones de utilidad ====================

def quick_connect(timeout: float = 5.0) -> RobotClient:
    """
    Crea y conecta un cliente rápidamente.
    
    Args:
        timeout: Timeout para comandos
        
    Returns:
        RobotClient conectado
        
    Example:
        >>> robot = quick_connect()
        >>> robot.stand_up()
    """
    robot = RobotClient(timeout=timeout)
    if not robot.connect():
        raise RuntimeError("No se pudo conectar al robot")
    return robot


def safe_stop(robot: RobotClient) -> bool:
    """
    Ejecuta parada segura del robot.
    
    Args:
        robot: Cliente del robot
        
    Returns:
        bool: True si fue exitoso
        
    Example:
        >>> robot = quick_connect()
        >>> safe_stop(robot)
    """
    return robot.damp()
