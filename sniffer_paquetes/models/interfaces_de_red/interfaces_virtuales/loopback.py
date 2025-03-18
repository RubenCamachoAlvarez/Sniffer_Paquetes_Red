
"""Este módulo de Python contiene la definición de la clase que representa la interfaz de loopback utilizada en el sistema"""

from ..interfaz_red import InterfazRed

from ...unidades_de_datos_de_protocolo.suites_de_protocolos.tcp_ip.v4.capa_de_internet.IPv4 import DatagramaIPv4

from typing import Callable

import socket

from ....constants.net import ETH_P_IP

class InterfazLoopback(InterfazRed):

    def __init__(self, nombre, mtu):

        super().__init__(nombre, mtu)


    def capturar(self, numero_capturas=1):

        super().capturar(numero_capturas)

        lista_capturas = []

        socket_internet = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(ETH_P_IP))

        socket_internet.bind((self.nombre, 0))

        for captura in range(numero_capturas):

            octetos_datagrama, _ = socket_internet.recvfrom(self.mtu)

            octetos_datagrama = octetos_datagrama[14:]

            lista_capturas.append(octetos_datagrama)

        socket_internet.close()

        return lista_capturas[0] if numero_capturas == 1 else lista_capturas
        
    def capturar_pdu(self, numero_capturas : int = 1, accion : Callable[[DatagramaIPv4], None] = None):

        if numero_capturas < 1:

            raise ValueError("Se debe de realizar por lo menos una captura.")

        lista_capturas = []

        for captura in range(numero_capturas):

            octetos_datagrama = self.capturar()

            datagramaInternet = DatagramaIPv4(octetos_datagrama)

            lista_capturas.append(datagramaInternet)

            if callable(accion):

                accion(datagramaInternet)

        return lista_capturas[0] if numero_capturas == 1 else lista_capturas