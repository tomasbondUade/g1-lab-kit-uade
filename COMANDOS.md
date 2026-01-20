# Referencia Rápida de Comandos

Comandos más utilizados para trabajar con el Lab Kit.

---

## 🔧 Setup y verificación

### Instalación completa automática
```powershell
.\scripts\setup_windows.ps1
```

### Instalación forzada (reinstalar todo)
```powershell
.\scripts\setup_windows.ps1 -Force
```

### Instalación sin entorno virtual
```powershell
.\scripts\setup_windows.ps1 -SkipVenv
```

### Verificar instalación
```powershell
.\scripts\verify_setup.ps1
```

---

## 🐍 Entorno virtual Python

### Crear entorno virtual
```powershell
python -m venv venv
```

### Activar entorno virtual
```powershell
.\venv\Scripts\Activate.ps1
```

### Desactivar entorno virtual
```powershell
deactivate
```

### Solucionar error de permisos
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## 📦 Gestión de paquetes

### Actualizar pip
```powershell
python -m pip install --upgrade pip
```

### Instalar SDK de Unitree
```powershell
cd third_party\unitree_sdk2_python
pip install -e .
cd ..\..
```

### Instalar dependencias del proyecto
```powershell
pip install -r env\requirements.txt
```

### Listar paquetes instalados
```powershell
pip list
```

### Ver información de un paquete específico
```powershell
pip show unitree-sdk2py
pip show cyclonedds
```

---

## 🔍 Verificación de componentes

### Verificar versión de Python
```powershell
python --version
```

### Verificar versión de Git
```powershell
git --version
```

### Verificar versión de pip
```powershell
pip --version
```

### Verificar módulo instalado
```powershell
python -c "import unitree_sdk2py; print('OK')"
python -c "import cyclonedds; print('OK')"
python -c "import numpy; print('OK')"
python -c "import cv2; print('OK')"
```

---

## 🌐 Red y conectividad

### Ver interfaces de red disponibles
```powershell
ipconfig
Get-NetAdapter
```

### Ver información detallada de una interfaz
```powershell
ipconfig /all
```

### Hacer ping al robot
```powershell
ping 192.168.123.161  # Reemplazar con IP del robot
```

### Ver tabla de rutas
```powershell
route print
```

---

## 🤖 Ejemplos con el robot

### Leer estado del robot (high-level)
```powershell
cd third_party\unitree_sdk2_python\example\g1\high_level
python read_highstate.py [INTERFAZ_RED]
```

### Control de movimiento (high-level)
```powershell
cd third_party\unitree_sdk2_python\example\g1\high_level
python sportmode_test.py [INTERFAZ_RED]
```

### Leer estado low-level
```powershell
cd third_party\unitree_sdk2_python\example\g1\low_level
python lowlevel_control.py [INTERFAZ_RED]
```

### Obtener video de cámara
```powershell
cd third_party\unitree_sdk2_python\example\g1
python camera_opencv.py [INTERFAZ_RED]
```

### Ejemplo DDS básico (publisher/subscriber)
```powershell
# Terminal 1
cd third_party\unitree_sdk2_python\example\helloworld
python publisher.py

# Terminal 2
cd third_party\unitree_sdk2_python\example\helloworld
python subscriber.py
```

---

## 📝 Git

### Clonar repositorio
```powershell
git clone <URL_DEL_REPO>
```

### Ver estado del repositorio
```powershell
git status
```

### Ver cambios
```powershell
git diff
```

### Actualizar repositorio
```powershell
git pull
```

### Actualizar SDK de Unitree
```powershell
cd third_party\unitree_sdk2_python
git pull
cd ..\..
```

---

## 🧹 Limpieza

### Eliminar entorno virtual
```powershell
Remove-Item -Recurse -Force venv
```

### Eliminar SDK de Unitree
```powershell
Remove-Item -Recurse -Force third_party\unitree_sdk2_python
```

### Limpiar caché de pip
```powershell
pip cache purge
```

### Limpiar archivos __pycache__
```powershell
Get-ChildItem -Recurse -Filter "__pycache__" | Remove-Item -Recurse -Force
Get-ChildItem -Recurse -Filter "*.pyc" | Remove-Item -Force
```

---

## 🐛 Debugging

### Ejecutar Python en modo verbose
```powershell
python -v script.py
```

### Ver información del sistema Python
```powershell
python -m site
```

### Ver variables de entorno Python
```powershell
python -c "import sys; print('\n'.join(sys.path))"
```

### Ver configuración de pip
```powershell
pip config list
```

---

## 📊 Información del sistema

### Ver información del procesador
```powershell
Get-WmiObject Win32_Processor | Select-Object Name, NumberOfCores, NumberOfLogicalProcessors
```

### Ver memoria RAM
```powershell
Get-WmiObject Win32_ComputerSystem | Select-Object TotalPhysicalMemory
```

### Ver espacio en disco
```powershell
Get-PSDrive C
```

### Ver versión de Windows
```powershell
winver
```

---

## 🔐 Permisos y seguridad

### Ver política de ejecución actual
```powershell
Get-ExecutionPolicy -List
```

### Cambiar política de ejecución (usuario actual)
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Ejecutar PowerShell como administrador
```powershell
Start-Process powershell -Verb runAs
```

---

## 📖 Ayuda y documentación

### Ayuda de un comando PowerShell
```powershell
Get-Help [comando]
Get-Help Get-NetAdapter
```

### Ayuda de pip
```powershell
pip help
pip help install
```

### Ayuda de Python
```powershell
python --help
```

### Abrir documentación del proyecto
```powershell
# En Windows, abrir archivo en navegador/editor por defecto
start docs\01_instalacion_windows.md
```

---

## 🆘 Enlaces útiles

- **Repositorio del Lab Kit**: Ver README.md
- **SDK Unitree**: https://github.com/unitreerobotics/unitree_sdk2_python
- **Documentación Unitree**: https://support.unitree.com/home/en/developer
- **Python oficial**: https://www.python.org/
- **Git oficial**: https://git-scm.com/

---

**💡 Tip**: Guarda este archivo como referencia rápida durante el desarrollo.
