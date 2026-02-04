import os
def limpar():
    os.system("cls")
limpar()

def alterna():
    print(input("Vai dar certo ou vai dar erro? "))
    numero = (int(input("digite o valor de número: ")) + 5)
    print(numero)
alterna()