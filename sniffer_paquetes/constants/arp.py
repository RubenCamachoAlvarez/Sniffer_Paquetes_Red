"""

Este módulo contiene constantes relacionadas al Protocolo de Resolución de Direcciones (ARP).

El valor de estas constantes fueron sacadas directamente de las constantes que forman parte del archivo de cabecera
if_arp.h el cual se encuentra en los archivos que conforman el núcleo de Linux.

"""

#Constantes para la definición de distinto tipo de hardware.

#Constante que representa a una interfaz de red Ethernet.
ARPHRD_ETHER = 1 

#Constante que representa a un interfaz de red IEEE 802.2 Ethernet.
ARPHRD_IEEE802 = 6

#Constante que representa a una interfaz de red de Loopback.
ARPHRD_LOOPBACK = 772

#Constante que representa a un interfaz de red Wi-Fi
ARPHRD_IEEE80211 = 801

#Constante que representa a una interfaz de red de Wi-Fi + el encabezado Prism2.
ARPHRD_IEEE80211_PRISM = 802

#Constante que representa a una interfaz de red de Wi-Fi + el encabezado radiotap.
ARPHRD_IEEE80211_RADIOTAP = 803

