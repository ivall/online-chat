import socket
import select
import pickle
from models.user import User
from utils import broadcast, get_user

HOST = '127.0.0.1'
PORT = 51234

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    print('Serwer został włączony.')
    server.listen()
    inputs = [server]
    users = []
    while True:
        readable, writable, exceptional = select.select(inputs, [], inputs)
        for s in readable:
            if s is server:
                # User connected to server
                conn, addr = server.accept()
                inputs.append(conn)
                nickname = conn.recv(1024)
                user = User(conn, nickname)
                users.append(user)
                print(f"Nowy użytkownik: {nickname}")
            else:
                try:
                    data = s.recv(1024)
                except ConnectionResetError as e:
                    # User closed connection
                    user = get_user(users, s)
                    user_nickname = user.get_username
                    print(f"{user_nickname} wyszedł.")
                    inputs.remove(s)
                    users.remove(user)
                    s.close()
                    broadcast(inputs, f'{user_nickname} wyszedł.')
                    continue
                if data:
                    # Data from user
                    data = pickle.loads(data)
                    if data.type == 'message':
                        broadcast(inputs, f'{data.author}: {data.content}')
