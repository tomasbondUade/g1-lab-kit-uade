# Script de instalación automática
# G1/Go2 Lab Kit (UADE) - Windows
#
# Este script automatiza la instalación del entorno de desarrollo.
# Requisitos previos: Git y Python ya deben estar instalados.
#
# Uso: .\scripts\setup_windows.ps1

param(
    [switch]$SkipVenv = $false,
    [switch]$Force = $false
)

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  Instalación Automática Lab Kit" -ForegroundColor Cyan
Write-Host "  Unitree G1/Go2 - UADE" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

# Variables
$REPO_ROOT = $PSScriptRoot | Split-Path
$THIRD_PARTY = Join-Path $REPO_ROOT "third_party"
$SDK_PATH = Join-Path $THIRD_PARTY "unitree_sdk2_python"
$VENV_PATH = Join-Path $REPO_ROOT ".venv"
$REQUIREMENTS = Join-Path $REPO_ROOT "env\requirements.txt"

# Función para verificar comandos
function Test-Command {
    param($Command)
    try {
        Get-Command $Command -ErrorAction Stop | Out-Null
        return $true
    } catch {
        return $false
    }
}

# Función para mostrar progreso
function Write-Step {
    param($Step, $Total, $Message)
    Write-Host "`n[$Step/$Total] $Message" -ForegroundColor Yellow
}

# Verificaciones previas
Write-Host "Verificando requisitos previos...`n" -ForegroundColor Cyan

if (-not (Test-Command "git")) {
    Write-Host "❌ ERROR: Git no está instalado" -ForegroundColor Red
    Write-Host "   Instalar desde: https://git-scm.com/download/win" -ForegroundColor Gray
    exit 1
}
Write-Host "✓ Git encontrado" -ForegroundColor Green

if (-not (Test-Command "python")) {
    Write-Host "❌ ERROR: Python no está instalado" -ForegroundColor Red
    Write-Host "   Instalar desde: https://www.python.org/downloads/" -ForegroundColor Gray
    exit 1
}

# Verificar versión de Python
$pythonVersion = python --version 2>&1
$versionMatch = [regex]::Match($pythonVersion, "(\d+)\.(\d+)")
$major = [int]$versionMatch.Groups[1].Value
$minor = [int]$versionMatch.Groups[2].Value

if ($major -lt 3 -or ($major -eq 3 -and $minor -lt 8)) {
    Write-Host "❌ ERROR: Python versión muy antigua: $pythonVersion" -ForegroundColor Red
    Write-Host "   Se requiere Python >= 3.8" -ForegroundColor Gray
    exit 1
}
Write-Host "✓ Python encontrado: $pythonVersion" -ForegroundColor Green

if (-not (Test-Command "pip")) {
    Write-Host "❌ ERROR: pip no está instalado" -ForegroundColor Red
    Write-Host "   Ejecutar: python -m ensurepip --upgrade" -ForegroundColor Gray
    exit 1
}
Write-Host "✓ pip encontrado" -ForegroundColor Green

Write-Host "`n¡Requisitos previos OK! Iniciando instalación...`n" -ForegroundColor Green

# Paso 1: Clonar SDK de Unitree
Write-Step 1 5 "Descargando SDK de Unitree..."

if (Test-Path $SDK_PATH) {
    if ($Force) {
        Write-Host "⚠ SDK ya existe. Eliminando por parámetro -Force..." -ForegroundColor Yellow
        Remove-Item -Path $SDK_PATH -Recurse -Force
    } else {
        Write-Host "✓ SDK ya existe, omitiendo descarga" -ForegroundColor Green
        Write-Host "  (Usar -Force para forzar re-descarga)" -ForegroundColor Gray
    }
}

if (-not (Test-Path $SDK_PATH)) {
    Write-Host "Clonando repositorio de Unitree..." -ForegroundColor Cyan
    Push-Location $THIRD_PARTY
    try {
        git clone https://github.com/unitreerobotics/unitree_sdk2_python.git
        if ($LASTEXITCODE -ne 0) {
            Write-Host "❌ ERROR: Fallo al clonar SDK de Unitree" -ForegroundColor Red
            Pop-Location
            exit 1
        }
        Write-Host "✓ SDK descargado correctamente" -ForegroundColor Green
    } catch {
        Write-Host "❌ ERROR: $($_.Exception.Message)" -ForegroundColor Red
        Pop-Location
        exit 1
    }
    Pop-Location
}

# Paso 2: Crear entorno virtual
Write-Step 2 5 "Configurando entorno virtual..."

if ($SkipVenv) {
    Write-Host "⚠ Omitiendo creación de entorno virtual (parámetro -SkipVenv)" -ForegroundColor Yellow
} else {
    if (Test-Path $VENV_PATH) {
        if ($Force) {
            Write-Host "⚠ Entorno virtual ya existe. Eliminando por parámetro -Force..." -ForegroundColor Yellow
            Remove-Item -Path $VENV_PATH -Recurse -Force
        } else {
            Write-Host "✓ Entorno virtual ya existe" -ForegroundColor Green
            Write-Host "  (Usar -Force para recrear)" -ForegroundColor Gray
        }
    }
    
    if (-not (Test-Path $VENV_PATH)) {
        Write-Host "Creando entorno virtual..." -ForegroundColor Cyan
        python -m venv $VENV_PATH
        if ($LASTEXITCODE -ne 0) {
            Write-Host "❌ ERROR: Fallo al crear entorno virtual" -ForegroundColor Red
            exit 1
        }
        Write-Host "✓ Entorno virtual creado (.venv)" -ForegroundColor Green
    }
    
    # Activar entorno virtual
    Write-Host "Activando entorno virtual..." -ForegroundColor Cyan
    $activateScript = Join-Path $VENV_PATH "Scripts\Activate.ps1"
    
    # Verificar política de ejecución
    $policy = Get-ExecutionPolicy -Scope CurrentUser
    if ($policy -eq "Restricted") {
        Write-Host "⚠ Ajustando política de ejecución de PowerShell..." -ForegroundColor Yellow
        Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
    }
    
    & $activateScript
    Write-Host "✓ Entorno virtual activado" -ForegroundColor Green
}

# Paso 3: Actualizar pip
Write-Step 3 5 "Actualizando pip..."
python -m pip install --upgrade pip --quiet
if ($LASTEXITCODE -ne 0) {
    Write-Host "⚠ Advertencia: No se pudo actualizar pip" -ForegroundColor Yellow
} else {
    Write-Host "✓ pip actualizado" -ForegroundColor Green
}

# Paso 4: Instalar SDK de Unitree
Write-Step 4 5 "Instalando SDK de Unitree..."

Write-Host "Instalando dependencias del SDK (esto puede tardar varios minutos)..." -ForegroundColor Cyan
Push-Location $SDK_PATH
pip install -e .
$sdkInstallResult = $LASTEXITCODE
Pop-Location

if ($sdkInstallResult -ne 0) {
    Write-Host "❌ ERROR: Fallo al instalar SDK de Unitree" -ForegroundColor Red
    Write-Host "`nIntenta manualmente:" -ForegroundColor Gray
    Write-Host "  cd third_party\unitree_sdk2_python" -ForegroundColor Gray
    Write-Host "  pip install -e ." -ForegroundColor Gray
    exit 1
}
Write-Host "✓ SDK de Unitree instalado" -ForegroundColor Green

# Paso 5: Instalar dependencias adicionales
Write-Step 5 6 "Instalando dependencias adicionales del kit..."

if (Test-Path $REQUIREMENTS) {
    Write-Host "Instalando desde requirements.txt..." -ForegroundColor Cyan
    pip install -r $REQUIREMENTS
    if ($LASTEXITCODE -ne 0) {
        Write-Host "⚠ Advertencia: Algunos paquetes no se instalaron correctamente" -ForegroundColor Yellow
    } else {
        Write-Host "✓ Dependencias adicionales instaladas" -ForegroundColor Green
    }
} else {
    Write-Host "⚠ No se encontró requirements.txt, omitiendo" -ForegroundColor Yellow
}

# Paso 6: Crear archivo .env si no existe
Write-Step 6 6 "Configurando archivo .env..."

$envExample = Join-Path $REPO_ROOT "env\.env.example"
$envFile = Join-Path $REPO_ROOT ".env"

if (Test-Path $envExample) {
    if (-not (Test-Path $envFile)) {
        Write-Host "Creando archivo .env desde template..." -ForegroundColor Cyan
        Copy-Item $envExample $envFile
        Write-Host "✓ Archivo .env creado" -ForegroundColor Green
        Write-Host "  ⚠ IMPORTANTE: Edita .env con tus configuraciones" -ForegroundColor Yellow
    } else {
        Write-Host "✓ Archivo .env ya existe" -ForegroundColor Green
    }
} else {
    Write-Host "⚠ No se encontró .env.example" -ForegroundColor Yellow
}

# Verificación final
Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  VERIFICACIÓN FINAL" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

Write-Host "Verificando módulos instalados..." -ForegroundColor Cyan

$modulosRequeridos = @("cyclonedds", "numpy", "cv2", "unitree_sdk2py")
$todosOK = $true

foreach ($modulo in $mo.venv\Scripts\Activate.ps1`n" -ForegroundColor White
    Write-Host "  2. Editar configuración:" -ForegroundColor Gray
    Write-Host "     Edita .env con tus valores (IP del robot, etc.)`n" -ForegroundColor White
    Write-Host "  3. Verificar instalación:" -ForegroundColor Gray
    Write-Host "     .\scripts\verify_setup.ps1`n" -ForegroundColor White
    Write-Host "  4"  ✓ $modulo" -ForegroundColor Green
    } else {
        Write-Host "  ✗ $modulo" -ForegroundColor Red
        $todosOK = $false
    }
}

# Resumen final
Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  RESUMEN DE INSTALACIÓN" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

if ($todosOK) {
    Write-Host "✅ INSTALACIÓN COMPLETA Y EXITOSA" -ForegroundColor Green
    Write-Host "`nPróximos pasos:" -ForegroundColor Cyan
    Write-Host "  1. Activar entorno virtual (si no está activo):" -ForegroundColor Gray
    Write-Host "     .\venv\Scripts\Activate.ps1`n" -ForegroundColor White
    Write-Host "  2. Verificar instalación:" -ForegroundColor Gray
    Write-Host "     .\scripts\verify_setup.ps1`n" -ForegroundColor White
    Write-Host "  3. Leer documentación:" -ForegroundColor Gray
    Write-Host "     docs\02_configuracion_red.md" -ForegroundColor White
    Write-Host "     docs\03_primer_ejecucion_y_pruebas.md`n" -ForegroundColor White
} else {
    Write-Host "⚠ INSTALACIÓN COMPLETA CON ERRORES" -ForegroundColor Yellow
    Write-Host "`nAlgunos módulos no se instalaron correctamente." -ForegroundColor Gray
    Write-Host "Revisa los mensajes de error arriba y consulta:" -ForegroundColor Gray
    Write-Host "  docs\01_instalacion_windows.md" -ForegroundColor White
    Write-Host "  docs\05_troubleshooting.md`n" -ForegroundColor White
}

Write-Host "========================================`n" -ForegroundColor Cyan
