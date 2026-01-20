# Configuración (YAML)

Este proyecto usa archivos YAML para centralizar configuraciones sin hardcodear valores en el código.

## Cómo se usan

1) Copiá los `.example.yaml` a archivos reales (sin `.example`), si el módulo lo requiere:
   - `robot_config.example.yaml` → `robot_config.yaml`
   - `network.example.yaml` → `network.yaml`
   - `limits.example.yaml` → `limits.yaml`

2) Ajustá valores según el laboratorio (Ethernet, IP, límites de seguridad).

> **Nota:** valores sensibles (por ejemplo IP del robot si cambia) se pueden mantener en `.env`.
> Los YAML son para parámetros "estructurales" y límites del modo clase.

## Archivos de configuración

### `robot_config.yaml`
Configuración general del robot: tipo, SDK, telemetría, logging.

### `network.yaml`
Configuración de red (solo Ethernet): interfaz, direccionamiento, healthcheck.

### `limits.yaml`
Límites de seguridad para operación en aula (modo clase): deadman, safe stop, motion limits.

## Importante

⚠️ **NO subir** archivos `*.yaml` (sin `.example`) a Git.
Solo subir los `.example.yaml` como plantillas.
