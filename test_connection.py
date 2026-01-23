"""
Test de conexión básica con el robot Go2
========================================
Script simple para verificar la conexión con el robot.
"""
import sys
import time
import os

# Configurar CycloneDDS para evitar error de log en Windows
os.environ['CYCLONEDDS_URI'] = '<CycloneDDS><Domain><Id>0</Id></Domain><Tracing><Verbosity>none</Verbosity></Tracing></CycloneDDS>'

from unitree_sdk2py.core.channel import ChannelFactoryInitialize
from unitree_sdk2py.go2.sport.sport_client import SportClient

def test_connection(robot_ip="192.168.123.18"):
    """Prueba la conexión con el robot."""
    print("=" * 60)
    print("TEST DE CONEXIÓN - Robot Go2")
    print("=" * 60)
    print(f"\n🤖 Intentando conectar con el robot en IP: {robot_ip}")
    print("⚠️  Asegúrate de que no haya obstáculos alrededor del robot.\n")
    
    try:
        # Inicializar el canal de comunicación
        print("📡 Inicializando canal de comunicación...")
        # Probar sin IP específica (modo broadcast)
        ChannelFactoryInitialize(0)
        
        # Crear cliente deportivo
        print("🔧 Creando cliente...")
        sport_client = SportClient()
        sport_client.SetTimeout(5.0)
        sport_client.Init()
        
        print("✅ Conexión establecida exitosamente!\n")
        print("-" * 60)
        print("Comandos básicos de prueba:")
        print("  1 - Stand Up (pararse)")
        print("  2 - Stand Down (agacharse)")
        print("  0 - Damp (modo relajado)")
        print("  q - Salir")
        print("-" * 60)
        
        while True:
            cmd = input("\nIngresa comando (solo el número): ").strip()
            
            # Extraer solo el primer carácter para ser más flexible
            if cmd:
                cmd = cmd[0].lower()
            
            if cmd == 'q':
                print("👋 Finalizando...")
                break
            elif cmd == '1':
                print("🐕 Enviando comando: Stand Up")
                sport_client.StandUp()
                time.sleep(1)
                print("   ✓ Comando enviado")
            elif cmd == '2':
                print("🐕 Enviando comando: Stand Down")
                sport_client.StandDown()
                time.sleep(1)
                print("   ✓ Comando enviado")
            elif cmd == '0':
                print("🐕 Enviando comando: Damp (modo relajado)")
                sport_client.Damp()
                time.sleep(1)
                print("   ✓ Comando enviado")
            else:
                print("❌ Comando no reconocido. Usa: 0, 1, 2 o q")
        
    except Exception as e:
        print(f"\n❌ Error al conectar con el robot:")
        print(f"   {type(e).__name__}: {e}")
        print("\n💡 Sugerencias:")
        print("   - Verifica que el robot esté encendido")
        print("   - Confirma la IP del robot (actualmente: {})".format(robot_ip))
        print("   - Comprueba la conexión de red con: ping {}".format(robot_ip))
        return False
    
    return True

if __name__ == "__main__":
    # Cargar IP desde argumento o usar la del .env
    robot_ip = sys.argv[1] if len(sys.argv) > 1 else "192.168.123.18"
    test_connection(robot_ip)
