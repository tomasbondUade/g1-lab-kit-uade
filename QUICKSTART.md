# Guía de Inicio Rápido — G1/Go2 Lab Kit

Esta es una guía condensada para instalación y primer uso. Para detalles completos, consulta la documentación en `docs/`.

---

## ✅ Checklist de instalación

### Antes de empezar

- [ ] Tienes permisos de administrador en tu PC
- [ ] Conexión a Internet estable
- [ ] Al menos 5 GB de espacio libre en disco

---

## 📥 Paso 1: Instalar requisitos previos

### Git
```powershell
git --version
```
Si no está instalado: https://git-scm.com/download/win

### Python 3.10+
```powershell
python --version
```
**Requerido**: Python 3.10 o superior (recomendado 3.11)  
Si no está instalado: https://www.python.org/downloads/
⚠️ **Importante**: Marcar "Add Python to PATH" durante instalación

### Visual Studio Build Tools
Descargar: https://visualstudio.microsoft.com/visual-cpp-build-tools/
- Seleccionar: "Desktop development with C++"

---

## 📥 Paso 2: Clonar repositorio

```powershell
# Navegar a tu carpeta de proyectos
cd $HOME\Desktop  # O la ubicación que prefieras

# Clonar el repositorio
git clone https://github.com/tomasbondUade/g1-lab-kit-uade.git
cd g1-lab-kit-uade
```

---

## 🤖 Paso 3: Instalar SDK de Unitree

**Antes de instalar las dependencias del Lab Kit, debes instalar el SDK de Unitree:**

Consulta las instrucciones completas en: [third_party/README.md](third_party/README.md)

### Opción rápida con Git:
```powershell
# Desde la raíz del proyecto
cd third_party
git clone https://github.com/unitreerobotics/unitree_sdk2_python.git
cd ..
```

### Verificar que se instaló correctamente:
```powershell
# Deberías ver carpetas: example/, unitree_sdk2py/, setup.py, etc.
ls third_party\unitree_sdk2_python
```

---

## 🐍 Paso 4: Crear entorno virtual e instalar dependencias

### Instalación manual (Recomendada - Probada)

```powershell
# 1. Crear entorno virtual
python -m venv env
.\env\Scripts\Activate.ps1

# 2. Instalar cyclonedds (dependencia crítica)
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org cyclonedds==0.10.2

# 3. Instalar SDK de Unitree
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -e third_party/unitree_sdk2_python

# 4. Instalar dependencias del Lab Kit
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r env/requirements.txt

# 5. Instalar dependencias adicionales
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org python-dotenv pandas
```

**Nota sobre SSL:** Los flags `--trusted-host` son necesarios en redes corporativas/UADE que usan certificados SSL internos.

### Opción alternativa: Script automático

```powershell
.\scripts\setup_windows.ps1
```

⚠️ Si el script falla por SSL, usa la instalación manual arriba.

---

## ⚙️ Paso 5: Configurar archivo .env

```powershell
# Crear archivo .env desde la plantilla
copy .env.example .env

# Editar configuración
notepad .env
```

Configura los valores según tu setup:

```env
# Tipo de robot
ROBOT_TYPE=go2        # o 'g1' si usas robot humanoide

# IP del robot (para modo live)
ROBOT_IP=192.168.123.18

# Interfaz de red (obtenerla con: ipconfig)
NETWORK_INTERFACE=Ethernet

# Modo de datos
DATA_MODE=replay      # 'replay' para datos grabados, 'live' para robot real
```

> **Tip**: Puedes empezar con `DATA_MODE=replay` para probar sin robot.

---

## ✔️ Paso 6: Verificar instalación (sin robot)

```powershell
# Asegúrate de que el entorno virtual esté activo
.\env\Scripts\Activate.ps1

# Ejecutar validación del entorno
python examples/01_hello_robot.py
```

**Salida esperada:**
```
✓ Archivo .env encontrado
✓ SDK detectado
✓ config/, data/, third_party/, src/, examples/
✅ Todo listo! El kit está configurado correctamente.
```

Si hay errores, consulta: [docs/05_troubleshooting.md](docs/05_troubleshooting.md)

---

## 🎮 Paso 7: Primera prueba (Modo Replay - sin robot)

```powershell
# Analizar sesión de ejemplo incluida
python examples/05_replay_demo.py
```

**Resultado esperado:** Análisis completo de la sesión `20260115_1430_G1_ROBOTICA_G3` con estadísticas de movimiento.

Este modo te permite aprender a usar el Lab Kit sin necesidad de tener el robot conectado.

---

## 🔌 Paso 8 (Opcional): Conectar al robot y prueba en vivo

### 8.1 Conectar al robot

1. **Encender el robot**
2. **Conectar por Ethernet** (recomendado) o WiFi
   - Ver instrucciones detalladas: [docs/02_configuracion_red.md](docs/02_configuracion_red.md)
3. **Anotar la IP del robot** (ejemplo: `192.168.123.18`)
4. **Obtener nombre de interfaz de red**:
   ```powershell
   ipconfig
   ```
   Buscar el adaptador conectado al robot (ej: `Ethernet`, `Wi-Fi`)

### 8.2 Actualizar .env para modo live

```powershell
notepad .env
```

Modificar:
```env
ROBOT_IP=192.168.123.18      # Tu IP del robot
NETWORK_INTERFACE=Ethernet    # Tu interfaz de red
DATA_MODE=live                # Cambiar a live
```

### 8.3 Verificar conectividad

```powershell
# Ping al robot
ping 192.168.123.18

# Si responde, el robot está accesible
```

### 8.4 Primera prueba con robot

```powershell
# Monitor de telemetría en tiempo real
python examples/02_telemetry_check.py --mode live
```

**Resultado esperado:** Monitor actualizándose cada 0.5s con datos del robot en tiempo real

**Resultado esperado:** Monitor actualizándose cada 0.5s con datos del robot en tiempo real

---

## 📖 Próximos pasos

Una vez que la instalación funcione:

1. **Lee la documentación completa**:
   - [Introducción y objetivos](docs/00_intro_y_objetivo.md)
   - [Configuración de red](docs/02_configuracion_red.md)
   - [Ejemplos y pruebas](docs/03_primer_ejecucion_y_pruebas.md)
   - [Seguridad en el aula](docs/04_seguridad_operacion_aula.md)

2. **Explora los ejemplos del Lab Kit**:
   - `examples/01_hello_robot.py` — Verificación de entorno
   - `examples/02_telemetry_check.py` — Monitor en tiempo real
   - `examples/03_log_session.py` — Grabación de sesiones
   - `examples/04_safe_stop.py` — Sistema de parada de emergencia
   - `examples/05_replay_demo.py` — Análisis de datos grabados

3. **Revisa los ejemplos del SDK de Unitree**:
   - `third_party/unitree_sdk2_python/example/g1/` — Ejemplos para G1
   - `third_party/unitree_sdk2_python/example/go2/` — Ejemplos para Go2

4. **Usa los notebooks de Jupyter**:
   ```powershell
   jupyter notebook notebooks/
   ```
   - `00_intro.ipynb` — Introducción al Lab Kit
   - `01_replay_analysis.ipynb` — Análisis de sesiones
   - `02_telemetry_viz.ipynb` — Visualización de telemetría
   - `03_data_exploration.ipynb` — Exploración de datos

---

## ❓ ¿Problemas?

### Script de instalación falla
→ Sigue la instalación manual paso a paso en [docs/01_instalacion_windows.md](docs/01_instalacion_windows.md)

### Error: "cyclonedds not found"
```powershell
pip install cyclonedds==0.10.2
```

### Error al activar entorno virtual
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Python no reconocido
- Reinstalar Python marcando "Add Python to PATH"
- Reiniciar PowerShell/CMD

### No puedo instalar el SDK de Unitree
→ Consulta [third_party/README.md](third_party/README.md) para instrucciones detalladas

### Robot no responde al ping
→ Verifica configuración de red en [docs/02_configuracion_red.md](docs/02_configuracion_red.md)

### Más problemas
→ Consulta [docs/05_troubleshooting.md](docs/05_troubleshooting.md)

---

## 🆘 Soporte

- **Documentación completa**: Carpeta `docs/`
- **Ejemplos del Lab Kit**: Carpeta `examples/`
- **Ejemplos del SDK**: `third_party/unitree_sdk2_python/example/`
- **Equipo docente**: Contacta a tu profesor/ayudante

---

**¡Listo para empezar! 🚀**
