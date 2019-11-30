"""
    Contains the logic for the mover object
"""
from utilities.Consts import directions, available_moves
class Mover:
    # Instntiating the object at the origin/start point of its journey
    def __init__(self, pixel):
        self.pixelC = pixel
        # Initial co-ordinates for the mover object which is (0, 0)
        self.x = 0
        self.y = 0
        # Keeping track of taken paths in order to analyze it
        self.visited_coordinates = []  # Just keeps track of the travelled co-ordinates
    # --------------------------------------------------------------------------
    # Setter Functions
    # Setting the coordinates if the object
    def set_coordinates(self, x, y):
        # The movement object should be instantiated here
        self.x = x
        self.y = y

    # Setting the scale so the logic can be applied
    def set_scale(self, scale):
        self.scale = scale

    # Setting the needed dimensions
    def set_dimensions(self, col, row):
        self.col = col
        self.row = row
    # Helpers-------------------------------------------------------------------
    # Changing the values for different moves
    def available_moves(self):
        # There two possible scenarios: either it is the first movement which
        # the list should be instantiated or it is not the first movement sot
        # the list should be resseted.
        self.reset()
        for dir in possible_directions:
            x, y = coordinate_change(dir)
            if check_range(x, y) and pixelC[x][y] != 6556180:
                self.possible_moves[dir] = True
    # Returns the new coordinate for a specific movement
    def coordinate_change(self, key):
        return directions[key]
    # Checks to see if the point is in range and not dark
    def validate_point(self):
        pass
    # Checks to see if the point is in the grid
    def check_range(self, x, y):
        if (0 <= x < self.scale * self.col) and (0 <= y < self.scale * self.row):
            return True
        return False
    # Resets the available moves
    def reset(self):
        self.possible_moves = {
            "right": False,
            "left": False,
            "up": False,
            "down": False
        }
    # --------------------------------------------------------------------------
    # Logic
    def move_logic(self, x, y):
        # For each set of movement, first we add the movement to the next
        # movement of the current movement and then we equal the current
        # movement to the new movement.
        # ----------------------------------------------------------------------
        # Note: 6556180 is the color of the blocks
        # The default moves with the priority are: 1. Down 2. Left 3. Left 4. Up
        pass
        """
            If there were no movement available then the specific point is a dead
            end and also that point should be considered a dead end so it should
            get out of there so thee point should be added to the dead ends array
            and the object should recheck the possibilities
        """
        self.visited_coordinates.append((x, y))


    # Checks to see if the object should proceed to a point or not
    def point_confirm(self, x, y):
        # Checks to s
        if not (x, y) in self.visited_coordinates:
            return True
