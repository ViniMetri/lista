def somar ( num1, num2):
    return num1 + num2
def sub (num1, num2):
    return num1 - num2
def div (num1, num2):
    return num1 / num2
def mult (num1, num2):
    return num1 * num2

num1 = float(input("Digite o 1° numero: "))
num2 = float(input("Digite o 2° numero: "))
somar( num1, num2)
sub(num1, num2)
div(num1, num2)
mult(num1, num2)

print(f"soma = {somar}")
print(f"subtração = {sub}")
print(f"divisão = {div}")
print(f"multiplicação = {mult}")