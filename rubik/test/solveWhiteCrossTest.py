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
            
            expectedResult = {} 
            expectedResult['cube'] = 'yroyyygbrbbbgbbybbwwwwwwwwwggrggoggorrrrrrbyyyygoooooo'
            
            lst_cube = createCubeListFromInputParms(inputDict)           
            rotatedCube = rotateCubeClockwise(lst_cube)
            
            str1 = "".join(rotatedCube[0])
            print(str1)
            str2 = "".join(rotatedCube[1])
            str3 = "".join(rotatedCube[2])
            str4 = "".join(rotatedCube[3])
            str5 = "".join(rotatedCube[4])
            str6 = "".join(rotatedCube[5]) 
            print(str6)
            str_cube = str1+str2+str3+str4+str5+str 
            

              
            self.assertEqual(expectedResult.get('cube'), str_cube)
    
