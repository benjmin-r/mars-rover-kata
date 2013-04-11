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

    def test_move_one_forward_three_backward_west(self):
        rover = Rover(Position(0, 0), Direction.for_direction("west"))
        rover.move(('f', 'b', 'b', 'b'))
        self.assertEquals((0, 2), rover.get_position())

    def test_move_two_forward_one_backwards_north(self):
        rover = Rover(Position(0, 0), Direction.for_direction("north"))
        rover.move(('f', 'f', 'b'))
        self.assertEquals((1, 0), rover.get_position())

    def test_move_five_forward_eight_backwards_east(self):
        rover = Rover(Position(0, 0), Direction.for_direction("east"))
        rover.move(('f', 'f', 'f', 'f', 'f', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b',))
        self.assertEquals((0, -3), rover.get_position())

if __name__ == '__main__':
    unittest.main()
