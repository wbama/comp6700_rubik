"""
    Created on 03/05/2022
    @author: Waldo du Toit
    unittests for solving the white cross
    
"""
import unittest
from rubik.solveLowerLayer import solveLowerLayer
from rubik.solveMiddleLayer import solveMiddleLayer

#need to update this. this is not a white cross. Look at the sides too
class SolveMiddleLayerTest(unittest.TestCase):  
    
           
    def test_010_SolveMiddleLayer(self):   
        inputDict = {}
        #inputDict['cube'] = 'SoYsssowwSww33YssSSwsSSo3Ys3ooSwo3SwosYwoYw33sSY3YYY3o'  
        inputDict['cube'] = 'SoYsssowwSww33YssSSwsSSo3Ys3ooSwo3SwosYwoYw33sSY3YYY3o'
        var_w = inputDict['cube'][-5]
        expectedResult_col = var_w 
                   

        actualResult = solveMiddleLayer(inputDict)[0]
        self.assertEqual(expectedResult_col, actualResult[5][1])
        self.assertEqual(expectedResult_col, actualResult[5][2])
        self.assertEqual(expectedResult_col, actualResult[5][3])
        self.assertEqual(expectedResult_col, actualResult[5][4])
        self.assertEqual(expectedResult_col, actualResult[5][5])
        self.assertEqual(expectedResult_col, actualResult[5][6])
        self.assertEqual(expectedResult_col, actualResult[5][7])
        self.assertEqual(expectedResult_col, actualResult[5][8])
        #sides should also be solved
        self.assertEqual(actualResult[0][3], actualResult[0][4], actualResult[0][5])
        self.assertEqual(actualResult[0][6], actualResult[0][7], actualResult[0][7])
        
        self.assertEqual(actualResult[1][3], actualResult[1][4], actualResult[1][5])
        self.assertEqual(actualResult[1][6], actualResult[1][7], actualResult[1][7])
        
        self.assertEqual(actualResult[2][3], actualResult[2][4], actualResult[2][5])
        self.assertEqual(actualResult[2][6], actualResult[2][7], actualResult[2][7])
        
        self.assertEqual(actualResult[3][3], actualResult[3][4], actualResult[3][5])
        self.assertEqual(actualResult[3][6], actualResult[3][7], actualResult[3][7])

        
        
          



            
 


    
