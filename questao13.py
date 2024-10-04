import re
def Verificar (verificador):
    resultado = re.search(r'@', verificador)
    if resultado:
        print(f"seu email é {verificador}")
                

verificador = input("Digite um email: ")
Verificar(verificador)