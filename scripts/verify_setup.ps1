# Script de verificación de instalación
# G1/Go2 Lab Kit (UADE)
#
# Este script verifica que todos los componentes necesarios estén instalados correctamente.
# Uso: .\scripts\verify_setup.ps1

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  Verificación de Instalación Lab Kit" -ForegroundColor Cyan
Write-Host "  Unitree G1/Go2 - UADE" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

$errores = 0
$advertencias = 0

# 1. Verificar Git
Write-Host "[1/7] Verificando Git..." -ForegroundColor Yellow
try {
    $gitVersion = git --version 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "  ✓ Git instalado: $gitVersion" -ForegroundColor Green
    } else {
        Write-Host "  ✗ Git no encontrado" -ForegroundColor Red
        Write-Host "    Instalar desde: https://git-scm.com/download/win" -ForegroundColor Gray
        $errores++
    }
} catch {
    Write-Host "  ✗ Git no encontrado" -ForegroundColor Red
    Write-Host "    Instalar desde: https://git-scm.com/download/win" -ForegroundColor Gray
    $errores++
}

# 2. Verificar Python
Write-Host "`n[2/7] Verificando Python..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    if ($LASTEXITCODE -eq 0) {
        # Extraer número de versión
        $versionMatch = [regex]::Match($pythonVersion, "(\d+)\.(\d+)")
        $major = [int]$versionMatch.Groups[1].Value
        $minor = [int]$versionMatch.Groups[2].Value
        
        if ($major -ge 3 -and $minor -ge 8) {
            Write-Host "  ✓ Python instalado: $pythonVersion" -ForegroundColor Green
        } else {
            Write-Host "  ⚠ Python instalado pero versión muy antigua: $pythonVersion" -ForegroundColor Yellow
            Write-Host "    Se requiere Python >= 3.8" -ForegroundColor Gray
            $advertencias++
        }
    } else {
        Write-Host "  ✗ Python no encontrado" -ForegroundColor Red
        Write-Host "    Instalar desde: https://www.python.org/downloads/" -ForegroundColor Gray
        $errores++
    }
} catch {
    Write-Host "  ✗ Python no encontrado" -ForegroundColor Red
    Write-Host "    Instalar desde: https://www.python.org/downloads/" -ForegroundColor Gray
    $errores++
}

# 3. Verificar pip
Write-Host "`n[3/7] Verificando pip..." -ForegroundColor Yellow
try {
    $pipVersion = pip --version 2>&1
    if ($LASTEXITCODE -eq 0) {
        Write-Host "  ✓ pip instalado: $pipVersion" -ForegroundColor Green
    } else {
        Write-Host "  ✗ pip no encontrado" -ForegroundColor Red
        Write-Host "    Ejecutar: python -m ensurepip --upgrade" -ForegroundColor Gray
        $errores++
    }
} catch {
    Write-Host "  ✗ pip no encontrado" -ForegroundColor Red
    Write-Host "    Ejecutar: python -m ensurepip --upgrade" -ForegroundColor Gray
    $errores++
}

# 4. Verificar estructura del repositorio
Write-Host "`n[4/7] Verificando estructura del proyecto..." -ForegroundColor Yellow
$directoriosRequeridos = @("docs", "config", "third_party", "env", "scripts")
$todosExisten = $true

foreach ($dir in $directoriosRequeridos) {
    if (Test-Path $dir) {
        Write-Host "  ✓ Directorio encontrado: $dir" -ForegroundColor Green
    } else {
        Write-Host "  ✗ Directorio no encontrado: $dir" -ForegroundColor Red
        $todosExisten = $false
        $errores++
    }
}

# 5. Verificar SDK de Unitree
Write-Host "`n[5/7] Verificando SDK de Unitree..." -ForegroundColor Yellow
if (Test-Path "third_party\unitree_sdk2_python") {
    Write-Host "  ✓ SDK de Unitree encontrado" -ForegroundColor Green
    
    # Verificar archivos clave del SDK
    if (Test-Path "third_party\unitree_sdk2_python\setup.py") {
        Write-Host "  ✓ setup.py encontrado" -ForegroundColor Green
    } else {
        Write-Host "  ⚠ setup.py no encontrado en el SDK" -ForegroundColor Yellow
        $advertencias++
    }
} else {
    Write-Host "  ✗ SDK de Unitree NO encontrado" -ForegroundColor Red
    Write-Host "    Ejecutar: cd third_party; git clone https://github.com/unitreerobotics/unitree_sdk2_python.git" -ForegroundColor Gray
    $errores++
}

# 6. Verificar módulos Python instalados
Write-Host "`n[6/7] Verificando módulos Python..." -ForegroundColor Yellow

# Verificar si está en un entorno virtual
$enVenv = $env:VIRTUAL_ENV -ne $null
if ($enVenv) {
    Write-Host "  ℹ Entorno virtual detectado: $env:VIRTUAL_ENV" -ForegroundColor Cyan
} else {
    Write-Host "  ⚠ No se detectó entorno virtual activo" -ForegroundColor Yellow
    Write-Host "    Recomendado: .\.venv\Scripts\Activate.ps1" -ForegroundColor Gray
    $advertencias++
}

# Verificar módulos clave
$modulosRequeridos = @("cyclonedds", "numpy", "cv2")
foreach ($modulo in $modulosRequeridos) {
    try {
        $resultado = python -c "import $modulo; print('OK')" 2>&1
        if ($resultado -match "OK") {
            Write-Host "  ✓ Módulo '$modulo' instalado" -ForegroundColor Green
        } else {
            Write-Host "  ✗ Módulo '$modulo' NO instalado" -ForegroundColor Red
            $errores++
        }
    } catch {
        Write-Host "  ✗ Módulo '$modulo' NO instalado" -ForegroundColor Red
        $errores++
    }
}

# Verificar SDK de Unitree
try {
    $resultado = python -c "import unitree_sdk2py; print('OK')" 2>&1
    if ($resultado -match "OK") {
        Write-Host "  ✓ SDK Unitree (unitree_sdk2py) instalado" -ForegroundColor Green
    } else {
        Write-Host "  ✗ SDK Unitree (unitree_sdk2py) NO instalado" -ForegroundColor Red
        Write-Host "    Ejecutar: cd third_party\unitree_sdk2_python; pip install -e ." -ForegroundColor Gray
        $errores++
    }
} catch {
    Write-Host "  ✗ SDK Unitree (unitree_sdk2py) NO instalado" -ForegroundColor Red
    Write-Host "    Ejecutar: cd third_party\unitree_sdk2_python; pip install -e ." -ForegroundColor Gray
    $errores++
}

# 7. Verificar Visual Studio Build Tools (opcional pero recomendado)
Write-Host "`n[7/7] Verificando Visual Studio Build Tools..." -ForegroundColor Yellow
$vsWhere = "${env:ProgramFiles(x86)}\Microsoft Visual Studio\Installer\vswhere.exe"
if (Test-Path $vsWhere) {
    $vsInstallations = & $vsWhere -products * -requires Microsoft.VisualStudio.Component.VC.Tools.x86.x64
    if ($vsInstallations) {
        Write-Host "  ✓ Visual Studio Build Tools detectado" -ForegroundColor Green
    } else {
        Write-Host "  ⚠ Visual Studio instalado pero componentes C++ no detectados" -ForegroundColor Yellow
        Write-Host "    Puede ser necesario para compilar algunas dependencias" -ForegroundColor Gray
        $advertencias++
    }
} else {
    Write-Host "  ⚠ Visual Studio Build Tools no detectado" -ForegroundColor Yellow
    Write-Host "    Puede ser necesario para compilar algunas dependencias" -ForegroundColor Gray
    Write-Host "    Descargar: https://visualstudio.microsoft.com/visual-cpp-build-tools/" -ForegroundColor Gray
    $advertencias++
}

# Resumen
Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  RESUMEN" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

if ($errores -eq 0 -and $advertencias -eq 0) {
    Write-Host "`n✅ TODO CORRECTO - Instalación completa" -ForegroundColor Green
    Write-Host "`nPróximos pasos:" -ForegroundColor Cyan
    Write-Host "  1. Leer: docs\02_configuracion_red.md" -ForegroundColor Gray
    Write-Host "  2. Leer: docs\03_primer_ejecucion_y_pruebas.md" -ForegroundColor Gray
} elseif ($errores -eq 0) {
    Write-Host "`n⚠ INSTALACIÓN COMPLETA CON ADVERTENCIAS" -ForegroundColor Yellow
    Write-Host "  Advertencias: $advertencias" -ForegroundColor Yellow
    Write-Host "`nLa instalación es funcional pero revisa las advertencias arriba." -ForegroundColor Gray
} else {
    Write-Host "`n❌ INSTALACIÓN INCOMPLETA" -ForegroundColor Red
    Write-Host "  Errores: $errores" -ForegroundColor Red
    Write-Host "  Advertencias: $advertencias" -ForegroundColor Yellow
    Write-Host "`nPor favor, corrige los errores antes de continuar." -ForegroundColor Gray
    Write-Host "Consulta: docs\01_instalacion_windows.md" -ForegroundColor Gray
}

Write-Host "`n========================================`n" -ForegroundColor Cyan

# Retornar código de salida apropiado
if ($errores -gt 0) {
    exit 1
} else {
    exit 0
}
