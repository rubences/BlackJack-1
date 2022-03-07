import random
from pedir_numero import pedir_entrada_numero_delimitado

cartas = {
    chr(0x1f0a1): 1,
    chr(0x1f0a2): 2,
    chr(0x1f0a3): 3,
    chr(0x1f0a4): 4,
    chr(0x1f0a5): 5,
    chr(0x1f0a6): 6,
    chr(0x1f0a7): 7,
    chr(0x1f0a8): 8,
    chr(0x1f0a9): 9,
    chr(0x1f0aa): 10,
    chr(0x1f0ab): 11,
    chr(0x1f0ad): 12,
    chr(0x1f0ae): 13,
}
baraja = (list(cartas.values())) * 4

def simbolo_carta(carta):
    if carta == 1:
        carta = chr(0x1f0a1)
    elif carta == 2:
        carta = chr(0x1f0a2)
    elif carta == 3:
        carta = chr(0x1f0a3)
    elif carta == 4:
        carta = chr(0x1f0a4)
    elif carta == 5:
        carta = chr(0x1f0a5)
    elif carta == 6:
        carta = chr(0x1f0a6)
    elif carta == 7:
        carta = chr(0x1f0a7)
    elif carta == 8:
        carta = chr(0x1f0a8)
    elif carta == 9:
        carta = chr(0x1f0a9)
    elif carta == 10:
        carta = chr(0x1f0aa)
    elif carta == 11:
        carta = chr(0x1f0ab)
    elif carta == 12:
        carta = chr(0x1f0ad)
    else:
        carta = chr(0x1f0ae)
    return carta

def puntuacion(carta, total):
    if carta == 1:
        total += 11
    elif carta == 2:
        total += 2
    elif carta == 3:
        total += 3
    elif carta == 4:
        total += 4
    elif carta == 5:
        total += 5
    elif carta == 6:
        total += 6
    elif carta == 7:
        total += 7
    elif carta == 8:
        total += 8
    elif carta == 9:
        total += 9
    elif carta == 10:
        total += 10
    elif carta == 11:
        total += 10
    elif carta == 12:
        total += 10
    elif carta == 13:
        total += 10
    return total

def carta_inicial(baraja):
    mano = []
    total = 0
    for i in range(2):
        random.shuffle(baraja)
        carta = baraja.pop()
        puntos = puntuacion(carta, 0)
        total += puntos
        carta = simbolo_carta(carta)
        mano.append(carta)
    return mano, total

def pedir_carta(mano, total, baraja):
    carta = baraja.pop()
    if carta == 1:
        puntos = 11
    elif carta == 11:
        puntos = 10
    elif carta == 12:
        puntos = 10
    elif carta == 13:
        puntos = 10
    else:
        puntos = carta
    total += puntos
    carta = simbolo_carta(carta)
    mano.append(carta)
    return mano, total

def resultados(jugador, banca):
    print("La banca tiene " + str(banca[0]) + " que son " + str(banca[1]) + " puntos.")
    print("Tú has sacado " + str(jugador[0]) + " que son " + str(jugador[1]) + " puntos.")

def partida(jugador, banca):
    if jugador[1] == 21:
        resultados(jugador, banca)
        print("Tienes un blackjack!!!, Has ganado!!!")
    elif banca[1] == 21:
        resultados(jugador, banca)
        print("Has perdido :(, la banca tiene un blackjack")
    elif jugador[1] > 21 and banca[1] > 21:
        resultados(jugador, banca)
        print("Te has pasado de 21, termina el juego sin ganadores ni perdedores.")
    elif jugador[1] > 21:
        resultados(jugador, banca)
        print("Te has pasado de 21, has perdido.")
    elif banca[1] > 21:
        resultados(jugador, banca)
        print("La banca se ha pasado, tú ganas.")
    elif jugador[1] < banca[1]:
        resultados(jugador, banca)
        print("Has perdido, la banca tiene más puntos.")
    elif jugador[1] > banca[1]:
        resultados(jugador, banca)
        print("Has ganado a la banca!!!")

def jugar_de_nuevo():
    otra = pedir_entrada_numero_delimitado("¿Quieres jugar de nuevo?: Sí=1, No=2", 1, 2)
    if otra == 1:
        jugador = []
        banca = []
        baraja = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] * 4
        juego()
    else:
        print("Gracias por jugar.")
        return False

  
def juego():
    opcion = 0
    print("Vamos a jugar Blackjack!!!")
    jugador = list(carta_inicial(baraja))
    banca = list(carta_inicial(baraja))
    if banca[1] == 21:
        print("La banca tiene " + str(banca[0]) + " que son " + str(banca[1]) + " puntos.")
        print("Tú has sacado " + str(jugador[0]) + " que son " + str(jugador[1]) + " puntos.")
        print("La banca ha sacado un blackjack, por lo que pierdes.")
        SioNo = jugar_de_nuevo()
        if SioNo == False:
            opcion = 3
    elif jugador[1] == 21:
        print("La banca tiene " + str(banca[0]) + " que son " + str(banca[1]) + " puntos.")
        print("Tú has sacado " + str(jugador[0]) + " que son " + str(jugador[1]) + " puntos.")
        print("Has sacado un blackjack!!!, se acabó el juego.")
        SioNo = jugar_de_nuevo()
        if SioNo == False:
            opcion = 3
    else:
        while opcion != 3:
            print("La banca tiene " + str(banca[0]) + " que son " + str(banca[1]) + " puntos.")
            print("Tú has sacado " + str(jugador[0]) + " que son " + str(jugador[1]) + " puntos.")
            opcion = pedir_entrada_numero_delimitado("¿Quieres coger carta(1), plantarte(2) o acabar(3)?", 1, 3)
            if opcion == 1:
                jugador = list(pedir_carta(jugador[0], jugador[1], baraja))
                while puntuacion(banca[0], banca[1]) < 16:
                    banca = list(pedir_carta(banca[0], banca[1], baraja))
                partida(jugador, banca)
                SioNo = jugar_de_nuevo()
                if SioNo == False:
                    break
            if opcion == 2:
                while puntuacion(banca[0], banca[1]) < 16:
                    banca = list(pedir_carta(banca[0], banca[1], baraja))
                partida(jugador, banca)
                SioNo = jugar_de_nuevo()
                if SioNo == False:
                    break
            if opcion == 3:
                print("Gracias por jugar.")
                break

juego()