'''
    Generates the map and holds it's properties
'''
# Needed modules for the pygame and random
import pygame
import random
# Minor utilites used to ease the data transfering process
from utilities.Consts import vals
from mover import Mover
from utilities import Consts
# Map module
class Map:
    # Initializing the Object with the default values for rows, cols and scale
    def __init__(self, consts):
        # The core blocks of the object that helps
        # us build the map and manipulate it
        self.row = consts.row
        self.col = consts.col
        self.scale = consts.scale
        # Holds the blocks
        self.blocks = []
        # The difficulty level of the maze
        self.diff = 0.32
        # The delay time for the mover object
        self.delay = 1000
    # -------------------------------------------------------------------
    # Verification of the map--------------------------------------------
    # -------------------------------------------------------------------
    def get_array(self):
        """ Gets the map in the format of 1/0 array """
        # Keeps track of the map as an array
        self.array = []
        # The two for loops have the same functionality as the x-y system
        for r in range(self.row):
            # Instantiating the
            self.array.append([])
            for c in range(self.col):
                # Checks to see if the coordinates are in the blocks arrays or not
                if (r, c) in self.blocks:
                    self.array[r].append("0")
                else:
                    self.array[r].append("1")

    # ---------------------------------------------------------------------------------------------------
    # Runs the main process
    def run(self):
        # Instantiating the initial properties for the application
        pygame.init()
        height, width = self.col * self.scale, self.row * self.scale
        # Setting the height and width
        self.gameDisplay = pygame.display.set_mode((height, width))
        # Setting the caption
        pygame.display.set_caption('HM0-01')
        # Setting the logo
        gameIcon = pygame.image.load('logo.png')
        pygame.display.set_icon(gameIcon)

        # Initializing the pixel property
        self.pixel = pygame.PixelArray(self.gameDisplay)

        """Drawing the map:"""
        # Instantiating the mover object
        self.obj = Mover(self.pixel)
        self.obj.set_dimensions(self.col, self.row)
        # Setting the scale for that
        self.obj.set_scale(self.scale)

        # generating the blocks within the maze
        self.maze()
        # Finalizing the process of making the map
        self.generate_map()

    # Generates the map
    def generate_map(self):
        for r in range(self.row):
            for c in range(self.col):
                # Checks to see if the coordinates are in the blocks arrays or not
                if (r, c) in self.blocks:
                    self.block(c * self.scale, r * self.scale, Consts.Black)
                else:
                    self.block(c * self.scale, r * self.scale)

        # Instantiating the mover object on the domain of the movement
        self.block(0, 0, Consts.Item)

    # Maze: Generates the random blocks within the map
    def maze(self):
        # Getting the number of blocks in the map
        num = int((self.row * self.col) * self.diff)
        for i in range(num):
            self.blocks.append(((random.randrange(self.row)), (random.randrange(self.col))))
        # Generate the array of the map
        self.get_array()

    # Block: Draws blocks pixel by pixel
    def block(self, x, y, color=Consts.White):
        for r in range(self.scale):
            for c in range(self.scale):
                self.pixel[x + r][y + c] = color
    # --------------------------------------------------------------------------
    # Logic related functions---------------------------------------------------
    # --------------------------------------------------------------------------
    # This for the manual movement
    def move(self, dx, dy):0
        # At the beginning it should be checked to see if the co-ordinates are
        # in the demanded range so we won't have any, errors regarding the
        # function not being in the range.
        if self.obj.check_range(self.obj.x + self.scale * dx, self.obj.y + self.scale * dy):
            # After checking to see for the co-ordinates it is up to the mover object to decide the movement
            if self.pixel[self.obj.x + self.scale * dx][self.obj.y + self.scale * dy] != 6556180:
                self.block(self.obj.x, self.obj.y)
                self.obj.set_coordinates(self.obj.x + self.scale * dx, self.obj.y + self.scale * dy)
                self.block(self.obj.x, self.obj.y, Consts.Item)

    # This for general movement
    def autoMove(self):
        if self.obj.move_logic(self.obj.x, self.obj.y):
            # Use the move_logic for the needed instructions
            x, y = self.obj.move_logic(self.pixel, self.obj.x, self.obj.y)

            # The process of movement:
            self.block(self.obj.x, self.obj.y)  # Delete the current place of the block
            self.obj.set_coordinates(x, y)  # Set the new coordinates for the moving object
            self.block(self.obj.x, self.obj.y, Consts.Item)  # Draw the block with it's new place
            self.obj.visited_coordinates.append((x, y))  # Track the visited coordinates
            pygame.time.wait(self.delay)
