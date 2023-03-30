from abc import ABC, abstractmethod

# from Jugador import Jugador


class JuegoMesa(ABC):

    @abstractmethod
    def repartir_baraja(self):
        pass

    @abstractmethod
    def escojer_ganador(self):
        pass

    @abstractmethod
    def jugar(self):
        pass

