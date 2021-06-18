import errors
from termcolor import colored

def main():
    class debugClass:
        def __init__(self):
            pass

        def printDebug(self, debugLevel, msg):
            """
            debugLevel = 1: info
            debugLevel = 2: warning
            debugLevel = 3: important warning
            debugLevel = 4: error
            """

            #Checking validity of debugLevel
            if type(debugLevel) == int:
                if not (debugLevel <= 4 and debugLevel >= 1):
                    raise errors.invalidDebugLevelError()
            else:
                raise errors.invalidDebugLevelError()

            #When debugLevel is valid
            #Checking validity of msg
            if type(msg) != str:
                raise invalidDebugMsgError()

            #When msg is valid
            if debugLevel == 1: #Info
                print(msg)
            elif debugLevel == 2: #Warning
                print(colored(msg, "yellow"))
            elif debugLevel == 3: #Important warning
                print(colored(msg, "red"))
            elif debugLevel == 4: #Error
                print(colored(msg, "white", "on_red"))


    class applClass:
        def __init__(self, screenSize = None):
            #When screenSize not entered manually
            if screenSize == None:
                self.screenSize = (1200, 600)

            #When screenSize entered manually
            #Checking validity of screenSize
            else:
                if type(screenSize) == tuple:
                    if len(screenSize) == 2:
                        for val in screenSize:
                            if type(val) != int:
                                raise errors.invalidScreenSizeError()

                        if screenSize[0] <= 1356 and screenSize[0] >= 1:
                            if not (screenSize[1] <= 677 and screenSize[1] >= 1):
                                raise errors.invalidScreenSizeError()
                        else:
                            raise errors.invalidScreenSizeError()
                    else:
                        raise errors.invalidScreenSizeError()
                else:
                    raise errors.invalidScreenSizeError()

                #When screenSize is valid
                self.screenSize = screenSize

if __name__ == "__main__":
    main()
