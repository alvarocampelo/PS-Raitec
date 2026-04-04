from models.client import Client
from models.room import Room
from models.booking import Booking
from models.admin import Admin

class HotelController:

    def __init__(self):
        self.login_attempts = 0  # Contador de erros
        self.admin_password = "teste"
        self.client_dict: dict[str, Client] = {}
        self.room_dict: dict[str, Room] = {}
        self.booking_dict: dict[str, Booking] = {}

    #Autentica o administrador. 
    def accessAuthentication(self, password: str) -> bool:
        
        # Realiza a autenticação do administrador com controle de tentativas.
        # Retorna True se a senha estiver correta, False caso contrário.
        
        # Constante que define o teto de erros permitidos antes do bloqueio
        MAX_ATTEMPTS = 3 

        # Verifica primeiro se o sistema já está bloqueado por excesso de erros
        # Isso impede que o usuário continue tentando mesmo se acertar a senha depois
        if self.login_attempts >= MAX_ATTEMPTS:
            print("ACESSO BLOQUEADO: Limite de tentativas excedido. Contate o suporte.")
            return False

        # Comparação da senha fornecida com a senha armazenada no controlador
        if password == self.admin_password:
            # Se acertar, resetamos o contador para 0. 
            # Isso garante que futuras falhas não acumulem com erros antigos já resolvidos.
            self.login_attempts = 0 
            print("Autenticação bem-sucedida! Bem-vindo, Admin.")
            return True
        
        else:
            # Se errar, incrementamos o contador de falhas da instância
            self.login_attempts += 1
            
            # Cálculo dinâmico de quantas chances o usuário ainda tem
            tentativas_restantes = MAX_ATTEMPTS - self.login_attempts
            
            # Feedback visual para o usuário não ser pego de surpresa pelo bloqueio
            print(f"Erro: Senha incorreta! Tentativas restantes: {tentativas_restantes}")
            
            return False
        
    # Registra o cliente
    def register_client(self, client: Client):
        
        # Garante que o que foi passado é realmente uma instância da classe Client.
        
        if not isinstance(client, Client):
            print("Erro: O objeto fornecido não é um Cliente válido.")
            return

        try:
            
            # Tenta obter o CPF usando o método getter do objeto cliente.
            cpf = client.get_cpf()
            
            
            # Se o CPF vier vazio ou nulo, interrompe o processo lançando um erro.
            if not cpf:
                raise ValueError("CPF não pode estar vazio.")

            
            
            # Se já existir no dicionário, impede o cadastro para não sobrescrever um cliente antigo.
            if cpf in self.client_dict:
                print(f"Erro: O CPF {cpf} já está cadastrado.")
            
            else:
                # Adiciona o objeto cliente ao dicionário, usando o CPF como chave para busca rápida.
                self.client_dict[cpf] = client
                print(f"Cliente {client.get_name()} registrado com sucesso!")

        except Exception as e:
            # Captura qualquer erro inesperado (ex: erro no get_cpf) e exibe uma mensagem amigável 
            # em vez de deixar o programa travar (crash).
            print(f"Erro ao registrar cliente: {e}")

    # Registra reserva e altera o status do quarto
    
    def register_booking(self, booking: Booking):
        if not isinstance(booking, Booking):
            print("Erro: O objeto fornecido não é uma Reserva válida.")
            return

        try:
            b_id = booking.get_id()
            if b_id in self.booking_dict:
                print(f"Erro: A reserva ID {b_id} já existe.")
            else:
                self.booking_dict[b_id] = booking
                print(f"Reserva {b_id} registrada com sucesso!")
        except Exception as e:
            print(f"Erro ao registrar reserva: {e}")

    # Solicita a reserva
    def reqBooking(self, booking: Booking) -> None:
        room = booking.get_room()
        checkin = booking.get_checkin()
        checkout = booking.get_checkout()

        # Verifica se há conflito com reservas existentes para este quarto
        for b in self.booking_dict.values():
            if b.get_room().get_number() == room.get_number():
                # Lógica de sobreposição de datas
                if not (checkout <= b.get_checkin() or checkin >= b.get_checkout()):
                    print("Erro: O quarto já está reservado para este período!")
                    return # Encerra após o erro

        self.register_booking(booking) # Ao final de tudo, registra a reserva

    # Remove ou cancela uma reserva do sistema.

    def remove_booking(self, booking_id: int):
        
       
        # Verifica se a reserva existe e se não está 'Em Andamento' antes de apagar.
        booking = self.booking_dict.get(booking_id)

        if not booking:
            print(f"Erro: A reserva com ID {booking_id} não foi encontrada.")
            return

        try:
            # Se o hóspede já estiver no hotel, você não pode simplesmente apagar a reserva.
            # Ele precisa fazer o Check-out primeiro para encerrar a conta.
            if booking.get_active() == True:
                print(f"Erro: Não é possível remover a reserva {booking_id}. O hóspede já realizou Check-in.")
                return

            # Ao remover a reserva, garante-se que o quarto volte a ficar disponível.
            room = booking.get_room()
            if room.get_occupied():
                room.set_occupied(False)

            # remove
            del self.get_all_bookings()[booking_id]
            print(f"Sucesso: Reserva {booking_id} removida/cancelada com sucesso.")

        except Exception as e:
            print(f"Erro inesperado ao remover reserva: {e}")

    # Ativa a reserva e ocupa o quarto.
    def checkIn(self, booking_id: int):
        booking = self.booking_dict.get(booking_id)
        if not booking:
            print("Erro: Reserva não encontrada.")
            return

        # Ativa a reserva e ocupa o quarto
        booking.set_active(True)
        booking.get_room().set_occupied(True)
        print(f"Check-in realizado para {booking.get_client().get_name()}!")

    # Finaliza a reserva e libera o quarto.
    def checkOut(self, booking_id: int):
        booking = self.booking_dict.get(booking_id)
        if booking and booking.get_active():
            # Desativa a reserva e remove a reserva
            booking.set_active(False) 
            self.remove_booking(booking_id) 
            print(f"Check-out da reserva {booking_id} concluído. Quarto liberado.")
        else:
            print("Erro: Reserva não encontrada ou não está ativa.")

    # Registra o quarto

    def register_room(self, room: Room):
        if not isinstance(room, Room):
            print("Erro: O objeto fornecido não é um Quarto válido.")
            return

        try:
            number = room.get_number()
            if number in self.room_dict:
                print(f"Erro: O quarto {number} já está cadastrado.")
            else:
                self.room_dict[number] = room
                print(f"Quarto {number} registrado com sucesso!")
        except Exception as e:
            print(f"Erro ao registrar quarto: {e}")

    # Remove um quarto do sistema.

    def remove_room(self, room_number: int):
  
        #Verifica se o quarto existe e se não há hóspedes nele antes de apagar.

        room = self.room_dict.get(room_number)

        if not room:
            print(f"Erro: O quarto {room_number} não foi encontrado no sistema.")
            return

        try:
            # Não é possível remover um quarto da base de dados se houver alguém com check-in ativo
            if room.get_occupied():
                print(f"Erro: Não é possível remover o quarto {room_number}. Ele está Ocupado no momento.")
                return

            # Remove o par chave-valor do dicionário
            del self.room_dict[room_number]
            print(f"Sucesso: Quarto {room_number} removido do sistema permanentemente.")

        except Exception as e:
            print(f"Erro inesperado ao remover quarto: {e}")
    
    # Retorna todos os quartos
    def get_all_rooms(self):
        return self.room_dict

    # Retorna todos as reservas
    def get_all_bookings(self):
        return self.booking_dict

    # Retorna todos os clientes
    def get_all_clients(self):
        return self.client_dict