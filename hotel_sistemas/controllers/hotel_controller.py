from models.client import Client
from models.room import Room
from models.booking import Booking
from models.admin import Admin

class HotelController:

    admin_password="teste"

    def __init__(self):
        self.client_dict: dict[str, Client] = {}
        self.room_list: list[Room]= []
        self.booking_dict: dict[str, Booking] = {}

    def register_client(self, client: Client):
        try:
            # O sistema tenta extrair os dados do objeto
            # Se 'client' for None ou não for um objeto, vai gerar um erro
            client_data = vars(client) 
            client_cpf = client_data.get("cpf")

            # Verifica se o CPF existe no objeto
            if not client_cpf:
                raise ValueError("O objeto Client não possui um CPF válido.")

            # Lógica de registro
            if client_cpf not in self.client_dict:
                self.client_dict[client_cpf] = client_data #É adicionado os dados do novo cliente ao dicionário
                print(f"Cliente {client.nome} registrado com sucesso!")
            else:
                print(f"Erro: O CPF {client_cpf} já está cadastrado.")

        except TypeError:
            print("Erro: Você tentou registrar algo que não é um objeto válido.")
        
        except AttributeError:
            print("Erro: O objeto passado como parâmetro não possui os atributos necessários de um Cliente.")
            
        except Exception as e:
            # Captura qualquer erro inesperado e mostra a mensagem
            print(f"Ocorreu um erro inesperado: {e}")

        return

    def dict_clients(self) -> dict[str, Client]:
        return self.client_dict
    
    #def register_booking()
    #criar funcoes gerais do hotel...