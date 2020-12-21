class Message:
    def __init__(self, content, author):
        self._type = 'message'
        self._content = content
        self._author = author

    @property
    def type(self) -> str:
        return self._type

    @property
    def content(self) -> str:
        return self._content

    @property
    def author(self) -> str:
        return self._author
