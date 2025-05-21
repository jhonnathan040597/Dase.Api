class MessageService:
    def __init__(self):
        self.messages = []
        self.load_initial_data()
   
    # Patch se usa para modificar un campo específico de un mensaje     
    def patch_message(self, user_id, update_data):
        for message in self.messages:
            if isinstance(message, dict) and message.get("ID") == user_id:
                message.update(update_data)  # Modifica solo lo enviado
                return True
        return False  # Usuario no encontrado

    def load_initial_data(self):
        INITIAL_DATA = [
            {"ID": "1118567951", "nombre": "Jhonnathan D Gutierrez", "años": 28},
            {"ID": "1006552279", "nombre": "Dany Higuera", "años": 24}
        ]
        if not self.messages:
            self.messages.extend(INITIAL_DATA)

    def add_message(self, message):
        self.messages.append(message)

    def update_message(self, user_id, update_data):
        for message in self.messages:
            if isinstance(message, dict) and message.get("ID") == user_id:
                message.update(update_data)
                return True
        return False

    def get_messages(self):
        return self.messages

    def clear_messages(self):
        self.messages = []

message_service = MessageService()