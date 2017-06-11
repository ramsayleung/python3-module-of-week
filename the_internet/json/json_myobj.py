class Myobj:
    def __init__(self, s):
        self.s = s

    def __repr__(self):
        return '<Myobj({})>'.format(self.s)
