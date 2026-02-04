import os
def limpar():
    os.system("cls")
limpar()


def epar(a):
    par = (a % 2 == 0)
    return par
print(epar(2))

print("===" * 20)

# Para retornar par ou impar:
def par_ou_impar(a):
    if epar(a):
        return "par"
    else: 
        return "impar"
print(par_ou_impar(4))