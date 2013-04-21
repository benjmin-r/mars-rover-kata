
class Rover():

    def __init__(self, position, direction):
        self.position = position
        self.direction = direction

    def move(self, commands):
        for cmd in commands:
            if cmd == 'f':
                self.direction.forward(self.position)
            elif cmd == 'b':
                self.direction.backward(self.position)
            elif cmd == 'l':
                self.direction = self.direction.turn_left()

    def get_position(self):
        return self.position

class Position():

    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def __repr__(self):
        return "<Position x=%s, y=%s>" % (self.pos_x, self.pos_y)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return other.pos_x == self.pos_x and other.pos_y == self.pos_y
        else: 
            return False

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return other.pos_x != self.pos_x or other.pos_y != self.pos_y
        else:
            return True

    def down(self):
        self.pos_x -= 1

    def up(self):
        self.pos_x += 1

    def left(self):
        self.pos_y -= 1

    def right(self):
        self.pos_y += 1

class NorthDirection():

    def forward(self, position):
        return position.up()

    def backward(self, position):
        return position.down()

    def turn_left(self):
        return Direction.W

class WestDirection():

    def forward(self, position):
        return position.left()

    def backward(self, position):
        return position.right()


class SouthDirection():

    def forward(self, position):
        return position.down()

    def backward(self, position):
        return position.up()

class Direction():
    S = SouthDirection()
    N = NorthDirection()
    W = WestDirection()

