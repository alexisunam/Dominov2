import random

from dominio.Jugador import Jugador
from dominio.impl.Ficha import Ficha


class JugadorDomino(Jugador):

    def __init__(self, nombre):
        self.nombre: str = nombre
        self.mano: list[Ficha] = []
        self.puntuacion: int = 0
        self.is_human: bool = False

    def agregar_a_mano(self):
        pass

    def set_true_human(self, valor: bool):
        self.is_human = valor

    def seleccionar_ficha(self, fichas_validas):
        if self.is_human:
            fichas_validadas = []
            for ficha in fichas_validas:
                fichas_validadas.append(f'{ficha.izq}/{ficha.der}')
            print(f'Las fichas que puedes poner: {fichas_validadas}')
            print('Selecciona una ficha con un numero empezando desde la izquierda con 1,2,...')
            while True:
                selection = input("Pon el numero de la ficha que quieras poner: ")

                try:
                    index = int(selection) - 1
                    ficha = fichas_validas[index]
                    return ficha
                except (ValueError, IndexError):
                    print("Seleccion invalida. intente de nuevo.")
        else:
            return random.choice(fichas_validas)

    # def is_human(self):
    #     pass