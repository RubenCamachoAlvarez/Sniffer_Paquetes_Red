from .io_manager.io_cli import seleccionar_interfaz_red, mostrar_banner_inicio

from sniffer_paquetes.models.unidades_de_datos_de_protocolo.pdu import PDU

from sniffer_paquetes.models.unidades_de_datos_de_protocolo.unidades_de_datos.ieee_802.ieee_802_3_mac_frame import TramaMacEthernet

from sniffer_paquetes.models.unidades_de_datos_de_protocolo.suites_de_protocolos.tcp_ip.v4.capa_de_internet.IPv4 import DatagramaIPv4

import sys

import time

def imprimir_informacion_detallada_PDU(pdu : PDU):

    pdu.imprimir_informacion()

    if isinstance(pdu, TramaMacEthernet) and not pdu.es_trama_ieee_802_3 and pdu.longitud_tipo == 0x0800:

        datagrama_internet = DatagramaIPv4(pdu.datos)

        datagrama_internet.imprimir_informacion()

    print("\n═════════════════════════════════════════════════════\n")


def run_app():

    mostrar_banner_inicio()

    time.sleep(1)

    interfaz_escaneo = seleccionar_interfaz_red()

    if interfaz_escaneo != None:

        print("Iniciando captura de PDUs...\n")

        time.sleep(1)

        interfaz_escaneo.capturar_pdu(numero_capturas=20, accion=imprimir_informacion_detallada_PDU)

    else:

        print(f"No se han detectado interfaces compatibles que tengan soporte en el proyecto actualmente para poder capturar paquetes de red", file=sys.stderr)