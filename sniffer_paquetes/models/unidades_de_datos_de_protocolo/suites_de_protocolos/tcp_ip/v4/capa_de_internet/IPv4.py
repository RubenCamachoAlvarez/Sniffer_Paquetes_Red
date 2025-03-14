from .....pdu import PDU


class DatagramaIPv4(PDU):

    """
    Esta clase es utilizada para representar un datagrama de internet en la version 4 de la suite de protocolos TCP/IP.

    De manera análoga a las clases que modelan las distintas unidades de datos a nivel de capa de enlace de datos. Esta clase representa el
    PDU (protocol data unit) correspondiente en la capa de internet de acuerdo al modelo TCP/IP (modelo DoD).

    En general, de acuerdo a este modelo, en esta capa el PDU recibe el nombre de datagrama de internet.

    Campos del datagrama de internet.

        -Version -> 4 bits.
        -IHL (Internet Header Length/Longitud del Encabezado de Internet) -> 4 bits.
        -Tipo de servicio -> 8 bits.
        -Longitud total -> 16 bits.
        -Identificador -> 16 bits.
        -Flags -> 3 bits.
        -Fragment offset -> 13 bits.
        -TTL (Time To Live) -> 8 bits.
        -Protocolo -> 8 bits.
        -Checksum encabezado -> 16 bits.
        -Direccion de origen -> 32 bits.
        -Direccion destino -> 32 bits.
        -Opciones -> Tamaño de bits variable.
        -Padding -> Tamaño de bits variable que es utilizado para conseguir una alineacion de 32 bits (4 octetos). Los bits que sirven de padding tienen estado 0.
        -Datos -> octetos del protocolo de nivel superior transportado dentro del datagrama de internet.

    """

    def __init__(self, raw_octets_internet_datagram):

        #Inicializacion del PDU.

        super().__init__()

        self.version = None

        """Este campo del datagrama indica, en unidades de 32 bits (4 octetos), el tamaño del encabezado del datagrama de internet.
        El minimo valor que puede tomar este campo es 5 representando que el minimo tamaño del encabezado de un datagrama de internet es de 5x32 = 160 bits (20 octetos).
        El maximo valor que puede tomar este campo es de 15 representando de esta manera que el tamaño máximo del encabezado de un datagrama es de 15x32 = 480 bits
        (60 octetos)."""

        self.longitud_encabezado_internet = None

        self.tipo_de_servicio = None

        self.longitud_total = None

        self.identificador = None

        self.flags = None

        self.fragment_offset = None

        self.ttl = None

        self.protocolo = None

        self.checksum_encabezado = None

        self.direccion_origen = None

        self.direccion_destino = None

        self.opciones = None

        #self.padding = None Este campo del encabezado no tiene mucho sentido almacenarlo.

        self.datos = None


