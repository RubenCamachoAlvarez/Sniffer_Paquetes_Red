
"""Este módulo tiene la finalidad de proporcionar las funciones necesarias para manipular la interacción del programa
por medio de la línea de comandos."""

from sniffer_paquetes.utils.netutils import listar_interfaces_red

import sys

def seleccionar_interfaz_red():

    """Como su nombre lo indica, está función está encargada de mostrar las diferentes interfaces de red con las que
    cuenta el dispositivo que se ejecuta sobre un kernel de Linux, con el objetivo de que el usuario de la aplicación
    escoja con cual de estas interfaces es con la que desea realizar el escaneo de los paquetes de red que transitan
    por la red a la que se encuentra conectado su sistema por medio de la interfaz de red seleccionada."""

    interfaces = listar_interfaces_red()

    if len(interfaces) > 0:

        while(True):

            try:

                print("---------------------------------------------------------------")

                print("\nMENÚ DE INTERFACES DE RED\n")

                for indice_interfaz in range(len(interfaces)):

                    print(f"{indice_interfaz} -> {interfaces[indice_interfaz].nombre}")

                indice_seleccion = int(input("\nDigita el entero de la interfaz que deseas utilizar: "))

                if 0 <= indice_seleccion < len(interfaces):

                    break

                print("\nIngresa un entero que corresponda a una interfaz mostrada en el menú.\n", file=sys.stderr)

            except ValueError:

                print("\nError, ingrese un número entero.\n", file=sys.stderr)

    return interfaces[indice_seleccion] if len(interfaces) > 0 else None

        