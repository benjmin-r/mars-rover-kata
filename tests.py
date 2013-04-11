import unittest

from marsrover import Rover, Position, Direction


class RoverTest(unittest.TestCase):

    def test_move_one_forward(self):
        rover = Rover(Position(0, 0), Direction.for_direction("south"))
        rover.move(('f',))
        self.assertEquals((-1, 0), rover.get_position())

    def test_move_three_forward(self):
        rover = Rover(Position(0, 0), Direction.for_direction("south"))
        rover.move(('f', 'f', 'f'))
        self.assertEquals((-3, 0), rover.get_position())

    def test_move_two_forward_one_backwards(self):
        rover = Rover(Position(0, 0), Direction.for_direction("south"))
        rover.move(('f', 'f', 'b'))
        self.assertEquals((-1, 0), rover.get_position())

if __name__ == '__main__':
    unittest.main()
