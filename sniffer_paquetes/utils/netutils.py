"""Este modulo tiene la finalidad de definir diferentes funciones para realizar operaciones relacionadas a la red dentro
del sistemas con kernel de Linux."""

import os

from sniffer_paquetes.models.interfaces_de_red.interfaces_fisicas.ieee_802.ieee_802_3_ethernet import InterfazEthernet

from sniffer_paquetes.constants import arp

def listar_interfaces_red():

    """Esta función tiene el objetivo de listar todas las interfaces de red a las que el proyecto ofrece y no ofrece (aun) soporte
    para llevar a cabo la captura de paquetes de red."""

    lista_interfaces_red_soportadas = []

    lista_interfaces_red_no_soportadas = []

    #Ruta estandar en distribuciones GNU/Linux actuales donde se muestra el listado de interfaces de red conectadas al sistema.

    ruta_interfaces = "/sys/class/net/"

    #Obtenemos el nombre de las interfaces recorriendo los elementos presentes en el directorio pertinente a la ruta antes mencionada.

    for nombre_interfaz in os.listdir(ruta_interfaces):

        #Construimos la ruta al directorio que almacena la información de la interfaz en cuestión.

        ruta_interfaz = f"{ruta_interfaces}{nombre_interfaz}"

        #Esta variable será utilizada para almacenar el objeto que representa a una interfaz que tiene soporte dentro del proyecto.

        interfaz = None

        #Esta variable almacenará el valor que representa el tipo de hardware de la interfaz, de esta manera podemos saber si es una
        #interfaz Ethernet, Wi-Fi, etc.

        tipo_hardware_interfaz = None

        #Esta variable almacenará el valor del Maximum Transmission Unit de dicha interfaz.

        mtu_interfaz = None

        #Obtenemos el tipo de hardware de la interfaz.

        with open(f"{ruta_interfaz}/type", "r") as archivo_tipo_hardware:

            tipo_hardware_interfaz = int(archivo_tipo_hardware.read())

        #Obtenemos el mtu de la interfaz.

        with open(f"{ruta_interfaz}/mtu", "r") as archivo_mtu:

            mtu_interfaz = int(archivo_mtu.read())

        es_interfaz_inalambrica = False

        with open(f"{ruta_interfaz}/uevent", "r") as archivo_uevent:

            for linea in archivo_uevent:

                clave_valor = linea.strip().split("=")

                if clave_valor[0] == "DEVTYPE" and clave_valor[1] == "wlan":

                    es_interfaz_inalambrica = True

        #Si la interfaz de red listada corresponde a una interfaz de Ethernet.

        if not es_interfaz_inalambrica and tipo_hardware_interfaz == arp.ARPHRD_ETHER or tipo_hardware_interfaz == arp.ARPHRD_IEEE802:

            #Creamos un objeto que representa esta interfaz.

            interfaz = InterfazEthernet(nombre_interfaz, mtu_interfaz)

        #Si se encontró que la interfaz de red listada corresponde a un tipo de interfaz con soporte en el paquete sniffer_paquetes.

        if interfaz != None:

            #Agregamos el objeto que representa el tipo de la interfaz listada a la lista de interfaces que tienen soporte.

            lista_interfaces_red_soportadas.append(interfaz)

        else:

            #Si la interfaz listada no cuenta con soporte, agregamos su nombre a la respectiva lista.

            lista_interfaces_red_no_soportadas.append(nombre_interfaz)

    return lista_interfaces_red_soportadas, lista_interfaces_red_no_soportadas
