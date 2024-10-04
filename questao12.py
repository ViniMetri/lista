def Cel_Far(Cel):
    resultado = (Cel * 1.8) + 32
    return resultado


def Far_Cel(Far):
    resultado = (Far-32) / 1.8
    return resultado



print("--------------------------")
print("1- Celsius para Fahrenheit")
print("2- Fahrenheit para Celsius")
print("--------------------------")

escolha = int(input("Digite a opção:" ))


if escolha == 1:
    cel = float(input("Digite a Temperatuda em Celsius: "))
    print(Cel_Far(cel))
elif escolha == 2:
    far = float(input("Digite a Temperatura em Fahrenheit"))
    print(Far_Cel(far))