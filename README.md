# 📡🕵️**Sniffer de paquetes de red**🕵️📡

**Este proyecto es un sniffer de paquetes de red experimental desarrollado para sistemas GNU/Linux con el cual se puede realizar la captura del tráfico red haciendo uso de alguna de las interfaces de red del sistema.**

## 🚧🔨**Proyecto en desarrollo**⚙️🛠️ 

Este proyecto se encuentra en proceso de desarrollo constante, por lo cual es seguro que se realicen varias actualizaciones constantes en cortos períodos de tiempo.

**Una vez que este proyecto tenga una versión 100% estable para su uso este apartado será removido.**

## 🚀 **Características**
- ✅ Captura del tráfico de red a nivel de **capa de enlace de datos** y de **capa de red**.
- ✅ Soporte **por el momento** para únicamente sniffear tráfico por medio de **interfaces de red Ethernet**.
- ✅ Soporte para **Tramas MAC de Ethernet** y para el protocolo **IPv4** de la suite de protocolos **TCP/IP**.

## ⚠️ **Advertencia**

- 🚨 **Este programa ha sido desarrollado únicamente para distribuciones GNU/Linux debido a que hace uso de BSD sockets API y que interactúa con llamadas al sistema específicas para sistemas que utilizan el kernel de Linux.**

- 🚨 **Por el momento** el proyecto solo cuenta con soporte para capturar tráfico por medio de **interfaces físicas de red Ethernet**.

    Estamos trabajando arduamente que el día **Lunes 17 de Marzo de 2025** sea agregado oficialmente el soporte para sniffear tráfico de red por medio de **interfaces físicas de red Wi-Fi** y a traves de **interfaces loopback**.


## 🛠 Uso

Antes de ejecutar la aplicación es importante la configuración de un entorno virtual donde se ejecute de manera aislada la aplicación.

En la raíz del proyecto hay un archivo denominado **setup.sh** que se encarga de esto.

Estando en la raíz del proyecto, ejecuta este script de configuración con alguna de las dos siguientes maneras.

```bash
🐧user@host:~$ . ./setup.sh
```

```bash
🐧user@host:~$ source ./setup.sh
```

Una vez que el script se haya ejecutado correctamente, automáticamente estarás dentro y con el entorno virtual para poder ejecutar la aplicación.

Si quieres activar manualmente el entorno virtual de la aplicación, estando dentro del directorio que representa dicho entorno debes ejecutar lo siguiente.

```bash
🐧user@host:~$ source bin/activate
```

Para desactivar el entorno virtual utilizado por la aplicación únicamente necesitas el siguiente comando.

```bash
🐧user@host:~$ deactivate
```

🚨 **Si lo prefieres puede echar un ojo a los comandos del script y ejecutarlos por ti mismo**

⚠️ **Este proyecto no utiliza ninguna dependencia externa, por lo cual podría ejecutarse sin ningún problemas fuera de un entorno virutal.**
_____________________________________________________

El sniffer debe de ser ejecutados con **permisos de root** debido a que usa **raw sockets** y llamadas al sistema **ioctl()** para llevar a cabo la captura del tráfico por medio de las **interfaces Ethernet**.

Debido a ello, estando en la raíz del proyecto, la aplicación debe de ser ejecutada de la siguiente manera.

```bash
🐧user@host:~$ sudo python3 -m app
```


## 📂 **Estructura del Proyecto**
```
📂 Sniffer_Paquetes_Red/ (raíz del proyecto)
│── 📂 app/                # Lógica principal e interacción con el usuario
│── 📂 sniffer_paquetes/   # Paquete dedicado a la captura y procesamiento del tráfico de red
│── 📂 docs/               # Documentación adicional
│── 📝 LICENSE             # Licencia GPL v3
│── 📜 README.md           # Documentación principal
│── 📄 requirements.txt    # Dependencias necesarias
│── 🛠️ setup.sh            # Script de configuración inicial del proyecto.
```


