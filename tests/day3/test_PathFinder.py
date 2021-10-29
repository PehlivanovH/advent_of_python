import unittest

from classes.day3.PathFinder import PathFinder

class TestPathFinder(unittest.TestCase):

    def testSlope_CountEncounteredTrees(self):
        pathFinder = PathFinder();
        input = pathFinder.readInput("../../input/testDay3");
        treeCount = pathFinder.countTrees(input);
        self.assertEqual(7, treeCount);
