import unittest

from marsrover import Rover


class RoverTest(unittest.TestCase):

    def test_move_one_forward(self):
        rover = Rover(0, 0, "south")
        rover.move(('f',))
        self.assertEquals((-1, 0), rover.get_position())

if __name__ == '__main__':
    unittest.main()
