
class Rover():

    def __init__(self, position, direction):
        self.position = position
        self.direction = direction

    def move(self, commands=()):
        for cmd in commands:
            self.position = self.direction.move(self.position, cmd)

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

    def left(self):
        return Position(self.xpos, self.ypos-1)

    def right(self):
        return Position(self.xpos, self.ypos+1)

    def get_position(self):
        return (self.xpos, self.ypos)

class Direction():

    @staticmethod
    def for_direction(direction_str):
        if direction_str == "west":
            return WestDirection()
        if direction_str == "east":
            return EastDirection()
        if direction_str == "north":
            return NorthDirection()
        if direction_str == "south":
            return SouthDirection()

class EastDirection():

    def move(self, position, command):
        if command == 'f':
            return position.right()
        if command == 'b':
            return position.left()

class NorthDirection():

    def move(self, position, command):
        if command == 'f':
            return position.up()
        if command == 'b':
            return position.down()

class WestDirection():

    def move(self, position, command):
        if command == 'f':
            return position.left()
        if command == 'b':
            return position.right()

class SouthDirection():

    def move(self, position, command):
        if command == 'f':
            return position.down()
        if command == 'b':
            return position.up()

