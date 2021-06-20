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

            self.cableActiveColor = (255, 0, 0)
            self.cablePassiveColor = (135, 0, 0)

    #Defining colors
    color = colorClass()

    class cableClass:
        def __init__(self, activeColor = None, passiveColor = None):
            #When activeColor not entered manually
            if activeColor == None:
                self.activeColor = color.cableActiveColor

            #When activeColor entered manually
            else:
                #Checking validity of activeColor
                if type(activeColor) == tuple:
                    if len(activeColor) == 3:
                        for val in activeColor:
                            if type(val) == int:
                                if not (val <= 255 and val >= 1):
                                    raise errors.invalidColorError()
                            else:
                                raise errors.invalidColorError()
                    else:
                        raise errors.invalidColorError()
                else:
                    raise errors.invalidColorError()

                #When activeColor is valid
                self.activeColor = activeColor

            #When passiveColor not entered manually
            if passiveColor == None:
                self.passiveColor = color.cablePassiveColor

            #When passiveColor entered manually:
            else:
                #Checking validity of passiveColor
                if type(passiveColor) == tuple:
                    if len(passiveColor) == 3:
                        for val in passiveColor:
                            if type(val) == int:
                                if not (val <= 255 and val >= 1):
                                    raise errors.invalidColorError()
                            else:
                                raise errors.invalidColorError()
                    else:
                        raise errors.invalidColorError()
                else:
                    raise errors.invalidColorError()

                #When passiveColor is valid
                self.passiveColor = passiveColor

    class applClass:
        def __init__(self, screenSize = None):
            #When screenSize not entered manually
            if screenSize == None:
                self.screenSize = (1200, 600)

            #When screenSize entered manually
            else:
                #Checking validity of screenSize
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
