'''
    This object is going to track the movements of the object and then give 
    the necessary data when needed.
'''


class Move:
    def set_props(self, props):
        self.From = props.from_coor
        self.To = props.to_coor
        self.type = props.type