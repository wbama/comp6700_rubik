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
    
    def test_010_RotateIntoTShape(self):   
        inputDict = {}
        inputDict['cube'] = 'gwgbbobgrowbwrbwwgygrrgyrobwyoroyworgrooygwbyyybbwrogy'  
        #solve lower layer first, then rotate into T
        
        actualResult = solveMiddleLayer(inputDict)[0]
        #sides should also be solved
        if actualResult[0][1] == actualResult[0][4]:
            self.assertEqual(actualResult[0][1], actualResult[0][4], actualResult[0][6]) 
        elif actualResult[1][1] == actualResult[1][4]:
            self.assertEqual(actualResult[1][1], actualResult[1][4], actualResult[1][6]) 
        elif actualResult[2][1] == actualResult[2][4]:
            self.assertEqual(actualResult[2][1], actualResult[2][4], actualResult[2][6]) 
        elif actualResult[2][1] == actualResult[2][4]:
            self.assertEqual(actualResult[3][1], actualResult[3][4], actualResult[3][6])

        
        
          



            
 


    
