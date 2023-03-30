from abc import ABC, abstractmethod


class Jugador(ABC):

    @abstractmethod
    def agregar_a_mano(self):
        pass

    @abstractmethod
    def set_true_human(self, valor: bool):
        pass
    # @abstractmethod
    # def pintar_mano(self):
    #     pass
    # @abstractmethod
    # def is_human(self):
    #     pass