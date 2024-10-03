def autenticar(login, senha):
    for usuario in usuarios:
        if login == usuario['username']:
            
            for teste_senha in usuarios:
                if senha == teste_senha['password']:
                    print("Acesso Liberado")
                    break
                else:
                    print("Acesso Negado")
                    
        else:
            print("Acesso Negado")
        
usuarios = [
        {
            "username" : "teste",
            "password" : "admin"  
        },
        {
            "username" : "teste2",
            "password" : "admin2"
        },
        {
            "username" : "teste3",
            "password" : "admin3"
        }
    ]
    
login = input("Digite seu login: ")
senha = input("Digite sua senha: ")
autenticar(login, senha)