import unittest
import random
import metattt

class TestBoardFunctions(unittest.TestCase):
    def setup(self):
        self.largeBoard = Board(4,4)
        self.smallBoard = Board(1,1)
        self.highDim = Board(99,1)
        self.highSize = Board(1,99)
        self.midBoard = (2,2)
    