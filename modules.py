def inicializar_livros():
    arquivos = "livros.txt"

    with open(arquivos, 'r') as arquivo:
        conteudo = arquivo.read()

    print(conteudo)


def criar_conta():
    nome = input("Qual é seu nome? ")
    lista_de_usuarios = ["tony", "jonas", "douglas", "camila"]
    if not nome in lista_de_usuarios:
        senha = input("Digite sua senha: ")
        print(f"\nSeja bem-vindo(a) {nome}")

def login():
    print()
