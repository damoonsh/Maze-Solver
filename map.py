'''
    Generates the map and holds it's properties
'''
from Consts import vals
import Consts
import pygame
import random
from mover import Mover


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
        self.diff = 0.38
        # The delay time for the mover object
        self.delay = 2000

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
        self.obj = Mover()
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

        self.block(0, 0, Consts.Item)

    """
        Helper functions: Help the map to react to the necessary changes
    """

    # Maze
    def maze(self):
        num = int((self.row * self.col) * self.diff)
        for i in range(num):
            self.blocks.append(((random.randrange(self.row)), (random.randrange(self.col))))

    # Block: Draws blocks pixel by pixel
    def block(self, x, y, color=Consts.White):
        for r in range(self.scale):
            for c in range(self.scale):
                self.pixel[x + r][y + c] = color

    """Logic related functions: """

    # This for the manual movement
    def move(self, dx, dy):
        # Setting some variables, so we can check if the movement makes sense or not
        out_range_x = (self.obj.x + self.scale * dx >= 0 and self.obj.x + self.scale * dx < self.scale * self.col)
        out_range_y = (self.obj.y + self.scale * dy >= 0 and self.obj.y + self.scale * dy < self.scale * self.row)
        out_range = out_range_x and out_range_y

        # At the beginning it should be checked to see if the co-ordinates are in the demanded range so we won't
        # have any, errors regarding the function not being in the range
        if out_range:
            # After checking to see for the co-ordinates it is up to the mover object to decide the movement
            if self.pixel[self.obj.x + self.scale * dx][self.obj.y + self.scale * dy] != 6556180:
                self.block(self.obj.x, self.obj.y)
                self.obj.set_coordinates(self.obj.x + self.scale * dx, self.obj.y + self.scale * dy)
                self.block(self.obj.x, self.obj.y, Consts.Item)

    # This for general movement
    def autoMove(self):
        if self.obj.move_logic(self.pixel, self.obj.x, self.obj.y):
            # Use the move_logic for the needed instructions
            x, y = self.obj.move_logic(self.pixel, self.obj.x, self.obj.y)

            # The process of movement:
            self.block(self.obj.x, self.obj.y)  # Delete the current place of the block
            self.obj.set_coordinates(x, y)  # Set the new coordinates for the moving object
            self.block(self.obj.x, self.obj.y, Consts.Item)  # Draw the block with it's new place
            self.obj.visited_coordinates.append((x, y))  # Track the visited coordinates

            # Set a delay so the process can be tracked
            pygame.time.wait(self.delay)
        else:
            print('The end')
