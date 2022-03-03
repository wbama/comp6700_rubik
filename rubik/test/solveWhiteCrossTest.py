import unittest
import rubik.solveWhiteCross as sc

class SolveWhiteCrossTest(unittest.TestCase):
    
        def test_010_ShouldRotateYellowCenterToFront(self):
            inputDict = {}
            inputDict['cube'] = 'ggrggoggoyroyyygbrbbbgbbybbwwwwwwwwwrryrryrrbooyooyoog'
            inputDict['op'] = 'solve'           
    
            expectedResult = {}
            expectedResult['cube'] = 'yroyyygbrbbbgbbybbwwwwwwwwwggrggoggorrrrrrbyyyygoooooo'
            expectedResult['status'] = 'ok'
            actualResult = sc.solveWhiteCross(inputDict)
            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))   
    
