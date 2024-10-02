def soma_lista(quantitdade):
    lista = []
    for i in range(1, quantitdade + 1):
        numeros = int(input("Digite um numero: "))
        lista.append(numeros)
    return sum(lista)

quantitdade = int(input("Quantos numeros você quer digitar: "))
resultado = soma_lista(quantitdade)
print(resultado)