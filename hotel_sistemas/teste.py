from controllers import hotel_controller


class Client:
    def __init__(self, nome: str, cpf: str):
        self.nome = nome
        self.cpf = cpf

# Supondo que sua classe se chame HotelManager
manager = hotel_controller.HotelController()

print("--- INICIANDO TESTES ---")

# TESTE 1: Registro Normal (Sucesso)
print("\nTeste 1: Registro Válido")
c1 = Client("Alice", "123.456.789-00")
manager.register_client(c1)

# TESTE 2: Duplicação (Deve cair no seu 'else')
print("\nTeste 2: CPF Duplicado")
c2 = Client("Alice Repetida", "123.456.789-00")
manager.register_client(c2)

# TESTE 3: Objeto Inválido (Deve cair no AttributeError)
print("\nTeste 3: Passando uma String em vez de Objeto")
manager.register_client("Não sou um cliente")

# TESTE 4: Objeto Nulo (Deve cair no TypeError)
print("\nTeste 4: Passando None")
manager.register_client(None)

# TESTE 5: Objeto sem CPF (Deve cair no seu ValueError customizado)
print("\nTeste 5: Cliente sem CPF")
c3 = Client("Bruno", "") # CPF Vazio
manager.register_client(c3)

print("\n--- FIM DOS TESTES ---")
print(f"Estado final do dicionário: {manager.client_dict}")