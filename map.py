'''
Generates the map and holds it's properties
'''
import Consts
import pygame
import random

class Map:
    # Initializing the Object with the default values for rows, cols and scale
    def __init__(self, cols=10, rows=10, scale=40):
        self.row = rows
        self.col = cols
        self.scale = scale
        self.blocks = []

    # Runs the whole app
    def run(self):
        # Instantiating the initial properties for the application
        pygame.init()
        height , width = self.col * self.scale, self.row * self.scale
        self.gameDisplay = pygame.display.set_mode((height, width))
        self.pixel = pygame.PixelArray(self.gameDisplay)

        # Making the map
        self.maze()
        self.generate_map()

    # Generates the map
    def generate_map(self):
        for r in range(self.row):
            for c in range(self.col):
                if any((r, c)) in self.blocks:
                    print('Black')
                    self.block(r * self.scale, c * self.scale , Consts.Black)
                else:
                    self.block(r * self.scale, c * self.scale)

    """
        Helper functions: Help the map to react to the necessary changes
    """
    # Maze
    def maze(self):
        num = int((self.row * self.col) * 0.20)
        print(num)
        for i in range(num):
            self.blocks.append(((random.randrange(9) + 1), (random.randrange(9) + 1)))
        print('Maze: ', self.blocks)

    # Block: Draws blocks pixel by pixel
    def block(self, x, y, color=Consts.White):
        for r in range(self.scale):
            for c in range(self.scale):
                self.pixel[x + r][y + c] = color