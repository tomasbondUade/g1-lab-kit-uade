# Examples — G1/Go2 Lab Kit

Estos ejemplos son el "punto de entrada" para actividades de clase.
Cada ejemplo intenta ser:
- simple
- reproducible
- seguro (cuando hay robot real)

## Requisitos previos
- Instalación completada: `docs/01_instalacion_windows.md`
- Red Ethernet configurada: `docs/02_configuracion_red.md`
- Primera prueba realizada: `docs/03_primer_ejecucion_y_pruebas.md`
- Protocolo de seguridad: `docs/04_seguridad_operacion_aula.md`

## Modos de ejecución
- **Replay (sin robot):** usa datos en `data/samples/`
- **Live (con robot):** requiere Ethernet + checklist LSP + operador/observador

## Variables esperadas (.env)
- `ROBOT_TYPE=G1` o `GO2`
- `ROBOT_IP=<ip_del_robot>` (solo live)
- `SESSION_NAME=YYYYMMDD_HHMM_ROBOT_MATERIA_GRUPO` (recomendado)
- `DATA_MODE=replay` o `live` (opcional, si lo implementamos)

---

## Ejemplos disponibles

### 01_hello_robot.py ✅
**Objetivo:** validar que el kit está operativo (entorno + SDK + paths).

**Uso:**
```powershell
python examples/01_hello_robot.py
```

**Salida esperada:** 
- Confirmación de .env cargado
- SDK detectado con path completo
- Configuración actual (ROBOT_TYPE, ROBOT_IP, DATA_MODE, NETWORK_INTERFACE)
- Validación de estructura de carpetas (config/, data/, src/, examples/, third_party/)

**Estado:** ✅ Funcional - Probado con Go2

---

### 02_telemetry_check.py ✅
**Objetivo:** verificar lectura de telemetría en tiempo real.

**Uso:**
```powershell
# Modo live (con robot)
python examples/02_telemetry_check.py --mode live

# Modo replay (con sesión grabada)
python examples/02_telemetry_check.py --mode replay --sample data/samples/sessions/example_session
```

**Salida esperada (live):**
- Monitor en tiempo real que se actualiza cada 0.5s
- Estado general (modo, gait_type, mensajes recibidos)
- Posición (x, y, z)
- Orientación (body height)
- Velocidad (lineal y angular)
- Frecuencia: ~300 Hz

**Estado:** ✅ Funcional - Probado con Go2  
**Nota:** Se configura CycloneDDS automáticamente para evitar error de log en Windows

---

### 03_log_session.py ✅
**Objetivo:** grabar sesiones de telemetría con naming estándar.

**Uso:**
```powershell
# Grabar 30 segundos (por defecto)
python examples/03_log_session.py --materia Robotica --grupo G1 --operator "Tu Nombre"

# Especificar duración
python examples/03_log_session.py --duration 60 --materia Prog1 --grupo G3

# Usar nombre custom
python examples/03_log_session.py --session 20260123_1000_GO2_Test_Demo
```

**Salida:**
- Carpeta en `data/local/sessions/YYYYMMDD_HHMM_ROBOT_MATERIA_GRUPO/`
- `telemetry.csv` - Datos de telemetría (~300 registros/segundo)
- `metadata.json` - Información completa de la sesión
- `README.md` - Documentación generada automáticamente

**Estado:** ✅ Funcional - Probado con Go2 (3001 registros en 10s)

---

### 04_safe_stop.py ✅
**Objetivo:** probar parada segura del robot.

**Uso:**
```powershell
# Modo replay (simulación - sin robot)
python examples/04_safe_stop.py --mode replay

# Modo live (con robot - REQUIERE CONFIRMACIÓN)
python examples/04_safe_stop.py --mode live --confirm
```

**Modo Live - Protocolo de seguridad:**
1. Requiere flag `--confirm` (valida lectura de protocolo)
2. Verificación de perímetro despejado
3. Confirmación manual antes de ejecutar
4. Comando StandUp -> cuenta regresiva 3-2-1 -> DAMP
5. Log automático guardado en `data/local/safety_logs/`

**Salida:**
- Tiempo de respuesta del comando
- Estado final del robot
- Log de seguridad con timestamp

**Estado:** ✅ Funcional - Probado en ambos modos  
> ⚠️ **ADVERTENCIA:** Modo live solo bajo supervisión y con protocolo completo

---

### 05_replay_demo.py ✅
**Objetivo:** analizar sesiones grabadas sin necesidad de robot.

**Uso:**
```powershell
# Analizar última sesión grabada
python examples/05_replay_demo.py

# Analizar sesión específica
python examples/05_replay_demo.py 20260123_1638_GO2_Robotica_G1
```

**Salida esperada:**
1. **Metadata de la sesión:** Nombre, robot, operador, tiempos, duración
2. **Telemetría:** Total de registros, columnas disponibles, primeras 5 filas
3. **Estadísticas:** Min/max/mean/std de posición y altura
4. **Comandos:** Log de comandos ejecutados durante la sesión
5. **Resumen:** Duración, frecuencia de muestreo, materia, grupo

**Estado:** ✅ Funcional - Carga sesiones de `data/local/` o `data/samples/`  
**Ejemplo real:** Analiza sesión con 3001 registros @298Hz en 10.1 segundos

---

## Convención de nombres (sesión/log)
`YYYYMMDD_HHMM_ROBOT_MATERIA_GRUPO`

Ej: `20260120_1030_G1_Prog1_G3`

## Soporte
Si algo falla, consultar:
- `docs/05_troubleshooting.md`
y adjuntar el error completo + capturas.
---

## 🐛 Errores comunes y soluciones

### Error: "cannot open for writing /tmp/cdds.LOG"
**Causa:** CycloneDDS intenta escribir en ruta Linux en Windows  
**Solución:** Los ejemplos 02, 03 y 04 configuran automáticamente:
```python
os.environ['CYCLONEDDS_URI'] = '<CycloneDDS><Domain><Id>0</Id></Domain><Tracing><Verbosity>none</Verbosity></Tracing></CycloneDDS>'
```

### Error: "ModuleNotFoundError: No module named 'dotenv'"
**Causa:** Falta instalar python-dotenv  
**Solución:**
```powershell
pip install python-dotenv
```

### Error: "Import 'unitree_sdk2py' could not be resolved"
**Causa:** VSCode usando Python global en vez del entorno virtual  
**Solución:**
1. Ctrl+Shift+P → "Python: Select Interpreter"
2. Seleccionar `env\Scripts\python.exe`
3. Recargar ventana si es necesario

### Robot no responde / "channel factory init error"
**Solución probada:**
- **NO especificar IP** en `ChannelFactoryInitialize(0)` - usa broadcast
- Verificar conexión: `ping 192.168.123.18`
- Reiniciar el robot si es necesario
- Asegurar que no hay firewall bloqueando DDS

### Frecuencia de telemetría baja
**Esperado:** ~300 Hz (298-300 registros/segundo)  
Si es menor:
- Verificar latencia de red: `ping -n 100 192.168.123.18`
- Cerrar aplicaciones que usen red intensivamente
- Usar cable Ethernet de calidad (Cat 6 recomendado)