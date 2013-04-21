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

    def test_move_one_forward_two_backward_turn_left(self):
        self._move_and_test_rover(Position(0,0),
                Direction.N,
                ('f', 'b', 'b', 'l', 'f'),
                Position(-1, -1))

    def test_move_one_forward_two_backward_turn_right(self):
        self._move_and_test_rover(Position(0,0),
                Direction.S,
                ('f', 'b', 'b', 'r', 'f'),
                Position(1, -1))

    def test_move_one_forward_two_backward_turn_left(self):
        self._move_and_test_rover(Position(0,0),
                Direction.S,
                ('f', 'b', 'b', 'l', 'f', 'f'),
                Position(1, 2))

    def test_move_east_and_turn_left_twice(self):
        self._move_and_test_rover(Position(0,0),
                Direction.E,
                ('f', 'b', 'l', 'l', 'f', 'f'),
                Position(0, -2))

    def _move_and_test_rover(self, position, direction, movement, expected_position):
        rover = Rover(position, direction)
        rover.move(movement)
        self.assertEquals(expected_position, rover.get_position())

    def test_move_west_on_finite_grid(self):
        rover = Rover(Position(10, 10), Direction.W, (20, 20))
        rover.move(('f', 'f'))
        self.assertEquals(Position(10, 8), rover.get_position())

    def test_move_east_on_finite_grid_with_wrapping(self):
        rover = Rover(Position(10, 10), Direction.E, (10, 10))
        rover.move(('f', 'f', 'f'))
        self.assertEquals(Position(10, -8), rover.get_position())

    def test_wrapping_left_edge(self):
        rover = Rover(Position(20, -30), Direction.W, (30, 30))
        rover.move(('f', 'f'))
        self.assertEquals(Position(20, 29), rover.get_position())

    def test_wrapping_upper_edge(self):
        rover = Rover(Position(20, 0), Direction.N, (20, 30))
        rover.move(('f', 'f', 'f', 'f'))
        self.assertEquals(Position(-17, 0), rover.get_position())

if __name__ == '__main__':
    unittest.main()
