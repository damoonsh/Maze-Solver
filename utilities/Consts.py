# -----------------------------
# Colours:
Black = (100, 10, 20)
White = (125, 250, 25)
Item = (20, 20, 190)

possible_directions = ["right", "left", "up", "down"]

class vals:
    def set_props(self, scale=50, rows=5, cols=10):
        self.scale = scale
        self.row = rows
        self.col = cols

    def __str__(self):
        print(f'col: {self.col}, row: {self.row}, scale: {self.scale}')
