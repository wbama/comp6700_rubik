import unittest
from rubik.solveWhiteCross import solveWhiteCross


class SolveWhiteCrossTest(unittest.TestCase):    
             
            
        def test_010_SolveWhiteCross(self):
            inputDict = {}
            inputDict['cube'] = 'ygrgybbbbwroogowyygyrwwwbgybygbbooyrwbwrowrrgyroorggwo'    
            expectedResult = 'w'             

            actualResult = solveWhiteCross(inputDict)
            self.assertEqual(expectedResult, actualResult[0][1])
            self.assertEqual(expectedResult, actualResult[0][3])
            self.assertEqual(expectedResult, actualResult[0][4])
            self.assertEqual(expectedResult, actualResult[0][5])
            self.assertEqual(expectedResult, actualResult[0][7])
            
        


    
