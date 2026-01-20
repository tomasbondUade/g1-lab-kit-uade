# Fixtures - Datos de Prueba

> Datos estáticos para tests

---

## Estructura

```
fixtures/
├── README.md          # Este archivo
├── config/            # Configs YAML de prueba
└── sessions/          # Sesiones de prueba completas
```

---

## Uso

Los fixtures se cargan desde `conftest.py` pero también pueden incluirse archivos estáticos aquí para tests más complejos.

### Ejemplo

```python
import pytest
from pathlib import Path

@pytest.fixture
def fixture_config():
    """Cargar config desde fixtures/"""
    fixture_dir = Path(__file__).parent / "fixtures"
    return fixture_dir / "config" / "test_config.yaml"
```

---

## Notas

- Mantener fixtures simples y mínimos
- Preferir fixtures dinámicos en `conftest.py` cuando sea posible
- Usar fixtures estáticos solo para casos muy específicos
