class Booking:
    _id_counter=1

    def __init__(self, client: Client, room: Room, checkin: Date, days: int, total_expense: float):
        self._id_counter= Booking._id_counter
        Booking._id_counter+=1

        self._client= client
        self._room= room
        self._checkin= checkin
        self._days= days
        self._total_expense= total_expense
    
    #getters
    def get_id(self):
        return self._id

    def get_client(self):
        return self._client

    def get_room(self):
        return self._room

    def get_checkin(self):
        return self._checkin

    def get_days(self):
        return self._days

    def get_total_expense(self):
        return self._total_expense
    
    #setters
    def set_client(self, client):
        self._client = client

    def set_room(self, room):
        self._room = room

    def set_checkin(self, checkin):
        self._checkin = checkin

    def set_days(self, days):
        if days > 0:
            self._days = days

    def set_total_expense(self, total_expense):
        if total_expense >= 0:
            self._total_expense = total_expense

