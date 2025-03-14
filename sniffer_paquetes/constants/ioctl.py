"""
Este módulo contiene diferentes constantes que pueden ser utilizadas para el uso de la llamada al sistema ioctl() con el objetivo de interactuar directamente con el
driver de los dispositivos.

En este caso, estas constantes estan definidas originalmente para poder interactuar directamente con el driver/controlador de la tarjeta de red en dispositivos que
utilicen Linux como kernel de sistema operativo.

"""

#Constante que indica el código de operación definido por el núcleo de Linux para obtener las flags que indican el estado actual de una interfaz de red. 

SIOCGIFFLAGS = 0x8913

#Constante que indica el código de operación específico para el kernel de Linux para establecer las flags que indican el estado actual de la intefaz una interfaz de red.

SIOCSIFFLAGS = 0x8914

#Constante que tiene asociado el valor para indicar, en el kernel de Linux, el modo promiscuo en una interfaz de red Ethernet (IEEE 802.3).

IFF_PROMISC = 0x100
