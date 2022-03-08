import unittest
from rubik.solveDaisy import solveDaisy



class SolveDaisyTest(unittest.TestCase):   
            
  
        def test_010_SolveDaisy_y_0(self):
            inputDict = {}
            inputDict['cube'] = 'ygrgybbbbwroogowyygyrwwwbgybygbbooyrwbwrowrrgyroorggwo'    
            expectedResult = 'w'             

            actualResult = solveDaisy(inputDict)[0]
            print(actualResult)
            self.assertEqual(expectedResult, actualResult[1])
            self.assertEqual(expectedResult, actualResult[3])
            self.assertEqual(expectedResult, actualResult[5])
            self.assertEqual(expectedResult, actualResult[7])


    
