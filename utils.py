def broadcast(clients, message):
    # Sends message to all users
    for client in clients:
        if client == clients[0]:
            continue
        client.send(message.encode('utf-8'))


def get_user(users, connection):
    # Get user by socket
    for user in users:
        if user.get_socket == connection:
            return user
