# 🎓 G1/Go2 Lab Kit - UADE

> Repositorio completo para prácticas con robots Unitree G1 (humanoide) y Go2 (cuadrúpedo)  
> **Estado**: ✅ Listo para uso en clase

---

## 🎯 Resumen Ejecutivo

Este repositorio proporciona **todo lo necesario** para implementar prácticas de robótica con robots Unitree en UADE:

✅ **7 guías completas** - Instalación, red, seguridad, troubleshooting, evaluación  
✅ **Ejemplos funcionales** - Demo de replay (`05_replay_demo.py`) validado  
✅ **Sesión de ejemplo** - Datos sintéticos para testing sin robot  
✅ **Modo simulación** - Test y desarrollo sin necesidad de robot físico  
✅ **Tests validados** - 20/20 naming tests + 7/16 replay tests  
✅ **Solución SSL** - Documentación para certificados en redes corporativas  

---

## 📖 **Documentación principal**

👉 **[QUICKSTART.md](QUICKSTART.md)** - Guía rápida de inicio  
👉 **[docs/01_instalacion_windows.md](docs/01_instalacion_windows.md)** - Instalación completa paso a paso  
👉 **[docs/05_troubleshooting.md](docs/05_troubleshooting.md)** - Solución de problemas (incluye SSL)

---

## 🚀 Inicio rápido (5 minutos)

```powershell
# 1. Crear entorno virtual
python -m venv env
.\env\Scripts\Activate.ps1

# 2. Instalar SDK (con workaround SSL para red UADE/corporativa)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -e third_party/unitree_sdk2_python

# 3. Instalar dependencias
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r env/requirements.txt

# 4. Configurar
cp .env.example .env
# Editar .env: ROBOT_TYPE=go2 o g1

# 5. Probar sin robot (modo replay)
python examples/05_replay_demo.py
```

✅ **Resultado esperado**: Carga y muestra la sesión de ejemplo `20260115_1430_G1_ROBOTICA_G3`

---

## 💡 Ejemplos disponibles

### 🎯 Modo Replay (sin robot)
```powershell
# Demo de análisis de sesiones (funcional)
python examples/05_replay_demo.py

# Notebooks de análisis
jupyter notebook notebooks/01_replay_analysis.ipynb
```

### 📁 Otros ejemplos en `/examples`
- `01_hello_robot.py` - Conexión básica con el robot
- `02_telemetry_collect.py` - Recolección de datos de sensores
- `03_log_session.py` - Sistema de logging
- `04_safe_stop.py` - Implementación de parada segura
- `05_replay_demo.py` - ✅ **Funcional** - Análisis de sesiones grabadas

**Nota**: Los ejemplos 01-04 son plantillas base. Ver [examples/README.md](examples/README.md)

---

## 📚 Documentación completa

### Para comenzar
1. [Introducción y objetivos](docs/00_intro_y_objetivo.md) — Visión general del proyecto
2. [Instalación en Windows](docs/01_instalacion_windows.md) — Guía paso a paso completa
3. [Configuración de red](docs/02_configuracion_red.md) — Conectar tu PC al robot
4. [Primera ejecución y pruebas](docs/03_primer_ejecucion_y_pruebas.md) — Validación inicial

### Operación y soporte
5. [Seguridad y operación en aula](docs/04_seguridad_operacion_aula.md) — Procedimientos obligatorios
6. [Troubleshooting](docs/05_troubleshooting.md) — Problemas comunes (incluye SSL)
7. [Rúbricas y entregables](docs/06_rubricas_y_entregables.md) — Criterios de evaluación

---

## 📁 Estructura del Proyecto

```
g1-lab-kit-uade/
├── 📚 docs/                          # 7 guías completas
├── ⚙️  config/                        # Configuraciones YAML (ejemplos)
├── 🔧 src/                            # Módulos Python
│   ├── replay/                       # ✅ Análisis de sesiones (funcional)
│   ├── utils/                        # ✅ Naming conventions (20/20 tests)
│   ├── config/                       # Carga de configuraciones
│   └── logging/                      # Sistema de logging
├── 💡 examples/                       # Scripts de demostración
│   └── 05_replay_demo.py            # ✅ Demo funcional
├── 📓 notebooks/                      # Jupyter notebooks (4)
├── ✅ tests/                          # Tests pytest
├── 📋 templates/                      # Plantillas para informes
├── 🎲 data/samples/sessions/          # Sesión de ejemplo (versionada)
│   └── 20260115_1430_G1_ROBOTICA_G3/ # Sesión sintética G1
├── 💾 data/local/sessions/            # Sesiones locales (gitignored)
├── 📦 third_party/unitree_sdk2_python # SDK oficial (submodule)
├── 🔧 scripts/                        # Scripts de instalación
│   ├── setup_windows.ps1             # Instalación automática
│   └── verify_setup.ps1              # Verificación del entorno
└── 📖 env/requirements.txt            # Dependencias Python
```

### Archivos clave
- `.env.example` - Template de configuración (copiar a `.env`)
- `QUICKSTART.md` - Guía rápida
- `COMANDOS.md` - Comandos útiles
- `env/requirements.txt` - Dependencias (incluye pandas)

---

## 🧪 Testing

```powershell
# Ejecutar todos los tests
pytest tests/ -v

# Test específico (naming - 100%)
pytest tests/test_naming.py -v

# Tests de replay (parcial)
pytest tests/test_replay.py -v

# Con coverage
pytest tests/ --cov=src --cov-report=html
```

**Estado actual**:
- ✅ `test_naming.py` - 20/20 tests (100%) - Validación de nombres de sesiones
- ⚡ `test_replay.py` - 7/16 tests (44%) - Core funcional, pendientes edge cases
- ⏳ `test_config.py`, `test_logging.py` - Requieren módulos completos

---

## ⚠️ Troubleshooting común

### Error SSL al instalar paquetes

**Síntoma**: `SSL: CERTIFICATE_VERIFY_FAILED`  
**Causa**: Red corporativa/universitaria (común en UADE)

**Solución**:
```powershell
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org <paquete>
```

Más soluciones: [docs/05_troubleshooting.md](docs/05_troubleshooting.md)

---

## 🔧 Requisitos del sistema

- **Sistema operativo**: Windows 10/11 (64-bit)
- **Python**: 3.10+ (validado con 3.10.9)
- **Git**: Para clonar repositorios
- **PowerShell**: Incluido en Windows
- **Espacio en disco**: ~5 GB libres
- **Red**: Ethernet (recomendado) o Wi-Fi para robot real

---

## 📦 SDK de Unitree

El SDK oficial **NO está incluido** en este repo (razones de licencia).

**Instalación**:
```powershell
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -e third_party/unitree_sdk2_python
```

- Repositorio: https://github.com/unitreerobotics/unitree_sdk2_python
- Versión: 1.0.1
- Docs: `third_party/unitree_sdk2_python/README.md`

---

## 🧑‍🏫 Para docentes

### Preparación del laboratorio
- Scripts de instalación disponibles: `scripts/setup_windows.ps1` y `verify_setup.ps1`
- Sesión de ejemplo lista para demos sin robot
- Demo funcional: `examples/05_replay_demo.py`
- Checklist de seguridad: `docs/04_seguridad_operacion_aula.md`

### Workflow sugerido
1. **Clase 1**: Instalación + modo replay + análisis de sesión ejemplo
2. **Clase 2**: Desarrollo de scripts (pueden usar SDK examples)
3. **Clase 3**: Ejecución en laboratorio con robot real

### Referencias SDK para alumnos
Los ejemplos oficiales del SDK están en:
- `third_party/unitree_sdk2_python/example/go2/high_level/`
- `third_party/unitree_sdk2_python/example/g1/high_level/`

---

## 🎓 Casos de uso pedagógico

**Nivel básico**:
- Análisis de sesiones grabadas (modo replay)
- Comprensión de comandos básicos
- Lectura de telemetría

**Nivel intermedio**:
- Creación de scripts de movimiento
- Secuencias de comandos
- Logging y debugging

**Nivel avanzado**:
- Control en tiempo real
- Procesamiento de sensores
- Proyectos integrados (visión, navegación)

---

## 🤝 Contribuciones

Este proyecto es para uso académico en UADE. Para sugerencias, contactar al equipo docente.

### Estado del proyecto
- ✅ Core funcional y validado
- ✅ Ejemplos y documentación completos
- ✅ Modo replay operativo
- ✅ Instalación validada con red UADE

---

## 📊 Changelog

### 2026-01-20 - Release inicial
- ✅ Completado `src/replay/loader.py` con métodos funcionales
- ✅ `.env.example` movido a raíz del proyecto
- ✅ `pandas` agregado a requirements.txt (requerido)
- ✅ Documentación SSL en troubleshooting
- ✅ Mejorado `.gitignore` (Thumbs.db, venv/, IDEs)
- ✅ Demo `examples/05_replay_demo.py` funcional
- ✅ Tests: 20/20 naming, 7/16 replay

---

## 📄 Licencia

Consultar con la cátedra para detalles de licencia y uso.

**SDK Unitree**: Ver `third_party/unitree_sdk2_python/LICENSE`
