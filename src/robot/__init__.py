"""
src.robot - Conexión y comunicación con robot

Clase principal: RobotClient

Example:
    >>> from src.robot import RobotClient
    >>> 
    >>> robot = RobotClient()
    >>> robot.connect()
    >>> robot.stand_up()
    >>> robot.damp()
    >>> robot.disconnect()
"""

from .client import RobotClient, quick_connect, safe_stop

__all__ = ['RobotClient', 'quick_connect', 'safe_stop']
