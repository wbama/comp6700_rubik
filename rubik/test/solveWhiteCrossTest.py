import unittest
import rubik.solveWhiteCross as sc
from rubik.solveRotations import rotateCubeClockwise
from rubik.solveRotations import createCubeListFromInputParms

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
            
            inputResult = createCubeListFromInputParms(inputDict)         
    
            expectedResult = [['g', 'g', 'g', 'g', 'g', 'g', 'o', 'o', 'r'], ['r', 'r', 'r', 'r', 'r', 'r', 'b', 'y', 'y'], ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'g', 'y'], ['o', 'o', 'o', 'o', 'o', 'o', 'g', 'y', 'y'], ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'], ['g', 'y', 'y', 'b', 'y', 'r', 'r', 'y', 'o']]


            actualResult = rotateCubeClockwise(inputDict)
            self.assertEqual(expectedResult, actualResult)
    
