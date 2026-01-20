# Sesión de Ejemplo: 20260115_1430_G1_ROBOTICA_G3

> Sesión sintética de ejemplo para demostración y testing

---

## Información

- **Fecha**: 15 de enero 2026, 14:30
- **Robot**: G1 (humanoide)
- **Materia**: ROBOTICA
- **Grupo**: G3
- **Operador**: Juan Pérez
- **Duración**: 30 minutos (simplificado a ~2.5s en telemetría)
- **Nivel de riesgo**: 1 (postura y gestos básicos)

---

## Descripción

Sesión demostrativa que muestra:
- Movimientos básicos (stand_up, balance, sit_down)
- Telemetría de 4 joints + velocidad + IMU + batería
- Comandos con timestamps
- Metadata completa

---

## Uso

### Cargar con módulo replay

```python
from src.replay.loader import load_session

session = load_session("data/samples/sessions/20260115_1430_G1_ROBOTICA_G3")
print(session.get_metadata())
df = session.get_telemetry()
print(df.head())
```

### Analizar con notebook

Abrir `notebooks/01_replay_analysis.ipynb` y cambiar la ruta de sesión a esta.

---

## Archivos

- `metadata.json` - Información de la sesión
- `telemetry.csv` - Datos de sensores (26 registros)
- `commands.log` - Comandos ejecutados (11 eventos)
- `README.md` - Este archivo

---

**Nota**: Esta es una sesión sintética para propósitos educativos. Los valores no representan datos reales del robot.
