'''
    Contains the logic for the mover object
'''
class Mover:
    def __init__(self):
        self.x = 0
        self.y = 0
    # Setting the coordinates if the object
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y
    # Setting the scale so the logic can be applied
    def set_scale(self, scal):
        self.scale = scal
    # The logic of the mover is stated here
    def move_logic(self, pixelC, x, y):
        ''' Contains the logic needed for the object to move '''
        color = pixelC[x][y]
        if
