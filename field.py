


class field:
    def __init__(self, size):
        self.size = size
        self.field = []
        self.populate()

    def populate(self):
        for x in range(0, self.size):
            self.field.append([])
            for y in range(0, self.size):
                self.field[x].append('W')

    def loadbod(self, body):
        boundtest = True
        dims = [body.x, body.y]
        for dim in dims:
            if not(dim >= 0 & dim < self.size):
                print('point out of bounds') # throw error
                boundtest = False
        if boundtest:
            self.field[body.x][body.y] = body.interact(self.field[body.x][body.y])

    def display(self):
        for x in self.field:
            print(''.join(x))
