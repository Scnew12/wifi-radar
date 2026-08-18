GUÍA ANTI-ERRORES (¡Léelo antes de ejecutar!)
Si vas a probar el script en una máquina virtual (Kali Linux / VirtualBox), evita estos 4 fallos típicos:

1. 🌐 La VM no detecta los celulares de tu casa
El problema: Si dejas la red en modo NAT, Kali estará aislado en una subred propia y no verá nada.

La solución: En VirtualBox ve a Configuración -> Red, cambia a Adaptador Puente (Bridged Adapter) y en la casilla Modo Promiscuo selecciona Permitir Todo.

2. 🚫 Error: Unable to locate package spd-say
El problema: Intentar instalar directamente spd-say falla porque no es el nombre del paquete.

La solución: El paquete oficial en los repositorios de Kali/Debian se llama speech-dispatcher:

Bash
sudo apt install speech-dispatcher -y
3. ❌ Error de red en Kali: Temporary failure resolving 'http.kali.org'
El problema: Al cambiar la VM a Adaptador Puente, Kali a veces pierde la resolución de nombres DNS.

La solución: Agrega manualmente el DNS de Cloudflare en Kali con esta línea:

Bash
echo "nameserver 1.1.1.1" | sudo tee /etc/resolv.conf
4. 🔐 Error de Git 403 Permission Denied al hacer Push
El problema: Windows tiene guardadas las credenciales de otra cuenta de GitHub en el Administrador de Credenciales.

La solución: Si usas VS Code, borra las credenciales genéricas de GitHub en Windows (git:https://github.com) y asegúrate de hacer un git commit antes de intentar el git push origin main.

👤 Autor
Desarrollado por Dev.Tley (Scnew12)

Proyecto creado para la serie "Scripts Útiles - Día 1"