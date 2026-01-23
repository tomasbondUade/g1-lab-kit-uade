"""
03_log_session.py
=================
Objetivo: Generar una sesión de logs con naming estándar.

Modo: Replay (simula log) / Live (guarda telemetría real)

Uso:
    python examples/03_log_session.py --session 20260120_1030_G1_Prog1_G3
    
    # O deja que se genere automáticamente
    python examples/03_log_session.py

Salida esperada:
    - Carpeta creada en data/local/sessions/<SESSION_NAME>/
    - Archivo telemetry.csv (o .parquet)
    - Archivo metadata.json con info de la sesión
"""

import os
import sys
import time
import json
import argparse
import csv
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

# Configurar CycloneDDS
os.environ['CYCLONEDDS_URI'] = '<CycloneDDS><Domain><Id>0</Id></Domain><Tracing><Verbosity>none</Verbosity></Tracing></CycloneDDS>'

from unitree_sdk2py.core.channel import ChannelSubscriber, ChannelFactoryInitialize
from unitree_sdk2py.idl.default import unitree_go_msg_dds__SportModeState_
from unitree_sdk2py.idl.unitree_go.msg.dds_ import SportModeState_

# Importar utilidades de naming
sys.path.insert(0, str(Path(__file__).parent.parent))
from src.utils.naming import generate_session_name

class SessionLogger:
    """Logger para guardar sesiones de telemetría."""
    
    def __init__(self, session_path: Path):
        self.session_path = session_path
        self.session_path.mkdir(parents=True, exist_ok=True)
        
        self.telemetry_file = session_path / "telemetry.csv"
        self.commands_file = session_path / "commands.log"
        self.metadata_file = session_path / "metadata.json"
        
        self.csv_file = None
        self.csv_writer = None
        self.start_time = None
        self.message_count = 0
        self.metadata = {}
        
    def start(self, metadata: dict):
        """Inicia el logging de la sesión."""
        self.start_time = datetime.now()
        self.metadata = metadata
        self.metadata['start_time'] = self.start_time.isoformat()
        
        # Crear CSV con headers
        self.csv_file = open(self.telemetry_file, 'w', newline='')
        self.csv_writer = csv.writer(self.csv_file)
        self.csv_writer.writerow([
            'timestamp', 'mode', 'gait_type', 'foot_raise_height',
            'pos_x', 'pos_y', 'pos_z', 'body_height',
            'vel_x', 'vel_y', 'vel_z', 'yaw_speed'
        ])
        
        print(f"✅ Sesión iniciada: {self.session_path.name}")
        print(f"📁 Guardando en: {self.session_path}")
        
    def log_state(self, msg: SportModeState_):
        """Callback para guardar estado del robot."""
        if self.csv_writer is None:
            return
            
        timestamp = (datetime.now() - self.start_time).total_seconds()
        
        self.csv_writer.writerow([
            timestamp,
            msg.mode,
            msg.gait_type,
            msg.foot_raise_height,
            msg.position[0], msg.position[1], msg.position[2],
            msg.body_height,
            msg.velocity[0], msg.velocity[1], msg.velocity[2],
            msg.yaw_speed
        ])
        
        self.message_count += 1
        
        # Mostrar progreso cada 100 mensajes
        if self.message_count % 100 == 0:
            print(f"   📊 Registros guardados: {self.message_count} ({timestamp:.1f}s)")
    
    def stop(self):
        """Finaliza el logging y guarda metadata."""
        if self.csv_file:
            self.csv_file.close()
            
        end_time = datetime.now()
        duration = (end_time - self.start_time).total_seconds()
        
        # Actualizar metadata
        self.metadata['end_time'] = end_time.isoformat()
        self.metadata['duration_seconds'] = duration
        self.metadata['total_records'] = self.message_count
        
        # Guardar metadata
        with open(self.metadata_file, 'w') as f:
            json.dump(self.metadata, f, indent=2)
        
        # Crear README
        readme_path = self.session_path / "README.md"
        with open(readme_path, 'w') as f:
            f.write(f"# Sesión: {self.metadata['session_name']}\n\n")
            f.write(f"- **Robot:** {self.metadata['robot_type']}\n")
            f.write(f"- **Inicio:** {self.metadata['start_time']}\n")
            f.write(f"- **Duración:** {duration:.1f} segundos\n")
            f.write(f"- **Registros:** {self.message_count}\n")
            if 'operator' in self.metadata:
                f.write(f"- **Operador:** {self.metadata['operator']}\n")
            f.write(f"\n## Archivos\n\n")
            f.write(f"- `telemetry.csv` - Datos de telemetría\n")
            f.write(f"- `metadata.json` - Metadatos de la sesión\n")
            f.write(f"- `commands.log` - Log de comandos (si aplica)\n")
        
        print(f"\n✅ Sesión finalizada")
        print(f"   ⏱️  Duración: {duration:.1f} segundos")
        print(f"   📊 Registros guardados: {self.message_count}")
        print(f"   📁 Archivos creados:")
        print(f"      - {self.telemetry_file.name}")
        print(f"      - {self.metadata_file.name}")
        print(f"      - {readme_path.name}")

def main():
    # Cargar .env
    project_root = Path(__file__).parent.parent
    load_dotenv(project_root / ".env")
    
    # Parsear argumentos
    parser = argparse.ArgumentParser(description="Grabar sesión de telemetría")
    parser.add_argument("--session", 
                       help="Nombre de sesión (YYYYMMDD_HHMM_ROBOT_MATERIA_GRUPO)")
    parser.add_argument("--duration", type=int, default=30,
                       help="Duración en segundos (default: 30)")
    parser.add_argument("--materia", default="Demo",
                       help="Nombre de la materia (default: Demo)")
    parser.add_argument("--grupo", default="Test",
                       help="Nombre del grupo (default: Test)")
    parser.add_argument("--operator", default="Usuario",
                       help="Nombre del operador")
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("G1/Go2 Lab Kit - Log Session")
    print("=" * 60)
    
    # Generar o usar nombre de sesión
    robot_type = os.getenv("ROBOT_TYPE", "g1")
    
    if args.session:
        session_name = args.session
    else:
        session_name = generate_session_name(
            robot_type=robot_type,
            materia=args.materia,
            grupo=args.grupo
        )
    
    # Crear path de sesión
    session_path = project_root / "data" / "local" / "sessions" / session_name
    
    # Preparar metadata
    metadata = {
        'session_name': session_name,
        'robot_type': robot_type,
        'robot_ip': os.getenv("ROBOT_IP", "unknown"),
        'materia': args.materia,
        'grupo': args.grupo,
        'operator': args.operator,
        'lab_location': 'Local'
    }
    
    # Inicializar logger
    logger = SessionLogger(session_path)
    
    try:
        # Conectar al robot
        print(f"\n🔴 Conectando al robot...")
        ChannelFactoryInitialize(0)
        
        # Iniciar sesión
        logger.start(metadata)
        
        # Suscribirse a telemetría
        subscriber = ChannelSubscriber("rt/sportmodestate", SportModeState_)
        subscriber.Init(logger.log_state, 10)
        
        print(f"⏱️  Grabando durante {args.duration} segundos...")
        print("   (Presiona Ctrl+C para detener antes)\n")
        
        # Grabar durante el tiempo especificado
        time.sleep(args.duration)
        
        # Finalizar
        logger.stop()
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Grabación interrumpida por el usuario")
        logger.stop()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        if logger.csv_file:
            logger.stop()
        return False
    
    return True

if __name__ == "__main__":
    main()
