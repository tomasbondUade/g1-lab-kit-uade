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

# TODO: Implementar lectura de telemetría
# - Modo replay: cargar CSV/parquet de data/samples/
# - Modo live: suscribirse a topics del robot (usando unitree_sdk2py)
# - Mostrar valores en tiempo real o estadísticas

def main():
    print("=" * 50)
    print("G1/Go2 Lab Kit - Telemetry Check")
    print("=" * 50)
    
    # TODO: Parsear argumentos
    # import argparse
    # parser = argparse.ArgumentParser()
    # parser.add_argument("--mode", choices=["replay", "live"], default="replay")
    # parser.add_argument("--sample", help="Path to sample session (replay mode)")
    # args = parser.parse_args()
    
    # TODO: Si mode=replay
    #   - Cargar telemetry.csv de la sesión sample
    #   - Mostrar estadísticas (pandas.describe())
    
    # TODO: Si mode=live
    #   - Conectar al robot (usar módulo de src/ cuando exista)
    #   - Suscribirse a telemetría
    #   - Mostrar valores en loop (Ctrl+C para salir)
    
    print("\n[TODO] Este ejemplo está pendiente de implementación.")
    print("Ver: examples/README.md para más información.")

if __name__ == "__main__":
    main()
