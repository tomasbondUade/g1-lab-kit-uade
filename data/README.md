# data/

Esta carpeta se usa para almacenar datos de prueba y datos locales.

## Regla principal
- **data/local/**: datos reales de uso en clases (logs, videos, etc.) → **NO se versionan**
- **data/samples/**: datos de ejemplo pequeños y anónimos → **SÍ se versionan** (para modo replay)

## Estructura
- `samples/`:
  - sesiones pequeñas para pruebas rápidas
  - deben ser livianas y no contener datos sensibles
- `local/`:
  - sesiones reales del día a día
  - cada sesión debe usar naming estándar: `YYYYMMDD_HHMM_ROBOT_MATERIA_GRUPO`

## Naming estándar
`YYYYMMDD_HHMM_ROBOT_MATERIA_GRUPO`

Ej: `20260120_1030_G1_Prog1_G3`

## Contenido generado por sesión

Cada sesión de grabación (`examples/03_log_session.py`) crea automáticamente:

### Archivos obligatorios:
- **`telemetry.csv`** - Datos de telemetría en formato CSV
  - Columnas: timestamp, mode, gait_type, foot_raise_height, pos_x, pos_y, pos_z, body_height, vel_x, vel_y, vel_z, yaw_speed
  - Frecuencia típica: ~298-300 Hz (registros por segundo)
  
- **`metadata.json`** - Información de la sesión
  ```json
  {
    "session_name": "20260123_1638_GO2_Robotica_G1",
    "robot_type": "go2",
    "robot_ip": "192.168.123.18",
    "materia": "Robotica",
    "grupo": "G1",
    "operator": "TBond",
    "start_time": "2026-01-23T16:38:36.930303",
    "end_time": "2026-01-23T16:38:46.990566",
    "duration_seconds": 10.060263,
    "total_records": 3001
  }
  ```

- **`README.md`** - Documentación generada automáticamente
  - Resumen de la sesión
  - Estadísticas básicas
  - Lista de archivos

### Archivos opcionales:
- **`commands.log`** - Log de comandos ejecutados (si aplica)

## Ejemplo de sesión real

Ubicación: `data/local/sessions/20260123_1638_GO2_Robotica_G1/`
- 3001 registros de telemetría
- 10.1 segundos de duración
- Frecuencia: 298 Hz
- Robot: Go2
- Operador: TBond

Analizar con: `python examples/05_replay_demo.py 20260123_1638_GO2_Robotica_G1`
