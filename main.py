import errors

def main():
    class applClass:
        def __init__(self, screenSize = None):
            if screenSize == None:
                self.screenSize = (1200, 600)
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

                self.screenSize = screenSize

    appl = applClass((1200, 600))

if __name__ == "__main__":
    main()
