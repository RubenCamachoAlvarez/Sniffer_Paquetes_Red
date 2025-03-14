class InterfazEthernet:

    """"Esta clase representa un ejemplar de una intefaz de red física Ethernet.

    El propósito es incorporar el funcionamiento que este tipo de interfaces de red deben de seguir para poder sniffer el tráfico de red a nivel de capa de enlace
    de datos."""


    def __init__(self, nombre, mtu):

        #Instanciación de un nuevo ejemplar que representa a una Interfaz de Red Ethernet

        super().__init__(nombre, mtu)




