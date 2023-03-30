from dominio.impl.Ficha import Ficha
from dominio.JuegoMesa import JuegoMesa
from dominio.impl.JugadorDomino import JugadorDomino
from dominio.impl.TableroDomino import TableroDomino
from dominio.impl.CreadorBarajaDomino import CreadorBarajaDomino


# PAtron mediator
class JuegoDomino(JuegoMesa):

    def __init__(self, jugadores: list[JugadorDomino]):
        self.jugadores: list[JugadorDomino] = jugadores
        self.tablero_domino: TableroDomino = TableroDomino()
        self.pozo: list[Ficha] = CreadorBarajaDomino().crear_baraja()
        self.ganador: JugadorDomino = JugadorDomino("")
        self.puntuacion_alta: float = 0.0
        self.jugador_actual: int = 0
        self.fin_del_juego: bool = False

    def repartir_baraja(self):

        for jugador in self.jugadores:
            print(jugador)
            for num in range(1, 8):
                jugador.mano.append(self.pozo.pop())

    def jugar(self):
        self.repartir_baraja()
        self.escojer_primer_ficha()
        while not self.fin_del_juego:
            jugador = self.jugadores[self.jugador_actual]
            print(f'Es el turno de {jugador.nombre}')
            print(f'Tu mano: {jugador.nombre}')
            mano_jugador = []
            for ficha in jugador.mano:
                mano_jugador.append(f'{ficha.izq}/{ficha.der}')
            print(mano_jugador)

            fichas_tablero = []
            for ficha in self.tablero_domino.tablero:
                fichas_tablero.append(f'{ficha.izq}/{ficha.der}')
            print(f'Tablero: {fichas_tablero}')
            # print(f'Tablero: {self.tablero_domino.tablero}')
            fichas_validas = self.get_fichas_validas(jugador)
            if fichas_validas:
                ficha_selleccionada = jugador.seleccionar_ficha(fichas_validas)
                self.tablero_domino.jugar_ficha(ficha_selleccionada, jugador)
                if len(jugador.mano) == 0:
                    print(f'{jugador.nombre} a Ganado!')


            else:
                print("Ninguna ficha que se pueda jugar, toma una del pozo")
                if not self.tomar_del_pozo(jugador):
                    print("El pozo esta vacio, fin del juego!")
                    self.fin_del_juego = True
            self.jugador_actual = (self.jugador_actual + 1) % len(self.jugadores)

    def escojer_primer_ficha(self):

        for jugador in self.jugadores:

            for ficha in jugador.mano:
                if ficha.is_mula() and ficha.izq == ficha.der and not self.tablero_domino.tablero:
                    if ficha.izq == 6:
                        self.tablero_domino.tablero.append(jugador.mano.pop(jugador.mano.index(ficha)))
                        break
                    elif ficha.izq == 4:
                        self.tablero_domino.tablero.append(jugador.mano.pop(jugador.mano.index(ficha)))
                        break
                    elif ficha.izq == 3:
                        self.tablero_domino.tablero.append(jugador.mano.pop(jugador.mano.index(ficha)))
                        break
                    elif ficha.izq == 2:
                        self.tablero_domino.tablero.append(jugador.mano.pop(jugador.mano.index(ficha)))
                        break
                    elif ficha.izq == 1:
                        self.tablero_domino.tablero.append(jugador.mano.pop(jugador.mano.index(ficha)))
                        break
                    elif ficha.izq == 0:
                        self.tablero_domino.tablero.append(jugador.mano.pop(jugador.mano.index(ficha)))
                        break
        for ficha in self.pozo:
            if ficha.is_mula() and ficha.izq == ficha.der and not self.tablero_domino.tablero:
                if ficha.izq == 6:
                    self.tablero_domino.tablero.append(self.pozo.pop(self.pozo.index(ficha)))
                    break
                elif ficha.izq == 4:
                    self.tablero_domino.tablero.append(self.pozo.pop(self.pozo.index(ficha)))
                    break
                elif ficha.izq == 3:
                    self.tablero_domino.tablero.append(self.pozo.pop(self.pozo.index(ficha)))
                    break
                elif ficha.izq == 2:
                    self.tablero_domino.tablero.append(self.pozo.pop(self.pozo.index(ficha)))
                    break
                elif ficha.izq == 1:
                    self.tablero_domino.tablero.append(self.pozo.pop(self.pozo.index(ficha)))
                    break
                elif ficha.izq == 0:
                    self.tablero_domino.tablero.append(self.pozo.pop(self.pozo.index(ficha)))
                    break

    def get_fichas_validas(self, jugador: JugadorDomino):
        fichas_validas = []
        for ficha in jugador.mano:
            if self.tablero_domino.is_jugable(ficha):
                fichas_validas.append(ficha)
        return fichas_validas

    def escojer_ganador(self):
        for jugador in self.jugadores:
            if jugador.puntuacion > self.puntuacion_alta:
                self.puntuacion_alta = jugador.puntuacion
                self.ganador = jugador

    def tomar_del_pozo(self, jugador):
        if not self.pozo:
            return False
        jugador.mano.append(self.pozo.pop())
        return True