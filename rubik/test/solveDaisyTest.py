import unittest
from rubik.solveRotations import createCubeListFromInputParms
from rubik.solveRotations import y_0_WhiteLeafPos0_5
from rubik.solveDaisy import solveDaisy



class SolveDaisyTest(unittest.TestCase):   
            
  
        def test_010_SolveWhiteCross(self):
            inputDict = {}
            inputDict['cube'] = 'ygrgybbbbwroogowyygyrwwwbgybygbbooyrwbwrowrrgyroorggwo'    
            expectedResult = 'w'             

            actualResult = solveDaisy(inputDict)[0]
            print(actualResult)
            self.assertEqual(expectedResult, actualResult[1])
            self.assertEqual(expectedResult, actualResult[3])
            self.assertEqual(expectedResult, actualResult[5])
            self.assertEqual(expectedResult, actualResult[7])


    
