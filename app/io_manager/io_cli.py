
"""Este módulo tiene la finalidad de proporcionar las funciones necesarias para manipular la interacción del programa
por medio de la línea de comandos."""

from sniffer_paquetes.utils.netutils import listar_interfaces_red

import sys

def seleccionar_interfaz_red():

    """Como su nombre lo indica, está función está encargada de mostrar las diferentes interfaces de red con las que
    cuenta el dispositivo que se ejecuta sobre un kernel de Linux, con el objetivo de que el usuario de la aplicación
    escoja con cual de estas interfaces es con la que desea realizar el escaneo de los paquetes de red que transitan
    por la red a la que se encuentra conectado su sistema por medio de la interfaz de red seleccionada."""

    interfaces_soportadas, interfaces_no_soportadas = listar_interfaces_red()

    if len(interfaces_no_soportadas) > 0:

        print("\nINTERFACES DE RED NO SOPORTADAS\n", file=sys.stderr)

        for nombre_interfaz in interfaces_no_soportadas:

            print(f"-> {nombre_interfaz}", file=sys.stderr)


    if len(interfaces_soportadas) > 0:

        while(True):

            try:

                print("\n---------------------------------------------------------------")

                print("\nMENÚ DE INTERFACES DE RED SOPORTADAS\n")

                for indice_interfaz in range(len(interfaces_soportadas)):

                    print(f"{indice_interfaz} -> {interfaces_soportadas[indice_interfaz].nombre}")

                indice_seleccion = int(input("\nDigita el entero de la interfaz que deseas utilizar: "))

                if 0 <= indice_seleccion < len(interfaces_soportadas):

                    break

                print("\nIngresa un entero que corresponda a una interfaz mostrada en el menú.", file=sys.stderr)

            except ValueError:

                print("\nError, ingrese un número entero.", file=sys.stderr)

    return interfaces_soportadas[indice_seleccion] if len(interfaces_soportadas) > 0 else None

        