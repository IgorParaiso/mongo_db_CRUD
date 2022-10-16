from utils import config
from utils.splash_screen import SplashScreen
from controller.controller_cliente import Controller_Cliente
from controller.controller_laboratorio import Controller_Laboratorio
from controller.controller_agenda import Controller_Agenda
from reports.relatorios import Relatorio

tela_inicial = SplashScreen()
relatorio = Relatorio()
ctrl_Cliente = Controller_Cliente()
ctrl_lab = Controller_Laboratorio()
ctrl_agenda = Controller_Agenda()

def menu_relatorio():
    print(config.MENU_RELATORIOS)
    choice = int(input())
    config.clear_console(1)

    if choice == 1:
        relatorio.get_relatorio_clientes()
    elif choice == 2:
        relatorio.get_relatorio_agenda()
    elif choice == 3:
        relatorio.get_relatorio_laboratorios()
    elif choice == 4:
        relatorio.get_relatorio_clientes_lab()
    elif choice == 5:
        relatorio.get_relatorio_total_clientes()
    elif choice == 0:
        print("")
    else:
        print('opção inválida')

def menu_inserir():
    running = True
    while running:
        config.clear_console(1)
        print(config.MENU_ENTIDADES)
        choice = int(input('Escolha uma entidade\n'))
        config.clear_console(1)

        if choice == 1:
            print(config.MENU_ATRIBUTOS_CLIENTES)
            novo_cliente = ctrl_Cliente.inserir_cliente()
        elif choice == 2:
            print(config.MENU_ATRIBUTOS_AGENDA)
            nova_agenda = ctrl_agenda.inserir_agenda()
        elif choice == 3:
            print(config.MENU_ATRIBUTOS_LABORATORIOS)
            novo_lab = ctrl_lab.inserir_laboratorio()
        elif choice == 0:
            break
        else:
            print('opção inválida')

        continuar = input("Gostaria de inserir mais um registro? (Insira S para sim e N para não) ")
        if continuar.upper() == "N":
            running = False

def menu_remover():
    running = True
    while running:
    
        config.clear_console(1)
        print(config.MENU_ENTIDADES)
        choice = int(input('Escolha uma entidade\n'))
        config.clear_console(1)

        if choice == 1:
            relatorio.get_relatorio_clientes()
            ctrl_Cliente.excluir_cliente()
        elif choice == 2:
            relatorio.get_relatorio_agenda()
            ctrl_agenda.exclui_agenda()
        elif choice == 3:
            relatorio.get_relatorio_laboratorios()
            ctrl_lab.excluir_laboratorio()
        elif choice == 0:
            break
        else:
            print('opção inválida')
        
        continuar = input("Gostaria de excluir mais um registro? (Insira S para sim e N para não) ")
        if continuar.upper() == "N":
            running = False


def menu_atualizar():
    running = True
    while running:
        config.clear_console(1)
        print(config.MENU_ENTIDADES)
        choice = int(input('Escolha uma entidade\n'))
        config.clear_console(1)

        if choice == 1:
            print(config.MENU_ATRIBUTOS_CLIENTES)
            cliente_atualizado = ctrl_Cliente.atualizar_cliente()
        elif choice == 2:
            print(config.MENU_ATRIBUTOS_AGENDA)
            agenda_atualizada = ctrl_agenda.atualizar_agenda()
        elif choice == 3:
            print(config.MENU_ATRIBUTOS_LABORATORIOS)
            laboratorio_atualizado = ctrl_lab.atualizar_laboratorio()
        elif choice == 0:
            break
        else:
            print('opção inválida')
        
        continuar = str(input("Gostaria de atualizar mais um registro? (Insira S para sim e N para não) "))
        if continuar.upper() == "N":
            running = False

def run():

    while True:
        print(tela_inicial.get_updated_screen())
        print(config.MENU_PRINCIPAL)
        choice = int(input())
        config.clear_console(1)
        
        if choice == 1: #Relatórios
            menu_relatorio()
        
        elif choice == 2: #Inserir registros
            menu_inserir()

        elif choice == 3: #Remover registros
            menu_remover()
        
        elif choice == 4: #Atualizar registros
            menu_atualizar()
        
        elif choice == 5: #Sair
            print("Muito obrigado por usar o sistema")
            exit(0)
        else:
            print("opção inválida")
            exit(1)


if __name__ == '__main__':
    run()