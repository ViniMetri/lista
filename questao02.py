def num_digito(valor):
    tamanho = str(valor)
    tamanho = len(valor)
    print(f"esse numero tem {tamanho} digitos")

valor = int(input("Digite um numero inteiro: "))
num_digito(valor)