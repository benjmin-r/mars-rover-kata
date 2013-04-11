
class Rover():

    def __init__(self, xpos, ypos, direction):
        self.xpos = xpos
        self.ypos = ypos
        self.direction = direction

    def move(self, commands=()):
        for cmd in commands:
            if cmd == 'f' and self.direction == 'south':
                self.xpos = self.xpos-1

    def get_position(self):
        return (self.xpos, self.ypos)
