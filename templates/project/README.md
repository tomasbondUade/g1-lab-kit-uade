# [Nombre del Proyecto/TP]

> Template de proyecto para trabajos prácticos con G1/Go2 Lab Kit

---

## Información del Proyecto

- **Materia:** [Nombre de la materia]
- **Grupo:** [Número/Nombre del grupo]
- **Fecha de inicio:** [DD/MM/YYYY]
- **Fecha de entrega:** [DD/MM/YYYY]

### Integrantes

- [Apellido, Nombre - Legajo]
- [Apellido, Nombre - Legajo]
- [Apellido, Nombre - Legajo]

---

## Descripción

[Breve descripción del proyecto: qué hace, para qué sirve, qué problema resuelve]

---

## Objetivos

- [ ] [Objetivo 1]
- [ ] [Objetivo 2]
- [ ] [Objetivo 3]

---

## Estructura del Proyecto

```
proyecto/
├── README.md           (este archivo)
├── requirements.txt    (dependencias Python)
├── .gitignore
├── src/               (código fuente)
│   ├── __init__.py
│   ├── main.py        (punto de entrada)
│   └── [módulos].py
├── notebooks/         (análisis de datos)
│   └── analisis.ipynb
├── data/             (datos del proyecto)
│   └── sessions/     (sesiones grabadas)
├── docs/             (documentación adicional)
│   └── informe.md    (informe final)
└── tests/            (tests - opcional)
    └── test_*.py
```

---

## Instalación y Setup

### Requisitos previos

- Python 3.10+
- Lab Kit instalado (ver `docs/01_instalacion_windows.md`)
- Robot G1/GO2 (solo si se ejecuta en modo live)

### Instalación

```bash
# 1. Clonar/copiar este proyecto
cd trabajos/
cp -r templates/project/ mi_proyecto/
cd mi_proyecto/

# 2. Activar entorno virtual del lab kit
..\.venv\Scripts\Activate.ps1

# 3. Instalar dependencias adicionales (si las hay)
pip install -r requirements.txt

# 4. Configurar .env (si es necesario)
# Copiar y editar .env del lab kit principal
```

---

## Uso

### Modo Replay (sin robot)

```bash
# Usar datos de ejemplo
python src/main.py --mode replay --session data/sessions/ejemplo
```

### Modo Live (con robot)

⚠️ **Requiere protocolo de seguridad completo**

```bash
# Asegurar que .env tiene ROBOT_IP configurado
python src/main.py --mode live
```

---

## Desarrollo

### Estructura de código

**src/main.py**
- Punto de entrada del programa
- Parse de argumentos
- Inicialización de módulos

**src/[modulo].py**
- [Descripción del módulo]

### Flujo de ejecución

1. [Paso 1: Inicialización]
2. [Paso 2: Carga de datos / Conexión]
3. [Paso 3: Procesamiento]
4. [Paso 4: Resultados / Visualización]

---

## Testing

```bash
# Ejecutar tests (si se implementan)
pytest tests/

# Ejecutar con coverage
pytest --cov=src tests/
```

---

## Resultados

[Describir resultados obtenidos, incluir gráficos, métricas]

### Sesiones analizadas

| Sesión | Robot | Duración | Observaciones |
|--------|-------|----------|---------------|
| [20260120_1030_G1_...] | G1 | 10 min | [OK] |
| [...] | GO2 | 5 min | [OK] |

### Métricas

[Incluir métricas relevantes del proyecto]

---

## Problemas Conocidos

- [ ] [Problema 1 - Descripción]
- [ ] [Problema 2 - Descripción]

---

## TODOs

- [ ] [TODO 1]
- [ ] [TODO 2]
- [ ] [TODO 3]

---

## Referencias

[Documentación, papers, tutoriales usados]

1. [Referencia 1]
2. [Referencia 2]

---

## Licencia y Créditos

Proyecto realizado para [Nombre de la materia] - UADE

Basado en G1/Go2 Lab Kit template
