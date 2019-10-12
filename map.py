"""
    Generates the map and holds it's properties
"""
import Consts
import pygame


class Map:
    def __init__(self, cols=10, rows=10, scale=40):
        self.row = rows
        self.col = cols
        self.scale = scale

    def run(self):
        pygame.init()
        self.gameDisplay = pygame.display.set_mode((self.col * self.scale, self.row * self.scale))
        self.pixel = pygame.PixelArray(self.gameDisplay)

        self.generate_map()

    def generate_map(self):
        for r in range(self.row):
            for c in range(self.col):
                self.block(r * self.scale, c * self.scale)

    def block(self, x, y, color=(80, 80, 80)):
        for r in range(self.scale):
            for c in range(self.scale):
                self.pixel[x + r][y + c] = (0, 9, 100)