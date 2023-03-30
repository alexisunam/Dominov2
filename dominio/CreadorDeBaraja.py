from abc import ABC, abstractmethod


class CreadorDeBaraja(ABC):

    @abstractmethod
    def crear_baraja(self):
        pass