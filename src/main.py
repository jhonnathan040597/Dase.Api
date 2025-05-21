from fastapi import FastAPI, HTTPException
from message_service import message_service  # Importa el servicio

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "¡hello world!"}

@appt.pos("/api/message")
def send_message(message: dict):
    message_service.add_message(message)
    return {"message": "Mensaje recibido correctamente."}

@app.put("/api/message/{user_id}")
def update_user(user_id: str, update_data: dict):
    if not message_service.update_message(user_id, update_data):
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"message": "Datos actualizados correctamente"}

@app.get("/api/messages")
def read_messages():
    return message_service.get_messages()

@app.delete("/api/messages")
def delete_messages(user_id: str):
    if not message_service.clear_messages():
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"message": "Mensajes eliminados correctamente"}
    