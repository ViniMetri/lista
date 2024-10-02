def calculadora (operacao, num1, num2):
    match operacao:
        case 1:
                print(f"{num1} + {num2} = {num1 + num2}")
        case 2:
            print(f"{num1} - {num2} = {num1 + num2}")
        case 3:
            print(f"{num1} / {num2} = {num1 / num2}")
        case 4:
            print(f"{num1} x {num2} = {num1 * num2}")
        
        
print("Digite 1 para somar: ")
print("Digite 2 para subtrair: ")
print("Digite 3 para divisão: ")
print("Digite 4 para multiplicação: ")
operacao = int(input())

num1 = float(input("Digite o 1° numero: "))
num2 = float(input("Digite o 2° numero: "))
calculadora(operacao, num1, num2)