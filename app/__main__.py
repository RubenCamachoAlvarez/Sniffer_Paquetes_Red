from .io_manager.io_cli import seleccionar_interfaz_red, mostrar_banner_inicio

from sniffer_paquetes.models.unidades_de_datos_de_protocolo.pdu import PDU

import sys

import time

def callback(pdu : PDU):

    pdu.imprimir_informacion()

    print("\n═════════════════════════════════════════════════════\n")

if __name__ == "__main__":

    mostrar_banner_inicio()

    time.sleep(1)

    interfaz_escaneo = seleccionar_interfaz_red()

    if interfaz_escaneo != None:

        print(f"\nInterfaz escogida: {interfaz_escaneo.nombre}\n")

        time.sleep(1)

        interfaz_escaneo.capturar_pdu(numero_capturas=10, accion=callback )

    else:

        print(f"No se han detectado interfaces compatibles que tengan soporte en el proyecto actualmente para poder capturar paquetes de red", file=sys.stderr)