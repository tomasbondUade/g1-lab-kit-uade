"""
05_replay_demo.py
=================
Objetivo: Cargar y mostrar datos de una sesión grabada (modo replay).

Modo: Replay ONLY (no requiere robot)

Uso:
    python examples/05_replay_demo.py [session_name]
    
    Si no se provee session_name, usa la sesión de ejemplo en data/samples/

Salida esperada:
    - Metadata de la sesión
    - Primeros registros de telemetría
    - Comandos ejecutados
    - Estadísticas básicas
"""

import sys
from pathlib import Path

# Agregar src al path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.replay.loader import load_session, list_sessions


def main():
    print("=" * 60)
    print("G1/Go2 Lab Kit - Replay Demo")
    print("=" * 60)
    
    # Parsear argumentos
    if len(sys.argv) > 1:
        session_name = sys.argv[1]
        # Buscar primero en local, luego en samples
        session_path = project_root / "data" / "local" / "sessions" / session_name
        if not session_path.exists():
            session_path = project_root / "data" / "samples" / "sessions" / session_name
    else:
        # Buscar sesiones primero en local, luego en samples
        local_dir = project_root / "data" / "local" / "sessions"
        samples_dir = project_root / "data" / "samples" / "sessions"
        
        sessions = list_sessions(local_dir)
        if not sessions:
            sessions = list_sessions(samples_dir)
        
        if not sessions:
            print("✗ No hay sesiones disponibles")
            print("\n💡 Opciones:")
            print("  1. Graba una sesión: python examples/03_log_session.py")
            print("  2. Especifica una sesión: python examples/05_replay_demo.py [nombre_sesion]")
            sys.exit(1)
        
        session_path = sessions[0]
        session_name = sessions[0].name
    
    print(f"\n[1] Cargando sesión: {session_name}")
    
    # Validar que existe
    if not session_path.exists():
        print(f"✗ Sesión no encontrada: {session_name}")
        print(f"  Buscado en: {session_path}")
        print("\n💡 Sesiones disponibles:")
        
        # Listar sesiones disponibles
        for dir_path in [project_root / "data" / "local" / "sessions",
                         project_root / "data" / "samples" / "sessions"]:
            sessions = list_sessions(dir_path)
            if sessions:
                print(f"\n  En {dir_path.relative_to(project_root)}:")
                for s in sessions:
                    print(f"    - {s.name}")
        sys.exit(1)
    
    # Cargar sesión
    try:
        session = load_session(session_path)
        print(f"✓ Sesión cargada correctamente")
    except Exception as e:
        print(f"✗ Error al cargar sesión: {e}")
        sys.exit(1)
    
    # Mostrar metadata
    print("\n[2] Metadata de la sesión:")
    print("-" * 60)
    metadata = session.get_metadata()
    for key, value in metadata.items():
        print(f"  {key:20s}: {value}")
    
    # Cargar telemetría
    print("\n[3] Telemetría:")
    print("-" * 60)
    df = session.get_telemetry()
    
    if df is not None and len(df) > 0:
        print(f"  Total de registros: {len(df)}")
        print(f"  Columnas: {', '.join(df.columns.tolist())}")
        print(f"\n  Primeras 5 filas:")
        print(df.head().to_string(index=False))
        
        print(f"\n  Estadísticas básicas (posición):")
        if 'pos_x' in df.columns:
            stats = df[['pos_x', 'pos_y', 'pos_z', 'body_height']].describe()
            print(stats.to_string())
    else:
        print("  ⚠ No hay datos de telemetría disponibles")
    
    # Mostrar comandos
    print("\n[4] Comandos ejecutados:")
    print("-" * 60)
    commands = session.get_commands()
    
    if commands:
        for cmd in commands[:10]:  # Primeros 10
            print(f"  [{cmd['timestamp']}] {cmd['event']}")
            if cmd['details']:
                print(f"      {cmd['details']}")
        if len(commands) > 10:
            print(f"  ... y {len(commands) - 10} más")
    else:
        print("  ⚠ No hay comandos registrados")
    
    # Resumen
    print("\n[5] Resumen:")
    print("-" * 60)
    duration_seconds = metadata.get('duration_seconds', 0)
    total_records = metadata.get('total_records', len(df) if df is not None else 0)
    
    print(f"  Duración total: {duration_seconds:.1f} segundos ({duration_seconds/60:.2f} minutos)")
    print(f"  Robot: {metadata.get('robot_type', 'N/A').upper()}")
    print(f"  Registros totales: {total_records}")
    if duration_seconds > 0 and total_records > 0:
        print(f"  Frecuencia: ~{total_records/duration_seconds:.0f} Hz")
    
    if 'operator' in metadata:
        print(f"  Operador: {metadata['operator']}")
    if 'materia' in metadata:
        print(f"  Materia: {metadata['materia']} - Grupo: {metadata.get('grupo', 'N/A')}")
    
    print("\n" + "=" * 60)
    print("✓ Replay completado exitosamente")
    print("\n💡 Para análisis más detallado:")
    print(f"  - Jupyter: notebooks/01_replay_analysis.ipynb")
    print(f"  - CSV directo: {session_path / 'telemetry.csv'}")
    print("=" * 60)


if __name__ == "__main__":
    main()
    main()
