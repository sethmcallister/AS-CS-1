class Box():
#private class variables
    _height = 0
    _width = 0
    _depth = 0

    def __init__(self, height, width, depth):
        #initialiser
        self._height = height
        self._width = width
        self._depth = depth
    def getVolume(self):
        #accessor to get volume
        return self._height*self._width*self._depth


#create an instants of box for lift
lift = Box(10,10,10)
        
#create an instants of box for fridge
fridge = Box (5,5,5)

print("volume of lift: {} cm^3".format(lift.getVolume()))

print("volume of frige: {} cm^3".format(fridge.getVolume()))

