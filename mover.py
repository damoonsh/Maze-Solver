'''
    Contains the logic for the mover object
'''
from Tracker import *
class Mover:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.visited_coordinates = []
        self.track = Tracker()
    # Setting the coordinates if the object
    def set_coordinates(self, x, y):
        # The movement object should be instantiated here
        self.x = x
        self.y = y
    # Setting the scale so the logic can be applied
    def set_scale(self, scal):
        self.scale = scal
    # The logic of the mover is stated here
    def move_logic(self, pixelC, x, y, deadEnd=False):
        """Loggings"""
        ''' Contains the logic needed for the object to move '''
        # Check for down :
        if self.check_range(x, y + self.scale) and (self.point_confirm(x, y + self.scale) or deadEnd):
            if pixelC[x][y + self.scale] != 6556180:
                return x, y + self.scale
        # Check for right:
        if self.check_range(x + self.scale, y) and (self.point_confirm(x + self.scale, y) or deadEnd):
            if pixelC[x + self.scale][y] != 6556180:
                return x + self.scale, y
        # Check for left :
        if self.check_range(x - self.scale, y) and (self.point_confirm(x - self.scale, y) or deadEnd):
            if pixelC[x - self.scale][y] != 6556180:
                return x - self.scale, y
        # Check for up :
        if self.check_range(x, y - self.scale) and (self.point_confirm(x, y - self.scale) or deadEnd):
            if pixelC[x][y - self.scale] != 6556180:
                return x, y - self.scale
        # If there were no movement available then it should go back some how
        # And also that point should be considered a dead end so it should come back to it
        #, So thee point should be added to the dead ends array and the object should recheck the possibilities
        self.move_logic(pixelC, x, y, True)


    # Checks to see if we are in the range or not
    def check_range(self, x, y):
        if (x >= 0 and x < self.scale * 10) and (y >= 0 and y < self.scale * 10):
            return True
        return False
    # Checks to see if the object should proceed to a point or not
    def point_confirm(self, x, y):
        # Checks to see if the point is been visited before
        if (x,y) in self.visited_coordinates:
            return False
        return True