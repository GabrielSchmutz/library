from modules import *
import readchar
import os

def main():
    while True:
        os.system("clear")
        print("Usuário não cadastrado/logado")
        print("Bem vindo(a) ao sistema da Biblioteca! O que desejas fazer?\n\na) Procurar livros \nb) Criar conta\n")
        key = readchar.readkey()

        if key == 'a' or key == 'A':
            os.system("clear")
            print("Aqui está uma lista de livros:\n\n=================\n")
            inicializar_livros()
            print("=================")
            print("\nGostaria de pegar algum livro emprestado?\na) Sim\nb) Não")
            key = readchar.readkey()
            if key == 'a' or key == 'A':
                print("Qual livro você deseja pegar emprestado?\n")
            elif key == 'b' or key == 'B':
                print("Muito obrigado. Tchau")
                break
        elif key == 'b' or key == 'B':
             criar_conta()


if __name__ == "__main__":
    main()
