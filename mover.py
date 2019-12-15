"""
    This module controls and tracks the movement of the object within the grid.
"""
class Mover:
    def __init__(self, pixel):
        """Initializing some variables and also setting the pixel controller
        attribute for the moving object"""
        self.pixelC = pixel
        # Initial co-ordinates for the mover object which is (0, 0)
        self.x = 0
        self.y = 0
        # Keeping track of taken paths in order to analyze it
        self.paths = []
        # Keeping the track of general visited coordinates
        # [(x, y), "Movement type"]
        self.current_path = []
        self.dead_ends = []
    # --------------------------------------------------------------------------
    # Setter Functions
    def set_coordinates(self, x, y):
        """The mutation of the object's coordinates happens via this function"""
        self.x, self.y = x, y
    def set_scale(self, scale):
        """letting the object to know about the scale of the map to move in the
        grid, also sets the coordinates for different movements"""
        self.scale = scale
        self.directions = {
            "right": (self.x + self.scale, self.y),
            "left": (self.x - self.scale, self.y),
            "up": (self.x, self.y - self.scale),
            "down": (self.x, self.y + self.scale)
        }
    def set_dimensions(self, col, row):
        """Setting the needed dimensions"""
        self.col, self.row = col, row
    # Helpers-------------------------------------------------------------------
    # Changing the values for different moves
    def available_moves(self):
        """Just checks 4 different directions and changes the values in
        possible_moves dictionary."""
        # Reset the possible_moves dic from the previous move
        self.reset()
        # Check different directions
        for dir in ["right", "left", "up", "down"]:
            # Gets the coordinates for the direction
            x, y = self.directions[dir]
            # Checks to see if the point is in range and not dark
            if self.check_range(x, y) and self.pixelC[x][y] != 6556180:
                self.possible_moves[dir] = True

    def check_range(self, x, y):
        """ Checks to see if the point is in the grid """
        if (0 <= x < self.scale * self.col)and (0 <= y < self.scale * self.row):
            return True
        return False

    def reset(self):
        """ Resets the available moves """
        self.possible_moves = {
            "right": False,
            "left": False,
            "up": False,
            "down": False
        }
        self.directions = {
            "right": (self.x + self.scale, self.y),
            "left": (self.x - self.scale, self.y),
            "up": (self.x, self.y - self.scale),
            "down": (self.x, self.y + self.scale)
        }
    # --------------------------------------------------------------------------
    # Logic---------------------------------------------------------------------
    # --------------------------------------------------------------------------
    def adjust_path(self):
        """Adjust the new path based on the previous from where it results to
        the deadends."""
        pass

    def move_logic(self, x, y):
        """The decision making part of the mover object happens here."""
        # ----------------------------------------------------------------------
        # Note: 6556180 is the color of the blocks
        self.available_moves()
        print((self.x / self.scale, self.y / self.scale), self.possible_moves)
        # 1: Technicly when U have no where to go u have encountered a deadend
        # so we are going to a base case when it is assumed that we have at least
        # one available movement but if it wasn't then

        # If there is at least one True in the moves then take it, if not then
        # there is a deadend being encountered
        if True in self.possible_moves.values():
            # Base case: The priorety is 1. Down 2. Right 3. Left 4.Up
            for dir in ["down", "right", "left", "up"]:
                if self.possible_moves[dir]:
                    # Add the points to the visited and current_path list
                    self.visited.append((self.x, self.y))
                    self.current_path.append((self.x, self.y))
                    # Sending the new coordinates to the map
                    return self.directions[dir]
        else:
            # This path is broken
            self.dead_ends.append((self.x, self.y))
            self.paths.append(self.current_path)

            self.current_path = []
