
"""Este módulo tiene la finalidad de proporcionar las funciones necesarias para manipular la interacción del programa
por medio de la línea de comandos."""

from sniffer_paquetes.utils.netutils import listar_interfaces_red

import sys

import termios

def mostrar_banner_inicio():

    banner = """
    ███████╗███╗   ██╗██╗███████╗███████╗███████╗██████╗ 
    ██╔════╝████╗  ██║██║██╔════╝██╔════╝██╔════╝██╔══██╗
    ███████╗██╔██╗ ██║██║█████╗  █████╗  █████╗  ██████╔╝
    ╚════██║██║╚██╗██║██║██╔══╝  ██╔══╝  ██╔══╝  ██╔══██╗
    ███████║██║ ╚████║██║██║     ██║     ███████╗██║  ██║
    ╚══════╝╚═╝  ╚═══╝╚═╝╚═╝     ╚═╝     ╚══════╝╚═╝  ╚═╝
    ═════════════════════════════════════════════════════
            Sniffer de tráfico de red - Capa 2
    ═════════════════════════════════════════════════════
    """
    
    print(banner)

def modo_no_canonico(habilitar=False):

    """Esta función tiene la intención de poner la salida estándar utilizada por la aplicación
    en modo no canónico con el objetivo de poder capturar inmediatamente las teclas presionadas
    por el usuario al solicitar ingresar una entrada."""

    configuracion = termios.tcgetattr(sys.stdin.fileno())[:]

    if habilitar == True:

        configuracion[3] &= ~termios.ICANON

    else:

        configuracion[3] |= termios.ICANON

    termios.tcsetattr(sys.stdin.fileno(), termios.TCSANOW, configuracion)

def seleccionar_interfaz_red():

    """Como su nombre lo indica, está función está encargada de mostrar las diferentes interfaces de red con las que
    cuenta el dispositivo que se ejecuta sobre un kernel de Linux, con el objetivo de que el usuario de la aplicación
    escoja con cual de estas interfaces es con la que desea realizar el escaneo de los paquetes de red que transitan
    por la red a la que se encuentra conectado su sistema por medio de la interfaz de red seleccionada."""

    interfaces_soportadas, interfaces_no_soportadas = listar_interfaces_red()

    if len(interfaces_no_soportadas) > 0:

        print("\nINTERFACES DE RED NO SOPORTADAS\n", file=sys.stderr)

        for nombre_interfaz in interfaces_no_soportadas:

            print(f"-{nombre_interfaz}\n", file=sys.stderr)


    if len(interfaces_soportadas) > 0:

        while(True):

            try:

                print("═════════════════════════════════════════════════════")

                print("\nMENÚ DE INTERFACES DE RED SOPORTADAS\n")

                for indice_interfaz in range(len(interfaces_soportadas)):

                    print(f"{indice_interfaz} -> {interfaces_soportadas[indice_interfaz].nombre}")

                print("\nSelecciona la interfaz quie deseas utilizar: ", end="", flush=True)

                modo_no_canonico(habilitar=True)

                indice_seleccion = int(sys.stdin.read(1))

                modo_no_canonico(habilitar=False)

                if 0 <= indice_seleccion < len(interfaces_soportadas):

                    print("")

                    break

                print("\nIngresa un entero que corresponda a una interfaz mostrada en el menú.", file=sys.stderr)

            except ValueError:

                print("\nError, ingrese un número entero.", file=sys.stderr)

    return interfaces_soportadas[indice_seleccion] if len(interfaces_soportadas) > 0 else None
