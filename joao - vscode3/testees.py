import os
def limpar():
  os.system("cls")
limpar()
import math
from time import sleep


while True:

 print("=== Menus ===\n")
 print("1 - Menu matematico")
 print("2 - Menu While")
 print("3 - Menu For")
 print("4 - Menu Função")

 escolha = input("Digite sua escolha: ")



 if escolha == "1":
  limpar()    
  print(" === Menu matematico ===\n")
  print("1 - Potenciação")
  print("2 - Raiz")
  print("3 - Multiplicação")
  print("4 - Adição")
  print("5 - Subtração")
  print("6 - Divisão")
  print("7 - Fatorial")

  opcao = input("Digite sua escolha: ")
  if opcao == "1":
    limpar()
    print("=== Potenciação ===")
    base = float(input("Digite a base: "))
    expoente = float(input("Digite o expoente: "))
    resultado = math.pow(base, expoente)
    print(f"{base} ** {expoente} = {resultado}")


  elif opcao == "2":
    limpar()
    print("=== Raiz Quadrada ===")
    numero = float(input("Digite a base: "))
    raiz = math.sqrt(numero)
    print(f"a raiz de {numero} equivale a {raiz}")

  elif opcao == "3":
    limpar()
    print("=== Multiplicação ===")
    numero = int(input("Digite um número:"))
    numero2 = int(input("Digite o multiplicador: "))
    resultado = numero * numero2
    print(f"{numero} * {numero2} = {resultado}")


  elif opcao == "4":
   limpar()
   print("=== Adição ===")
   numero1 = int(input("Digite um número: "))
   numero2 = int(input("Digite outro número: "))
   resultado = numero1 + numero2
   print(f"{numero1} + {numero2} = {resultado}")

  elif opcao == "5":
    limpar()
    print("=== Subtração ===\n")
    numero1 = int(input("Digite um número:"))
    numero2 = int(input("Digite outro número: "))
    resultado = numero1 - numero2
    print(f"{numero1} - {numero2} ")

  elif opcao == "6":
    limpar()
    print("=== Divisão ===\n")
    numero = float(input("Digite um número:"))
    divisor = float(input("Digite o divisor: "))
    resultado = numero / divisor
    print(f"{numero} / {divisor} = {resultado}")


  elif opcao == "7":
    limpar()
    print("=== Fatorial ===")
    numero = int(input("Digite o número: "))
    fatorial = math.factorial(numero)
    print(f"O fatorial de {numero} = {fatorial}")


 elif escolha == "2":
  limpar()
  print("=== Menu While ===")
  print("1 - Crescente while")
  print("2 - Decrescente While")
  print("3 - Loop de nome")
  print("4 - Senha incorreta")

  opcao = input("Digite sua escolha: ")
 
  if opcao == "1":
    
    contador = int(input("Digite um número para o contador: "))
    limitador = int(input("Digite até que número deseja contar: "))
    while contador <= limitador:
        print(contador)
        contador += 1
  
  elif opcao == "2":
    limpar()
    contador = int(input("Digite um número para o contador: "))
    limitador = int(input("Digite um número para o limitador: "))
    while contador >= limitador:
      print(contador)
      contador -= 1
  
  elif opcao == "3":
    limpar()
    nome = ""

    while nome != "sair":
     nome = input("Digite um nome(ou 'sair'): ")
  
  elif opcao == "4":
   limpar()
   senha = int(input("Digite a senha:"))
   while senha != 1234:
     print("Senha incorreta!")
     senha = int(input("Digite a senha correta:"))
   sleep(3)
   limpar()
   print("Senha correta!")
   limpar()

