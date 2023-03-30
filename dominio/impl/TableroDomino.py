from dominio.impl.Ficha import Ficha
from dominio.impl.JugadorDomino import JugadorDomino


class TableroDomino:
    def __init__(self):
        self.tablero: list[Ficha] = []

    def is_jugable(self, ficha):
        if not self.tablero:
            if ficha.is_mula():
                if ficha.izq == 6 and ficha.der == 6:
                    return True
                elif ficha.izq == 5 and ficha.der == 5:
                    return True
                elif ficha.izq == 4 and ficha.der == 4:
                    return True
                elif ficha.izq == 3 and ficha.der == 3:
                    return True
                elif ficha.izq == 2 and ficha.der == 2:
                    return True
                elif ficha.izq == 1 and ficha.der == 1:
                    return True
                elif ficha.izq == 0 and ficha.der == 0:
                    return True
                else:
                    return False
        else:

            izq_fin = self.tablero[0].izq
            der_fin = self.tablero[-1].der
            return ficha.izq in (izq_fin, der_fin) or ficha.der in (izq_fin, der_fin)

    def is_vacio(self):
        if not self.tablero:
            return True
        else:
            return False

    def izq_fin(self):
        return self.tablero[0].izq if len(self.tablero) > 0 else None

    def der_fin(self):
        return self.tablero[-1].der if len(self.tablero) > 0 else None

    def jugar_ficha(self, ficha: Ficha, jugador: JugadorDomino):
        if self.is_vacio():
            print("El tablero aun no a jugado mula")
        elif ficha.izq == self.izq_fin():
            print(f'----- Ficha lado izq: {ficha.izq}')
            print(f'------ fiacha izq, lado izq: {self.tablero}')
            self.tablero.insert(0, ficha)
            jugador.mano.remove(ficha)
        elif ficha.der == self.der_fin():
            self.tablero.insert(-1, ficha)
            jugador.mano.remove(ficha)
        else:
            raise ValueError("La ficha no puede ser jugada")
    #
    # def __str__(self):
    #
    #     for ficha in self.tablero:

