# Tests - G1 Lab Kit

> Tests unitarios y de integración para validar funcionalidad del kit

---

## Estructura

```
tests/
├── README.md              # Este archivo
├── conftest.py            # Fixtures compartidos (pytest)
├── test_config.py         # Tests de src/config/
├── test_naming.py         # Tests de src/utils/naming.py
├── test_replay.py         # Tests de src/replay/
├── test_logging.py        # Tests de src/logging/
└── fixtures/              # Datos de prueba
    ├── config/            # Configs de prueba
    └── sessions/          # Sesiones de prueba
```

---

## Instalación

Para ejecutar tests necesitas pytest:

```powershell
# Activar entorno virtual
.venv\Scripts\Activate.ps1

# Instalar pytest
pip install pytest pytest-cov
```

---

## Ejecutar tests

### Todos los tests

```powershell
pytest
```

### Tests específicos

```powershell
# Solo config
pytest tests/test_config.py

# Solo naming
pytest tests/test_naming.py

# Con verbose
pytest -v

# Con coverage
pytest --cov=src --cov-report=html
```

### Tests por módulo

```powershell
# Config
pytest tests/test_config.py -v

# Utils
pytest tests/test_naming.py -v

# Replay
pytest tests/test_replay.py -v

# Logging
pytest tests/test_logging.py -v
```

---

## Fixtures

Los fixtures compartidos están en `conftest.py`:

- `temp_dir` - Directorio temporal para tests
- `sample_config` - Config YAML de ejemplo
- `sample_session` - Sesión completa de ejemplo
- `sample_metadata` - Metadata JSON de ejemplo

---

## Coverage

Para generar reporte de coverage:

```powershell
pytest --cov=src --cov-report=html
```

El reporte HTML estará en `htmlcov/index.html`

---

## Notas

- Los tests NO requieren robot conectado
- Usan fixtures y datos sintéticos
- Tests de robot/safety requieren hardware (marcados como `@pytest.mark.hardware`)
- Para CI/CD se pueden ejecutar solo tests sin hardware: `pytest -m "not hardware"`
