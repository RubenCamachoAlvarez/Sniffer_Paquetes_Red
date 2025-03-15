from .io_manager.io_cli import seleccionar_interfaz_red

from sniffer_paquetes.models.unidades_de_datos_de_protocolo.pdu import PDU

import sys

def callback(pdu : PDU):

    pdu.imprimir_informacion()

    print("--------------------------------------")

if __name__ == "__main__":

    interfaz_escaneo = seleccionar_interfaz_red()

    if interfaz_escaneo != None:

        print(f"\nInterfaz escogida: {interfaz_escaneo.nombre}\n")

        interfaz_escaneo.capturar_pdu(numero_capturas=10, accion=callback )

    else:

        print(f"No se han detectado interfaces compatibles que tengan soporte en el proyecto actualmente para poder capturar paquetes de red", file=sys.stderr)