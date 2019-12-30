"""
    This module controls and tracks the movement of the object within the grid.
"""
# Some needed variables
dirs = ["down", "right", "left", "up"]


# Mover module
class Mover:
    def __init__(self, pixel):
        """Initializing some variables and also setting the pixel controller
        attribute for the moving object"""
        self.pixelC = pixel
        # Initial co-ordinates for the mover object which is (0, 0)
        self.x, self.y = 0, 0
        # Keeping track of taken paths in order to analyze it
        self.paths = []
        # Keeping the track of general visited coordinates
        self.visited = []
        # [(x, y), "Movement type"]
        self.current_path = []
        # Keeping track of the deadends
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
                # self.possible_moves["options"].append[dir]
                self.possible_moves[dir] = True

    def check_range(self, x, y):
        """ Checks to see if the point is in the grid"""
        if (0 <= x < self.scale * self.col) and (0 <= y < self.scale * self.row):
            return True
        return False

    def reset(self):
        """ Resets the available moves"""
        self.possible_moves = {
            "right": False,
            "left": False,
            "up": False,
            "down": False,
        }
        self.directions = {
            "right": self.get_coor("right", self.x, self.y),
            "left": self.get_coor("left", self.x, self.y),
            "up": self.get_coor("up", self.x, self.y),
            "down": self.get_coor("down", self.x, self.y)
        }

    def get_coor(self, Type, x, y):
        """Gives the assumed values for different directions"""
        if Type.lower() == "right":
            return (x + self.scale, y)
        if Type.lower() == "left":
            return (x - self.scale, y)
        if Type.lower() == "up":
            return (x, y - self.scale)
        if Type.lower() == "down":
            return (x, y + self.scale)
    # --------------------------------------------------------------------------
    # Debugging utilities-------------------------------------------------------
    # --------------------------------------------------------------------------
    def printList(self, l):
        for z in l:
            print('----', z)
    # --------------------------------------------------------------------------
    # Logic---------------------------------------------------------------------
    # --------------------------------------------------------------------------
    def adjust_path(self):
        """Adjust the new path based on the previous from where it resulted to
        a deadend."""
        pre_path = self.paths[-1]  # The previous path that ended in a deadend
        print("-Adjusting have started for")
        self.printList(pre_path)
        # Check the coordinates within the previous path and find 
        # where is it that the path is taken to a deadend
        for i in range(len(pre_path)):
            # Check to see the other possible options in each of the 
            # point that could be taken, if there are any.
            move = pre_path[len(pre_path) - 1 - i]  # Get the move for analysis
            print('--Checking the move:', move, ',index:', int(len(pre_path) - 1 - i))
            # Getting the coordinates of that move
            (x, y) = move["coor"][0], move["coor"][1]
            print('The coordinate getting checked is: ', int(x), int(y))
            # Go through the four different movements in order to see if it can be done
            for dir in move["options"]:
                print('---', dir, 'option exists, ')
                # If a certain movement is not taken for that specific 
                # coordinate and it is not in the deadends list
                dir_coor = self.get_coor(dir, x, y)  # Get the coordinate if that move have been made
                tried = dir in move["move_type"] # If the movement type has been tested before
                deadend = dir_coor in self.dead_ends # If the coordinate is a dead end
                visited = dir_coor in self.visited
                print('Tried:', tried, ',deadend:', deadend)
                condition = not (tried and deadend and visited)  # General condition
                # If those conditions where satisfied then re-adjust the new path
                if condition:
                    print(dir, 'could be taken.')
                    # Reset the visited coordinates for the new path
                    self.visited = []
                    pre_path[len(pre_path) - 1 - i]["move_type"].append(dir) 
                    # The problem might be in sending the directions[dir]
                    print('--Returning ')
                    self.printList(pre_path[:len(pre_path) - i])
                    return pre_path[0:len(pre_path) - i], self.get_coor(dir, move["coor"][0], move["coor"][1])
                else: # If the conditions where not met then that point is technically a deadend
                    print('--Adding', move["coor"], 'to dead ends.')
                    self.dead_ends.append(move["coor"])
        # In this case there might not be a solution to the whole thing at all
        return [], (self.x, self.y)
    
    def deadend_counter(self):
        """Returns the new coordinate where the path should be tested."""
        # Add the coordinate as a deadend so we will know that it will lead to a deadend
        print('adding', int(self.x), int(self.y), ' to dead ends.')
        self.dead_ends.append((self.x, self.y))
        # This path has been failed so, will just put in the failed ones
        self.paths.append(self.current_path)
        self.current_path, coor = self.adjust_path()
        return coor[0], coor[1]

    def move_logic(self):
        """The decision making part of the mover object happens here."""
        # ----------------------------------------------------------------------
        # Note: 6556180 is the color of the blocks
        # ----------------------------------------------------------------------
        # Get the available moving methods for the whole coordinate
        self.available_moves()
        # Technically when U have no where to go u have encountered a deadend
        # so we are going to a base case when it is assumed that we have at
        # least one available movement but if this wasn't the case, then we 
        # should go through the path and see where it was that led us to a dead 
        # end.
        # ----------------------------------------------------------------------
        # If there is at least one True in the moves then take it, if not, then
        # there is a deadend being encountered
        # Deadend protocol: when there is no way to move for the specific point, the
        # protocol is activated however it is important to note that point is not added 
        # to the current path
        if True in self.possible_moves.values():
            # Base case: The priority is (1.Down 2.Right 3.Left 4.Up)
            for dir in dirs:
                move_available = self.possible_moves[dir]
                visited = self.directions[dir] in self.visited
                deadend = self.directions[dir] in self.dead_ends
                # print('Av: ', move_available, ',Visited:', visited, ',deadend:', deadend)
                # If the direction is available and if it is not in the previously visited one
                if move_available and not (visited or deadend):
                    # The structure of path = coor: shows the coordinate that the
                    # attributes belong to. options: shows the options the Mover
                    # had. move_type: shows the moves from the coordinate
                    path_info = {
                        "coor": (self.x, self.y),
                        "options": [d for d in dirs if self.possible_moves[d] and not (d in self.visited)],
                        "move_type": [dir]
                    }
                    # print(path_info, self.directions[dir])
                    # Add the points to the visited and current_path list
                    self.current_path.append(path_info)
                    self.visited.append((self.x, self.y))
                    # Sending the new coordinates to the map
                    return self.directions[dir]
        # If there have not been any available moves then go through the deadend protocol.
        return self.deadend_counter()