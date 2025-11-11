# 📡🕵️**Sniffer de paquetes de red**🕵️📡

**Este proyecto es un sniffer de paquetes de red experimental desarrollado para sistemas GNU/Linux con el cual se puede realizar la captura del tráfico red, así como la inspección de las tramas MAC y datagramas de internet.**


## 🚀 **Características**
- ✅ Captura del tráfico de red a nivel de **capa de enlace de datos** y de **capa de red**.
- ✅ Soporte nátivo para sniffear tráfico por medio de **adaptadores de red Ethernet** e **interfaces loopback**.
- ✅ Soporte para inspeccionar las **Tramas MAC** enviadas a través de paquetes Ethernet y para inspeccionar el datagrama de internet **IPv4** de la suite de protocolos **TCP/IP**.

## ⚠️ **Consideraciones**

- 🚨 **Es necesario que el sistema Linux que ejecute este programa tenga montado el sistema de archivos virtual 'sysfs' en /sys/**

- 🚨 **Este programa ha sido desarrollado únicamente para distribuciones GNU/Linux debido a que hace uso de llamadas al sistema específicas del kernel de Linux.**

- 🚨 **Por el momento** el proyecto solo cuenta con soporte para capturar tráfico por medio de **adaptadores Ethernet** y de **interfaces loopback**.

- 🚨 Si utilizas una distribución Debian o Ubuntu, el instalador de la aplicación verificará que tu sistema tenga instalado el paquete **python3-venv** el cual es necesario para poder crear de manera correctar entornos virtuales por medio del comando

```
🐧user@host:~$ python3 -m venv .
```


## 🛠 Uso

Antes de ejecutar la aplicación es importante la configuración de un entorno virtual donde se ejecute de manera aislada la aplicación.

En la raíz del proyecto hay un archivo denominado **setup.sh** que se encarga de esto.

Estando en la raíz del proyecto, ejecuta este script de configuración con alguna de las siguientes dos maneras.

```bash
🐧user@host:~$ . ./setup.sh
```

```bash
🐧user@host:~$ source ./setup.sh
```

Una vez que el script se haya ejecutado correctamente, automáticamente estarás tendrás activado el entorno virtual para poder ejecutar la aplicación.

Si quieres activar manualmente el entorno virtual de la aplicación, posicionate en la carpeta raíz del proyecto y ejecuta el siguiente comando.

```bash
🐧user@host:~$ source bin/activate
```
ó
```bash
🐧user@host:~$ . bin/activate
```

Para desactivar el entorno virtual ejecuta el siguiente comando.

```bash
🐧user@host:~$ deactivate
```

⚠️ **Este proyecto no utiliza ninguna dependencia externa, por lo cual podría ejecutarse sin ningún problemas fuera de un entorno virutal, sin embargo se recomienda su creación para garantizar una ejecución segura que no afecte la instalación global de Python en tu sistema.**
___

El sniffer debe de ser ejecutado con **permisos de root** debido a que usa **raw sockets** y llamadas al sistema **ioctl()** para llevar a cabo la captura del tráfico por medio de los adaptadores e interfaces ofrecidos por el sistema.

De este modo, una vez activado el entorno virtual de la aplicación, ejecuta el sniffer a través del siguiente comando.

```bash
🐧user@host:~$ sudo python -m app
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
