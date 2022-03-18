"""
    Created on 03/05/2022
    @author: Waldo du Toit
    unittests for solving the white cross
    
"""


import unittest
from rubik.solveWhiteCross import solveWhiteCross

#need to update this. this is not a white cross. Look at the sides too
class SolveWhiteCrossTest(unittest.TestCase):                 
    #y in position 0, w in position 2
        def test_010_SolveWhiteCross_y0(self):
            inputDict = {}
            inputDict['cube'] = 'rwrrygooggyrybyowybbbbwrroyoogwggbrywowgrrwgygwwboboyb'    
            expectedResult = 'w'             

            actualResult = solveWhiteCross(inputDict)[0]
            self.assertEqual(expectedResult, actualResult[2][1])
            self.assertEqual(expectedResult, actualResult[2][3])
            self.assertEqual(expectedResult, actualResult[2][4])
            self.assertEqual(expectedResult, actualResult[2][5])
            self.assertEqual(expectedResult, actualResult[2][7])
            #sides should be same color as the middle cells
            self.assertEqual(actualResult[1][5], actualResult[1][4])
            self.assertEqual(actualResult[4][1], actualResult[4][4])
            self.assertEqual(actualResult[3][3], actualResult[3][4])
            self.assertEqual(actualResult[5][7], actualResult[5][4])
            
        def test_020_SolveWhiteCross_y1(self):
            inputDict = {}
            inputDict['cube'] = 'bwwogbrrboygryoywgrgbwbgygbyywowbrygowwrroobgygrborwyo'    
            expectedResult = 'w'             

            actualResult = solveWhiteCross(inputDict)[0]
            self.assertEqual(expectedResult, actualResult[3][1])
            self.assertEqual(expectedResult, actualResult[3][3])
            self.assertEqual(expectedResult, actualResult[3][4])
            self.assertEqual(expectedResult, actualResult[3][5])
            self.assertEqual(expectedResult, actualResult[3][7])
            #sides should be same color as the middle cells
            self.assertEqual(actualResult[0][3], actualResult[0][4])
            self.assertEqual(actualResult[4][3], actualResult[4][4])
            self.assertEqual(actualResult[2][5], actualResult[2][4])
            self.assertEqual(actualResult[5][3], actualResult[5][4])
            
        def test_030_SolveWhiteCross_y2(self):
            inputDict = {}
            inputDict['cube'] = 'bbbbwrroyoogwggbryrwrrygooggyrybyowyygwrrgwowbyobobwwg'    
            expectedResult = 'w'             

            actualResult = solveWhiteCross(inputDict)[0]
            self.assertEqual(expectedResult, actualResult[0][1])
            self.assertEqual(expectedResult, actualResult[0][3])
            self.assertEqual(expectedResult, actualResult[0][4])
            self.assertEqual(expectedResult, actualResult[0][5])
            self.assertEqual(expectedResult, actualResult[0][7])
            
        def test_040_SolveWhiteCross_y3(self):
            inputDict = {}
            inputDict['cube'] = 'gyrybyowybbbbwrroyoogwggbryrwrrygoogwgwgroyrwwbbwoygbo'    
            expectedResult = 'w'             

            actualResult = solveWhiteCross(inputDict)[0]
            self.assertEqual(expectedResult, actualResult[1][1])
            self.assertEqual(expectedResult, actualResult[1][3])
            self.assertEqual(expectedResult, actualResult[1][4])
            self.assertEqual(expectedResult, actualResult[1][5])
            self.assertEqual(expectedResult, actualResult[1][7])
            
        def test_050_SolveWhiteCross_y4(self):
            inputDict = {}
            inputDict['cube'] = 'gwwboboyboygwbyyyrygwrrgwowggyogrowbrwrrygoogyorrwbbbb'    
            expectedResult = 'w'             

            actualResult = solveWhiteCross(inputDict)[0]
            self.assertEqual(expectedResult, actualResult[5][1])
            self.assertEqual(expectedResult, actualResult[5][3])
            self.assertEqual(expectedResult, actualResult[5][4])
            self.assertEqual(expectedResult, actualResult[5][5])
            self.assertEqual(expectedResult, actualResult[5][7])
            
        def test_060_SolveWhiteCross_y5(self):
            inputDict = {}
            inputDict['cube'] = 'wowgrrwgyryyybwgyobyobobwwgbworgoyggyorrwbbbbrwrrygoog'    
            expectedResult = 'w'             

            actualResult = solveWhiteCross(inputDict)[0]
            self.assertEqual(expectedResult, actualResult[4][1])
            self.assertEqual(expectedResult, actualResult[4][3])
            self.assertEqual(expectedResult, actualResult[4][4])
            self.assertEqual(expectedResult, actualResult[4][5])
            self.assertEqual(expectedResult, actualResult[4][7])
            
        def test_070_SolveWhiteCross_y5_WhiteNow1(self):
            inputDict = {}
            inputDict['cube'] = '1o1grr1gyryyyb1gyobyobob11gb1orgoyggyorr1bbbbr1rrygoog'    
            expectedResult = '1'             

            actualResult = solveWhiteCross(inputDict)[0]
            self.assertEqual(expectedResult, actualResult[4][1])
            self.assertEqual(expectedResult, actualResult[4][3])
            self.assertEqual(expectedResult, actualResult[4][4])
            self.assertEqual(expectedResult, actualResult[4][5])
            self.assertEqual(expectedResult, actualResult[4][7])
            
        def test_080_SolveWhiteCross_y0_NoYellow(self): #if yellow not exist, then [4][4] is yellow, [5][4] is white, which is now g
            inputDict = {}
            inputDict['cube'] = 'owog1bwgggobwowrrw11rowoogw1rgbr1bggbbobb11rwrr1wg1rob'    
            expectedResult = 'g'             

            actualResult = solveWhiteCross(inputDict)[0]
            self.assertEqual(expectedResult, actualResult[5][1])
            self.assertEqual(expectedResult, actualResult[5][3])
            self.assertEqual(expectedResult, actualResult[5][4])
            self.assertEqual(expectedResult, actualResult[5][5])
            self.assertEqual(expectedResult, actualResult[5][7])
            
            
        


    
