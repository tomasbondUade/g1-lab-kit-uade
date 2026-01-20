# Seguridad y operación en aula — Unitree G1 / Go2

Este documento define el protocolo mínimo para operar robots Unitree en clases y actividades académicas.
Aplica a **G1 (humanoide)** y **Go2 (cuadrúpedo)**.

> ✅ Objetivo: operar de forma **segura, repetible y trazable**, minimizando riesgos para personas, equipos y el robot.

---

## 1) Principios obligatorios

1. **Seguridad primero:** si hay duda, se ejecuta **STOP**.
2. **Un solo controlador a la vez:** no se permiten comandos simultáneos de múltiples PCs.
3. **Perímetro respetado:** nadie ingresa al área de operación mientras el robot tenga movimiento habilitado.
4. **Deadman activo:** el movimiento solo se habilita con deadman / confirmación del operador.
5. **Trazabilidad:** todo uso debe registrarse con checklist (Forms) y, cuando corresponda, logs.

---

## 2) Roles y responsabilidades

### 2.1 Operador responsable (obligatorio)
- Única persona autorizada a:
  - habilitar/deshabilitar movimiento
  - iniciar rutinas
  - ejecutar stop seguro
- Verifica checklist pre-uso
- Decide finalizar sesión ante incidentes

### 2.2 Observador de seguridad (obligatorio en validación con robot)
- Controla el perímetro físico
- Da la señal de "OK para habilitar"
- Puede ordenar STOP si ve riesgo
- Evita que terceros se acerquen

### 2.3 Equipo (grupo de alumnos)
- Ejecuta scripts solo cuando tiene el token de control
- Mantiene distancia del robot
- Reporta inmediatamente cualquier comportamiento inesperado
- No toca el robot salvo indicación del operador

---

## 3) Perímetro y condiciones del espacio

### 3.1 Perímetro recomendado
- **Mínimo:** 2–3 m despejados alrededor del robot
- Sin objetos en el piso (mochilas, cables sueltos, sillas)
- Sin líquidos cerca

### 3.2 Señalización (recomendado)
- Cinta o marcación del perímetro
- Cartel visible: "Área de operación — No ingresar"

### 3.3 Condiciones del piso
- Preferir superficie plana y seca
- Evitar alfombras sueltas o piso resbaladizo

---

## 4) Stop y Deadman (conceptos operativos)

### 4.1 STOP (parada segura)
Se define un mecanismo de parada:
- **Software:** comando/función de "safe stop"
- **Físico** (si aplica): método/elemento disponible según el modelo y configuración del laboratorio

**Regla:** el operador y el observador deben saber exactamente cómo ejecutar STOP **en menos de 1 segundo**.

### 4.2 Deadman
El deadman es el "seguro" que evita movimiento involuntario.
Ejemplos:
- tecla presionada
- botón/trigger en joystick
- confirmación explícita en consola

**Regla:** sin deadman, no hay movimiento habilitado.

---

## 5) Token de control (un solo equipo controla)

Para evitar colisiones de comandos:
- Existe un **token de control** (físico o lógico)
- Solo el equipo con token puede enviar comandos
- El operador entrega y retira el token

### 5.1 Implementación recomendada
- **Modo simple:** "turno" definido por el operador (lista de grupos)
- **Modo formal:** un objeto físico (tarjeta) + registro en el checklist (grupo actual)

---

## 6) Flujo de operación (pre / durante / post)

### 6.1 Pre-uso (antes de habilitar movimiento)
1) Preparar el espacio
- [ ] perímetro despejado
- [ ] señal de "sin personas dentro"
- [ ] cables ordenados

2) Inspección rápida del robot
- [ ] estructura sin piezas flojas visibles
- [ ] sensores/cámara limpios (si aplica)
- [ ] batería en buen estado y con carga suficiente

3) Verificaciones de software y red
- [ ] PC autorizada conectada por Ethernet
- [ ] IP del robot confirmada (si aplica)
- [ ] ping responde (si aplica)
- [ ] entorno y SDK listos (según `docs/01` y `docs/03`)

4) Checklist obligatorio (Forms)
- Completar el formulario antes de iniciar:
  - **Checklist LSP Robots Unitree**: [LINK_AL_FORMS]

> ✅ Recomendación: si el uso es "solo replay", igual registrar sesión pero sin habilitar movimiento.

---

### 6.2 Durante el uso (operación controlada)
- El operador mantiene atención constante
- El observador controla el perímetro
- El equipo ejecuta scripts en modo incremental (de menor riesgo a mayor riesgo)

**Se ejecuta STOP inmediato si ocurre:**
- una persona ingresa al perímetro
- desconexión / pérdida de control
- comportamiento inesperado del robot
- riesgo de caída / inestabilidad
- comandos fuera de lo esperado
- batería baja crítica

**Logs (si aplica):**
- Activar logging
- Guardar sesión con nombre estándar:
  - `YYYYMMDD_HHMM_ROBOT_MATERIA_GRUPO`
  - Ej: `20260120_1030_G1_Prog1_G3`

---

### 6.3 Post-uso (cierre y condición del robot)
1) Cierre seguro
- [ ] deshabilitar movimiento
- [ ] apagar en orden
- [ ] retirar token de control

2) Guardado de evidencia
- [ ] logs guardados (si hubo)
- [ ] nombre de sesión registrado
- [ ] observaciones de la sesión registradas

3) Reporte de condición (obligatorio)
- Completar sección "Post-uso" del Forms (si hay daños/observaciones):
  - [LINK_AL_FORMS] (Sección "Post-uso: condición del robot")

4) Batería y almacenamiento
- [ ] definir si se carga batería o se guarda
- [ ] almacenar en lugar designado

---

## 7) Niveles de riesgo (guía rápida)

**Nivel 0 (sin robot):**
- replay, análisis de logs, notebooks, dashboard con datos grabados

**Nivel 1 (bajo):**
- telemetría, pruebas de conexión, postura/gesto simple (sin desplazamiento)

**Nivel 2 (medio):**
- teleoperación lenta, rutinas cortas, cambios de postura controlados

**Nivel 3 (alto):**
- movimientos continuos, pruebas prolongadas, visión + control en tiempo real

> Regla: iniciar siempre por Nivel 0/1 y subir gradualmente.

---

## 8) Registro y trazabilidad (qué se guarda y dónde)

Se recomienda un repositorio institucional de sesiones:
- Carpeta por sesión con nombre estándar
- Subcarpetas: `checklist/`, `logs/`, `media/`, `informe/`

Estructura sugerida (ejemplo):
- `Robots_Unitree/01_Sesiones/2026/G1/2026-01/20260120_1030_G1_Prog1_G3/`

---

## 9) Apéndice: checklist mínimo de 60 segundos (operador)

- [ ] perímetro OK
- [ ] batería OK (≥ umbral del laboratorio)
- [ ] stop accesible
- [ ] deadman probado
- [ ] token asignado
- [ ] ping/IP ok (si aplica)
- [ ] forms completado

---

## 10) Enlaces

- Instalación: `docs/01_instalacion_windows.md`
- Red Ethernet: `docs/02_configuracion_red.md`
- Primera ejecución y pruebas: `docs/03_primer_ejecucion_y_pruebas.md`
- Checklist LSP (Forms): [LINK_AL_FORMS]
