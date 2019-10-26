'''
    Contains the logic for the mover object
'''
from Tracker import Move


class Mover:
    # Instntiating the object at the origin/start point of its journey
    def __init__(self):
        # Initial co-ordinates for the mover object which is (0, 0)
        self.x = 0
        self.y = 0
        # Keeping track of taken paths in order to analyze it
        self.visited_coordinates = [] # Just keeps track of the travelled co-ordinates
        self.moves = [] # Saves the moves being taken
        self.move = Move()
        # self.move.set_before("base")
        # Knowing which point are deadends:
        self.deadEnds = []
    # Setter Functions===================================================
    # Setting the coordinates if the object
    def set_coordinates(self, x, y):
        # The movement object should be instantiated here
        self.x = x
        self.y = y

    # Setting the scale so the logic can be applied
    def set_scale(self, scal):
        self.scale = scal

    # Setting the needed dimensions
    def set_dimensions(self, col, row):
        self.col = col
        self.row = row
    # Logic==============================================================
    """Logic part: """
    def move_logic(self, pixelC, x, y, deadEnd=False):
        ''' Contains the logic needed for the object to move '''
        # For each set of movement, first we add the movement to the next
        # movement of the current movement and then we equal the current
        # movement to the new movement.
        # -------------------------------------------------------------------------------------------------
        # Note: 6556180 is the color of the blocks
        # The default moves with the priority are: 1. Down 2. Left 3. Left 4. Up
        # DOWN :
        if self.check_range(x, y + self.scale) and self.point_confirm(x, y + self.scale):
            if pixelC[x][y + self.scale] != 6556180:
                self.manage_tracking((x, y + self.scale), "D")
                return x, y + self.scale
        # RIGHT :
        if self.check_range(x + self.scale, y) and self.point_confirm(x + self.scale, y):
            if pixelC[x + self.scale][y] != 6556180:
                self.manage_tracking((x + self.scale, y), "R")
                return x + self.scale, y
        # LEFT :
        if self.check_range(x - self.scale, y) and self.point_confirm(x - self.scale, y):
            if pixelC[x - self.scale][y] != 6556180:
                self.manage_tracking((x - self.scale, y), "L")
                return x - self.scale, y
        # UP:
        if self.check_range(x, y - self.scale) and self.point_confirm(x, y - self.scale):
            if pixelC[x][y - self.scale] != 6556180:
                self.manage_tracking((x, y -self.scale), "U")
                return x, y - self.scale
        """
            If there were no movement available then the specific point is a dead
            end and also that point should be considered a dead end so it should
            get out of there so thee point should be added to the dead ends array
            and the object should recheck the possibilities
        """
        self.visited_coordinates.append((x, y))
    # Helper=============================================================================
    # Manage the move objects
    def manage_tracking(self, to, move_type):
        # Instantiating the new move Object
        next_move = Move()
        properies = {
            "from_coor": (self.x, self.y),
            "to_coor": (to),
            "move_type": move_type
        } # Default values
        # Set the properties for the new move object
        next_move.set_props(properies)
        # Set the before value of the new move object
        next_move.set_before(self.move)
        # set the after value of the move object
        self.move.set_after(next_move)
        # Kepp track of the movements by keeping it in the array
        self.moves.append(self.move)
        print(self.move.__str__())
        # Proceeding to the next object
        self.move = next_move
    #
    # def check_moves(self):
    #     for move in self.moves:
    #         print(move.)
    # Checks to see if we are in the range or not
    def check_range(self, x, y):
        if (x >= 0 and x < self.scale * self.col) and (y >= 0 and y < self.scale * self.row):
            return True
        return False

    # Checks to see if the object should proceed to a point or not
    def point_confirm(self, x, y):
        # Checks to see if the point is been visited before
        return True
