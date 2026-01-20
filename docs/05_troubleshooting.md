# Troubleshooting — G1/Go2 Lab Kit (Windows)

Este documento reúne soluciones rápidas para los problemas más comunes al instalar o ejecutar el kit en Windows.

> ✅ Regla de oro: si algo falla, primero verificar **(1) venv activa**, **(2) SDK en third_party**, **(3) red Ethernet (si hay robot)**.

---

## 🧭 1) Checklist rápido (30 segundos)

Desde la raíz del repo:

- [ ] Estoy en `g1-lab-kit-uade/`
- [ ] Veo `(.venv)` en la terminal (entorno activado)
- [ ] Existe `third_party/unitree_sdk2_python/`
- [ ] Si hay robot: `ping <IP_DEL_ROBOT>` responde

Comandos:

```powershell
cd <ruta>\g1-lab-kit-uade
.\.venv\Scripts\activate
dir third_party\unitree_sdk2_python
ping <IP_DEL_ROBOT>
```

---

## 🐍 2) Problemas con Python

### 2.1 python no se reconoce / abre Microsoft Store

**Síntoma:** `python --version` falla o abre la store.

**Solución:**
1. Instalar Python desde [python.org](https://www.python.org/)
2. Marcar **Add Python to PATH**
3. Cerrar y abrir PowerShell
4. Reprobar:
   ```powershell
   python --version
   ```

### 2.2 Tengo varias versiones de Python y usa la incorrecta

**Solución:**

Ver ubicación:
```powershell
where python
python --version
```

Usar el Python correcto al crear venv (según el caso).

---

## 📦 2.3 Error SSL al instalar paquetes (pip)

**Síntoma:** 
```
SSL: CERTIFICATE_VERIFY_FAILED
certificate verify failed: self signed certificate in certificate chain
```

**Causa:** Red corporativa/universitaria con proxy o certificados propios (común en UADE).

**Solución rápida:**
```powershell
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org <paquete>
```

**Ejemplo:**
```powershell
# Instalar SDK
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -e third_party/unitree_sdk2_python

# Instalar requirements
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r env/requirements.txt
```

**Solución permanente** (configurar pip):
```powershell
pip config set global.trusted-host "pypi.org files.pythonhosted.org"
```

---

## 🧪 3) Problemas con entorno virtual (venv)

### 3.1 activate.ps1 bloqueado por políticas

**Solución** (solo en esta terminal):
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\activate
```

### 3.2 No aparece (.venv) luego de activar

**Solución:**

Confirmar que existe `.venv` y el script:
```powershell
dir .venv
dir .venv\Scripts\activate.ps1
```

Si no existe, recrearlo:
```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

---

## 📦 4) Problemas con pip / dependencias

### 4.1 pip install -r env\requirements.txt falla

**Soluciones comunes:**

Actualizar pip:
```powershell
python -m pip install --upgrade pip
```

Reintentar:
```powershell
pip install -r env\requirements.txt
```

### 4.2 "Permission denied" o errores raros

**Solución:**
- Asegurate de tener venv activa (para no instalar global).
- Ejecutar PowerShell como usuario normal (no suele requerir admin).

---

## 🧩 5) Problemas con el SDK de Unitree

### 5.1 No existe third_party/unitree_sdk2_python/

**Solución:**

Seguir `third_party/README.md` y clonar:
```powershell
cd third_party
git clone https://github.com/unitreerobotics/unitree_sdk2_python.git
cd ..
```

### 5.2 Está descargado pero la estructura no coincide

**Esperado:**
- `third_party/unitree_sdk2_python/unitree_sdk2py/`
- `third_party/unitree_sdk2_python/example/`

**Verificar:**
```powershell
dir third_party\unitree_sdk2_python
dir third_party\unitree_sdk2_python\unitree_sdk2py
dir third_party\unitree_sdk2_python\example
```

### 5.3 Errores al ejecutar ejemplos del SDK

**Reglas:**

Ejecutar ejemplos desde la carpeta del SDK (para rutas relativas):
```powershell
cd third_party\unitree_sdk2_python
python example\helloworld\subscriber.py
```

Revisar README del SDK por prerequisitos de red/puertos.

---

## 🌐 6) Problemas de red (Ethernet)

Para detalles completos, ver [docs/02_configuracion_red.md](02_configuracion_red.md).

### 6.1 No hay link (Windows dice "No conectado")

**Solución:**
- Cambiar cable
- Cambiar puerto del switch
- Probar otro adaptador Ethernet (si es USB)
- Confirmar que el robot esté encendido

### 6.2 Tengo IP 169.254.x.x

**Significa:** no recibiste IP (sin DHCP).

**Solución:**
- Si el laboratorio usa DHCP, revisar router/switch.
- Si es conexión directa o IP fija, configurar IP manual según estándar del lab.

Ver IP:
```powershell
ipconfig
```

### 6.3 ping <IP_DEL_ROBOT> no responde

**Solución:**
- Confirmar IP del robot y subred
- Confirmar que PC y robot están en la misma subred
- Probar `arp -a` para ver vecinos:
  ```powershell
  arp -a
  ```
- Si el firewall bloquea ICMP (solo para test), probar temporalmente con permiso o desactivar (según política del lab).

### 6.4 ping responde pero se corta / latencia alta

**Solución:**
- Usar switch dedicado y cable corto
- Evitar adaptadores USB de mala calidad
- Revisar cables dañados o flojos
- Evitar múltiples redes en paralelo (Wi-Fi activo + Ethernet)

---

## 🧠 7) Problemas con .env / configuración

### 7.1 No existe .env

**Solución:**
```powershell
copy env\.env.example .env
```

Editar `.env` y completar:
```env
ROBOT_TYPE=G1  # o GO2
ROBOT_IP=...
```

### 7.2 Cambié la IP y sigue intentando la vieja

**Solución:**
- Confirmar que editaste el `.env` correcto (en la raíz del repo)
- Cerrar y abrir terminal
- Reintentar ejecución

---

## ▶️ 8) Problemas al ejecutar "primeras pruebas" (docs/03)

### 8.1 El ejemplo helloworld no corre

**Solución:**

Asegurate de estar dentro del SDK:
```powershell
cd third_party\unitree_sdk2_python
python example\helloworld\subscriber.py
```

Abrir otra terminal y correr el publisher.

### 8.2 Error "Module not found"

**Solución:**
- Confirmar venv activa
- Confirmar que el SDK existe
- Ejecutar desde el directorio correcto (SDK o raíz según corresponda)

---

## 🧾 9) Qué información adjuntar cuando pedís ayuda

Copiar y pegar (ideal):

**Versiones:**
```powershell
python --version
pip --version
git --version
```

**Estructura SDK:**
```powershell
dir third_party\unitree_sdk2_python
dir third_party\unitree_sdk2_python\unitree_sdk2py
dir third_party\unitree_sdk2_python\example
```

**Red (si hay robot):**
```powershell
ipconfig
ping <IP_DEL_ROBOT>
```

**El error completo** (texto o captura)

---

## 📌 10) Referencia rápida de comandos (Windows)

```powershell
# Activar venv
.\.venv\Scripts\activate

# Ver IPs
ipconfig

# Probar conectividad al robot
ping <IP_DEL_ROBOT>

# Ver tabla ARP
arp -a

# Instalar dependencias
pip install -r env\requirements.txt
```
