import os
def limpar():
    os.system("cls")
limpar()


def contar_letras():
    palavra = input("Digite qualquer coisa: ")
    print(f"A palavra {palavra} possui {len(palavra)} letras")
contar_letras()