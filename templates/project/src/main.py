"""
main.py
=======
Punto de entrada del proyecto.

Uso:
    python src/main.py --mode replay --session data/sessions/ejemplo
    python src/main.py --mode live
"""

import argparse
import sys
from pathlib import Path

# Agregar src/ al path si es necesario
sys.path.insert(0, str(Path(__file__).parent.parent))

# TODO: Importar módulos del lab kit
# from src.config import load_config
# from src.robot import RobotConnection
# from src.logging import SessionLogger


def parse_args():
    """Parse argumentos de línea de comandos."""
    parser = argparse.ArgumentParser(
        description="[Nombre del proyecto]"
    )
    
    parser.add_argument(
        "--mode",
        choices=["replay", "live"],
        default="replay",
        help="Modo de ejecución (replay sin robot, live con robot)"
    )
    
    parser.add_argument(
        "--session",
        type=str,
        help="Path a sesión (solo modo replay)"
    )
    
    parser.add_argument(
        "--duration",
        type=int,
        default=10,
        help="Duración en segundos (solo modo live)"
    )
    
    return parser.parse_args()


def main():
    """Función principal."""
    args = parse_args()
    
    print("=" * 50)
    print("[NOMBRE DEL PROYECTO]")
    print("=" * 50)
    print(f"Modo: {args.mode}")
    
    # TODO: Implementar lógica del proyecto
    
    if args.mode == "replay":
        print("\nModo REPLAY (sin robot)")
        if args.session:
            print(f"Sesión: {args.session}")
            # TODO: Cargar sesión
            # session = load_session(Path(args.session))
            # TODO: Procesar datos
        else:
            print("ERROR: --session requerido en modo replay")
            return 1
    
    elif args.mode == "live":
        print("\nModo LIVE (con robot)")
        print("⚠️  REQUIERE protocolo de seguridad completo")
        print(f"Duración: {args.duration}s")
        
        # TODO: Conectar al robot
        # config = load_config()
        # robot = RobotConnection(config)
        # robot.connect()
        
        # TODO: Ejecutar operación
        
        # TODO: Desconectar
        # robot.disconnect()
    
    print("\n[TODO] Implementar lógica del proyecto")
    return 0


if __name__ == "__main__":
    sys.exit(main())
