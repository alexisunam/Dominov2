from random import shuffle
from dominio.CreadorDeBaraja import CreadorDeBaraja
from .Ficha import Ficha


class CreadorBarajaDomino(CreadorDeBaraja):

    def crear_baraja(self):
        # numeros: list[tuple] = []
        numeros = [(i, j) for i in range(7) for j in range(7)]
        for numero in numeros:
            if numero[0] != numero[1]:
                if numero[::-1] in numeros:
                    numeros.remove(numero[::-1])
        baraja = [Ficha(i, j) for (i, j) in numeros]

        shuffle(baraja)
        # for ficha in baraja:
            # print(f"Ficha: {ficha.izq}, {ficha.der}")
        return baraja
