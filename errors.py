class invalidDebugLevelError(Exception):
    def __init__(self):
        self.msg = "Debug level must in rannge of (1, 4)"
        super().__init__(self.msg)

class invalidDebugMsgError(Exception):
    def __init__(self):
        self.msg = "Message must be str"
        super().__init__(self.msg)

class invalidScreenSizeError(Exception):
    def __init__(self):
        self.msg = "asd"
        super().__init__(self.msg)
