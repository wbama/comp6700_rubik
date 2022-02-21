import unittest
import rubik.solve as solve



class SolveTest(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass
    
    def test_solve_010_ShouldRotateValidNominalCubeF(self):
        inputDict = {}
        inputDict['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        inputDict['rotate'] = 'F'
        inputDict['op'] = 'solve'
        
        expectedResult = {}
        expectedResult['cube'] = 
        
        
        
        
    def test010_ShouldTestNominalNEvenlyDivisibleBy3(self):
        n = 3
        expectedResult = "fizz"
        actualResult = fb.fizzbuzz(n)
        self.assertEqual(expectedResult, actualResult)
    
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


