class invalidDebugLevelError(Exception):
    def __init__(self):
        self.msg = "Debug level must be in rannge of (1, 4)"
        super().__init__(self.msg)

class invalidDebugMsgError(Exception):
    def __init__(self):
        self.msg = "Message must be str type"
        super().__init__(self.msg)

class invalidScreenSizeError(Exception):
    def __init__(self):
        self.msg = "Screen size must be tuple type, it must contain 2 elements, the type of all elements must be int, the first element must be in range of (1, 1356), the second element must be in range of (1, 677)"
        super().__init__(self.msg)

class invalidColorError(Exception):
    def __init__(self):
        self.msg = "Color must be tuple type, it must contains 3 elements, the type of all elements must be int, all elements must be in range of (0, 255)"
        super().__init__(self.msg)

class invalidPosError(Exception):
    def __init__(self):
        self.msg = "asd"
        super().__init__(self.msg)

class invalidCableIdError(Exception):
    def __init__(self):
        self.msg = "Cable id must be int type"
        super().__init__(self.msg)

class cableIdNotFoundError(Exception):
    def __init__(self):
        self.msg = "asd"
        super().__init__(self.msg)
