
class TramaMacEthernet:

    def __init__(self):

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
            de protocolo de nivel superior) transportado por la trama.

            En contraste, el estandar de la IEEE 803.2 oficialmente define que el tercer campo de la trama MAC es length (longitud) y de acuerdo
            al estandar este debe de ser utilizado para definir el numero de bytes útiles que conforman el payload "transportado" en el siguiente
            campo.

            - payload = Campo donde se transportan los bytes útiles que corresponde a los datos de los protocolos de red superiores, es decir los datos de los protocolos de red que residen desde la capa de red hasta la capa de aplicación del modelo OSI.

            - relleno = Campo utilizado en caso de necesitar bytes de relleno para obtener la longitud minima del payload de la trama.

            - secuencia de verificacion de la trama = Es un campo que transporta un valor que permite verificar que los datos de la trama no sean
            erroneas al ser recibida por el receptor.

        """

        self.direccion_destino = None

        self.direccion_origin = None

        self.longitud_tipo = None

        self.datos = None

