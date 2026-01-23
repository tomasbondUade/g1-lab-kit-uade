"""
Ejemplo usando context manager
==============================
"""

import time
from src.robot import RobotClient

def main():
    print("Demo - Context Manager")
    print("=" * 60)
    
    # Usando context manager (con with)
    # Se conecta automáticamente al entrar y desconecta al salir
    with RobotClient() as robot:
        print("✅ Conectado (automático)")
        
        # Suscribir a telemetría
        robot.subscribe_telemetry()
        
        # Esperar datos
        print("\n⏳ Esperando telemetría...")
        state = robot.wait_for_telemetry(timeout=5.0)
        
        if state:
            print(f"📊 Posición: x={state.position[0]:.3f}, y={state.position[1]:.3f}, z={state.position[2]:.3f}")
            print(f"📊 Altura: {state.body_height:.3f} m")
        
        # Comandos
        print("\n🐕 Stand Up")
        robot.stand_up()
        time.sleep(2)
        
        print("🛑 Damp")
        robot.damp()
    
    print("\n✅ Desconectado (automático)")

if __name__ == "__main__":
    main()
