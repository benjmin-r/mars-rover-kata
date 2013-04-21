
class Rover():

    def __init__(self, position, direction):
        self.position = position

    def move(self, commands):
        for cmd in commands:
            if cmd == 'f':
                self.position.down()
            else:
                self.position.up()

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

class Direction():
    S = 'south'
