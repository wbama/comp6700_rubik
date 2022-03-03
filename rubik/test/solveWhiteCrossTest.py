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
            inputDict['cube'] = 'bgbgyrywgogyygywooggrbwywrobwyobrywrwworoorywgbrorbbbg'
            inputDict['op'] = 'solve'  
            
            lst_cube = createCubeListFromInputParms(inputDict) 
            str1 = "".join(lst_cube[0])
            str2 = "".join(lst_cube[1])
            str3 = "".join(lst_cube[2])
            str4 = "".join(lst_cube[3])
            str5 = "".join(lst_cube[4])
            str6 = "".join(lst_cube[5])                       
         
            str_cube = str1+str2+str3+str4+str5+str    
            expectedResult = str_cube
            actualResult = rotateCubeClockwise(lst_cube)
            self.assertEqual(expectedResult, actualResult)
    
