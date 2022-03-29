"""
    Created on 03/05/2022
    @author: Waldo du Toit
    unittests for solving the white cross
    
"""


import unittest
from rubik.solveLowerLayer import solveLowerLayer

#need to update this. this is not a white cross. Look at the sides too
class SolveLowerLayerTest(unittest.TestCase):  
    def test_010_SolveLowerLayer(self):   
        inputDict = {}
        inputDict['cube'] = 'gwwboboyboygwbyyyrygwrrgwowggyogrowbrwrrygoogyorrwbbbb'    
        expectedResult = 'w'             

        actualResult = solveLowerLayer(inputDict)[0]
        self.assertEqual(expectedResult, actualResult[5][1])
        self.assertEqual(expectedResult, actualResult[5][3])
        self.assertEqual(expectedResult, actualResult[5][4])
        self.assertEqual(expectedResult, actualResult[5][5])
        self.assertEqual(expectedResult, actualResult[5][7])
        #sides should be same color as the middle cells
        self.assertEqual(actualResult[3][7], actualResult[3][4])
        self.assertEqual(actualResult[0][7], actualResult[0][4])
        self.assertEqual(actualResult[1][7], actualResult[1][4])
        self.assertEqual(actualResult[2][7], actualResult[2][4])            


            
 


    
