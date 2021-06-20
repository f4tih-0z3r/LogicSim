import errors
from termcolor import colored
import pygame

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

    class colorClass:
        def __init__(self):
            self.black = (0, 0, 0)
            self.white = (255, 255, 255)
            
            self.red = (255, 0, 0)
            self.green = (0, 255, 0)
            self.blue = (0, 0, 255)

            self.bgColor = (40, 40, 40)

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

        #Main running function
        def run(self):
            #Defining colors
            color = colorClass()

            #Defining pygame surface(window)
            pygame.init()
            surface = pygame.display.set_mode(self.screenSize)
            pygame.display.set_caption("LogicSim")

            running = True

            #Main surface loop
            while running:
                #Pygame event control
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                #Things to do
                surface.fill(color.bgColor)

                pygame.display.flip()

    #Application starter
    appl = applClass((1200, 600))
    appl.run()

#Main python starter
if __name__ == "__main__":
    main()
