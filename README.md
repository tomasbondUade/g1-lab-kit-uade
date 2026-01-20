# 🎓 G1/Go2 Lab Kit - UADE

> Repositorio completo para prácticas con robots Unitree G1 (humanoide) y Go2 (cuadrúpedo)  
> **Estado**: ✅ Listo para entrega a profesores

---

## 🎯 Resumen Ejecutivo

Este repositorio proporciona **todo lo necesario** para implementar prácticas de robótica con robots Unitree en UADE:

✅ **7 guías completas** - Instalación, red, seguridad, troubleshooting, evaluación  
✅ **Configuración estructurada** - YAML + .env con convenciones consistentes  
✅ **Templates profesionales** - Informes, proyectos, checklists LSP  
✅ **Sesión de ejemplo** - Datos sintéticos para testing sin robot  
✅ **2 notebooks funcionales** - Validación y análisis  
✅ **Tests validados** - 20/20 tests de naming pasando  

---

## 📖 **IMPORTANTE: Leer primero**

### Para profesores:
👉 **[PARA_PROFESORES.md](PARA_PROFESORES.md)** - Estado completo, limitaciones y recomendaciones de uso

### Para alumnos:
👉 **[docs/01_instalacion_windows.md](docs/01_instalacion_windows.md)** - Guía de instalación paso a paso

---

## 🚀 Inicio rápido

### Opción A: Instalación automática (recomendada)

```powershell
# 1. Clonar el repositorio
git clone <URL_DEL_REPO>
cd g1-lab-kit-uade

# 2. Ejecutar script de instalación
.\scripts\setup_windows.ps1

# 3. Verificar instalación
.\scripts\verify_setup.ps1
```

### Opción B: Instalación manual

Sigue la guía completa: **[docs/01_instalacion_windows.md](docs/01_instalacion_windows.md)**

---

## 📚 Documentación

### Para comenzar
1. **[Introducción y objetivos](docs/00_intro_y_objetivo.md)** — Qué es el Lab Kit y para qué sirve
2. **[Instalación en Windows](docs/01_instalacion_windows.md)** — Guía paso a paso completa
3. **[Configuración de red](docs/02_configuracion_red.md)** — Conectar tu PC al robot
4. **[Primera ejecución y pruebas](docs/03_primer_ejecucion_y_pruebas.md)** — Ejemplos básicos

### Operación y soporte
5. **[Seguridad y operación en aula](docs/04_seguridad_operacion_aula.md)** — Procedimientos seguros
6. **[Troubleshooting](docs/05_troubleshooting.md)** — Solución de problemas comunes
7. **[Rúbricas y entregables](docs/06_rubricas_y_entregables.md)** — Evaluación de trabajos

---

## � Estructura del Proyecto

```
g1-lab-kit-uade/
├── docs/                    # 📚 Documentación completa (7 guías)
├── config/                  # ⚙️ Configuraciones YAML (robot, red, límites)
├── src/                     # 🔧 Módulos Python (replay, config, utils, logging)
├── examples/                # 💡 Scripts demostración (05_replay_demo.py funcional)
├── notebooks/               # 📓 Jupyter notebooks (validación, análisis)
├── tests/                   # ✅ Tests pytest (20/20 naming tests pasando)
├── templates/               # 📋 Plantillas para informes/proyectos
├── data/
│   ├── samples/sessions/    # 🎲 Sesión sintética para testing
│   └── local/sessions/      # 💾 Sesiones locales (gitignored)
└── third_party/             # 📦 unitree_sdk2_python (submodule)
```

---

## 🧪 Testing

```powershell
# Ejecutar todos los tests
pytest tests/ -v

# Test específico (naming - 20/20 passing)
pytest tests/test_naming.py -v

# Con coverage
pytest tests/ --cov=src --cov-report=html
```

**Estado actual de tests**:
- ✅ `test_naming.py` - 20/20 tests pasando (100%)
- ⏳ Otros tests dependen de módulos en desarrollo

---

## �🔧 Requisitos del sistema

- **Sistema operativo**: Windows 10/11 (64-bit)
- **Python**: 3.10+ (recomendado 3.11)
- **Git**: Para clonar repositorios
- **PowerShell**: Incluido en Windows
- **Espacio en disco**: ~5 GB libres

---

## 📦 SDK de Unitree

Este repositorio **NO incluye** el SDK oficial de Unitree por razones de licencia.

El SDK se descarga automáticamente con el script de instalación, o manualmente desde:
- Repositorio oficial: https://github.com/unitreerobotics/unitree_sdk2_python
- Instrucciones: [third_party/README.md](third_party/README.md)

---

## 🧑‍🏫 Para docentes

### Preparación del laboratorio
- Considera usar una **imagen de disco** con todo preinstalado
- El script `setup_windows.ps1` facilita la instalación en múltiples equipos
- Revisa la [guía de seguridad](docs/04_seguridad_operacion_aula.md) antes de cada clase

### Verificación previa
```powershell
.\scripts\verify_setup.ps1
```

---

## 🤝 Contribuciones

Este proyecto es para uso académico en UADE. Para sugerencias o mejoras, contacta al equipo docente.

---

## 📄 Licencia

Consultar con la cátedra para detalles de licencia y uso permitido