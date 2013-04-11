
class Rover():

    def __init__(self, position, direction):
        self.position = position
        self.direction = direction

    def move(self, commands=()):
        for cmd in commands:
            if cmd == 'f' and self.direction == 'south':
                self.position = self.position.down()
            if cmd == 'b' and self.direction == 'south':
                self.position = self.position.up()

    def get_position(self):
        return self.position.get_position()

class Position():

    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos

    def down(self):
        return Position(self.xpos-1, self.ypos)

    def up(self):
        return Position(self.xpos+1, self.ypos)

    def get_position(self):
        return (self.xpos, self.ypos)
