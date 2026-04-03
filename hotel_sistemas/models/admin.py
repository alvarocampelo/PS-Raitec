class Admin:
    _id_counter=1

    def __init__(self, name: str, password: int):
        self._id= Admin._id_counter
        Admin._id_counter+=1

        self._name= name
        self._password= password
    
    #getters
    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_password(self):
        return self._password

    #setters
    def set_name(self, name):
        self._name = name

    def set_password(self, password):
        if len(str(password)) >= 4:
            self._password = password
        else:
            print("Erro: A senha deve ter pelo menos 4 dígitos.")
            #arrumar loop para manter até senha adequada