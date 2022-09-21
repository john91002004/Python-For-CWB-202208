import unittest

from MathFunction import calCombinationAmount


class CombinationTest(unittest.TestCase): 

    def testCombinationResult(self): 
        self.assertEqual( calCombinationAmount(3, 0), 1) 
        self.assertEqual( calCombinationAmount(3, 1), 3) 
        self.assertEqual( calCombinationAmount(3, 2), 3) 
        self.assertEqual( calCombinationAmount(3, 3), 1) 
        self.assertEqual( calCombinationAmount(10, 3), 10*9*8/3/2/1) 
        self.assertEqual( calCombinationAmount(10, 7), 10*9*8/3/2/1) 
        self.assertEqual( calCombinationAmount(10, 9), 10) 

if __name__ == '__main__': 
    unittest.main(verbosity=4)
