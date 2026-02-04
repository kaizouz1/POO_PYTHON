import os
def limpar():
    os.system("cls")
limpar()

total = 100

def adicionar(valor):
    a = total + valor
    print(f"{total} + {valor} equivale a {a}")
adicionar(10)
print(f"O total global equivale a {total}")

