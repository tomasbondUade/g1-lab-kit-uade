# Notebooks — G1/Go2 Lab Kit

Jupyter notebooks para análisis interactivo, visualización y experimentación.

## Diferencia con `examples/`

- **examples/**: scripts que se ejecutan directo (`.py`) → validación, logging, control
- **notebooks/**: análisis interactivo (`.ipynb`) → exploración, visualización, reportes

## Requisitos previos

1. Instalación completada: `docs/01_instalacion_windows.md`
2. Dependencias instaladas (incluyendo pandas, matplotlib si aplica)
3. Para notebooks con gráficos, instalar:
   ```bash
   .venv\Scripts\python -m pip install matplotlib seaborn jupyter
   ```

## Uso

### Iniciar Jupyter
Desde la raíz del proyecto (con `.venv` activado):

```bash
.venv\Scripts\Activate.ps1
jupyter notebook notebooks/
```

O con VS Code (recomendado):
1. Abrir `.ipynb` en VS Code
2. Seleccionar kernel: `.venv` (Python del proyecto)
3. Ejecutar celdas con `Shift+Enter`

## Notebooks disponibles

### 00_intro.ipynb
**Objetivo:** Validar setup del entorno en modo interactivo.
- Verificar .env cargado
- Verificar SDK disponible
- Mostrar configuración básica
- Modo: Replay/Live

---

### 01_replay_analysis.ipynb
**Objetivo:** Analizar sesiones grabadas (modo replay).
- Cargar sesión de `data/samples/` o `data/local/`
- Calcular estadísticas (pandas)
- Visualizar telemetría (matplotlib)
- Exportar reportes

**Solo Replay** (no requiere robot)

---

### 02_telemetry_viz.ipynb
**Objetivo:** Visualización avanzada de telemetría.
- Gráficos interactivos (seaborn/plotly si aplica)
- Comparación entre sesiones
- Análisis de tendencias
- Modo: Replay

---

### 03_data_exploration.ipynb
**Objetivo:** Exploración libre de datos para proyectos.
- Template para análisis custom
- Ejemplos de análisis estadístico
- Modo: Replay

---

## Naming de sesiones de análisis

Si guardás notebooks de análisis específicos (por grupo), usar:

`YYYYMMDD_MATERIA_GRUPO_analisis.ipynb`

Ejemplo: `20260120_Prog1_G3_analisis.ipynb`

## Tips

- **Siempre ejecutar celdas en orden** (de arriba a abajo)
- **Reiniciar kernel** si algo no funciona: `Kernel → Restart & Clear Output`
- **No commitear notebooks con outputs grandes** (limpiar antes de commit)
- **Para datos grandes**: usar `data/local/` (no se versiona)

## Soporte

Si algo falla:
- `docs/05_troubleshooting.md`
- Verificar que `.venv` está activado
- Verificar que jupyter está instalado: `pip list | grep jupyter`
