from enum import Enum

class Direction(Enum):
    NORTH = 'NORTH'
    EAST = 'EAST'
    SOUTH = 'SOUTH'
    WEST = 'WEST'

class Movement(Enum):
    WALK = 'WALK'
    RUN = 'RUN'

class Robot:
    """Class to manage robot information and movement"""

    def __init__(self, x, y, f, boardx = 4, boardy = 4):
        self.x = int(x)
        self.y = int(y)
        self.boardx = int(boardx)
        self.boardy = int(boardy)
        self.move_speed = Movement.WALK

        if f == 'NORTH':
            self.f = Direction.NORTH
        elif f == 'SOUTH':
            self.f = Direction.SOUTH
        elif f == 'EAST':
            self.f = Direction.EAST
        elif f == 'WEST':
            self.f = Direction.WEST
    
    def report(self):
        print(f"{self.x},{self.y},{self.f}")

    def move(self):
        # North & South - y axis
        move_amount = self.get_move_amount(self.move_speed)
        
        if self.check_boundary(self.f):
            if self.f == Direction.NORTH:
                self.y += move_amount
            elif self.f == Direction.SOUTH:
                self.y -= move_amount
            # East & West - x axis
            elif self.f == Direction.EAST:
                self.x += move_amount
            elif self.f == Direction.WEST:
                self.x -= move_amount
            
    def check_boundary(self, direction):
        if direction == Direction.SOUTH:
            return self.y != 0
        elif direction == Direction.WEST:
            return self.x != 0
        elif direction == Direction.NORTH:
            return self.y != self.boardy
        elif direction == Direction.EAST:
            return self.x != self.boardx
    
    def get_move_amount(self, speed):
        # speed will alter the unit amount
        if speed == Movement.WALK:
            return 1
        elif speed == Movement.RUN:
            return 2
    
    def left(self):
        if self.f == Direction.NORTH:
            self.f = Direction.WEST
        elif self.f == Direction.EAST:
            self.f = Direction.NORTH
        elif self.f == Direction.SOUTH:
            self.f = Direction.EAST
        elif self.f == Direction.WEST:
            self.f = Direction.SOUTH

    def right(self):
        if self.f == Direction.NORTH:
            self.f = Direction.EAST
        elif self.f == Direction.EAST:
            self.f = Direction.SOUTH
        elif self.f == Direction.SOUTH:
            self.f = Direction.WEST
        elif self.f == Direction.WEST:
            self.f = Direction.NORTH

    def charge(self):
        # match self.f:
        #     case Direction.NORTH:
        #         self.y += 4 - self.y
        #         return
        #     case Direction.SOUTH:
        #         self.y -= self.y
        #         return
        #     case Direction.WEST:
        #         self.x -= self.x
        #         return
        #     case Direction.EAST:
        #         self.x += 4 - self.x
        #         return

        # Check the direction of the robot
        if self.f == Direction.NORTH: 
            self.y += self.boardy - self.y
        elif self.f == Direction.SOUTH:
            self.y -= self.y
        elif self.f == Direction.WEST:
            self.x -= self.x
        elif self.f == Direction.EAST:
            self.x += self.boardx - self.x

        