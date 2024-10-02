def num_vogais(mensagem):
    vogais = "aeiouAEIOU"
    vogais_encontradas = []
    
    for letras in mensagem:
        if letras in vogais:
            vogais_encontradas.append(letras)
            
    return vogais_encontradas

print("Digite sua mensagem : ")
mensagem = input()
resultado = num_vogais(mensagem)
print(resultado)