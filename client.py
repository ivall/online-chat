import socket
import threading
import pickle
from models.message import Message

HOST = '127.0.0.1'
PORT = 51234

username = bytes(input("Nazwa użytkownika: ").encode('utf-8'))


class Client:
    def __init__(self):
        self._s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        # Connect to server
        self._s.connect((HOST, PORT))
        self._s.sendall(username)
        threading.Thread(target=self.retrieve_data).start()

    def retrieve_data(self):
        # Wait for data from server
        while True:
            data = self._s.recv(1024)
            if not data:
                break
            print(data.decode('utf-8'))

    def send_message(self, content):
        # Send message to server
        msg = Message(content, username)
        msg = pickle.dumps(msg)
        self._s.send(msg)


client = Client()
client.connect()
while True:
    # Wait for message
    msg = str(input())
    if msg:
        client.send_message(msg)
