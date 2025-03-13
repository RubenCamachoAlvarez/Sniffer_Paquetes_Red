
class InterfazRed:

    """

    Esta es la superclase que declara todos los atributos y métodos abstractos base que tienen las diferentes interfaces
    de red que cuentan con soporte en este proyecto para poder llevar a cabo el proceso de sniffeo de los paquetes que
    se encuentren en transito a traves de la red a la que la interfaz de red se encuentre conectada.

    Atributos:

        - nombre -> Almacena el nombre de la interfaz de red.
        - mtu (Maximum Transmission Unit) -> Indica la cantidad máxima de bytes del payload que puede transportar la unidad de datos utilizada por la red dentro de un solo paquete.

    """

    def __init__(self, nombre, mtu):

        self.nombre = nombre

        self.mtu = mtu
