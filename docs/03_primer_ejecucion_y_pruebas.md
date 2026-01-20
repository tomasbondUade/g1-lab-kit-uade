# Primera ejecución y pruebas — G1/Go2 Lab Kit (Windows)

Este documento valida que tu instalación está correcta:
1) entorno Python y dependencias
2) SDK oficial `unitree_sdk2_python` presente
3) conectividad por Ethernet (si hay robot)
4) ejecución de un ejemplo del SDK
5) (más adelante) ejecución de los ejemplos del Lab Kit

---

## ✅ Objetivo

Al finalizar, deberías poder:
- confirmar que Python + venv funcionan
- confirmar que el SDK está en la ruta correcta
- ejecutar al menos **1 ejemplo** del SDK (sin y/o con robot)
- dejar el entorno listo para correr los ejemplos del kit

---

## 1) Checklist rápido (antes de empezar)

Desde la raíz del repo `g1-lab-kit-uade/`:

- [ ] Estás en la carpeta del repo
- [ ] El entorno virtual está activo (`(.venv)` visible)
- [ ] El SDK existe en `third_party/unitree_sdk2_python/`
- [ ] Si hay robot: PC y robot están conectados por Ethernet y en la misma red

Comandos útiles:

```powershell
cd <ruta_a>\g1-lab-kit-uade
.\.venv\Scripts\activate
dir third_party\unitree_sdk2_python
```

---

## 2) Verificar entorno Python

### 2.1 Versiones
```powershell
python --version
pip --version
```

### 2.2 Dependencias del kit
```powershell
pip install -r env\requirements.txt
```

Si ya estaba instalado, puede decir "Requirement already satisfied".

---

## 3) Verificar el SDK (estructura y accesibilidad)

### 3.1 Estructura esperada

Debe existir:
- `third_party/unitree_sdk2_python/unitree_sdk2py/`
- `third_party/unitree_sdk2_python/example/`

Verificar:
```powershell
dir third_party\unitree_sdk2_python
dir third_party\unitree_sdk2_python\example
```

---

## 4) (Opcional) Verificar red por Ethernet (solo si hay robot)

Si tenés la IP del robot:

```powershell
ping <IP_DEL_ROBOT>
```

Si no responde:
- volver a [docs/02_configuracion_red.md](02_configuracion_red.md) (troubleshooting)

---

## 5) Ejecutar un ejemplo del SDK (prueba base)

El SDK trae ejemplos dentro de `third_party/unitree_sdk2_python/example/`.
El objetivo es ejecutar un ejemplo simple para confirmar que el SDK corre.

### 5.1 Ingresar a la carpeta del SDK
```powershell
cd third_party\unitree_sdk2_python
```

### 5.2 Listar ejemplos disponibles
```powershell
dir example
```

Vas a ver carpetas como:
- `helloworld/`
- `high_level/`
- `low_level/`
- `front_camera/`

(la disponibilidad exacta depende de la versión del SDK)

### 5.3 Ejemplo recomendado: helloworld (publisher/subscriber)

Este ejemplo suele usarse para verificar comunicación pub/sub.

**Abrir dos terminales PowerShell:**

**Terminal A:**
```powershell
cd <ruta_a>\g1-lab-kit-uade\third_party\unitree_sdk2_python
python example\helloworld\subscriber.py
```

**Terminal B:**
```powershell
cd <ruta_a>\g1-lab-kit-uade\third_party\unitree_sdk2_python
python example\helloworld\publisher.py
```

Si corre sin errores, el entorno y el SDK están bien montados.

> Si el ejemplo requiere robot o configuración adicional, usar un ejemplo alternativo
> o consultar el README del SDK.

### 5.4 Volver a la raíz del repo
```powershell
cd <ruta_a>\g1-lab-kit-uade
```

---

## 6) Prueba del kit (cuando estén los ejemplos)

Cuando el kit tenga ejemplos propios en `examples/`, se ejecutarán así:

```powershell
python examples\01_hello_robot.py
```

**Ejemplos previstos:**
- `01_hello_robot.py` (conexión + telemetría)
- `02_log_session.py` (logging)
- `03_safe_routine.py` (deadman + safe stop)
- `05_replay_demo.py` (modo replay sin robot)

> Si todavía no existen, esta sección queda como guía para cuando se agreguen.

---

## 7) Errores comunes (rápidos)

### A) "python no se reconoce" o abre Microsoft Store
- Instalar Python desde [python.org](https://www.python.org/)
- Marcar "Add Python to PATH"
- Cerrar y abrir PowerShell
- Verificar: `python --version`

### B) "No se puede ejecutar activate.ps1"
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\activate
```

### C) "No encuentra unitree_sdk2_python"
Confirmar que existe:
- `third_party/unitree_sdk2_python/`

### D) Error en ejemplos del SDK
- Ejecutar desde dentro del folder del SDK (`third_party/unitree_sdk2_python`)
- Revisar el README del SDK por requisitos adicionales
- Verificar que el robot (si aplica) esté accesible por red

---

## 8) Evidencia de verificación (para docentes / laboratorio)

Para registrar que un equipo quedó listo, adjuntar:
- salida de `python --version`
- salida de `pip --version`
- captura o log de ejecución exitosa del ejemplo (helloworld o equivalente)
