import unittest
from rubik.solveWhiteCross import solveWhiteCross


class SolveWhiteCrossTest(unittest.TestCase):                 
            
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
            
        def test_020_SolveWhiteCross_y1(self):
            inputDict = {}
            inputDict['cube'] = 'oogwggbryrwrrygooggyrybyowybbbbwrroywryorgwgwobgyowbbw'    
            expectedResult = 'w'             

            actualResult = solveWhiteCross(inputDict)[0]
            self.assertEqual(expectedResult, actualResult[3][1])
            self.assertEqual(expectedResult, actualResult[3][3])
            self.assertEqual(expectedResult, actualResult[3][4])
            self.assertEqual(expectedResult, actualResult[3][5])
            self.assertEqual(expectedResult, actualResult[3][7])
            
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
            
            
        


    
