# Templates — G1/Go2 Lab Kit

Plantillas reutilizables para trabajos prácticos, informes y proyectos.

## Contenido

```
templates/
  report/           # Templates de informes de práctica
  project/          # Templates de proyectos/TPs
  analysis/         # Templates de análisis de datos
  forms/            # Templates de formularios y checklists
```

## Uso

### Para estudiantes (trabajos prácticos)

1. **Copiar template** a tu directorio de trabajo:
   ```bash
   # Ejemplo: copiar template de proyecto
   cp -r templates/project/ mis_trabajos/tp1_tracking/
   ```

2. **Completar** según la consigna:
   - Editar README.md con tu información
   - Implementar código en los archivos indicados
   - Completar informe con resultados

3. **Naming estándar**:
   ```
   YYYYMMDD_MATERIA_GRUPO_TEMA
   Ejemplo: 20260120_Prog1_G3_Tracking
   ```

### Para docentes

Los templates sirven para:
- Estandarizar entregables
- Facilitar corrección (estructura uniforme)
- Enseñar buenas prácticas (documentación, testing)
- Acelerar inicio de prácticas (menos setup, más foco en objetivos)

## Templates disponibles

### 📄 report/ - Informe de Práctica
Template de informe en Markdown para documentar sesiones de laboratorio.

**Incluye:**
- Portada con datos del grupo
- Secciones estándar (objetivos, desarrollo, resultados, conclusiones)
- Checklist de seguridad
- Formato para adjuntar datos/código

**Uso:**
```bash
cp templates/report/informe_template.md trabajos/20260120_Prog1_G3_informe.md
```

---

### 🚀 project/ - Proyecto/TP
Template de proyecto completo con estructura de código.

**Incluye:**
- README.md con instrucciones
- Estructura src/ para código
- Notebook de análisis
- requirements.txt
- .gitignore

**Uso:**
```bash
cp -r templates/project/ trabajos/tp1_tracking/
cd trabajos/tp1_tracking/
# Completar según consigna
```

---

### 📊 analysis/ - Análisis de Datos
Template de notebook para análisis de sesiones.

**Incluye:**
- Notebook pre-estructurado
- Secciones de carga, análisis, visualización
- Ejemplos de gráficos
- Exportación de resultados

**Uso:**
```bash
cp templates/analysis/analisis_template.ipynb trabajos/analisis_sesion_1.ipynb
```

---

### ✅ forms/ - Formularios y Checklists
Templates de checklists y formularios (Markdown).

**Incluye:**
- Checklist pre-práctica (LSP)
- Checklist post-práctica
- Formulario de reporte de incidentes

**Uso:**
- Imprimir o usar digitalmente antes/después de cada sesión
- Archivar en carpeta de la sesión

---

## Naming y organización

### Para entregas individuales/grupales:

```
trabajos/
  20260120_Prog1_G3_Tracking/
    README.md
    src/
    notebook_analisis.ipynb
    informe.md
    data/ (si aplica)
```

### Para informes de sesión:

```
data/local/sessions/20260120_1030_G1_Prog1_G3/
  metadata.json
  telemetry.csv
  informe_sesion.md  (opcional, copia de template)
```

## Tips

- **No modificar templates originales** - siempre copiar antes de usar
- **Usar naming estándar** para facilitar organización
- **Completar README.md** en cada proyecto (instrucciones de ejecución)
- **Incluir requirements.txt** si agregás dependencias
- **Limpiar notebooks** antes de entregar (Kernel → Restart & Clear Output)

## Personalización

Los docentes pueden:
1. Modificar templates según necesidades del curso
2. Crear templates adicionales para TPs específicos
3. Agregar secciones o quitar las no necesarias

**Recomendación:** mantener estructura base (README, src/, docs/) para consistencia.
