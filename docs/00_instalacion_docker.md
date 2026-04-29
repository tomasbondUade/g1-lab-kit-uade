# Instalación del entorno Unitree con Docker

Esta guía permite levantar el entorno de trabajo del G1/Go2 Lab Kit usando Docker.

## Requisitos previos

Antes de comenzar, instalar:

- Git
- Docker
- Docker Compose

## Verificar Docker

Ejecutar:

    docker --version
    docker-compose --version

En algunas computadoras el comando puede ser:

    docker compose version

## Descargar el repositorio

Ejecutar:

    git clone https://github.com/tomasbondUade/g1-lab-kit-uade.git
    cd g1-lab-kit-uade

## Construir la imagen Docker

Ejecutar:

    docker-compose build

## Ejecutar la verificación completa

Ejecutar:

    docker-compose run --rm unitree-lab bash scripts/docker_verify.sh

Si todo está correcto, deberían aparecer mensajes como:

    SDK Unitree OK
    NumPy OK
    OpenCV OK
    Pandas OK
    Todo listo! El kit está configurado correctamente.
    Replay completado exitosamente
    TEST COMPLETADO EXITOSAMENTE

## Entrar manualmente al contenedor

Ejecutar:

    docker-compose run --rm unitree-lab

Dentro del contenedor se puede ejecutar:

    python3 examples/01_hello_robot.py
    python3 examples/05_replay_demo.py
    python3 examples/04_safe_stop.py --mode replay

## Nota importante

El entorno queda preparado para trabajar en modo replay sin robot conectado.

Para usar el robot físico en modo live, se requiere configurar correctamente la red, la interfaz de conexión y las condiciones de seguridad.
