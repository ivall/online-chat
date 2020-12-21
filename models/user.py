class User:
    def __init__(self, socket, username):
        self._socket = socket
        self._username = username

    @property
    def get_socket(self):
        return self._socket

    @property
    def get_username(self) -> str:
        return self._username
