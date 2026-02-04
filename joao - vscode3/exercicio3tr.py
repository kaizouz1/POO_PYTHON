import os
def limpar():
    os.system("cls")
limpar()

numero = 10

def alterna(numero):
    print(input("Vai dar certo ou vai dar erro? "))
    numero += 5
    print(f"Número equivale a {numero}")
alterna(numero)