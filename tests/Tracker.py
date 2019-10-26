'''
    This object is going to track the movements of the object and then give
    the necessary data when needed.
'''

class Move:
    def __init__(self, props):
        # For the first movement the initial co-ordinate is (0, 0)
        self.From = (0, 0)
    def set_props(self, props):
        self.From = props["from_coor"]
        self.To = props["to_coor"]
        self.Type = props["move_type"]

    def set_after(self, after):
        self.after = after

    def set_before(self, before):
        self.before = before
