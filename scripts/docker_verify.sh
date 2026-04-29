#!/bin/bash

echo "============================================================"
echo "G1/Go2 Lab Kit - Verificación del entorno Docker"
echo "============================================================"

echo ""
echo "[1] Verificando Python..."
python3 --version

echo ""
echo "[2] Verificando Unitree SDK..."
python3 -c "import unitree_sdk2py; print('SDK Unitree OK')"

echo ""
echo "[3] Verificando dependencias principales..."
python3 -c "import numpy; print('NumPy OK')"
python3 -c "import cv2; print('OpenCV OK')"
python3 -c "import pandas; print('Pandas OK')"

echo ""
echo "[4] Verificando archivo .env..."
if [ -f ".env" ]; then
    echo ".env encontrado"
else
    echo ".env no encontrado. Copiando desde .env.example..."
    cp .env.example .env
fi

echo ""
echo "[5] Ejecutando Hello Robot..."
python3 examples/01_hello_robot.py

echo ""
echo "[6] Ejecutando Replay Demo..."
python3 examples/05_replay_demo.py

echo ""
echo "[7] Ejecutando Safe Stop en modo replay..."
python3 examples/04_safe_stop.py --mode replay

echo ""
echo "============================================================"
echo "Verificación finalizada"
echo "============================================================"
