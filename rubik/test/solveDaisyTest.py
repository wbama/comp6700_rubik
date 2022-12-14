"""
    Created on 03/05/2022
    @author: Waldo du Toit
    unittests for solving the daisy
    
"""


import unittest
from rubik.solveDaisy import solveDaisy
from rubik.solveRotations import createCubeListFromInputParms, createYellowAndWhiteVariables



class SolveDaisyTest(unittest.TestCase):  

   
    def test_010_SolveDaisy_y_0(self):
            inputDict = {}
            inputDict['cube'] = 'growbwyrrgroorogyywyobgyorrbgrgobwobyobwyyywwrbwgwbbgg'    
            expectedResult = 'w'             
            if createCubeListFromInputParms(inputDict)[0][4] == createYellowAndWhiteVariables(inputDict)[0]:
                actualResult = solveDaisy(inputDict)[0]
                self.assertEqual(expectedResult, actualResult[0][1])
                self.assertEqual(expectedResult, actualResult[0][3])
                self.assertEqual(expectedResult, actualResult[0][5])
                self.assertEqual(expectedResult, actualResult[0][7])
            
    def test_020_SolveDaisy_y_1(self):
            inputDict = {}
            inputDict['cube'] = 'ybybbrwwbgyrgyyogwwbyrgoowbrgrgwrryogwgwooboogoybrywrb'    
            expectedResult = 'w'             

            if createCubeListFromInputParms(inputDict)[1][4] == createYellowAndWhiteVariables(inputDict)[0]:
                actualResult = solveDaisy(inputDict)[0]
                self.assertEqual(expectedResult, actualResult[1][1])
                self.assertEqual(expectedResult, actualResult[1][3])
                self.assertEqual(expectedResult, actualResult[1][5])
                self.assertEqual(expectedResult, actualResult[1][7])
            
    def test_030_SolveDaisy_y_2(self):
            inputDict = {}
            inputDict['cube'] = 'rygbwrrggobwgrorroggowyoybbgwwborwoywyrrbwboybwyggyoyb'    
            expectedResult = 'w'             

            if createCubeListFromInputParms(inputDict)[2][4] == createYellowAndWhiteVariables(inputDict)[0]:
                actualResult = solveDaisy(inputDict)[0]
                self.assertEqual(expectedResult, actualResult[2][1])
                self.assertEqual(expectedResult, actualResult[2][3])
                self.assertEqual(expectedResult, actualResult[2][5])
                self.assertEqual(expectedResult, actualResult[2][7])
            
    def test_040_SolveDaisy_y_3(self):
            inputDict = {}
            inputDict['cube'] = 'grygoogyrorgwwwbrbwbrgrbwbrrywwyowroyyoobbrybygyggwboo'    
            expectedResult = 'w'             

            if createCubeListFromInputParms(inputDict)[3][4] == createYellowAndWhiteVariables(inputDict)[0]:
                actualResult = solveDaisy(inputDict)[0]
                self.assertEqual(expectedResult, actualResult[3][1])
                self.assertEqual(expectedResult, actualResult[3][3])
                self.assertEqual(expectedResult, actualResult[3][5])
                self.assertEqual(expectedResult, actualResult[3][7])
            
    def test_050_SolveDaisy_y_4(self):
            inputDict = {}
            inputDict['cube'] = 'qBu1HqHH111HBBqqBHqHq11qB1BBqBHuu1uu1uuuqBHHOOOuOOOOOO'    
            var_w = inputDict['cube'][-5]
            expectedResult = var_w  
                         
            if createCubeListFromInputParms(inputDict)[4][4] == createYellowAndWhiteVariables(inputDict)[0]:
                actualResult = solveDaisy(inputDict)[0]
                self.assertEqual(expectedResult, actualResult[4][1])
                self.assertEqual(expectedResult, actualResult[4][3])
                self.assertEqual(expectedResult, actualResult[4][5])
                self.assertEqual(expectedResult, actualResult[4][7])
            
    def test_060_SolveDaisy_y_5(self):
            inputDict = {}
            inputDict['cube'] = 'wbobrboygyywwborwyrbbgowrggywgrgywyworbowroogboygygrrb'    
            expectedResult = 'w'             

            if createCubeListFromInputParms(inputDict)[5][4] == createYellowAndWhiteVariables(inputDict)[0]:
                actualResult = solveDaisy(inputDict)[0]
                self.assertEqual(expectedResult, actualResult[5][1])
                self.assertEqual(expectedResult, actualResult[5][3])
                self.assertEqual(expectedResult, actualResult[5][5])
                self.assertEqual(expectedResult, actualResult[5][7])



    
