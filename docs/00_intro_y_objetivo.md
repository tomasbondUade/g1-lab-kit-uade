# Introducción y objetivo — G1/Go2 Lab Kit (UADE)

## 1) ¿Qué es este repositorio?

Este repositorio (“Lab Kit”) reúne **herramientas, configuraciones y ejemplos** para utilizar robots **Unitree** en actividades de clase y trabajos prácticos, con foco en:

- **Unitree G1 (humanoide)**
- **Unitree Go2 (cuadrúpedo)**

El objetivo es que docentes y estudiantes puedan **arrancar rápido** sin tener que resolver desde cero instalación, conexión, seguridad y logging en cada materia o comisión.

---

## 2) Objetivo general

Disponer de una base común para actividades académicas que permita:

- Conectar al robot y leer **telemetría** (estado, IMU, joints, batería, etc.)
- Ejecutar comandos de forma **segura** (deadman / stop seguro / límites “modo clase”)
- Registrar **logs de sesiones** para análisis posterior y generación de datasets
- Trabajar en modalidad **replay** (sin robot) para escalar a cursos con muchos grupos
- Servir como punto de partida para proyectos de **dashboard**, **visión** e **IA/ML**

---

## 3) Alcance del kit (qué incluye / qué no incluye)

### Incluye
- Documentación de instalación y configuración (Windows-first)
- Ejemplos mínimos (“hello robot”) y módulos reutilizables
- Procedimientos de seguridad operativa en aula
- Logging y estructura de datos para sesiones
- Modo replay con logs de ejemplo (cuando estén disponibles)

### No incluye
- El SDK oficial de Unitree dentro del repositorio.
  - El SDK se descarga por separado y se ubica en `third_party/unitree_sdk2_python/`
  - Ver instrucciones en: `third_party/README.md`

---

## 4) Principios de uso en clase

- **Seguridad primero:** ninguna actividad se ejecuta sin stop seguro y deadman definidos.
- **Un controlador a la vez:** se usa “token de control” para evitar comandos simultáneos.
- **Escalabilidad:** la mayoría de grupos trabaja con logs/replay; el robot se usa para validar.
- **Trazabilidad:** cada uso debe registrar un checklist y logs con nombre estándar.

---

## 5) Estructura del repositorio (resumen)

- `docs/` Documentación (instalación, red, seguridad, troubleshooting)
- `scripts/` Scripts de soporte (verificación del setup, etc.)
- `src/` Módulos base del kit (conexión, safety, telemetría, logging, replay)
- `examples/` Ejemplos listos para clase
- `config/` Configuraciones (red, límites, robot)
- `third_party/` Instrucciones para descargar el SDK oficial

---

## 6) Primeros pasos

1. Seguir la guía de instalación:
   - `docs/01_instalacion_windows.md`
2. Descargar el SDK oficial:
   - `third_party/README.md`
3. Ejecutar el primer ejemplo (cuando esté disponible):
   - `examples/01_hello_robot.py`

---

## 7) Soporte y mejoras

Si encontrás un error o querés proponer una mejora:
- Crear un issue en el repositorio con:
  - qué estabas haciendo
  - mensaje de error
  - pasos para reproducir
  - versión de Python y Windows
