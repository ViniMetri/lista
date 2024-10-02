def autenticar(login):
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
    if login in usuarios:
        print("oi")
    
login = input("Digite seu login: ")
senha = input("Digite sua senha: ")
autenticar(login)