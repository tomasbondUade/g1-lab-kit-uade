"""
02_telemetry_check.py
=====================
Objetivo: Verificar lectura de telemetría (estado básico del robot).

Modo: Replay (usa data/samples/) / Live (suscribe telemetría real)

Uso:
    # Replay (sin robot)
    python examples/02_telemetry_check.py --mode replay --sample data/samples/sessions/example_session
    
    # Live (con robot)
    python examples/02_telemetry_check.py --mode live

Salida esperada:
    - Valores de batería, IMU, joints (según disponibilidad)
    - Estadísticas básicas (min/max/avg si es replay)
"""

import os
import sys
import time
import argparse
from pathlib import Path
from dotenv import load_dotenv

# Configurar CycloneDDS para evitar error de log en Windows
os.environ['CYCLONEDDS_URI'] = '<CycloneDDS><Domain><Id>0</Id></Domain><Tracing><Verbosity>none</Verbosity></Tracing></CycloneDDS>'

from unitree_sdk2py.core.channel import ChannelSubscriber, ChannelFactoryInitialize
from unitree_sdk2py.idl.default import unitree_go_msg_dds__SportModeState_
from unitree_sdk2py.idl.unitree_go.msg.dds_ import SportModeState_

class TelemetryMonitor:
    """Monitor de telemetría para el robot Go2."""
    
    def __init__(self):
        self.last_state = None
        self.message_count = 0
        
    def state_handler(self, msg: SportModeState_):
        """Callback para procesar mensajes de estado."""
        self.last_state = msg
        self.message_count += 1
    
    def print_telemetry(self):
        """Imprime la telemetría actual."""
        if self.last_state is None:
            print("⏳ Esperando datos del robot...")
            return
        
        state = self.last_state
        
        # Limpiar pantalla
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("=" * 60)
        print("🤖 TELEMETRÍA DEL ROBOT GO2")
        print("=" * 60)
        
        # Estado general
        print(f"\n📊 Estado General:")
        print(f"   Mensajes recibidos: {self.message_count}")
        print(f"   Modo:              {state.mode}")
        print(f"   Gait type:         {state.gait_type}")
        print(f"   Foot raise height: {state.foot_raise_height:.3f} m")
        
        # Posición y orientación
        print(f"\n📍 Posición (x, y, z):")
        print(f"   {state.position[0]:7.3f}, {state.position[1]:7.3f}, {state.position[2]:7.3f} m")
        
        print(f"\n🧭 Orientación (body):")
        print(f"   Body height: {state.body_height:.3f} m")
        
        # Velocidad
        print(f"\n💨 Velocidad:")
        print(f"   Linear  (x,y,z): {state.velocity[0]:6.3f}, {state.velocity[1]:6.3f}, {state.velocity[2]:6.3f} m/s")
        print(f"   Angular (yaw):   {state.yaw_speed:6.3f} rad/s")
        
        # Footer
        print("\n" + "=" * 60)
        print("Presiona Ctrl+C para salir")
        print("=" * 60)

def mode_live():
    """Modo live: lee telemetría en tiempo real del robot."""
    print("\n🔴 MODO LIVE - Conectando al robot...")
    
    try:
        # Inicializar comunicación (sin IP específica, usa broadcast)
        print("📡 Inicializando canal de comunicación...")
        ChannelFactoryInitialize(0)
        
        # Crear monitor y suscriptor
        monitor = TelemetryMonitor()
        subscriber = ChannelSubscriber("rt/sportmodestate", SportModeState_)
        subscriber.Init(monitor.state_handler, 10)
        
        print("✅ Conectado! Leyendo telemetría...\n")
        
        # Loop principal
        while True:
            monitor.print_telemetry()
            time.sleep(0.5)  # Actualizar 2 veces por segundo
            
    except KeyboardInterrupt:
        print("\n\n👋 Finalizando monitoreo...")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\n💡 Sugerencias:")
        print("   - Verifica que el robot esté encendido")
        print("   - Confirma la conexión de red")
        return False
    
    return True

def mode_replay(sample_path):
    """Modo replay: carga y muestra estadísticas de una sesión grabada."""
    print("\n📼 MODO REPLAY")
    
    if not sample_path:
        print("❌ Error: Debes especificar --sample <path>")
        return False
    
    session_dir = Path(sample_path)
    
    if not session_dir.exists():
        print(f"❌ Error: No existe la sesión: {session_dir}")
        return False
    
    # Buscar archivo de telemetría
    telemetry_file = session_dir / "telemetry.csv"
    
    if not telemetry_file.exists():
        print(f"❌ Error: No se encontró telemetry.csv en: {session_dir}")
        return False
    
    print(f"📂 Cargando: {telemetry_file}")
    
    try:
        import pandas as pd
        df = pd.read_csv(telemetry_file)
        
        print(f"\n✅ Sesión cargada: {len(df)} registros")
        print("\n📊 Estadísticas:")
        print(df.describe())
        
        return True
        
    except ImportError:
        print("❌ Error: pandas no está instalado")
        print("💡 Instala con: pip install pandas")
        return False
    except Exception as e:
        print(f"❌ Error al cargar archivo: {e}")
        return False

def main():
    # Cargar .env
    project_root = Path(__file__).parent.parent
    load_dotenv(project_root / ".env")
    
    # Parsear argumentos
    parser = argparse.ArgumentParser(description="Verificar telemetría del robot")
    parser.add_argument("--mode", choices=["replay", "live"], 
                       default="live",
                       help="Modo de operación (default: live)")
    parser.add_argument("--sample", 
                       help="Path a sesión para modo replay")
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("G1/Go2 Lab Kit - Telemetry Check")
    print("=" * 60)
    
    if args.mode == "live":
        mode_live()
    else:
        mode_replay(args.sample)

if __name__ == "__main__":
    main()
