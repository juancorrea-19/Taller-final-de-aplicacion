import socket
import threading

class Mensaje:
    def __init__(self, remitente, contenido):
        self.remitente = remitente
        self.contenido = contenido

class Usuario:
    def __init__(self, nombre, conexion):
        self.nombre = nombre
        self.conexion = conexion

    def enviar_mensaje(self, mensaje):
        self.conexion.send(mensaje.encode("utf-8"))

class SalaDeChat:
    def __init__(self):
        self.usuarios = []

    def enviar_mensaje_a_todos(self, mensaje, remitente):
        for usuario in self.usuarios:
            if usuario != remitente:
                mensaje_completo = f"{remitente.nombre}: {mensaje}"
                usuario.enviar_mensaje(mensaje_completo)

def gestionar_cliente(usuario, sala):
    while True:
        try:
            mensaje_recibido = usuario.conexion.recv(1024).decode("utf-8")
            if mensaje_recibido:
                mensaje = Mensaje(usuario, mensaje_recibido)
                sala.enviar_mensaje_a_todos(mensaje.contenido, mensaje.remitente)
        except:
            sala.usuarios.remove(usuario)
            break

def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    servidor.bind(("localhost", 8080))
    servidor.listen(100)

    print("Servidor de chat iniciado en localhost:8080")

    sala = SalaDeChat()

    while True:
        conexion, direccion = servidor.accept()
        nombre_usuario = conexion.recv(1024).decode("utf-8")
        nuevo_usuario = Usuario(nombre_usuario, conexion)
        sala.usuarios.append(nuevo_usuario)
        print(f"{nombre_usuario} se ha unido al chat.")

        threading.Thread(target=gestionar_cliente, args=(nuevo_usuario, sala)).start()

if __name__ == "__main__":
    iniciar_servidor()
