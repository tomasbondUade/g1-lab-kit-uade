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

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

def main():
    print("=" * 60)
    print("G1/Go2 Lab Kit - Hello Robot")
    print("=" * 60)
    
    # Obtener path del proyecto (directorio raíz)
    project_root = Path(__file__).parent.parent
    env_file = project_root / ".env"
    
    # 1. Cargar .env
    print("\n📋 Cargando configuración...")
    if env_file.exists():
        load_dotenv(env_file)
        print(f"   ✓ Archivo .env encontrado: {env_file}")
    else:
        print(f"   ⚠️  Archivo .env no encontrado en: {env_file}")
        print(f"   💡 Copia .env.example a .env y configúralo")
    
    # 2. Verificar SDK
    print("\n🔧 Verificando Unitree SDK...")
    try:
        import unitree_sdk2py
        sdk_path = Path(unitree_sdk2py.__file__).parent
        print(f"   ✓ SDK detectado: {sdk_path}")
    except ImportError:
        print("   ✗ SDK no encontrado")
        print("   💡 Instala el SDK desde third_party/unitree_sdk2_python/")
        sys.exit(1)
    
    # 3. Mostrar configuración
    print("\n⚙️  Configuración actual:")
    robot_type = os.getenv("ROBOT_TYPE", "No configurado")
    robot_ip = os.getenv("ROBOT_IP", "No configurado")
    data_mode = os.getenv("DATA_MODE", "No configurado")
    network_interface = os.getenv("NETWORK_INTERFACE", "No configurado")
    
    print(f"   Tipo de robot:     {robot_type}")
    print(f"   IP del robot:      {robot_ip}")
    print(f"   Modo de datos:     {data_mode}")
    print(f"   Interfaz de red:   {network_interface}")
    
    # 4. Validar estructura de carpetas
    print("\n📁 Validando estructura del proyecto...")
    required_folders = ["config", "data", "third_party", "src", "examples"]
    all_exist = True
    
    for folder in required_folders:
        folder_path = project_root / folder
        if folder_path.exists():
            print(f"   ✓ {folder}/")
        else:
            print(f"   ✗ {folder}/ (no encontrado)")
            all_exist = False
    
    # 5. Resumen
    print("\n" + "=" * 60)
    if all_exist and env_file.exists():
        print("✅ Todo listo! El kit está configurado correctamente.")
        print("\n💡 Próximos pasos:")
        print("   - Ejecuta: python examples/02_telemetry_check.py")
        print("   - Para modo live: asegúrate que el robot esté conectado")
    else:
        print("⚠️  Hay algunos problemas de configuración.")
        print("   Revisa los mensajes anteriores.")
    print("=" * 60)

if __name__ == "__main__":
    main()
