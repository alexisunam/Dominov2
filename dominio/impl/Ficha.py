from dominio.ObjetoJuego import ObjetoJuego


class Ficha(ObjetoJuego):

    def __init__(self, izq, der):
        self.izq: str = izq
        self.der: str = der

    def is_mula(self):
        return self.izq == self.der

    def representar(self):
        return f'{self.izq}/{self.der}'


    def voltear(self):
        izq_nuevo = self.der
        der_nuevo = self.izq
        self.der = der_nuevo
        self.izq = izq_nuevo

    # def __str__(self):
    #     return f"cara1: {self.cara1}, cara2: {self.cara2}"
