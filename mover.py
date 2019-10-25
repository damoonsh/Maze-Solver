'''
    Contains the logic for the mover object
'''
from Tracker import Move


class Mover:
    def __init__(self):
        # Initial co-ordinates for the mover object which is (0, 0)
        self.x = 0
        self.y = 0
        # Keeping track of taken paths in order to analyze it
        self.visited_coordinates = [] # Just keeps track of the travelled co-ordinates
        self.moves = [] # Saves the moves being taken
        self.move = Move()
        # Knowing which point are deadends:
        self.deadEnds = []

    # Setting the coordinates if the object
    def set_coordinates(self, x, y):
        # The movement object should be instantiated here
        self.x = x
        self.y = y

    # Setting the scale so the logic can be applied
    def set_scale(self, scal):
        self.scale = scal

    # Getting the needed dimensions
    def set_dimensions(self, col, row):
        self.col = col
        self.row = row

    """Logic part: """
    # The logic of the mover is stated here
    def move_logic(self, pixelC, x, y, deadEnd=False):
        ''' Contains the logic needed for the object to move '''
        # For each set of movement, first we add the movement to the next
        # movement of the current movement and then we equal the current
        # movement to the new movement.
        # Instantiating the Move oebjct in order to track the whole thing
        next_move = Move()
        properies = {"From": (self.x, self.y), "To": (), "Type": ""} # Default values
        # -------------------------------------------------------------------------------------------------
        # Note: 6556180 is the color of the blocks
        # The default moves with the priority are: 1. Down 2. Left 3. Left 4. Up
        # DOWN :
        if self.check_range(x, y + self.scale) and self.point_confirm(x, y + self.scale):
            if pixelC[x][y + self.scale] != 6556180:
                return x, y + self.scale
        # RIGHT :
        if self.check_range(x + self.scale, y) and self.point_confirm(x + self.scale, y):
            if pixelC[x + self.scale][y] != 6556180:
                return x + self.scale, y
        # LEFT :
        if self.check_range(x - self.scale, y) and self.point_confirm(x - self.scale, y):
            if pixelC[x - self.scale][y] != 6556180:
                return x - self.scale, y
        # UP:
        if self.check_range(x, y - self.scale) and self.point_confirm(x, y - self.scale):
            if pixelC[x][y - self.scale] != 6556180:
                return x, y - self.scale
        """
            If there were no movement available then the specific point is a dead
            end and also that point should be considered a dead end so it should
            get out of there so thee point should be added to the dead ends array
            and the object should recheck the possibilities
        """
        self.visited_coordinates.append((x, y))
        self.dead_end_procedure()

    # Checks to see if we are in the range or not
    def check_range(self, x, y):
        if (x >= 0 and x < self.scale * 10) and (y >= 0 and y < self.scale * 10):
            return True
        return False

    # Checks to see if the object should proceed to a point or not
    def point_confirm(self, x, y):
        # Checks to see if the point is been visited before
        return True
