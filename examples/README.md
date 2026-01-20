# Examples — G1/Go2 Lab Kit

Estos ejemplos son el "punto de entrada" para actividades de clase.
Cada ejemplo intenta ser:
- simple
- reproducible
- seguro (cuando hay robot real)

## Requisitos previos
- Instalación completada: `docs/01_instalacion_windows.md`
- Red Ethernet configurada: `docs/02_configuracion_red.md`
- Primera prueba realizada: `docs/03_primer_ejecucion_y_pruebas.md`
- Protocolo de seguridad: `docs/04_seguridad_operacion_aula.md`

## Modos de ejecución
- **Replay (sin robot):** usa datos en `data/samples/`
- **Live (con robot):** requiere Ethernet + checklist LSP + operador/observador

## Variables esperadas (.env)
- `ROBOT_TYPE=G1` o `GO2`
- `ROBOT_IP=<ip_del_robot>` (solo live)
- `SESSION_NAME=YYYYMMDD_HHMM_ROBOT_MATERIA_GRUPO` (recomendado)
- `DATA_MODE=replay` o `live` (opcional, si lo implementamos)

---

## Ejemplos disponibles

### 01_hello_robot.py
**Objetivo:** validar que el kit está operativo (entorno + SDK + paths) y mostrar estado mínimo.
- Replay: OK
- Live: opcional (solo valida conectividad / configuración)

**Salida esperada:** confirmación de configuración cargada + SDK detectado.

---

### 02_telemetry_check.py
**Objetivo:** verificar lectura de telemetría (estado básico).
- Replay: usa una sesión sample
- Live: suscribe y muestra valores (batería/IMU/joints según se implemente)

**Salida esperada:** imprime valores o estadísticas básicas.

---

### 03_log_session.py
**Objetivo:** generar una sesión de logs con naming estándar.
- Replay: genera un "log simulado"
- Live: guarda telemetría real (si está habilitado)

**Salida esperada:** crea carpeta/archivo de sesión en `data/local/sessions/` (o donde se configure).

---

### 04_safe_stop.py
**Objetivo:** probar el stop seguro.
- Replay: simula stop
- Live: prueba stop en condiciones controladas (solo operador)

> ⚠️ Requiere protocolo de seguridad y perímetro despejado.

---

### 05_replay_demo.py
**Objetivo:** demostrar el flujo completo sin robot:
carga logs sample → analiza → muestra resumen.
- Replay: OK
- Live: no aplica

**Salida esperada:** resumen (duración, min/max/promedio de algunos campos, etc.).

---

## Convención de nombres (sesión/log)
`YYYYMMDD_HHMM_ROBOT_MATERIA_GRUPO`

Ej: `20260120_1030_G1_Prog1_G3`

## Soporte
Si algo falla, consultar:
- `docs/05_troubleshooting.md`
y adjuntar el error completo + capturas.
