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

### Python 3.8+
```powershell
python --version
```
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
git clone <URL_DEL_REPOSITORIO>
cd g1-lab-kit-uade
```

---

## 🐍 Paso 3: Instalación automática

### Opción recomendada: Script automático

```powershell
.\scripts\setup_windows.ps1
```

Este script:
- ✅ Descarga el SDK de Unitree
- ✅ Crea entorno virtual Python (`.venv`)
- ✅ Instala todas las dependencias
- ✅ Crea archivo `.env` desde template
- ✅ Verifica la instalación

### Opción manual (si el script falla)

```powershell
# 1. Descargar SDK
cd third_party
git clone https://github.com/unitreerobotics/unitree_sdk2_python.git
cd ..

# 2. Crear entorno virtual
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 3. Instalar dependencias
pip install -r env\requirements.txt

# 4. Instalar SDK
cd third_party\unitree_sdk2_python
pip install -e .
cd ..\..

# 5. Crear archivo .env
copy env\.env.example .env
```

---

## ✔️ Paso 4: Verificar instalación

```powershell
.\scripts\verify_setup.ps1
```

Deberías ver: ✅ TODO CORRECTO

Si hay errores, consulta: [docs/05_troubleshooting.md](docs/05_troubleshooting.md)

---

## ⚙️ Paso 5: Configurar el kit

Edita el archivo `.env` en la raíz del proyecto:

```powershell
notepad .env
```

Completa los valores necesarios:
7: Primera prueba

### Activar entorno virtual (si no está activo)
```powershell
.\.TWORK_INTERFACE=Ethernet # Tu interfaz de red
```

> **Importante**: El archivo `.env` ya debería existir (creado por el script de setup).

---

## 🔌 Paso 6: Conectar al robot

1. **Encender el robot**
2. **Conectar por WiFi o Ethernet**
   - Ver instrucciones detalladas: [docs/02_configuracion_red.md](docs/02_configuracion_red.md)
3. **Anotar la IP del robot** (ej: 192.168.123.161)

---

## 🎮 Paso 6: Primera prueba

### Activar entorno virtual (si no está activo)
```powershell
.\venv\Scripts\Activate.ps1
```

### Ejecutar ejemplo básico
```powershell
# Ejemplo: Leer estado del robot
cd third_party\unitree_sdk2_python\example\g1\high_level
python read_highstate.py [NOMBRE_INTERFAZ_RED]
```

Reemplaza `[NOMBRE_INTERFAZ_RED]` con el nombre de tu adaptador de red.

Para ver interfaces de red disponibles:
```powershell
ipconfig
```

---

## 📖 Próximos pasos

Una vez que la instalación funcione:

1. **Lee la documentación completa**:
   - [Introducción y objetivos](docs/00_intro_y_objetivo.md)
   - [Configuración de red](docs/02_configuracion_red.md)
   - [Ejemplos y pruebas](docs/03_primer_ejecucion_y_pruebas.md)

2. **Revisa los ejemplos disponibles**:
   - `third_party/unitree_sdk2_python/example/g1/` — Ejemplos para G1
   - `third_party/unitree_sdk2_python/example/go2/` — Ejemplos para Go2

3. **Lee sobre seguridad**:
   - [Seguridad en el aula](docs/04_seguridad_operacion_aula.md)

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

### Más problemas
→ Consulta [docs/05_troubleshooting.md](docs/05_troubleshooting.md)

---

## 🆘 Soporte

- **Documentación completa**: Carpeta `docs/`
- **Ejemplos del SDK**: `third_party/unitree_sdk2_python/example/`
- **Equipo docente**: Contacta a tu profesor/ayudante

---

**¡Listo para empezar! 🚀**
