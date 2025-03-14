
class TramaMacEthernet:

    def __init__(self, raw_octets_trama_mac : bytes):

        """
        Esta clase representa el formato de la trama MAC utilizada por las redes de Ethernet para transportar los datos a nivel de
        capa de enlace de datos.

        Debido a ello, los atributos que componen esta clase son los campos reales de los que se componen una trama MAC de acuerdo
        a como se encuentra definida dentro del estandar IEEE 802.3 que rige la construcción y operación física y lógica de redes
        de Ethernet.

        Atributos:

            - direccion_destino = Almacena la dirección física (MAC) del o de los equipos a los que va destinada la trama.
            - direccion_origen = Almacena la dirección física de la interfaz del equipo que ralizó el envio de la trama por el medio físico.

            - longitud_tipo = Este campo es especial.

            En la teoría hay dos tipos distintos de tramas MAC para redes de Ethernet: Las tramas MAC para redes Ethernet II y las tramas MAC
            para redes de Ethernet basadas en el estandar IEEE 802.3

            La especificación original de Ethernet II (lanzada en conjunto por Digital, Intel y Xerox) define que el tercer campo de la trama es
            tipo y básicamente es utilizado para indicar un valor como EtherType que sirve para indicar el contenido del payload (los datos
            de protocolo de nivel superior) transportado en el cuarto campo de la trama.

            En contraste, el estandar de la IEEE 803.2 oficialmente define que el tercer campo de la trama MAC debe de ser utilizado para indicar
            el numero de octetos transportados en el cuarto campo de la trama.
            campo.

            - payload = Campo donde se transportan los octetos que corresponden los datos de los protocolos de nivel superior, es decir, los datos
            de los protocolos de red de nivel superior que residen a partir de la capa de red hasta la capa de aplicación, tomando como base el
            modelo OSI.

            NOTA:

            Esta clase por el momento ha sido diseñada para únicamente dar soporte a "basic frames" (IEEE 802.3 original).

            En un futuro se agregará soporte para manejar "Q-tagged frames" (IEEE 802.1Q) y "Enveloped frames" (IEEE 802.1ad).

            Del mismo modo, a posteriorí de igual manera se incluirá soporte para los denominados "Jumbo Frames" para redes Gigabit Ethernet.

        """

        self.direccion_destino = None

        self.direccion_origen = None

        self.longitud_tipo = None

        self.datos = None

        self._procesar_octetos_trama_mac(raw_octets_trama_mac)



        def _procesar_octetos_trama_mac(raw_octets : bytes):

            self.direccion_destino = ":".join(f"{b:02x}" for octeto in raw_octets[:6])

            self.direccion_origen = ":".join(f"{b:02x}" for octeto in raw_octets[6:12])

            self.longitud_tipo = int.from_bytes(raw_octets[12:14], byteorder="big")

            self.datos = raw_octets[14:] 

