# Rúbricas y entregables — G1/Go2 Lab Kit (UADE)

Este documento define:
- qué debe entregar un equipo (alumnos) en actividades con robots Unitree
- convenciones de nombres (logs / sesiones / evidencias)
- una rúbrica base reutilizable por materias (programación, datos, IA, visión, robótica)
- criterios mínimos de aprobación ligados a seguridad

> ✅ Objetivo: estandarizar entregables para que sea fácil evaluar, comparar y reutilizar resultados entre materias y comisiones.

---

## 1) Entregables estándar (para cualquier actividad)

Cada actividad/trabajo práctico debe generar, como mínimo:

### 1.1 Evidencia mínima (obligatoria)
- **Checklist LSP completado** (Microsoft Forms) para la sesión
- **Nombre de sesión/log** definido (ver sección 2)
- **README corto** con: objetivo, cómo correr, resultados esperados

### 1.2 Entregables recomendados (según actividad)
- Logs (telemetría / eventos) en formato estándar
- Informe breve (Markdown/PDF) con conclusiones y métricas
- Video o capturas (si aplica) demostrando el resultado
- Código fuente en repo (estructura limpia + instrucciones)
- Notebook (si aplica) con análisis y gráficos

---

## 2) Convención de nombres (sesiones y archivos)

### 2.1 Nombre de sesión (obligatorio)
Formato:

`YYYYMMDD_HHMM_ROBOT_MATERIA_GRUPO`

Ejemplos:
- `20260120_1030_G1_Prog1_G3`
- `20260122_1400_GO2_CienciaDatos_G2`

**ROBOT:** `G1` o `GO2`  
**MATERIA:** abreviación simple (sin espacios)  
**GRUPO:** `G1`, `G2`, etc.

### 2.2 Estructura de carpeta por sesión (recomendada)
Dentro del repositorio de evidencias (Drive/SharePoint):

```text
<SESION>/
  checklist/
  logs/
  media/
  informe/
  codigo/   (opcional si el repo de código es otro)
```

### 2.3 Nombres de archivos sugeridos

**Logs:**
- `<SESION>_telemetry.csv` o `.parquet`
- `<SESION>_events.json`

**Informe:**
- `<SESION>_informe.md` o `.pdf`

**Video:**
- `<SESION>_demo.mp4`

**Capturas:**
- `<SESION>_img01.png`, `<SESION>_img02.png`

---

## 3) Criterios mínimos de aprobación (seguridad)

**No se aprueba** (o se invalida la demo) si:
- no existe checklist LSP de la sesión
- se habilitó movimiento sin deadman/stop definido
- se ejecutaron rutinas sin respetar perímetro o token de control
- hubo incidente grave sin reporte post-uso

> Seguridad no es opcional: es parte del criterio de evaluación.

---

## 4) Rúbrica base (100 puntos) — reutilizable

Esta rúbrica se adapta por materia. Los porcentajes/puntos pueden variar, pero la estructura base ayuda a estandarizar.

### 4.1 Seguridad y operación (20 pts)
- (10) Checklist LSP completo + protocolo aplicado
- (5) Token de control respetado / evidencia de turnos
- (5) Manejo de fallas (stop, timeouts, pérdida de red)

### 4.2 Calidad de software (25 pts)
- (10) Código claro y modular (nombres, estructura, funciones/clases)
- (5) Manejo de errores (reintentos, excepciones, logs)
- (5) Reproducibilidad (README de ejecución, configuración clara)
- (5) Buenas prácticas (formato, comentarios útiles, no hardcodear credenciales)

### 4.3 Funcionalidad técnica (25 pts)
- (10) Cumple el objetivo funcional (telemetría/control/visión/ML)
- (5) Robustez (no se rompe ante inputs comunes)
- (5) Rendimiento razonable (latencia/FPS/tasa de mensajes)
- (5) Integración correcta con SDK / arquitectura propuesta

### 4.4 Datos y métricas (20 pts)
- (10) Logs/dataset bien generados (esquema, timestamps, consistencia)
- (5) Métricas apropiadas (ej. error, FPS, accuracy, etc.)
- (5) Interpretación y conclusiones (no solo "corre", sino "qué aprendimos")

### 4.5 Presentación y documentación (10 pts)
- (5) README + guía de ejecución clara
- (5) Evidencia (video/capturas) + informe breve con resultados

---

## 5) Adaptaciones por tipo de materia (guía rápida)

### 5.1 Programación (Intro / Prog 1)

**Enfatizar:**
- claridad, manejo de errores, estructura, reproducibilidad

**Métricas sugeridas:**
- tiempo de ejecución, frecuencia de lectura, latencia básica

**Entregables mínimos:**
- script + README + captura/log

### 5.2 Algoritmos / Estructuras / POO

**Enfatizar:**
- estructuras (colas, prioridad), máquina de estados, diseño OO

**Métricas sugeridas:**
- complejidad / tiempos / latencia del scheduler

**Entregables mínimos:**
- código + tests unitarios + README

### 5.3 Programación avanzada / Arquitectura / Sistemas

**Enfatizar:**
- servicios, concurrencia, APIs, observabilidad

**Métricas sugeridas:**
- latencia end-to-end, tasa WS, estabilidad con reconexión

**Entregables mínimos:**
- backend + README + logs + checklist

### 5.4 Ciencia de Datos / ML / IA

**Enfatizar:**
- dataset, limpieza, features, evaluación

**Métricas sugeridas:**
- accuracy/F1, AUC, MAE, tasa de falsos positivos (anomalías)

**Entregables mínimos:**
- notebook + dataset/logs + reporte de métricas

### 5.5 Visión Artificial / Procesamiento de imagen

**Enfatizar:**
- pipeline, FPS, robustez, error de distancia/posición

**Métricas sugeridas:**
- FPS, tasa de pérdida de tracking, error promedio, latencia

**Entregables mínimos:**
- script + video demo + métricas

### 5.6 Robótica / Sistemas autónomos / RL

**Enfatizar:**
- percepción-decisión-control, seguridad y límites

**Métricas sugeridas:**
- estabilidad, error de seguimiento, episodios exitosos, tasa de recuperación

**Entregables mínimos:**
- diagrama de estados/BT + demo + logs

---

## 6) Plantillas recomendadas (para el repositorio)

Se recomienda mantener plantillas en `templates/`:
- `informe_tp.md` (estructura de informe)
- `checklist_demo.md` (pasos para demo)
- `rubrica_tp.xlsx` (rúbrica editable por cátedra)

**Estructura sugerida del informe (`informe_tp.md`):**
1. Objetivo
2. Contexto (robot, red, versión)
3. Metodología
4. Resultados y métricas
5. Problemas encontrados y soluciones
6. Conclusiones y próximos pasos
7. Links a código/datos/evidencia

---

## 7) Entrega sugerida (cómo presentar el trabajo)

### Opción A (recomendada): Repo + carpeta de sesión
- Repo Git con el código
- Carpeta por sesión con logs/media/informe
- Checklist Forms asociado

### Opción B: Todo en carpeta institucional
- Subcarpetas: `codigo/`, `logs/`, `media/`, `informe/`
- README general con instrucciones

---

## 8) Checklist de entrega (para alumnos)

Antes de entregar:

- [ ] Checklist LSP completado
- [ ] Sesión nombrada correctamente
- [ ] Logs guardados y subidos
- [ ] README con instrucciones
- [ ] Evidencia (video/capturas) si aplica
- [ ] Informe breve con métricas y conclusiones
- [ ] Si hubo incidentes, reporte post-uso completado

---

## 9) Para docentes: evaluación rápida (sugerencia)

Evaluación en 3 pasos:
1. **Validar seguridad/trazabilidad** (checklist + protocolo + logs)
2. **Validar objetivo funcional** (demo o replay + evidencia)
3. **Revisar calidad y métricas** (README + informe + repo)

---

## 10) Enlaces

- Seguridad y operación: [docs/04_seguridad_operacion_aula.md](04_seguridad_operacion_aula.md)
- Instalación: [docs/01_instalacion_windows.md](01_instalacion_windows.md)
- Red Ethernet: [docs/02_configuracion_red.md](02_configuracion_red.md)
- Primera ejecución: [docs/03_primer_ejecucion_y_pruebas.md](03_primer_ejecucion_y_pruebas.md)
- Troubleshooting: [docs/05_troubleshooting.md](05_troubleshooting.md)
- Checklist LSP (Forms): [LINK_AL_FORMS]
