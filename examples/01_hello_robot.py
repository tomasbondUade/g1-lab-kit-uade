"""
01_hello_robot.py
=================
Objetivo: Validar que el kit está operativo (entorno + SDK + paths) y mostrar configuración básica.

Modo: Replay (OK) / Live (opcional)

Uso:
    python examples/01_hello_robot.py

Salida esperada:
    - Confirmación de .env cargado
    - Confirmación de SDK detectado
    - Configuración básica (tipo de robot, IP si aplica)
"""

# TODO: Implementar validación del entorno
# - Cargar .env con python-dotenv
# - Verificar que existe unitree_sdk2py
# - Mostrar ROBOT_TYPE y ROBOT_IP (si está configurado)
# - Validar que existan carpetas config/, data/, third_party/

def main():
    print("=" * 50)
    print("G1/Go2 Lab Kit - Hello Robot")
    print("=" * 50)
    
    # TODO: Cargar .env
    # from dotenv import load_dotenv
    # import os
    # load_dotenv()
    # robot_type = os.getenv("ROBOT_TYPE", "No configurado")
    
    # TODO: Verificar SDK
    # try:
    #     import unitree_sdk2py
    #     print("✓ SDK detectado")
    # except ImportError:
    #     print("✗ SDK no encontrado")
    
    # TODO: Mostrar configuración
    # print(f"Tipo de robot: {robot_type}")
    # print(f"IP del robot: {os.getenv('ROBOT_IP', 'No configurado')}")
    
    print("\n[TODO] Este ejemplo está pendiente de implementación.")
    print("Ver: examples/README.md para más información.")

if __name__ == "__main__":
    main()
