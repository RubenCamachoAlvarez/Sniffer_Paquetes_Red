
"""Este módulo tiene la finalidad de proporcionar las funciones necesarias para manipular la interacción del programa
por medio de la línea de comandos."""

from sniffer_paquetes.utils.netutils import listar_interfaces_red

from sniffer_paquetes.models.interfaces_de_red.interfaz_red import InterfazRed

import sys

import termios

from typing import List

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

        configuracion[3] &= ~(termios.ICANON | termios.ECHO)

    else:

        configuracion[3] |= (termios.ICANON | termios.ECHO)

    termios.tcsetattr(sys.stdin.fileno(), termios.TCSANOW, configuracion)


def pintar_menu_seleccion_interfaz(lista_interfaces : List[InterfazRed], elemento_seleccionado : int = 0):

    numero_elementos = len(lista_interfaces)

    for indice, interfaz in enumerate(lista_interfaces):

        print(f" {"▶" if indice == (elemento_seleccionado % numero_elementos) else ""} {interfaz.nombre}")


def seleccionar_interfaz_red():

    print("\nListando interfaces de red del sistema...\n")

    interfaces_soportadas, interfaces_no_soportadas = listar_interfaces_red()

    numero_interfaces_red_soportadas = len(interfaces_soportadas)

    if len(interfaces_no_soportadas) > 0:

        print("\nINTERFACES DE RED NO SOPORTADAS\n")

        for nombre_interfaz in interfaces_no_soportadas:

            print(f"✗ - {nombre_interfaz}")

        print("\n═════════════════════════════════════════════════════")


    if numero_interfaces_red_soportadas > 0:

        print("\nINTERFACES DE RED SOPORTADAS\n")

        indice_interfaz_seleccionada = 0

        sys.stdout.write("\x1b[?25l")

        sys.stdout.flush()

        while True:

            pintar_menu_seleccion_interfaz(interfaces_soportadas, indice_interfaz_seleccionada)

            modo_no_canonico(True)

            caracter = sys.stdin.read(1)

            if caracter == '\n':

                modo_no_canonico(False)

                sys.stdout.write("\x1b[?25h")

                sys.stdout.flush()

                break

            elif caracter == "\x1b":
                
                try:

                    caracter = sys.stdin.read(1)

                    if caracter == "[":

                        caracter = sys.stdin.read(1)

                        if caracter in ["A", "B"]:

                            if caracter == "A":

                                indice_interfaz_seleccionada -= 1

                            else:

                                indice_interfaz_seleccionada += 1

                            indice_interfaz_seleccionada %= numero_interfaces_red_soportadas

                            for fila in range(numero_interfaces_red_soportadas):

                                sys.stdout.write("\x1b[1A")

                                sys.stdout.flush()

                                sys.stdout.write("\r")

                                sys.stdout.flush()

                                sys.stdout.write("\x1b[K")

                                sys.stdout.flush()

                except:

                    pass

        if numero_interfaces_red_soportadas > 0:

            interfaz_seleccionada : InterfazRed = interfaces_soportadas[indice_interfaz_seleccionada]

            print(f"\nInterfaz seleccionada '{interfaz_seleccionada.nombre}'\n")

            return interfaz_seleccionada
                    
        else:

            return None
