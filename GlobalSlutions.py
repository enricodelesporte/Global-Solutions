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
            suporte()

        elif (opcao == 7):
            print("Obrigado por contar a Safe Bag, espero te ver em breve!!")
            Executando = False
        
#Cadastro do usuário
def cadastro():
    print("\n----Cadastro----")
    nome = input("Qual seu nome completo: ").strip()

    #Verificação se o campo está preenchido
    while not nome: 
        print("Esse campo deve ser preenchido")
        nome = input().strip()

    email = input("Qual seu email: ").strip()

    #Verificação para saber se o email está correto
    while not email or "@" not in email or "." not in email:
        print("Email está inválido")
        email = input("Email: ").strip()

    senha = input("Digite sua senha: ").strip()

    #Validação da senha do usuário
    while not senha or len(senha) < 5:
        print("A senha deve conter pelo menos 5 caracteres.")
        senha = input("Senha: ").strip()

    for usuario in usuarios:
        if usuario.email == email:
            print("Já existe um usuário com esse email.")
            return
    
    #Adicionando usuário na lista de Usuários 
    usuario = Usuario(nome, email, senha)
    usuarios.append(usuario)
    print(f"Usuário {nome} cadastrado com sucesso!")

#Login do Usuário
def login():
    global usuarioLogado

    if not Usuario:
        print("Nenhum usuário registrado. Fazer cadastro.")
        return
    
    logado = False
    while not logado:
        print("\n----Login----")
        email = input("Email: ").strip()
        senha = input("Senha: ").strip()

        #Procura o usuário
        usuarioFiltrado = list(filter(lambda u: u.email == email and u.senha == senha, usuarios))

        #Válida as informações
        if usuarioFiltrado:
            usuarioLogado = usuarioFiltrado[0]
            print(f"Bem-vindo de volta, {usuarioLogado.nome}!")
            logado = True
        else:
            print("Email ou senha incorretos! Tente novamente ou faça seu cadastro. \n(1)Tentar novamente\n(2)Fazer cadastro")
            opcao = input().strip()
            if opcao == "1":
                continue
            elif opcao == "2":
                return cadastro()
            else: 
                print("Valor inválido! Tente novamente")
                continue
                

def criarMochila():
    if not usuarioLogado:
         print("Nenhum usuário cadastrado. Fazer login.")
         return

    print("----Criar Mochila----")
    nome = input("Nome da mochila: ").strip()
    categoria = input("Categoria: ").strip()
    descricao = "Mochila de sobrevivência contra desastres ambietais, nela contém os itens necessários para ficar bem até a chegada dos socorros."
   
    mochila = MochilaSobrevivencia(nome, descricao, categoria)
    mochilas.append(mochila)

    print(f"\nNome da mochila: {nome} \nDescrição: {descricao} \nCategoria: {categoria}")

def minhaMochila():

    print("----Minha Mochila----")
    if not usuarioLogado:
        print("Nenhu usuário encontrado! Fazer login.")
    elif not mochilas:
        print("Nenhuma mochila criada.")
    else:
        for i, mochila in enumerate(mochilas, start= 1):
            print(f"{i}. Mochila: {mochila.nome} Categoria: {mochila.categoria}")

def contatoEmergenia():
    print("----Contato de Emergência----")
    print("Qual emergência você precisa: \n(1)Ambulância \n(2)Bombeiro \n(3)Polícia")
    opcao = input().strip()

    if opcao == "1":
        print("Para chamar uma ambulância ligue para 192")
    elif opcao == "2":
        print("Para chamar os bombeiros ligue para 193")
    elif opcao == "3":
        print("Pra chamar a polícia ligue para 190") 
    else:
        print("Valor inválido! Tente novamente.")
        contatoEmergenia()

def suporte():
    print("----Suporte----")
    if not usuarioLogado:
        print("Nenhum usuário encontrado.Fazer login")
        return

    problema = input("Descreva seu problema: ").strip()
    if problema:
        print("Sua mensagem foi enviada para nosso suporte")
    else: 
        print("Este campo está vázio. Preencha corretamente.")

menuPrincipal()
