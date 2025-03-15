"""Este modulo tiene la finalidad de definir diferentes funciones para realizar operaciones relacionadas a la red dentro
del sistemas con kernel de Linux."""

import os

from sniffer_paquetes.models.interfaces_de_red.interfaces_fisicas.ieee_802.ieee_802_3_ethernet import InterfazEthernet

def listar_interfaces_red():

    lista_interfaces_red = []

    ruta_interfaces = "/sys/class/net/"

    for nombre_interfaz in os.listdir(ruta_interfaces):

        ruta_interfaz = f"{ruta_interfaces}{nombre_interfaz}"

        interfaz = None

        tipo_hardware_interfaz = None

        mtu_interfaz = None

        with open(f"{ruta_interfaz}/type", "r") as archivo_tipo_hardware:

            tipo_hardware_interfaz = int(archivo_tipo_hardware.read())

        with open(f"{ruta_interfaz}/mtu", "r") as archivo_mtu:

            mtu_interfaz = int(archivo_mtu.read())

        if tipo_hardware_interfaz == 1 or tipo_hardware_interfaz == 6:

            interfaz = InterfazEthernet(nombre_interfaz, mtu_interfaz)

        if interfaz != None:

            lista_interfaces_red.append(interfaz)

    return lista_interfaces_red