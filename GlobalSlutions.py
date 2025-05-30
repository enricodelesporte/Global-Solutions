#Importando as classes criadas
import ContatoEmergencia
import DesastreAmbiental
import ItemSobrevivencia
from MochilaSobrevivencia import MochilaSobrevivencia
import RegiaoRisco
from Usuario import Usuario

usuarios = []
usuarioLogado = None
mochilas = []

Executando = True 

#Criação do menu principal
def menuPrincipal():
    global Executando
    while Executando:
        print("\n---- Menu Principal ----")
        print("1. Cadastro")
        print("2. Login")
        print("3. Criar Mochila")
        print("4. Minha Mochila")
        print("5. Contao de Emergência")
        print("6. Suporte")
        print("7. Sair")

        #Escolha do usuário
        opcao = input()
        
        #Válidação da esolha do usuário
        if(not opcao.isdigit() or int(opcao) not in range(1,8)):
            print("Opção inválida. Digite um número de 1 a 7 para poder continuar")
            continue

        opcao = int(opcao)

        if (opcao == 1):
            cadastro()

        elif (opcao == 2):
            login()
        
        elif (opcao == 3):
            criarMochila()
        
        elif (opcao == 4):
            minhaMochila()

        elif (opcao == 5):
            contatoEmergenia()

        elif (opcao == 6):
            suport()

        elif (opcao == 7):
            print("Obrigado por contar a Safe Bag, espero te ver em breve!!")
            Executando = False
        
#Cadastro do usuário
def cadastro():
    print("\n----Cadastro----")
    print ("Qual seu nome completo:")
    nome = input().strip()

    #Verificação se o campo está preenchido
    while not nome: 
        print("Esse campo deve ser preenchido")
        nome = input().strip()

    print("Qual seu email: ")
    email = input().strip()

    #Verificação para saber se o email está correto
    while not email or "@" not in email or "." not in email:
        print("Email está inválido")
        print("Email: ")
        email = input().strip()

    print("Digite sua senha: ")
    senha = input().strip()

    #Validação da senha do usuário
    while not senha or len(senha) < 5:
        print("A senha deve conter pelo menos 5 caracteres.")
        senha = input("Senha: ").strip()

    for usuario in usuarios:
        if usuario.email == email:
            print("Já existe um usuário com esse email.")
            return
    
    #Adicionando usuário na lista de Usuários 
    usuario = {"nome": nome, "email": email, "senha": senha}
    usuarios.append(usuario)
    print(f"Usuário {nome} cadastrado com sucesso!")




menuPrincipal()
