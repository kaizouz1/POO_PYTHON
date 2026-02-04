import os
def limpar():
    os.system("cls")
limpar()

def saudacao(nome):
    print(f"Olá, {nome} seja bem-vindo")
    return nome
saudacao("João")

print("===" * 30)

def saudacao2():
    nome = input("Digite o seu nome:")
    print(f"Ola, {nome} seja bem-vindo")
saudacao2()

print("===" * 30)

def saudacao3():
    nome = input("Digite o seu nome:")
    return nome
nome1 = saudacao3()

print(f"Olá, {nome1} seja bem-vindo")


def soma(a,b):
    soma = a + b
    print(f"A + b = {soma}")
soma(10,20)