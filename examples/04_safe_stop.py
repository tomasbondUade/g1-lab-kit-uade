"""
04_safe_stop.py
===============
Objetivo: Probar el stop seguro en condiciones controladas.

⚠️ REQUIERE:
   - Protocolo de seguridad completo (docs/04_seguridad_operacion_aula.md)
   - Checklist LSP aprobado
   - Operador + Observador
   - Perímetro despejado
   - Token de control

Modo: Replay (simula stop) / Live (prueba stop real - SOLO OPERADOR)

Uso:
    # Replay (sin robot)
    python examples/04_safe_stop.py --mode replay
    
    # Live (con robot) - SOLO BAJO SUPERVISIÓN
    python examples/04_safe_stop.py --mode live --confirm

Salida esperada:
    - Confirmación de stop ejecutado
    - Tiempo de respuesta
    - Estado final del robot
"""

import os
import sys
import time
import argparse
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

# Configurar CycloneDDS
os.environ['CYCLONEDDS_URI'] = '<CycloneDDS><Domain><Id>0</Id></Domain><Tracing><Verbosity>none</Verbosity></Tracing></CycloneDDS>'

from unitree_sdk2py.core.channel import ChannelFactoryInitialize
from unitree_sdk2py.go2.sport.sport_client import SportClient

def log_test(test_name: str, success: bool, response_time: float, notes: str = ""):
    """Guarda log del test de seguridad."""
    project_root = Path(__file__).parent.parent
    log_dir = project_root / "data" / "local" / "safety_logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = log_dir / f"safe_stop_{timestamp}.log"
    
    with open(log_file, 'w') as f:
        f.write(f"Safe Stop Test Log\n")
        f.write(f"{'=' * 60}\n")
        f.write(f"Test: {test_name}\n")
        f.write(f"Timestamp: {datetime.now().isoformat()}\n")
        f.write(f"Success: {success}\n")
        f.write(f"Response Time: {response_time:.3f}s\n")
        if notes:
            f.write(f"Notes: {notes}\n")
        f.write(f"{'=' * 60}\n")
    
    print(f"   📝 Log guardado: {log_file.name}")

def test_safe_stop_replay():
    """Simula un test de safe stop sin robot real."""
    print("\n📼 MODO REPLAY - Simulando safe stop...")
    
    print("\n1️⃣  Verificando protocolo de seguridad...")
    time.sleep(0.5)
    print("   ✅ Checklist LSP: OK (simulado)")
    print("   ✅ Roles definidos: Operador + Observador")
    print("   ✅ Perímetro despejado: OK")
    
    print("\n2️⃣  Ejecutando comando de stop...")
    start_time = time.time()
    time.sleep(0.1)  # Simular latencia
    response_time = time.time() - start_time
    print(f"   ✅ Stop ejecutado en {response_time:.3f}s")
    
    print("\n3️⃣  Verificando estado final...")
    time.sleep(0.3)
    print("   ✅ Robot en modo Damp")
    print("   ✅ Motores desactivados")
    print("   ✅ Sistema seguro")
    
    log_test("Replay Safe Stop", True, response_time, "Simulación exitosa")
    
    return True

def test_safe_stop_live(sport_client: SportClient):
    """Ejecuta un test real de safe stop con el robot."""
    print("\n🔴 MODO LIVE - Test real de safe stop")
    
    print("\n⚠️  VERIFICACIONES PREVIAS:")
    print("   □ ¿Perímetro despejado?")
    print("   □ ¿Observador en posición?")
    print("   □ ¿Robot en posición estable?")
    print("   □ ¿Listo para emergency stop?")
    
    confirm = input("\n¿Confirmar ejecución? (escriba 'SI' para continuar): ")
    if confirm.upper() != "SI":
        print("❌ Test cancelado por el usuario")
        return False
    
    print("\n1️⃣  Preparando robot...")
    try:
        # Asegurar que el robot está en un estado conocido
        print("   Enviando comando: StandUp")
        sport_client.StandUp()
        time.sleep(2)
        print("   ✅ Robot preparado")
        
        print("\n2️⃣  Ejecutando SAFE STOP en 3 segundos...")
        for i in range(3, 0, -1):
            print(f"   {i}...")
            time.sleep(1)
        
        # Ejecutar stop
        start_time = time.time()
        print("   🛑 Ejecutando DAMP (safe stop)")
        sport_client.Damp()
        response_time = time.time() - start_time
        
        print(f"\n✅ Stop ejecutado en {response_time:.3f}s")
        
        print("\n3️⃣  Verificando estado final...")
        time.sleep(1)
        print("   ✅ Comando completado")
        print("   ℹ️  Verifica visualmente que el robot esté en modo relajado")
        
        log_test("Live Safe Stop", True, response_time, "Test exitoso con robot real")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Error durante el test: {e}")
        log_test("Live Safe Stop", False, 0.0, f"Error: {e}")
        return False

def main():
    # Cargar .env
    project_root = Path(__file__).parent.parent
    load_dotenv(project_root / ".env")
    
    # Parsear argumentos
    parser = argparse.ArgumentParser(
        description="Test de safe stop para robot",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
⚠️  ADVERTENCIA DE SEGURIDAD:
   El modo live ejecuta comandos reales en el robot.
   Solo usar bajo supervisión y con protocolo completo.
   
   Ver: docs/04_seguridad_operacion_aula.md
        """
    )
    parser.add_argument("--mode", 
                       choices=["replay", "live"], 
                       default="replay",
                       help="Modo de operación")
    parser.add_argument("--confirm", 
                       action="store_true",
                       help="Confirmar protocolo de seguridad (requerido para live)")
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("🛑 G1/Go2 Lab Kit - Safe Stop Test")
    print("=" * 60)
    
    # Validaciones de seguridad
    if args.mode == "live":
        print("\n⚠️  MODO LIVE ACTIVADO")
        
        if not args.confirm:
            print("\n❌ ERROR: Debes confirmar el protocolo de seguridad")
            print("   Usa: --confirm para confirmar que:")
            print("   - Has leído docs/04_seguridad_operacion_aula.md")
            print("   - Tienes un observador asignado")
            print("   - El perímetro está despejado")
            print("   - El robot está en condiciones seguras")
            sys.exit(1)
        
        print("\n✅ Protocolo de seguridad confirmado")
        
        # Conectar al robot
        try:
            print("📡 Conectando al robot...")
            ChannelFactoryInitialize(0)
            
            sport_client = SportClient()
            sport_client.SetTimeout(5.0)
            sport_client.Init()
            
            print("✅ Conectado al robot\n")
            
            # Ejecutar test live
            success = test_safe_stop_live(sport_client)
            
        except Exception as e:
            print(f"\n❌ Error de conexión: {e}")
            print("💡 Verifica que el robot esté encendido y conectado")
            sys.exit(1)
    
    else:
        # Modo replay (simulación)
        success = test_safe_stop_replay()
    
    # Resumen
    print("\n" + "=" * 60)
    if success:
        print("✅ TEST COMPLETADO EXITOSAMENTE")
    else:
        print("❌ TEST FALLÓ")
    print("=" * 60)

if __name__ == "__main__":
    main()
