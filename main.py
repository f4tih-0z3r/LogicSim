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

    class cableClass:
        def __init__(self, cableId, activeColor = None, passiveColor = None):
            self.cableId = cableId

            #Checking validity of cableId
            if type(cableId) == int:
                if cableId < 0:
                    raise errors.invalidCableIdError()
            else:
                raise errors.invalidCableIdError()

            #When cableId is valid
            #When activeColor not entered manually
            if activeColor == None:
                color = colorClass()
                self.activeColor = color.cableActiveColor
                del(color)

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
                color = colorClass()
                self.passiveColor = color.cablePassiveColor
                del(color)

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

            self.parts = []
            self.state = False

        def addPart(self, pos1, pos2):
            #Checking validity of pos1
            if type(pos1) == tuple:
                if len(pos1) == 2:
                    for val in pos1:
                        if not (type(val) == int):
                            raise errors.invalidPosError()
                else:
                    raise errors.invalidPosError()
            else:
                raise errors.invalidPosError()

            #When pos1 is valid
            #Checking validity of pos2
            if type(pos2) == tuple:
                if len(pos2) == 2:
                    for val in pos2:
                        if not (type(val) == int):
                            raise errors.invalidPosError()
                else:
                    raise errors.invalidPosError()
            else:
                raise errors.invalidPosError()

            #When pos2 is valid
            self.parts.append([pos1, pos2])

        def draw(self, surface):
            #When cable passive
            if self.state == False:
                for part in self.parts:
                    pygame.draw.line(surface, self.passiveColor, part[0], part[1])

            #When cable active
            elif self.state == True:
                for part in self.parts:
                    pygame.draw.line(surface, self.activeColor, part[0], part[1])

    class applClass:
        def __init__(self, surface):
            self.surface = surface

            self.cables = []

        def findCable(self, cableId):
            #Checking validity of cableId
            if type(cableId) == int:
                if cableId >= 0:
                    #When cableId is valid
                    cableToEdit = None
                    for cable in self.cables:
                        if cable.cableId == cableId:
                            cableToEdit = cable
                            break

                    #When entered cableId isn't in the self.cables list
                    if cableToEdit == None:
                        raise errors.cableIdNotFoundError()
                    #When entered cableId in the self.cables list
                    else:
                        cable = cableToEdit
                        del(cableToEdit)
                        return cable
                else:
                    raise errors.invalidCableError()
            else:
                raise errors.invalidCableIdError()

        def addCable(self):
            cableId = 0

            if len(self.cables) == 0:
                dynamicCable = cableClass(cableId)
            else:
                for cable in self.cables:
                    #When any cableId skipped in self.cables list
                    if cableId != cable.cableId:
                        dynamicCable = cableClass(cableId)
                        break

                    cableId += 1

                #When any cableId not skipped in self.cables list
                if len(self.cables) == cableId:
                    dynamicCable = cableClass(cableId)

            self.cables.append(dynamicCable)
            del(dynamicCable)

        def addCablePart(self, cableId, pos1, pos2):
            #Checking validity of pos1
            if type(pos1) == tuple:
                if len(pos1) == 2:
                    for val in pos1:
                        if not (type(val) == int):
                            raise errors.invalidPosError()
                else:
                    raise errors.invalidPosError()
            else:
                raise errors.invalidPosError()

            #When pos1 is valid
            #Checking validity pos2
            if type(pos2) == tuple:
                if len(pos2) == 2:
                    for val in pos2:
                        if not (type(val) == int):
                            raise errors.invalidPosError()
                else:
                    raise errors.invalidPosError()
            else:
                raise errors.invalidPosError()

            #When pos2 is valid
            #Adding part to cable
            cable = self.findCable(cableId)
            cable.parts.append((pos1, pos2))

        def changeState(self, cableId, state: bool):
            cable = self.findCable(cableId)
            cable.state = state

        def drawCable(self, cableId):
            cable = self.findCable(cableId)
            cable.draw(self.surface)

        def drawAllCables(self):
            for cable in self.cables:
                cable.draw(self.surface)

        #Main running function
        def run(self):
            #Defining color class
            color = colorClass()

            running = True

            self.addCable()
            self.addCablePart(0, (10, 20), (30, 40))

            self.addCable()
            self.addCablePart(1, (50, 60), (70, 80))
            self.changeState(1, True)

            #Main surface loop
            while running:
                #Pygame event control
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                #Things to do
                surface.fill(color.bgColor)

                self.drawAllCables()

                pygame.display.flip()

    #Defining pygame surface(window)
    pygame.init()
    surface = pygame.display.set_mode((1200, 600))
    pygame.display.set_caption("LogicSim")

    #Application starter
    appl = applClass(surface)
    appl.run()

#Main python starter
if __name__ == "__main__":
    main()
