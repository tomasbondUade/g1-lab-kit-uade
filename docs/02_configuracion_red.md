# Configuración de red (solo Ethernet) — Unitree G1 / Go2 (Windows)

Este documento explica cómo preparar la PC para comunicarse con el robot **solo por cable Ethernet**.
Está pensado para uso en laboratorio/clase y para repetir el proceso de forma consistente.

---

## ✅ Objetivo

- Conectar la PC al robot por **Ethernet**
- Garantizar que ambos estén en la **misma red/subred**
- Verificar conectividad (link + IP + ping)
- Dejar una configuración fácil de replicar en múltiples PCs

---

## 1) Topologías recomendadas (elegir una)

### Opción A (recomendada para clase): **PC ↔ Switch ↔ Robot**
- Ideal si hay varios equipos o querés orden en laboratorio.
- Puede coexistir con un router (para DHCP) sin usar Wi-Fi.

**Ventajas:** escalable, menos problemas, más control.

### Opción B: **PC ↔ Robot (cable directo)**
- Útil para pruebas rápidas.
- Puede requerir configurar IPs manuales.

**Ventajas:** simple.
**Desventaja:** si no hay DHCP, hay que setear IP manual.

---

## 2) Lo que necesitás conocer (definir como estándar del laboratorio)

Completar (lo define el responsable del equipo/lab):

- Robot: ☐ G1 ☐ Go2
- Método de IP:
  - ☐ DHCP (router/switch administrado)
  - ☐ IP fija del robot (estática)
- IP del robot (si es fija): ______________________
- Subred (si es fija): ____________________________
- Puertos/servicios necesarios (si aplica): ___________________

> Recomendación: si se puede, usar **DHCP** y registrar la IP en una planilla/etiqueta por robot.

---

## 3) Paso a paso (Windows) — Verificación física

1) Conectar el cable Ethernet (PC ↔ switch ↔ robot o PC ↔ robot).
2) Verificar LEDs del puerto Ethernet:
   - ☐ Link encendido (conexión física)
   - ☐ Activity parpadea (tráfico)
3) En Windows, verificar que el adaptador esté activo:
   - Abrir: **Configuración → Red e Internet → Ethernet**
   - Confirmar: "Conectado"

---

## 4) Obtener la IP (dos escenarios)

### Escenario 1 — DHCP (recomendado)
Si hay router/switch con DHCP:

1) Conectar robot y PC al mismo switch/router.
2) En la PC, verificar que recibió IP:
   - PowerShell:
     ```powershell
     ipconfig
     ```
3) Obtener IP del robot:
   - Opción A: Revisar la tabla de DHCP del router (leases)
   - Opción B: si el robot aparece en vecinos ARP (a veces funciona):
     ```powershell
     arp -a
     ```
   - Opción C: si el laboratorio tiene una planilla/etiqueta, usar esa IP.

> **Importante:** si no podés identificar la IP del robot por DHCP, definan un estándar (ej. router del lab + etiqueta por robot) para que sea repetible.

---

### Escenario 2 — IP fija (PC ↔ robot / sin DHCP)
Si el robot usa una IP fija conocida, hay que poner la PC en la **misma subred**.

Ejemplo:
- Robot: `192.168.123.10`
- Subred: `255.255.255.0`
- PC: `192.168.123.20`

---

## 5) Configurar IP fija en Windows (si hace falta)

### Opción A (GUI)
1) Configuración → Red e Internet → Ethernet → **Cambiar opciones del adaptador**
2) Click derecho en el adaptador Ethernet → Propiedades
3) Seleccionar **Protocolo de Internet versión 4 (TCP/IPv4)** → Propiedades
4) Marcar "Usar la siguiente dirección IP":
   - IP: `_________________`
   - Máscara: `_________________` (ej. 255.255.255.0)
   - Puerta de enlace: (opcional) `_________________`

### Opción B (PowerShell) (solo si el lab lo adopta como estándar)
> Usar solo si el equipo docente decide estandarizar por script.

- Ver adaptadores:
  ```powershell
  Get-NetAdapter
  ```

---

## 6) Verificar conectividad

### 6.1 Ver tu IP
```powershell
ipconfig
```

### 6.2 Ping al robot
```powershell
ping <IP_DEL_ROBOT>
```

**Esperado:** respuesta con tiempo (ms).
Si falla, ver sección "Troubleshooting".

### 6.3 Ver vecinos (opcional)
```powershell
arp -a
```

### 6.4 Test de puerto (si aplica)

Si sabés un puerto del servicio:

```powershell
Test-NetConnection <IP_DEL_ROBOT> -Port <PUERTO>
```

---

## 7) Integración con el kit (configurar IP en el proyecto)

### 7.1 En .env

Cargar o actualizar:

```env
ROBOT_TYPE=G1  # o GO2
ROBOT_IP=<IP_DEL_ROBOT>
```

El archivo `.env` NO se sube al repositorio.

---

## 8) Troubleshooting (problemas comunes)

### A) No hay link (LED apagado / Windows dice "No conectado")

- Probar otro cable
- Probar otro puerto del switch
- Probar otra placa/adaptador USB-Ethernet
- Confirmar que el robot esté encendido y el puerto activo

### B) Ping falla pero hay link

- Verificar que PC y robot estén en la misma subred
  - Ej: PC `192.168.1.20` y robot `192.168.123.10` → NO están en la misma subred
- Si estás en IP fija: corregir IP/máscara
- Si hay firewall: permitir ICMP (solo si el lab lo requiere)

### C) No sé la IP del robot

- Usar DHCP con router del lab y revisar leases
- Definir estándar de IP fija y etiquetar el robot (recomendado para repetibilidad)
- Registrar la IP en la planilla/Excel del área

### D) Conecta intermitente

- Evitar adaptadores USB inestables
- Cambiar cable/puerto
- Usar switch dedicado para robots (sin saturación)
- Evitar cables muy largos o dañados

---

## 9) Referencia rápida de comandos (Windows)

```powershell
ipconfig
ping <IP_DEL_ROBOT>
arp -a
Get-NetAdapter
Test-NetConnection <IP_DEL_ROBOT> -Port <PUERTO>
```
