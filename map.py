'''
Generates the map and holds it's properties
'''
import Consts
import pygame
import random
from mover import Mover

class Map:
    # Initializing the Object with the default values for rows, cols and scale
    def __init__(self, cols=10, rows=10, scale=40):
        self.row = rows
        self.col = cols
        self.scale = scale
        self.blocks = []
        self.diff = 0.4

    # Runs the whole app
    def run(self):
        # Instantiating the initial properties for the application
        pygame.init()
        height , width = self.col * self.scale, self.row * self.scale
        self.gameDisplay = pygame.display.set_mode((height, width))
        self.pixel = pygame.PixelArray(self.gameDisplay)

        # Drawing the map
        self.obj = Mover()
        self.maze()
        self.generate_map()

    # Generates the map
    def generate_map(self):
        for r in range(self.row):
            for c in range(self.col):
                # print((r, c) in self.blocks)
                if (r, c) in self.blocks:
                    self.block(r * self.scale, c * self.scale , Consts.Black)
                else:
                    self.block(r * self.scale, c * self.scale)

        self.block(0, 0, Consts.Item)

    """
        Helper functions: Help the map to react to the necessary changes
    """
    # Maze
    def maze(self):
        num = int((self.row * self.col) * self.diff)
        for i in range(num):
            self.blocks.append(((random.randrange(9) + 1), (random.randrange(9) + 1)))

    # Block: Draws blocks pixel by pixel
    def block(self, x, y, color=Consts.White):
        for r in range(self.scale):
            for c in range(self.scale):
                self.pixel[x + r][y + c] = color

    def move(self, dx, dy):
        # Setting some variables, so we can check if the movement makes sense or not
        out_range_x = (self.obj.x + self.scale * dx >= 0 or self.obj.x + self.scale * dx <= self.scale * self.col)
        out_range_y = (self.obj.y + self.scale * dy >= 0 or self.obj.y + self.scale * dy <= self.scale * self.row)
        out_range = out_range_x and out_range_y
        if out_range:
            if self.obj.should_move(self.pixel[self.obj.x + self.scale * dx][self.obj.y + self.scale * dy]):
                self.block(self.obj.x, self.obj.y)
                self.obj.set_coordinates(self.obj.x + self.scale * dx, self.obj.y + self.scale * dy)
                self.block(self.obj.x, self.obj.y, Consts.Item)