from ...interfaz_red import InterfazRed

import struct

import fcntl

import socket

from typing import Callable

from .....constants.net import IFNAMSIZ, ETH_P_ALL

from .....constants.ioctl import SIOCGIFFLAGS, SIOCSIFFLAGS, IFF_PROMISC

from .....models.unidades_de_datos_de_protocolo.unidades_de_datos.ieee_802.ieee_802_3_mac_frame import TramaMacEthernet

class InterfazEthernet (InterfazRed):

    """"Esta clase representa un ejemplar de una intefaz de red física Ethernet.

    El propósito es incorporar el funcionamiento que este tipo de interfaces de red deben de seguir para poder sniffer el tráfico de red a nivel de capa de enlace
    de datos."""


    def __init__(self, nombre, mtu):

        #Instanciación de un nuevo ejemplar que representa a una Interfaz de Red Ethernet

        super().__init__(nombre, mtu)


    def configurar_interfaz(self, modo_promiscuo=False):

        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:

            peticion_ioctl_interfaz = struct.pack(f"{IFNAMSIZ}sH", self.nombre.encode(), 0)

            respuesta_ioctl_interfaz = struct.unpack(f"{IFNAMSIZ}sH", fcntl.ioctl(sock.fileno(), SIOCGIFFLAGS, peticion_ioctl_interfaz))

            flags_interfaz = respuesta_ioctl_interfaz[1]

            if modo_promiscuo:

                flags_interfaz |= IFF_PROMISC

            else:

                flags_interfaz &= ~IFF_PROMISC

            peticion_set_ioctl_interfaz = struct.pack(f"{IFNAMSIZ}sH", self.nombre.encode(), flags_interfaz)

            fcntl.ioctl(sock.fileno(), SIOCSIFFLAGS, peticion_set_ioctl_interfaz)


    def capturar(self, numero_capturas=1):

        super().capturar(numero_capturas)

        lista_capturas = []

        for captura in range(numero_capturas):

            raw_socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(ETH_P_ALL))

            raw_socket.bind((self.nombre, 0))

            octetos_trama, _ = raw_socket.recvfrom(1518)

            lista_capturas.append(octetos_trama)

        return lista_capturas[0] if numero_capturas == 1 else lista_capturas

    
    def capturar_pdu(self, numero_capturas : int = 1, accion : Callable[[TramaMacEthernet], None] = None):

        lista_capturas = []

        for captura in range(numero_capturas):

            octetos_trama = self.capturar()

            tramaEthernet = TramaMacEthernet(octetos_trama)

            lista_capturas.append(tramaEthernet)

            if callable(accion):

                accion(tramaEthernet)

        return lista_capturas[0] if numero_capturas == 1 else lista_capturas

        