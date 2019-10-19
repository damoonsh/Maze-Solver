'''
    This object is going to track the movements of the object and then give the necessary data
    when needed
'''
class Movement:
    # Initializes the object with the given set of properties
    def __int__(self, type, fromCoor, toCoor):
        self.type = type
        self.From = fromCoor
        self.To  = toCoor
    def set_before(self, obj):
        self.before = obj
    def set_after(self, obj):
        self.after = obj

    def match(self, obj1, obj2):
        if obj1.type == obj2.type and obj1.From == obj2.From:
            return True
        return False
class Tracker:
    def __int__(self):
        self.moves = []

    def add_move(self, move):
        self.moves.append(move)