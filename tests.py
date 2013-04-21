import unittest

from marsrover import Rover, Position, Direction


class RoverTest(unittest.TestCase):

    def test_move_one_forward(self):
        self._move_and_test_rover(Position(0, 0),
                Direction.S,
                ('f',),
                Position(-1, 0))

    def test_move_one_forward_one_backward(self):
        self._move_and_test_rover(Position(0,0),
                Direction.S,
                ('f', 'b'),
                Position(0, 0))

    def test_move_one_forward_two_backward_north(self):
        self._move_and_test_rover(Position(0,0),
                Direction.N,
                ('f', 'b', 'b'),
                Position(-1, 0))

    def _move_and_test_rover(self, position, direction, movement, expected_position):
        rover = Rover(position, direction)
        rover.move(movement)
        self.assertEquals(expected_position, rover.get_position())


if __name__ == '__main__':
    unittest.main()
