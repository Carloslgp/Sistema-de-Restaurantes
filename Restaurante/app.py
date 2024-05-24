import os
import time

restaurantes = [{"nome":"Praça", "categoria":"Japonesa", "ativo":False},
                {"nome":"Pizza Suprema", "categoria":"Pizza", "ativo":True},
                {"nome":"Cantina", "categoria":"Italiano", "ativo":False}]

def voltar_ao_menu_principal():
    """Essa fução volta para o menu principal
    
    Inputs:
    -Recebe qualquer tecla

    Outputs:
    -Volta para a função "Main"
    
    """
    input("Digite qualquer tecla para voltar para o menu principal: ")
    main()

def exibir_subtitulo(texto):
    """Essa função exibe o subtitulo em cada entrada em diferentes partes do sistema"""
    os.system("cls")
    linha = '*' *(len(texto))
    print(linha)
    print(texto)
    print(linha)

def finalizar_app():
    """essa Função finaliza o app"""
    exibir_subtitulo("Finalizando app...")

def opcao_invalida():
    """ESsa função mostra que a opção digitada é inválida"""
    print("Opção inválida!\n")
    voltar_ao_menu_principal()


def exibir_nome_do_programa():
    """Exibe o nome do programa"""
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    """Exibe os processos que podem ser executados pelo programa"""
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Alternar estado do restaurante")
    print("4. Sair\n")

def cadastrar_novo_restaurante():
    """Cadastra um novo restaurante no sistema
    
    Inputs:
    -Nome do Restaurante
    -Categoria

    Outputs:
    -Adiciona um novo restaurante a lista de restaurantes
    
    """
    exibir_subtitulo("Cadastro de novos restaurantes:\n")
    nome_do_restaurante = input("Digite o nome do restaurante: ")
    categoria = input(f"Digite o nome da categoria do restaurante:{nome_do_restaurante}: ")
    dados_do_restaurante = {"nome":nome_do_restaurante, "categoria":categoria, "ativo":False}
    restaurantes.append(dados_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!!!")
    voltar_ao_menu_principal()

def listar_restaurantes():
    """Exibe os restaurantes cadastrados"""
    exibir_subtitulo("Listando restaurantes: ")

    print(f"{"Nome".ljust(20)} | {"Categoria".ljust(20)} | {"Status"}")
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = restaurante["ativo"]
        if ativo == True:
            ativo = "O restaurante está ativo"
        else:
            ativo = "O restaurante está inativo"
        print(f"{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}")
        time.sleep(0.5)

    voltar_ao_menu_principal()

def alternar_estado_do_restaurante():
    """Muda o status do restaurante para inativo ou ativo no sistema
    
    Inputs:
    -Recebe o nome do restaurante

    Outputs:
    -Muda o status do restaurante para ativo ou inativo caso o nome passado exista no sistema
    
    """
    exibir_subtitulo("Alterando estado do restaurante")
    nome_restaurante = input("Digite o nome do restaunrate que você deseja mudar o estado:")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso" if restaurante["ativo"] else f"O restaurante {nome_restaurante} foi desativado com sucesso"
            print(mensagem)
    if not restaurante_encontrado:
        print("O restaurante não foi encotrado")

    voltar_ao_menu_principal()

def escolher_opcao():
    """Faz o usuário escolher uma opção
    
    Inputs:
    -Recebe um certo número

    Outputs:
    -Executa uma determinada função
    
    """
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_do_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    """Exibe a parte principal do programa"""
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == "__main__":
    main()
