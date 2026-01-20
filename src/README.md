# src — G1/Go2 Lab Kit

Módulos reutilizables de Python para el Lab Kit.

## Estructura

```
src/
  config/       # Carga de configuración (YAML + .env)
  robot/        # Conexión y comunicación con robot
  safety/       # Límites de seguridad, deadman, safe stop
  logging/      # Logging de sesiones con naming estándar
  replay/       # Carga y análisis de sesiones grabadas
  utils/        # Utilidades varias
```

## Uso

Los módulos en `src/` son importados por:
- **examples/** (scripts de validación y control)
- **notebooks/** (análisis interactivo)
- **tests/** (cuando se implementen)

### Ejemplo de uso:

```python
from src.config import load_config
from src.robot import RobotConnection
from src.logging import SessionLogger

# Cargar configuración
config = load_config()

# Conectar al robot (si live)
if config.data_mode == "live":
    robot = RobotConnection(config)
    robot.connect()
    
    # Iniciar logging
    logger = SessionLogger(config)
    logger.start()
```

## Estado actual

**✓ Estructura:** Definida
**⏳ Implementación:** Pendiente (stubs con TODOs)

### Orden recomendado de implementación:

1. **src/config/** - Base para todo (carga .env y YAML)
2. **src/utils/** - Naming, validaciones básicas
3. **src/replay/** - No requiere robot (más simple)
4. **src/logging/** - Usa config + utils
5. **src/robot/** - Requiere robot real para testing
6. **src/safety/** - Requiere robot real + pruebas supervisadas

## Dependencias

- **Mínimas:** python-dotenv, PyYAML, pandas (ya en requirements.txt)
- **Para robot:** unitree_sdk2py (instalado aparte)
- **Opcionales:** numpy, matplotlib (para análisis avanzado)

## Testing

Cuando se implementen tests:
```bash
.venv\Scripts\Activate.ps1
python -m pytest tests/
```

## Notas

- Todos los paths usan `pathlib.Path` (cross-platform)
- Configuración viene de `.env` + `config/*.yaml`
- Logging sigue naming estándar: `YYYYMMDD_HHMM_ROBOT_MATERIA_GRUPO`
- Modo replay NO requiere robot (usa `data/samples/` o `data/local/`)
