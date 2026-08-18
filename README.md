# 📡 WiFi Radar v1.0 — by Dev.Tley

> **Detector de intrusos en red local con alertas visuales y de voz en tiempo real.**

---

## ¿Qué es y cómo funciona?
**WiFi Radar** es un script en Python que monitorea tu red Wi-Fi en tiempo real. 

1. **Línea Base:** Al iniciar, escanea las IP activas en tu subred.
2. **Escaneo Continuo:** Realiza barridos buscando nuevos dispositivos.
3. **Alerta:** Si un equipo desconocido se conecta, cambia la consola a **rojo neón** y te avisa por voz mediante el altavoz.

---
PORFA LEEEE EL ARCHIVO ANTI ERRORES ANTES DE EJECUTAR EL SCRIPT 


## Instalación y Uso Rápido

```bash
# 1. Clonar el repositorio
git clone [https://github.com/Scnew12/wifi-radar.git](https://github.com/Scnew12/wifi-radar.git)
cd wifi-radar

# 2. Instalar el paquete de voz (Linux / Kali)
sudo apt update && sudo apt install speech-dispatcher -y

# 3. Ejecutar el script
python3 wifi_radar.py
