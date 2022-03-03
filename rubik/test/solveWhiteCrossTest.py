import unittest
import rubik.solve as solve

class SolveWhiteCrossTest(unittest.TestCase):
    
        def test_010_ShouldRotateValidNominalCube_F(self):
            inputDict = {}
            inputDict['cube'] = 'rrbbbbgggryyyyoroyogryggobbwwwwwwwwwgrboorbbyoyyrrgoog'
            inputDict['rotate'] = 'F'
            inputDict['op'] = 'solve'           
    
            expectedResult = {}
            expectedResult['cube'] = 'gbrgbrgbbbyybyoyoyogryggobbwwowwywwygrboorwwwryrrrgoog'
            expectedResult['status'] = 'ok'
            actualResult = solve._solve(inputDict)
            self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
            self.assertEqual(expectedResult.get('status'), actualResult.get('status'))   
    
