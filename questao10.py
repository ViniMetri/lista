def numero_de_palavras(texto):
    palavras = texto.split( )
    quantidade = len(palavras)
    return quantidade

texto = input("Digite um texto: ")
resultado = numero_de_palavras(texto)
print(f"o texto possui {resultado} palavras")