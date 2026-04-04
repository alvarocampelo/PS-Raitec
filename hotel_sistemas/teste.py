from controllers.hotel_controller import HotelController
from models.client import Client
from models.room import Room
from models.booking import Booking
from models.admin import Admin
from controllers.hotel_controller import HotelController # Ajuste o import conforme sua pasta

def testar_sistema():
    controller = HotelController()

    # --- TESTE DE CLIENTE ---
    print("--- Testando Registro de Cliente ---")
    cliente1 = Client("123.456.789-00", 15, "João Silva")
    controller.register_client(cliente1)
    
    # Testar duplicata (deve dar erro)
    controller.register_client(cliente1) 
    
    # --- TESTE DE QUARTO ---
    print("\n--- Testando Registro de Quarto ---")
    quarto101 = Room(101, "Simples", 150.0, True)
    controller.register_room(quarto101)

    # --- TESTE DE RESERVA ---
    print("\n--- Testando Registro de Reserva ---")
    # Supondo que sua Booking receba id, cliente e quarto
    reserva1 = Booking("B001", cliente1, quarto101, 7) 
    controller.register_booking(reserva1)

    # --- VERIFICAÇÃO FINAL ---
    print("\n--- Estado Final do Sistema ---")
    print(f"Total de Clientes: {len(controller.get_all_clients())}")
    print(f"Total de Quartos: {len(controller.get_all_rooms())}")
    print(f"Total de Reservas: {len(controller.get_all_bookings())}")

if __name__ == "__main__":
    testar_sistema()




