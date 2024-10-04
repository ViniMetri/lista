def soma(quantidade):
    lista_numero = []
    for i in range (quantidade):
        numero = float(input("Digite um numero: "))
        lista_numero.append(numero)
    resultado = sum(lista_numero) / quantidade
    return resultado

   
      
     


quantidade_numeros = int(input("Digite a quantidade de numeros: "))
print(soma(quantidade_numeros))