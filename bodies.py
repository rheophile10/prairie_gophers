class body:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.interactions = {}

    def interact(self, other):
        return self.interactions[str(other)]

class gopher(body):
    def __init__(self, x, y):
        body.__init__(self, x,y)
        self.interactions= {
            "W":":@",
            ":@": "X",
            "_":":@"
        }

class grenade(body):
    def __init__(self, x, y):
        body.__init__(self, x,y)
        self.interactions= {
            "W":"_",
            ":@":"X",
            "_":"_"
        }
