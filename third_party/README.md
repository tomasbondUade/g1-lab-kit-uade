# SDK Unitree (unitree_sdk2_python)

Este proyecto usa el SDK oficial de Unitree:
**https://github.com/unitreerobotics/unitree_sdk2_python**

Por razones de **tamaño y licencia**, el SDK **NO se incluye** dentro de este repositorio.
Cada usuario debe descargarlo y ubicarlo en: `third_party/unitree_sdk2_python/`

---

## 🚀 Instalación automática (recomendada)

El script de setup del proyecto descarga e instala el SDK automáticamente:

```powershell
# Desde la raíz del proyecto
.\scripts\setup_windows.ps1
```

---

## 📥 Instalación manual

Si prefieres instalar manualmente o el script automático falla:

### Opción A: Clonar con Git (recomendada)

Desde la raíz del repositorio del Lab Kit:

```powershell
# 1. Instalar cyclonedds PRIMERO (dependencia crítica)
pip install cyclonedds==0.10.2

# 2. Clonar el SDK
cd third_party
git clone https://github.com/unitreerobotics/unitree_sdk2_python.git
cd unitree_sdk2_python

# 3. Instalar el SDK
pip install -e .

# 4. Volver a la raíz
cd ..\..
```

### Opción B: Descargar ZIP

1. **Instalar cyclonedds primero**:
   ```powershell
   pip install cyclonedds==0.10.2
   ```
2. Ir a: https://github.com/unitreerobotics/unitree_sdk2_python
3. Click en "Code" → "Download ZIP"
4. Extraer el contenido en: `third_party/unitree_sdk2_python/`
5. Instalar el SDK:
   ```powershell
   cd third_party\unitree_sdk2_python
   pip install -e .
   cd ..\..
   ```

---

## ✔️ Verificar instalación

### Método 1: Comprobar estructura de carpetas

```powershell
ls third_party\unitree_sdk2_python
```

Deberías ver:
- `example/` — Ejemplos de código
- `unitree_sdk2py/` — Código fuente del SDK
- `setup.py` — Script de instalación
- `README.md` — Documentación del SDK

### Método 2: Verificar módulo Python

```powershell
python -c "import unitree_sdk2py; print('SDK instalado correctamente')"
```

Si aparece "SDK instalado correctamente", ¡todo está bien! ✅

### Método 3: Usar script de verificación

```powershell
# Desde la raíz del proyecto
.\scripts\verify_setup.ps1
```

---

## 📚 Documentación del SDK

- **README oficial**: `third_party/unitree_sdk2_python/README.md`
- **Ejemplos G1**: `third_party/unitree_sdk2_python/example/g1/`
- **Ejemplos Go2**: `third_party/unitree_sdk2_python/example/go2/`
- **Documentación web**: https://support.unitree.com/home/en/developer

---

## 🔧 Dependencias del SDK

El SDK requiere las siguientes librerías (se instalan automáticamente):

- `cyclonedds==0.10.2` — Comunicación DDS
- `numpy` — Computación numérica
- `opencv-python` — Procesamiento de imagen/video

---

## ❓ Problemas comunes

### Error: "Microsoft Visual C++ 14.0 or greater is required"

**Solución**: Instalar Visual Studio Build Tools
- Descargar: https://visualstudio.microsoft.com/visual-cpp-build-tools/
- Seleccionar: "Desktop development with C++"
- Ver: [docs/01_instalacion_windows.md](../docs/01_instalacion_windows.md)

### El módulo no se importa

Asegúrate de:
1. Haber activado el entorno virtual (si usas uno):
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```
2. Haber instalado el SDK:
   ```powershell
   cd third_party\unitree_sdk2_python
   pip install -e .
   ```

---

## 🔄 Actualizar el SDK

Para actualizar a la última versión del SDK:

```powershell
cd third_party\unitree_sdk2_python

# Si clonaste con Git
git pull origin main

# Reinstalar
pip install -e . --upgrade

cd ..\..
```

---

## 📖 Más información

Para guías completas de instalación y uso, consulta:
- [Guía de instalación Windows](../docs/01_instalacion_windows.md)
- [Guía de inicio rápido](../QUICKSTART.md)
- [Troubleshooting](../docs/05_troubleshooting.md)
