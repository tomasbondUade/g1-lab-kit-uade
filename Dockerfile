FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV CYCLONEDDS_HOME=/opt/cyclonedds/install
ENV PATH="${CYCLONEDDS_HOME}/bin:${PATH}"
ENV LD_LIBRARY_PATH="${CYCLONEDDS_HOME}/lib:${LD_LIBRARY_PATH}"
ENV PYTHONPATH="/workspace:/opt/unitree_sdk2_python:${PYTHONPATH}"

RUN apt update && apt install -y \
    python3 \
    python3-pip \
    python3-venv \
    git \
    cmake \
    build-essential \
    wget \
    curl \
    nano \
    iproute2 \
    net-tools \
    iputils-ping \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt

RUN git clone -b releases/0.10.x https://github.com/eclipse-cyclonedds/cyclonedds.git && \
    cd cyclonedds && \
    mkdir build install && \
    cd build && \
    cmake .. -DCMAKE_INSTALL_PREFIX=../install && \
    cmake --build . --target install

RUN git clone https://github.com/unitreerobotics/unitree_sdk2_python.git && \
    cd unitree_sdk2_python && \
    pip3 install --upgrade pip && \
    pip3 install -e .

WORKDIR /workspace

COPY env/requirements.txt /tmp/requirements.txt

RUN pip3 install -r /tmp/requirements.txt || true

COPY . /workspace

CMD ["/bin/bash"]
