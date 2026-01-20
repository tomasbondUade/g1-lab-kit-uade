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
        session_path = project_root / "data" / "local" / "sessions" / session_name
        if not session_path.exists():
            session_path = project_root / "data" / "samples" / "sessions" / session_name
    else:
        # Usar primera sesión de samples
        samples_dir = project_root / "data" / "samples" / "sessions"
        sessions = list_sessions(samples_dir)
        if not sessions:
            print("✗ No hay sesiones disponibles en data/samples/sessions/")
            print("\nCrea una sesión o usa:")
            print("  python examples/05_replay_demo.py [nombre_sesion]")
            sys.exit(1)
        session_path = sessions[0]
        session_name = sessions[0].name
    
    print(f"\n[1] Cargando sesión: {session_name}")
    
    # Validar que existe
    if not session_path.exists():
        print(f"✗ Sesión no encontrada: {session_name}")
        print(f"  Buscado en: {session_path}")
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
        
        print(f"\n  Estadísticas básicas:")
        print(df.describe().to_string())
    else:
        print("  ⚠ No hay datos de telemetría disponibles")
    
    # Mostrar comandos
    print("\n[4] Comandos ejecutados:")
    print("-" * 60)
    commands = session.get_commands()
    
    if commands:
        for cmd in commands[:10]:  # Primeros 10
            print(f"  {cmd}")
        if len(commands) > 10:
            print(f"  ... y {len(commands) - 10} más")
    else:
        print("  ⚠ No hay comandos registrados")
    
    # Resumen
    print("\n[5] Resumen:")
    print("-" * 60)
    duration = session.duration()
    if duration:
        print(f"  Duración total: {metadata.get('duration_seconds', 'N/A')} segundos ({duration:.1f} minutos)")
    else:
        print(f"  Duración total: N/A")
    print(f"  Robot: {metadata.get('robot_type', 'N/A').upper()}")
    print(f"  Nivel de riesgo: {metadata.get('risk_level', 'N/A')}")
    
    print("\n" + "=" * 60)
    print("✓ Replay completado exitosamente")
    print("\nPara análisis más detallado, usa:")
    print(f"  notebooks/01_replay_analysis.ipynb")
    print("=" * 60)


if __name__ == "__main__":
    main()
# - Opcional: graficar (matplotlib)

def main():
    print("=" * 50)
    print("G1/Go2 Lab Kit - Replay Demo")
    print("=" * 50)
    
    # TODO: Parsear argumentos
    # import argparse
    # parser = argparse.ArgumentParser()
    # parser.add_argument("--session", default="data/samples/sessions/example_session",
    #                     help="Path to session directory")
    # args = parser.parse_args()
    
    # TODO: Validar que existe la sesión
    # from pathlib import Path
    # session_path = Path(args.session)
    # if not session_path.exists():
    #     print(f"ERROR: Sesión no encontrada: {args.session}")
    #     return
    
    # TODO: Cargar metadata.json
    # import json
    # with open(session_path / "metadata.json") as f:
    #     metadata = json.load(f)
    # print(f"\nSesión: {metadata.get('session_name', 'N/A')}")
    # print(f"Robot: {metadata.get('robot_type', 'N/A')}")
    # print(f"Operador: {metadata.get('operator', 'N/A')}")
    
    # TODO: Cargar telemetry.csv
    # import pandas as pd
    # telemetry = pd.read_csv(session_path / "telemetry.csv")
    # print(f"\nDuración: {telemetry['timestamp'].max() - telemetry['timestamp'].min()} s")
    # print("\nEstadísticas:")
    # print(telemetry.describe())
    
    # TODO: Opcional - graficar
    # import matplotlib.pyplot as plt
    # telemetry.plot(x="timestamp", y="battery", title="Batería")
    # plt.show()
    
    print("\n[TODO] Este ejemplo está pendiente de implementación.")
    print("Ver: examples/README.md para más información.")
    print("\nEste ejemplo NO requiere robot - solo data/samples/")

if __name__ == "__main__":
    main()
