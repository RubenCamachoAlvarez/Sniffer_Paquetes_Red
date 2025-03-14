import socket

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

        """

        Constructor de la clase abstracta que es utilizado como constructor base para poder instanciar cualquier tipo de interfaz de red genérica.

        """

        self.nombre = nombre

        self.mtu = mtu


    def configurar_interfaz(self):

        """
        
        Este método es puramente abstracto y nunca debe de llamarse si se esta tratando un objeto de una subclase como si fuera un objeto de la superclase, puesto que
        en cada subclase puede definir parametros en especifico y/o opciones que permitan configurar la interfaz de red respectiva.

        """

        pass

    
    def capturar(self, numero_capturas = 1):

        if numero_capturas < 1:

            raise ValueError("Por lo menos se debe de realizar una captura al invocar este método.")

        """
        
        Este método tiene como propósito el ser implementado por cada clase que represente a una interfaz
        de red en especifico para definir el comportamiento necesario para capturar un paquete de red.

        Este método debe de retornar los octetos en brutos de la captura.
        
        """

        pass
