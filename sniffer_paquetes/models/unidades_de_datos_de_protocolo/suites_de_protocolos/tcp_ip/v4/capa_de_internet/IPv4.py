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


    def procesar_pdu(self, raw_octets : bytes):

        """
        
        En esta clase, este metodo se encarga de realizar el proceso de extracción del encabezado del datagrama
        de internet, así como los datos que conforman el payload.
        
        """

        self.version = (raw_octets[0] & 0xF0) >> 4

        self.longitud_encabezado_internet = raw_octets[0] & 0x0F

        self.tipo_de_servicio = raw_octets[1] & 0xFF

        self.longitud_total = int.from_bytes(raw_octets[2:4], byteorder="big")

        self.identificador = int.from_bytes(raw_octets[4:6], byteorder="big")

        self.flags = (raw_octets[6] & 0xE0) >> 5

        self.fragment_offset = int.from_bytes(raw_octets[6:8], byteorder="big") & 0x1FFF

        self.ttl = raw_octets[8] & 0xFF

        self.protocolo = raw[9] & 0xFF

        self.checksum_encabezado = int.from_bytes(raw_octets[10:12], byteorder="big")

        self.direccion_origen = ".".join(f"{octeto:d}" for octeto in raw_octets[12:16])

        self.direccion_destino = ".".join(f"{octeto:d}" for octeto in raw_sockets[16:20])

        self.opciones = raw_octets[20:self.longitud_encabezado_internet*4]

        self.datos = raw_octets[(self.longitud_encabezado_internet * 4):]


    def imprimir_informacion(self):

        """Método abstracto que debe de implementar cada PDU para mostrar su información asociada correctamente."""

        print(f"Version: {self.version}")

        print(f"Longitud del encabezado del datagrama de internet: {self.longitud_encabezado_internet} octetos")

        print(f"Longitud total del datagrama de internet: {self.longitud_total} octetos")

        #Puede añadirse información acerca de la fragmentación del datagrama (en caso de aplicar).

        print(f"Time to Live (TTL): {self.ttl}")

        print(f"Protocolo transportado: {self.protocolo}")

        print(f"Checksum del encabezado: {self.checksum_encabezado}")

        print(f"Direccion IP origen: {self.direccion_origen}")

        print(f"Direccion IP destino: {self.direccion_destino}")




