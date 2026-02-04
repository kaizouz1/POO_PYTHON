import os
def limpar():
    os.system("cls")
limpar()

def desconto1(preco):
    porcentagem = preco * 0.10
    return porcentagem
desconto2 = desconto1(200)
precofl = 200 - desconto2
print(f"O desconto foi de {desconto2}")
print(f"O valor final ficou por {precofl}")