import unittest
from rubik.solveWhiteCross import solveWhiteCross


class SolveWhiteCrossTest(unittest.TestCase):                 
            
        def test_010_SolveWhiteCross_y0(self):
            inputDict = {}
            inputDict['cube'] = 'boygygrrbrwywbyyowgoorwobrogywwgyyrwwbobrboygggrwogbbr'    
            expectedResult = 'w'             

            actualResult = solveWhiteCross(inputDict)[0]
            self.assertEqual(expectedResult, actualResult[2][1])
            self.assertEqual(expectedResult, actualResult[2][3])
            self.assertEqual(expectedResult, actualResult[2][4])
            self.assertEqual(expectedResult, actualResult[2][5])
            self.assertEqual(expectedResult, actualResult[2][7])
            
        


    
