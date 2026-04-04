from controllers.hotel_controller import HotelController

controller = HotelController()

def start():
    print("Bem vindo")
    print("1 - Cliente")
    print("2 - Administrção")

def cliente_opcoes():
    print("1 - Cadastrar cliente")
    print("2 - Já sou Cliente")
    print("0 - Sair")

def admin_login():
    login= input("Login: ")
    password= input("Password: ")

def cadastrar_cliente():
    nome = input("Nome: ")
    idade = input("Idade: ")
    cpf = input("CPF: ")
    controller.cadastrar_cliente(nome, idade, cpf)
    print("Cliente cadastrado com sucesso!")

def login_cliente():
    cpf = input("CPF: ")


def cadastrar_quarto():
    numero = input("Número do quarto: ")
    controller.cadastrar_quarto(numero)
    print("Quarto cadastrado com sucesso!")

def fazer_reserva():
    cliente_id = input("ID do cliente: ")
    quarto_id = input("ID do quarto: ")
    checkin = input("Check-in (dd/mm/aaaa): ")
    dias = input("Dias: ")
    controller.fazer_reserva(cliente_id, quarto_id, checkin, dias)
    print("Reserva feita com sucesso!")

def listar_reservas():
    reservas = controller.listar_reservas()
    for r in reservas:
        print(r)

def sair():
    print("Encerrando...")
    exit()

def executar(opcao):
    acoes = {
        "1": cadastrar_cliente,
        "2": cadastrar_quarto,
        "3": fazer_reserva,
        "4": listar_reservas,
        "0": sair,
    }
    acao = acoes.get(opcao)
    if acao:
        acao()
    else:
        print("Opção inválida.")

def run():
    while True:
        exibir_opcoes()
        opcao = input("\nEscolha: ")
        executar(opcao)