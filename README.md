# G1/Go2 Lab Kit (UADE) — Unitree

Repositorio para actividades en clase con robots **Unitree G1** (humanoide) y **Go2** (cuadrúpedo).

## 🎯 Funcionalidades

- ✅ Conexión y telemetría con los robots
- ✅ Comandos seguros (deadman / safe stop)
- ✅ Logging de sesiones y generación de datasets
- ✅ Modo replay (trabajo sin robot físico)
- ✅ Base para proyectos de dashboard, visión e IA

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

## 🔧 Requisitos del sistema

- **Sistema operativo**: Windows 10 o superior (64-bit)
- **Python**: 3.8 o superior
- **Git**: Para clonar repositorios
- **Visual Studio Build Tools**: Para compilar dependencias
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