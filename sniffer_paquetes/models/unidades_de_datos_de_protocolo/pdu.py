
class PDU:

    """
    Esta clase representa una unidad de datos de protocolo de cualquier nivel respecto al modelo OSI.

    Básicamente esta clase fue desarrollada con el objetivo de meter métodos que los PDUs de cualquier protocolo en cualquier capa
    deberian de tener.

    Estos métodos son abstractos y es responsabilidad que cada clase que representa un PDU diferente los implemente.

    El método más importante que cualquier clase que represente un PDU debe de tener es el tener la capaicidad de poder imprimir
    la informacion de su encabezado.

    """

    def __init__(self):

        """Constructor que permite la constructor correcta de la superclase cuando una clase que representa a un tipo especial
        de PDU es instanciado."""

        pass


    def imprimir_informacion(self):

        """Método abstracto que debe de implementar cada PDU para mostrar su información asociada correctamente."""

        pass
