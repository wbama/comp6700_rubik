"""
    Created on 03/05/2022
    @author: Waldo du Toit
    unittests for solving the white cross
    
"""


import unittest
from rubik.solveLowerLayer import solveLowerLayer
from rubik.solveMiddleLayer import solveMiddleLayer

#need to update this. this is not a white cross. Look at the sides too
class SolveLowerLayerTest(unittest.TestCase):  
    # def test_010_SolveLowerLayer(self):   
    #     inputDict = {}
    #     inputDict['cube'] = 'oGog6og3Sg36S33o6gGo36SSS63go6gooSGo663GggGSS6SG3GGGg3'  
    #     var_w = inputDict['cube'][-5]
    #     expectedResult_col = var_w 
    #
    #
    #     actualResult = solveLowerLayer(inputDict)[0]
    #     self.assertEqual(expectedResult_col, actualResult[5][1])
    #     self.assertEqual(expectedResult_col, actualResult[5][2])
    #     self.assertEqual(expectedResult_col, actualResult[5][3])
    #     self.assertEqual(expectedResult_col, actualResult[5][4])
    #     self.assertEqual(expectedResult_col, actualResult[5][5])
    #     self.assertEqual(expectedResult_col, actualResult[5][6])
    #     self.assertEqual(expectedResult_col, actualResult[5][7])
    #     self.assertEqual(expectedResult_col, actualResult[5][8])
    #     #sides should also be solved
    #     self.assertEqual(actualResult[0][6], actualResult[0][7], actualResult[0][7])
    #     self.assertEqual(actualResult[1][6], actualResult[1][7], actualResult[1][7])
    #     self.assertEqual(actualResult[2][6], actualResult[2][7], actualResult[2][7])
    #     self.assertEqual(actualResult[3][6], actualResult[3][7], actualResult[3][7])
        
    # def test_020_SolveMiddleLayer(self):   
    #     inputDict = {}
    #     inputDict['cube'] = 'oGog6og3Sg36S33o6gGo36SSS63go6gooSGo663GggGSS6SG3GGGg3'  
    #
    #     actualResult = solveMiddleLayer(inputDict)[0]
    #     #sides should also be solved
    #     self.assertEqual(actualResult[0][4], actualResult[0][5], actualResult[0][6])
    #     self.assertEqual(actualResult[1][4], actualResult[1][5], actualResult[1][6])
    #     self.assertEqual(actualResult[2][4], actualResult[2][5], actualResult[2][6])
    #     self.assertEqual(actualResult[3][4], actualResult[3][5], actualResult[3][6])
    
    def test_030_RotateIntoTShape(self):   
        inputDict = {}
        inputDict['cube'] = 'oGog6og3Sg36S33o6gGo36SSS63go6gooSGo663GggGSS6SG3GGGg3'  
        #solve lower layer first, then rotate into T
        
        actualResult = solveMiddleLayer(inputDict)[0]
        #sides should also be solved
        self.assertEqual(actualResult[0][1], actualResult[0][4], actualResult[0][6])
        self.assertEqual(actualResult[1][1], actualResult[1][4], actualResult[1][6])
        self.assertEqual(actualResult[2][1], actualResult[2][4], actualResult[2][6])
        self.assertEqual(actualResult[3][1], actualResult[3][4], actualResult[3][6])

        
        
          



            
 


    
