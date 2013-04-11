
class Rover():

    def __init__(self, position, direction):
        self.position = position
        self.direction = direction

    def move(self, commands=()):
        for cmd in commands:
            direction = SouthDirection()
            self.position = direction.move(self.position, cmd)

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

class SouthDirection():

    def move(self, position, command):
        if command == 'f':
            return position.down()
        if command == 'b':
            return position.up()

