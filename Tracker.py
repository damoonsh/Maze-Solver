"""
    This object is going to track the movements of the object and then give
    the necessary data when needed.
"""
import random

class Move:
    def set_props(self, props):
        self.From = props["from_coor"]
        self.To = props["to_coor"]
        self.Type = props["move_type"]
        self.mkae_id()

    def set_after(self, after):
        self.after = after

    def set_before(self, before):
        self.before = before

    def mkae_id(self):
        id = ""
        for i in range(5):
            id += str(random.randrange(9))

        self.id = id

    def __str__(self):
        return f"id: {self.id}, type: {self.Type}, from: {self.From}, to: {self.To}"