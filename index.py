import os
import random
from colorama import Fore

jogarnovamente = "s"
jogadas = 0
quemjoga = 2
maxjogadas = 9
verivitorias = "n"

velha = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def tela():
    global velha
    global jogadas
    os.system("cls" if os.name == "nt" else "clear")  # Limpar o console

    print("    0   1   2")
    print("0:  " + velha[0][0] + " | " + velha[0][1] + ' | ' + velha[0][2])
    print("    -----------")
    print("1:  " + velha[1][0] + " | " + velha[1][1] + ' | ' + velha[1][2])
    print("    -----------")
    print("2:  " + velha[2][0] + " | " + velha[2][1] + ' | ' + velha[2][2])
    print("Jogadas: " + Fore.GREEN + str(jogadas) + Fore.RESET)

def jogadorjoga():
    global jogadas
    global quemjoga
    global maxjogadas

    if quemjoga == 2 and jogadas < maxjogadas:
        l = int(input("Linha: "))
        c = int(input("Coluna: "))

        try:
            while velha[l][c] != " ":
                l = int(input("Linha: "))
                c = int(input("Coluna: "))
            velha[l][c] = "X"
            quemjoga = 1
            jogadas += 1
        except:
            print("Linha e/ou coluna inválida!")

def cpujoga():
    global jogadas
    global quemjoga
    global verivitorias
    global maxjogadas

    if quemjoga == 1 and jogadas < maxjogadas:
        l = random.randrange(0, 3)
        c = random.randrange(0, 3)

        while velha[l][c] != " ":
            l = random.randrange(0, 3)
            c = random.randrange(0, 3)

        velha[l][c] = "O"
        jogadas += 1
        quemjoga = 2

while True:
    tela()
    jogadorjoga()
    cpujoga()




