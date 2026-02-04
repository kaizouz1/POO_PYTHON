import os
def limpar():
    os.system("cls")
limpar()


# escopo local e global

# Os valores abaixo são valores globais, funcionando no codigo inteiro
a = 5
b = (2 + a)
c = (6 + b)
def teste(c):
  # Os valores abaixos são valores locais, que funcionam apenas dentro da função
  a = 8
  b = 4
  c += 2
  print(f"A dentro da funçã vale {a}")
  print(f"B dentro da funçã vale {b}")
  print(f"C dentro da funçã vale {c}")
a = 5 
teste(a)
print(f"\n")
print(f"A fora da função vale {a}")
print(f"B fora da função vale {b}")
print(f"C fora da função vale {c}")
##teste
# Posso ir ao banheiro?