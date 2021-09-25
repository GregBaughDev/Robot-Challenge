class Robot:
    """Class to manage robot information and movement"""

    def __init__(self, x, y, f):
        self.x = int(x)
        self.y = int(y)
        self.f = f

    def report(self):
        print(f"{self.x},{self.y},{self.f}")

    def move(self):
        # North & South - y axis
        if self.f == 'NORTH' and self.y != 5:
            self.y += 1
        elif self.f == 'SOUTH' and self.y != 0:
            self.y -= 1
        # East & West - x axis
        elif self.f == 'EAST' and self.x != 5:
            self.x += 1
        elif self.f == 'WEST' and self.x != 0:
            self.x -= 1
    
    def left(self):
        if self.f == 'NORTH':
            self.f = 'WEST'
        elif self.f == 'EAST':
            self.f = 'NORTH'
        elif self.f == 'SOUTH':
            self.f = 'EAST'
        elif self.f == 'WEST':
            self.f = 'SOUTH'

    def right(self):
        if self.f == 'NORTH':
            self.f = 'EAST'
        elif self.f == 'EAST':
            self.f = 'SOUTH'
        elif self.f == 'SOUTH':
            self.f = 'WEST'
        elif self.f == 'WEST':
            self.f = 'NORTH'

    