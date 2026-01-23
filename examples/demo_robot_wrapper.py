"""
Ejemplo simple usando el wrapper RobotClient
============================================
"""

import time
from src.robot import RobotClient

def main():
    print("=" * 60)
    print("Demo - RobotClient Wrapper")
    print("=" * 60)
    
    # Crear cliente
    robot = RobotClient(timeout=5.0)
    
    # Conectar
    print("\n📡 Conectando al robot...")
    if not robot.connect():
        print("❌ No se pudo conectar")
        return
    
    print("✅ Conectado!")
    
    try:
        # Comandos básicos
        print("\n🐕 Enviando comandos...")
        
        print("  1. Stand Up")
        robot.stand_up()
        time.sleep(2)
        
        print("  2. Stand Down")
        robot.stand_down()
        time.sleep(2)
        
        print("  3. Damp (parada segura)")
        robot.damp()
        
        print("\n✅ Comandos ejecutados correctamente")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
    
    finally:
        # Siempre desconectar
        print("\n👋 Desconectando...")
        robot.disconnect()

if __name__ == "__main__":
    main()
