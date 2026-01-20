# Instalación en Windows — G1/Go2 Lab Kit (UADE)

Esta guía prepara tu PC para ejecutar el kit y, si corresponde, conectarte a un robot Unitree (G1 o Go2).

> **Importante:** el SDK oficial de Unitree **no viene incluido** en este repositorio. Se descarga aparte y se ubica en `third_party/` (ver Paso 3).

---

## 📋 0) Requisitos previos

### Software necesario (instalar una vez)
- **Windows 10/11** (64-bit)
- **Git** — para clonar repositorios
- **Python 3.10+** (recomendado **3.11**)
- **PowerShell** (incluido en Windows)

### ✅ Verificación rápida

Abrí PowerShell y ejecutá:

```powershell
git --version
python --version
pip --version
```

**Esperado**: Python debe ser **3.10 o superior**.

> Si algún comando falla, ve a la sección **"Instalación de requisitos"** más abajo.

---

## 🎯 Resumen de pasos

1. ✅ Verificar/instalar Git y Python
2. 📥 Descargar este repositorio
3. 🐍 Crear entorno virtual Python
4. 🤖 Descargar SDK oficial de Unitree
5. 📦 Instalar dependencias
6. ⚙️ Configurar el kit (.env y YAML)
7. ✔️ Verificar instalación

---

## 1️⃣ Instalación de requisitos (si faltan)

### 1.1 Instalar Git (si falta)

1. Descarga: https://git-scm.com/download/win
2. Ejecuta el instalador (dejar opciones por defecto)
3. **Importante**: Marca "Git from the command line and also from 3rd-party software"
4. Reinicia PowerShell
5. Verifica: `git --version`

### 1.2 Instalar Python 3.10+ (si falta)

1. Descarga: https://www.python.org/downloads/
   - Recomendado: **Python 3.11.x**
2. Ejecuta el instalador
3. **MUY IMPORTANTE**: 
   - ✅ Marca "**Add Python to PATH**"
   - ✅ Marca "**Install pip**"
4. Reinicia PowerShell
5. Verifica: `python --version` y `pip --version`

> ⚠️ Si `python` abre la Microsoft Store, necesitas reinstalar marcando "Add to PATH"

### 1.3 Visual Studio Build Tools (opcional pero recomendado)

Algunas dependencias Python requieren compilar extensiones en C/C++.

**Instalar solo si tienes errores** durante `pip install` relacionados con "Microsoft Visual C++".

1. Descarga: https://visualstudio.microsoft.com/visual-cpp-build-tools/
2. Ejecuta el instalador
3. Selecciona: ✅ **"Desktop development with C++"**
4. Instala (~6-7 GB)

---

## 4️⃣ Clonar el repositorio Lab Kit

Abre **PowerShell** y navega a la carpeta donde quieres instalar el proyecto:

```powershell
# Ejemplo: navegar al escritorio
cd $HOME\Desktop

# O navegar a una carpeta específica
cd C:\Users\TuUsuario\Documents\Proyectos
```

Clona el repositorio:

```powershell
git clone https://github.com/tu-usuario/g1-lab-kit-uade.git
cd g1-lab-kit-uade
```

> 📝 **Nota**: Reemplaza la URL con la URL correcta de tu repositorio.

---

## 3️⃣ Crear y activar entorno virtual

Es **obligatorio** usar un entorno virtual para aislar las dependencias:

```powershell
# Asegúrate de estar en la raíz del proyecto
cd g1-lab-kit-uade

# Crear entorno virtual
python -m venv .venv

# Activar el entorno virtual
.\.venv\Scripts\Activate.ps1
```

Si activó bien, verás `(.venv)` al inicio de la línea:

```
(.venv) PS C:\Users\...\g1-lab-kit-uade>
```

### 🔓 Si PowerShell bloquea la activación

Ejecutá:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

> 💡 **Nota**: Usamos `.venv` (con punto) como estándar Python. Siempre activa el entorno antes de trabajar.

---

## 4️⃣ Descargar el SDK oficial de Unitree (obligatorio)

El SDK oficial **NO viene incluido** en este repositorio por razones de licencia y tamaño.

🔗 **SDK oficial**: https://github.com/unitreerobotics/unitree_sdk2_python

El SDK debe quedar en: `third_party/unitree_sdk2_python/`

### Opción A (recomendada): Clonar con Git

Desde la raíz del repo:

```powershell
cd third_party
git clone https://github.com/unitreerobotics/unitree_sdk2_python.git
cd ..
```

### Opción B: Descargar ZIP

1. Ir al [repo del SDK en GitHub](https://github.com/unitreerobotics/unitree_sdk2_python)
2. Click en "Code" → "Download ZIP"
3. Descomprimir
4. Renombrar la carpeta a `unitree_sdk2_python`
5. Moverla a `third_party/unitree_sdk2_python/`

### ✔️ Verificación del SDK

```powershell
dir5️⃣ Instalar dependencias Python

Asegúrate de que el entorno `.venv` esté activado (debe verse `(.venv)` al inicio).

### Paso 1: Actualizar pip

```powershell
python -m pip install --upgrade pip
```

### Paso 2: Instalar dependencias del kit

```powershell
pip install -r env\requirements.txt
```

Esto instalará:
- `cyclonedds==0.10.2` — comunicación DDS con el robot
- `numpy` — operaciones numéricas
- `opencv-python` — procesamiento de imágenes/video
- `pyyaml` — lectura de archivos de configuración
- `python-dotenv` — lectura de variables de entorno
- Otras dependencias necesarias

> ⏱️ **Nota**: La instalación puede tomar varios minutos.

### Paso 3: Instalar el SDK de Unitree en modo editable

```powershell
cd third_party\unitree_sdk2_python
pip install -e .
cd ..\..
```

Est6️⃣ Configuración del kit

### 6.1 Crear archivo .env

El archivo `.env` contiene configuración local (IP del robot, tipo, etc.).

```powershell
# Copiar el template
copy env\.env.example .env
```

Abrí `.env` con un editor de texto y completá los valores:

```env
# Tipo de robot
ROBOT_TYPE=G1        # O "GO2"

# Conexión al robot
ROBOT_IP=192.168.123.161
ROBOT_PORT=8080

# Interfaz de red local
NETWORK_INTERFACE=Ethernet
```

> ⚠️ **Importante**: NO subas `.env` a Git (ya está en `.gitignore`).

### 6.2 Configuración YAML (opcional)

En `config/` hay archivos de ejemplo:
- `robot_config.example.yaml` — Configuración del robot
- `network.example.yaml` — Configuración de red
- `limits.example.yaml` — Límites de seguridad
8️⃣ Primer ejemplo (sin robot / modo replay)

CuanA) `python` abre Microsoft Store o "no se reconoce"

**Solución**:
1. Instalá Python desde [python.org](https://www.python.org/downloads/)
2. Durante la instalación, **MARCAR**: "Add Python to PATH"
3. Cerrar y reabrir PowerShell
4. Verificar: `python --version`

### B) PowerShell bloquea `activate`

**Error**: `cannot be loaded because running scripts is disabled`

**Solución**:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

### C) El SDK no aparece en `third_party/`

**Solución**: Asegurate de que la ruta sea exactamente:
```
third_party/unitree_sdk2_python/unitree_sdk2py/
```

Si está en otra ubicación, mové la carpeta al lugar correcto.

### D) Error: "Could not locate cyclonedds"

Durante `pip install -e .` del SDK:

**Solución**:
```powershell
# Instalar cyclonedds primero
pip install cyclonedds==0.10.2

# Luego reinstalar el SDK
cd third_party\unitree_sdk2_python
pip install -e .
cd ..\..
```

### E) Error: "Microsoft Visual C++ 14.0 or greater is required"

**Solución**: Instalar Visual Studio Build Tools (ver Paso 1.3)

###📞 Soporte

Si algo falla, adjuntá en tu consulta:

- Salida de `python --version`
- Salida de `pip --version`
- Captura del error completo
- Confirmación de que existe `third_party/unitree_sdk2_python/`

**Canales de soporte**:
- Equipo docente de la cátedra
- [Troubleshooting completo](05_troubleshooting.md)
- Issues en el repositorio (si aplica)

---

## 🎓 Para docentes: Preparación del laboratorio

### Instalación en múltiples equipos

Considera usar:

1. **Script de instalación automatizado**:
   ```powershell
   .\scripts\setup_windows.ps1
   ```

2. **Imagen de disco** con todo preinstalado:
   - Git, Python 3.11, Visual Studio Build Tools
   - Repositorio clonado y SDK descargado
   - Entornos virtuales preconfigurados

3. **Checklist impreso** de esta guía para alumnos

### Verificación previa a clase

```powershell
# En cada PC del laboratorio
.\scripts\verify_setup.ps1

# O test rápido manual
git --version
python --version
python -c "import unitree_sdk2py; print('OK')"
```

---

## 📚 Próximos pasos

Una vez completada la instalación:

1. **[Configuración de red](02_configuracion_red.md)** — Conectar tu PC al robot
2. **[Primera ejecución y pruebas](03_primer_ejecucion_y_pruebas.md)** — Ejemplos básicos
3. **[Seguridad y operación en aula](04_seguridad_operacion_aula.md)** — Procedimientos seguros

---

**✅ ¡Instalación completa!** Ya estás listo para empezar a trabajar con los robots Unitree. 🤖

```
Could not locate cyclonedds. Try to set CYCLONEDDS_HOME or CMAKE_PREFIX_PATH
```

**Solución**: Este error es común en Windows. Intenta:

1. Instalar cyclonedds primero manualmente:
   ```powershell
   pip install cyclonedds==0.10.2
   ```

2. Luego reinstala el SDK:
   ```powershell
   cd third_party\unitree_sdk2_python
   pip install -e .
   cd ..\..
   ```

### Error: "Microsoft Visual C++ 14.0 or greater is required"

**Solución**: Necesitas instalar Visual Studio Build Tools (ver paso 3).

### Python no se reconoce como comando

**Solución**: 
1. Python no está en el PATH
2. Reinstala Python y asegúrate de marcar "Add Python to PATH"
3. O agrega manualmente Python al PATH del sistema

### Error al activar entorno virtual en PowerShell

```
cannot be loaded because running scripts is disabled on this system
```

**Solución**:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## 🎓 Para docentes: Preparación del laboratorio

### Instalación en múltiples equipos

Considera usar:

1. **Imagen de disco** con todo preinstalado (Git, Python, Build Tools)
2. **Script de instalación** automatizado (próximamente en `scripts/setup_windows.ps1`)
3. **Documentación impresa** de esta guía para los alumnos

### Verificación previa a clase

Antes de cada sesión práctica, verifica en las PCs del laboratorio:

```powershell
# Test rápido
git --version
python --version
pip list | findstr cyclonedds
python -c "import unitree_sdk2py"
```

---

## 📚 Próximos pasos

Una vez completada la instalación, continúa con:

1. **[Configuración de red](02_configuracion_red.md)** — Conectar tu PC al robot
2. **[Primera ejecución y pruebas](03_primer_ejecucion_y_pruebas.md)** — Ejemplos básicos
3. **[Seguridad y operación en aula](04_seguridad_operacion_aula.md)** — Procedimientos seguros

---

## 📞 Soporte

Si encuentras problemas durante la instalación:

- Revisa la sección **Solución de problemas** más arriba
- Consulta: [troubleshooting.md](05_troubleshooting.md)
- Contacta al equipo docente o técnico de la cátedra

---

**✅ ¡Instalación completa!** Ya estás listo para empezar a trabajar con los robots Unitree.
