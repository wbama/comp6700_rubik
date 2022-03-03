import unittest
import rubik.solveWhiteCross as sc
from rubik.solveRotations import rotateCubeClockwise

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
            
            
        def test_020_RotateWholeCubeClockwise(self):
            inputDict = {}
            inputDict['cube'] = 'ggrggoggoyroyyygbrbbbgbbybbwwwwwwwwwrryrryrrbooyooyoog'
            inputDict['op'] = 'solve'           
    
            expectedResult = {}
            expectedResult['cube'] = 'ggggggoorrrrrrrbyybbbbbbbgyoooooogyywwwwwwwwwgyybyrryo'
            expectedResult['status'] = 'ok'
            actualResult = rotateCubeClockwise(inputDict)
            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))  
    
