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
    # The logic of the mover is stated here
    def should_move(self, color):
        ''' Contains the logic needed for the object to move '''


        # If the color was black then don't move
        if color == 6556180:
            return False

        # If none of the above statements were true then return True
        return True
