class Comment:
    CONTENT_LEN_MIN = 3
    CONTENT_LEN_MAX = 200
    CONTENT_LEN_ERR = f'Content must be between {CONTENT_LEN_MIN} and {CONTENT_LEN_MAX} characters long!'

    def __init__(self, content, author):
        self.content = content
        self._author = author

    @property
    def author(self):
        return self._author

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if len(value) < int(Comment.CONTENT_LEN_MIN) or len(value) > int(Comment.CONTENT_LEN_MAX):
            raise ValueError(f'{Comment.CONTENT_LEN_ERR}')
        self._content = value

    def __str__(self):
        return f'----------\n' \
               f'{self.content}\n' \
               f'User: {self.author}\n' \
               f'----------'
