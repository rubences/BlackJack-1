import sys

def pedir_entrada_numero(invitacion):
    while True:
        print(invitacion, end = ": ")
        entrada = input()
        try:
            entrada = int(entrada)
        except:
            print("Solo los caracteres [1-3] están autorizados.", file = sys.stderr)
        else:
            return entrada

def pedir_entrada_numero_delimitado(invitacion, minimo, maximo):
    while True:
        entrada = pedir_entrada_numero(invitacion)
        if minimo <= entrada <= maximo:
            return entrada