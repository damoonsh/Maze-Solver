'''
    This object is going to track the movements of the object and then give
    the necessary data when needed.
'''


class Move:
    def __init__(self):
        # For the first movement the initial co-ordinate is (0, 0)
        self.From = (0, 0)
        # Also the before will equal none
        self.before = "base"
        self.To = 0
        self.From = 0

    def set_props(self, props):
        self.From = props["from_coor"]
        self.To = props["to_coor"]
        self.Type = props["move_type"]

    def set_after(self, after):
        self.after = after

    def set_before(self, before):
        self.before = before

    def __str__(self):
        return f"type: {self.Type}, from:{self.From}, to:{self.To}, before{self.before.__str__()}"
