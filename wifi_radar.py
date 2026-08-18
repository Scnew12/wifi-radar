#!/usr/bin/env python3
"""
WiFi Radar v1.0 - Intruder Detection System
Created by Dev.Tley
"""

import sys
import time
import re
import shutil
import subprocess
import argparse
import platform
from typing import Set

# ==========================================
# PALETA DE COLORES NEÓN (KALI / CYBERPUNK)
# ==========================================
NEON_CYAN     = "\033[38;5;51m"
NEON_GREEN    = "\033[38;5;82m"
NEON_PURPLE   = "\033[38;5;141m"
BRIGHT_RED    = "\033[38;5;196m"
BRIGHT_YELLOW = "\033[38;5;226m"
COLOR_BOLD    = "\033[1m"
COLOR_RESET   = "\033[0m"


def mostrar_banner() -> None:
    
    banner = f"""{NEON_CYAN}{COLOR_BOLD}
   ██╗  ██╗██╗███████╗██╗    ██████╗  █████╗ ██████╗  █████╗ ██████╗ 
   ██║  ██║██║██╔════╝██║    ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗
   ███████║██║█████╗  ██║    ██████╔╝███████║██║  ██║███████║██████╔╝
   ██╔══██║██║██╔══╝  ██║    ██╔══██╗██╔══██║██║  ██║██╔══██║██╔══██╗
   ██║  ██║██║██║     ██║    ██║  ██║██║  ██║██████╔╝██║  ██║██║  ██║
   ╚═╝  ╚═╝╚═╝╚═╝     ╚═╝    ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
{NEON_PURPLE}   =================================================================
                            by Dev.Tley
   ================================================================={COLOR_RESET}
"""
    print(banner)


def hablar(mensaje: str) -> None:
    """Motor de síntesis de voz según la plataforma."""
    if shutil.which("termux-tts-speak"):
        subprocess.run(["termux-tts-speak", mensaje], check=False)
        return
    if shutil.which("spd-say"):
        subprocess.run(["spd-say", "-l", "es", mensaje], check=False)
        return
    if shutil.which("espeak"):
        subprocess.run(["espeak", "-v", "es", mensaje], check=False)
        return
    if platform.system() == "Darwin" and shutil.which("say"):
        subprocess.run(["say", mensaje], check=False)
        return
    sys.stdout.write("\a")
    sys.stdout.flush()


def obtener_dispositivos_activos() -> Set[str]:
    """Extrae las direcciones IP activas de la tabla ARP."""
    ips = set()
    try:
        if shutil.which("ip"):
            salida = subprocess.check_output(["ip", "neigh"], text=True, stderr=subprocess.DEVNULL)
            for linea in salida.splitlines():
                if "FAILED" not in linea:
                    m = re.search(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", linea)
                    if m:
                        ips.add(m.group(1))
        elif shutil.which("arp"):
            salida = subprocess.check_output(["arp", "-a"], text=True, stderr=subprocess.DEVNULL)
            matches = re.findall(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", salida)
            ips.update(matches)
    except Exception:
        pass
    return ips


def iniciar_escaneo(intervalo: int) -> None:
    """Ciclo principal de monitoreo en tiempo real."""
    mostrar_banner()
    
    print(f"{BRIGHT_YELLOW}[*] Escaneando segmento de red local...{COLOR_RESET}")
    dispositivos_conocidos = obtener_dispositivos_activos()
    
    print(f"{NEON_GREEN}[✔] Dispositivos seguros detectados: {len(dispositivos_conocidos)}{COLOR_RESET}")
    for ip in dispositivos_conocidos:
        print(f"   ├─ {NEON_CYAN}{ip}{COLOR_RESET}")

    print(f"\n{NEON_PURPLE}[🛰] RADAR ACTIVO | Monitoreando cada {intervalo}s...{COLOR_RESET}\n")
    hablar("Radar activo. Monitoreando red.")

    try:
        while True:
            time.sleep(intervalo)
            dispositivos_actuales = obtener_dispositivos_activos()
            nuevas_conexiones = dispositivos_actuales - dispositivos_conocidos

            if nuevas_conexiones:
                for ip_intruso in nuevas_conexiones:
                    alerta_txt = f"{BRIGHT_RED}{COLOR_BOLD}[ ALERTA DE INTRUSO] -> IP: {ip_intruso}{COLOR_RESET}"
                    print(alerta_txt)
                    hablar(f"Alerta. Nuevo dispositivo detectado: {ip_intruso}")
                    dispositivos_conocidos.add(ip_intruso)

    except KeyboardInterrupt:
        print(f"\n{BRIGHT_YELLOW}[!] Radar detenido por Dev.Tley.{COLOR_RESET}")
        sys.exit(0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="WiFi Radar by Dev.Tley")
    parser.add_argument("-i", "--intervalo", type=int, default=3, help="Intervalo en segundos")
    args = parser.parse_args()
    iniciar_escaneo(intervalo=args.intervalo)

    