class invalidDebugLevelError(Exception):
    def __init__(self):
        self.msg = "debugLevel must in rannge of (1, 4)"
        super().__init__(self.msg)

class invalidScreenSizeError(Exception):
    def __init__(self):
        self.msg = "asd"
        super().__init__(self.msg)
