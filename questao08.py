def primo(num):
    tot = 0
    for c in range(1, num + 1):
        if num % c == 0:
            tot +=1
    if tot == 2:
        print("É um numero primo")
    else:
        print("não é primo")
        

num = int(input("Digite um numero: "))
primo(num)
        