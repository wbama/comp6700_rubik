import unittest
from rubik.solveDaisy import solveDaisy



class SolveDaisyTest(unittest.TestCase):   
            
  
        def test_010_SolveDaisy_y_0(self):
            inputDict = {}
            inputDict['cube'] = 'ygrgybbbbwroogowyygyrwwwbgybygbbooyrwbwrowrrgyroorggwo'    
            expectedResult = 'w'             

            actualResult = solveDaisy(inputDict)[0]
            self.assertEqual(expectedResult, actualResult[0][1])
            self.assertEqual(expectedResult, actualResult[0][3])
            self.assertEqual(expectedResult, actualResult[0][5])
            self.assertEqual(expectedResult, actualResult[0][7])
            
        def test_020_SolveDaisy_y_1(self):
            inputDict = {}
            inputDict['cube'] = 'rggboyrgoygboyrwboroogrbbbobwgowrgrbywyrgwwyrwogybyyww'    
            expectedResult = 'w'             

            actualResult = solveDaisy(inputDict)[0]
            self.assertEqual(expectedResult, actualResult[1][1])
            self.assertEqual(expectedResult, actualResult[1][3])
            self.assertEqual(expectedResult, actualResult[1][5])
            self.assertEqual(expectedResult, actualResult[1][7])
            
        def test_030_SolveDaisy_y_2(self):
            inputDict = {}
            inputDict['cube'] = 'rygbwrrggobwgrorroggowyoybbgwwborwoywyrrbwboybwyggyoyb'    
            expectedResult = 'w'             

            actualResult = solveDaisy(inputDict)[0]
            self.assertEqual(expectedResult, actualResult[2][1])
            self.assertEqual(expectedResult, actualResult[2][3])
            self.assertEqual(expectedResult, actualResult[2][5])
            self.assertEqual(expectedResult, actualResult[2][7])


    
