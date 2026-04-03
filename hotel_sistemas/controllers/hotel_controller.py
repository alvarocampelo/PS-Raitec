from models.client import Client
from models.room import Room
from models.booking import Booking
from models.admin import Admin

class HotelController:

    admin_password="teste"

    def __init__(self):
        self.client_list: list[Client]= []
        self.room_list: list[Room]= []
        self.booking_list: list[Booking]= []

    def register_client(self, client: Client):
    
    def list_clients(self) -> list[Client]:
        return self.client_list

    #criar funcoes gerais do hotel...