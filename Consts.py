# -----------------------------
# Colours:
Black = (100, 10, 20)
White = (125, 250, 25)
Item = (30, 200, 90)

class vals:
    def set_props(self, scale=10, rows=10, cols=40):
        self.scale = scale
        self.row = rows
        self.col = cols

    def __str__(self):
        print(f'col: {self.col}, row: {self.row}, scale: {self.scale}')