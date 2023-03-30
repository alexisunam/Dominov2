# This is a sample Python script.
# from dominio.impl.CreadorBarajaDomino import CreadorBarajaDomino
from dominio.impl.JuegoDomino import JuegoDomino
from dominio.impl.JugadorDomino import JugadorDomino

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


FICHAS = []


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':



    # print_hi('PyCharm')
    # pozo_domino = CreadorBarajaDomino().crear_baraja()
    # jugador1 = JugadorDomino("Juan")
    # jugador2 = JugadorDomino("Alexis")
    # jugador3 = JugadorDomino("Ulises")
    # jugador4 = JugadorDomino("Emiliano")
    #
    # jugadores = [jugador1, jugador2, jugador3]
    #
    # for jugador in jugadores:
    #     for num in range(1, 8):
    #         jugador.mano.append(pozo_domino.pop())
    #     print(jugador.mano)
    #
    # for jugador in jugadores:
    #     print(f"Jugador: {jugador.nombre}")
    #     for ficha in jugador.mano:
    #         print(f"ficha: {ficha.cara1}, {ficha.cara2}")
    #
    # print(f"Pozo: {pozo_domino}")
    # for ficha in pozo_domino:
    #     print(f"Ficha: {ficha.cara1}, {ficha.cara2}")

    jugador_humano = JugadorDomino("Alexis")
    jugador_humano.set_true_human(True)

    jugadores = [jugador_humano, JugadorDomino("Maquina 1"), JugadorDomino("Maquina 2")]
    juego = JuegoDomino(jugadores)
    opcion = True
    while opcion:
        print("Seleccione una opcion: ")
        opcion1 = input("Seleccion 0 para leer las reglas o 1 para jugar")
        reglas = """
            visite esta pagina para ver las reglas
            https://www.mundijuegos.com.mx/multijugador/domino/reglas/
        """
        if opcion1 == "0":

            print(reglas)
        else:
            juego = JuegoDomino(jugadores)
            juego.jugar()
            desicion = input("Quieres volver a jugar (0) o salir (1)")
            if desicion == '0':
                juego_nuevo = JuegoDomino(jugadores)
                juego_nuevo.jugar()
            else:
                opcion = False






# See PyCharm help at https://www.jetbrains.com/help/pycharm/
