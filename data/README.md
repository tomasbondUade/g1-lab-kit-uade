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

## Contenido recomendado por sesión
- `telemetry.csv` (o .parquet)
- `events.json` (si aplica)
- `metadata.json` (operador, objetivo, etc.)
