import unittest
import rubik.solve as solve



class SolveTest(unittest.TestCase):    
 
    def test_solve_010_ShouldRotateValidNominalCube_F(self):

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
        
        
    def test_solve_020_ShouldRotateValidNominalCube_f(self):
        inputDict = {}
        inputDict['cube'] = 'rrbbbbgggryyyyoroyogryggobbwwwwwwwwwgrboorbbyoyyrrgoog'
        inputDict['rotate'] = 'f'
        inputDict['op'] = 'solve'
           
        expectedResult = {}
        expectedResult['cube'] = 'bbgrbgrbgyyyyyoooyogryggobbwwywwbwwbgrboorryrwwwrrgoog'
        expectedResult['status'] = 'ok'
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))        
        
    def test_solve_030_ShouldRotateValidNominalCube_R(self):
        inputDict = {}
        inputDict['cube'] = 'rrbbbbgggryyyyoroyogryggobbwwwwwwwwwgrboorbbyoyyrrgoog'
        inputDict['rotate'] = 'R'
        inputDict['op'] = 'solve'
           
        expectedResult = {}
        expectedResult['cube'] = 'rrybbggggryroyyyoyygrrggbbbwwwwwwwwwgrboobbbgoyorryooo'
        expectedResult['status'] = 'ok'
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_solve_040_ShouldRotateValidNominalCube_r(self):
        inputDict = {}
        inputDict['cube'] = 'rrbbbbgggryyyyoroyogryggobbwwwwwwwwwgrboorbbyoyyrrgoog'
        inputDict['rotate'] = 'r'
        inputDict['op'] = 'solve'
           
        expectedResult = {}
        expectedResult['cube'] = 'rrbbbrggyyoyyyoryrggrgggybbwwwwwwwwwgroooybbooybrrboog'
        expectedResult['status'] = 'ok'
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_solve_050_ShouldRotateValidNominalCube_B(self):
        inputDict = {}
        inputDict['cube'] = 'rrbbbbgggryyyyoroyogryggobbwwwwwwwwwgrboorbbyoyyrrgoog'
        inputDict['rotate'] = 'B'
        inputDict['op'] = 'solve'
           
        expectedResult = {}
        expectedResult['cube'] = 'rrbbbbgggrygyyoroooyobggbgrbwwrwwgwwyoyoorbbyoyyrrgwww'
        expectedResult['status'] = 'ok'
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_solve_060_ShouldRotateValidNominalCube_b(self):
        inputDict = {}
        inputDict['cube'] = 'rrbbbbgggryyyyoroyogryggobbwwwwwwwwwgrboorbbyoyyrrgoog'
        inputDict['rotate'] = 'b'
        inputDict['op'] = 'solve'
           
        expectedResult = {}
        expectedResult['cube'] = 'rrbbbbgggrygyyrrobrgbggboyoowwowwgwwwwwoorbbyoyyrrgyoy'
        expectedResult['status'] = 'ok'
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
        
    def test_solve_070_ShouldRotateValidNominalCube_L(self):
        inputDict = {}
        inputDict['cube'] = 'rrbbbbgggryyyyoroyogryggobbwwwwwwwwwgrboorbbyoyyrrgoog'
        inputDict['rotate'] = 'L'
        inputDict['op'] = 'solve'
           
        expectedResult = {}
        expectedResult['cube'] = 'grbobbbggryyyyoroyogoygrobowwwwwwwwwbrbgorrbyryybrggog'
        expectedResult['status'] = 'ok'
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))        
        
    def test_solve_080_ShouldRotateValidNominalCube_l(self):
        inputDict = {}
        inputDict['cube'] = 'rrbbbbgggryyyyoroyogryggobbwwwwwwwwwgrboorbbyoyyrrgoog'
        inputDict['rotate'] = 'l'
        inputDict['op'] = 'solve'
           
        expectedResult = {}
        expectedResult['cube'] = 'orbrbboggryyyyoroyogbygoobgwwwwwwwwwrrbborgbybyygrgrog'
        expectedResult['status'] = 'ok'
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_solve_090_ShouldRotateValidNominalCube_U(self):
        inputDict = {}
        inputDict['cube'] = 'rrbbbbgggryyyyoroyogryggobbwwwwwwwwwgrboorbbyoyyrrgoog'
        inputDict['rotate'] = 'U'
        inputDict['op'] = 'solve'
           
        expectedResult = {}
        expectedResult['cube'] = 'ryybbbgggogryyoroywwwyggobbrrbwwwwwwbogboryrboyyrrgoog'
        expectedResult['status'] = 'ok'
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_solve_100_ShouldRotateValidNominalCube_u(self):
        inputDict = {}
        inputDict['cube'] = 'rrbbbbgggryyyyoroyogryggobbwwwwwwwwwgrboorbbyoyyrrgoog'
        inputDict['rotate'] = 'u'
        inputDict['op'] = 'solve'
           
        expectedResult = {}
        expectedResult['cube'] = 'wwwbbbgggrrbyyoroyryyyggobbogrwwwwwwbryrobgoboyyrrgoog'
        expectedResult['status'] = 'ok'
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_solve_110_ShouldRotateValidNominalCube_D(self):
        inputDict = {}
        inputDict['cube'] = 'rrbbbbgggryyyyoroyogryggobbwwwwwwwwwgrboorbbyoyyrrgoog'
        inputDict['rotate'] = 'd'
        inputDict['op'] = 'solve'
           
        expectedResult = {}
        expectedResult['cube'] = 'rrbbbbwwwryyyyogggogryggroywwwwwwobbgrboorbbyorooryggy'
        expectedResult['status'] = 'ok'
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
        
    def test_solve_120_ShouldRotateValidNominalCube_d(self):
        inputDict = {}
        inputDict['cube'] = 'rrbbbbgggryyyyoroyogryggobbwwwwwwwwwgrboorbbyoyyrrgoog'
        inputDict['rotate'] = 'd'
        inputDict['op'] = 'solve'
           
        expectedResult = {}
        expectedResult['cube'] = 'rrbbbbroyryyyyoobbogryggwwwwwwwwwggggrboorbbyyggyrooro'
        expectedResult['status'] = 'ok'
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
# analysis of solve
#
#    inputs:
#        parms: dictionary input that is validated. Do not have to validate i
#        parms['op'] have to validate the keys ['op'] string, "solve", mandatory, arrives validated
#        parms['cube'] string; len = 54 chars [azAZ09], 9 occurences of each character, 6 distincs characters, 
#               middle will be one of the six; mandatory; arrives unvalidated
#        parms['rotate'] string; len >=0, [FfRrBbLlUuDd]; optional, defaulting to F if missing; arrives unvalidated

#    outputs:
#        side-effects: no state change; no external effects. No print statements
#        returns: dictionary
#        nominal: happy path
#            dictionary ['cube']: string len= 54
#            dictionary['status']: 'ok'

#        abnormal or sad path:
#            dictionary['status']: 'error: danger_error'
#        confidence level: written unittests to the level of boundary level analysis

#        happy path:
#            test 010: nominal valid cube with F rotation
#            test 020: nominal valid cube with f rotation
#            test 030: nominal valid cube with missing rotation
#            test 040: nominal valie cube with "" null string as rotation
#            test 050: boundary analysis for each of the rotations

#        sad path:
#            test 910: missing cube
#            test 920: valid cube, invalid rotation
#            test 930: have to test parms['cube'] and parms['rotate'] as they arrive unvalidated




    def testName(self):
        pass


