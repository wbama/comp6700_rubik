"""
    Created on 02/05/2022
    @author: Waldo du Toit
    unittests for solving the final solve solution
    03/17 - Added test 943. Fx did not give error on microservice. 
    
"""

import unittest
import rubik.solve as solve
#from rubik.solveRotations import createCubeListFromInputParms


class SolveTest(unittest.TestCase):  
 
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
        
        
    def test_020_ShouldRotateValidNominalCube_f(self):
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
    
        
    def test_030_ShouldRotateValidNominalCube_R(self):
        inputDict = {}
        inputDict['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        inputDict['rotate'] = 'R'
        inputDict['op'] = 'solve'           

        expectedResult = {}
        expectedResult['cube'] = 'ggyggyggyrrrrrrrrrwbbwbbwbbooooooooowwgwwgwwgyybyybyyb'
        expectedResult['status'] = 'ok'
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))

        
    def test_040_ShouldRotateValidNominalCube_r(self):
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
        
    def test_050_ShouldRotateValidNominalCube_B(self):
        inputDict = {}
        inputDict['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        inputDict['rotate'] = 'B'
        inputDict['op'] = 'solve'           

        expectedResult = {}
        expectedResult['cube'] = 'gggggggggrryrryrrybbbbbbbbbwoowoowoorrrwwwwwwyyyyyyooo'
        expectedResult['status'] = 'ok'
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))

        
    def test_060_ShouldRotateValidNominalCube_b(self):
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
        
    def test_070_ShouldRotateValidNominalCube_L(self):
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
             
        
    def test_080_ShouldRotateValidNominalCube_l(self):
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
        
    def test_090_ShouldRotateValidNominalCube_U(self):
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

        
    def test_100_ShouldRotateValidNominalCube_u(self):
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

        
    def test_110_ShouldRotateValidNominalCube_D(self):
        inputDict = {}
        inputDict['cube'] = 'rybbbrggryrybyoyyybgryggobbwwwwwwwwwgrrooybgooogrrboog'
        inputDict['rotate'] = 'D'
        inputDict['op'] = 'solve'

        expectedResult = {}
        expectedResult['cube'] = 'rybbbrwwwyrybyoggrbgryggyyywwwwwwobbgrrooybgooroorogbg'    
        expectedResult['status'] = 'ok'
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))

        
    def test_120_ShouldRotateValidNominalCube_d(self):
        inputDict = {}
        inputDict['cube'] = 'rybbbrggryrybyoyyybgryggobbwwwwwwwwwgrrooybgooogrrboog'
        inputDict['rotate'] = 'd'
        inputDict['op'] = 'solve'

        expectedResult = {}
        expectedResult['cube'] = 'rybbbryyyyrybyoobbbgryggwwwwwwwwwggrgrrooybgogbgorooro'
        expectedResult['status'] = 'ok'
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))      
      
        
       
    def test_130_ShouldRotateValidNominalCube_FLFFBUUdLfDrFLdRRdLLdRRu(self):

        inputDict = {}
        inputDict['cube'] = 'rbbgbobbgrgwyrywyobggrggywgoryyowowwyoobyrgwyrorrwbwob'
        inputDict['rotate'] = 'FLFFBUUdLfDrFLdRRdLLdRRu'
        inputDict['op'] = 'solve'           

        expectedResult = {}
        expectedResult['cube'] = 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        expectedResult['status'] = 'ok'
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))       


    def test_140_ShouldNoSolutionSolvedCube(self):

        inputDict = {}
        inputDict['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        inputDict['rotate'] = ''
        inputDict['op'] = 'solve'           

        expectedResult = {}
        expectedResult['cube'] = None
        expectedResult['solution'] = ""
        expectedResult['status'] = 'ok'
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('cube'), actualResult.get('cube'))
        self.assertEqual(expectedResult.get('status'), actualResult.get('status')) 
        self.assertEqual(expectedResult.get('solution'), actualResult.get('solution'))  
    
    def test_150_SolveLowerLayer(self):   
       
        inputDict = {}
        inputDict['cube'] = 'gwgbbobgrowbwrbwwgygrrgyrobwyoroyworgrooygwbyyybbwrogy'        
        inputDict['rotate'] = (solve._solve(inputDict)).get("solution")
        
        var_w = inputDict['cube'][-5]
        expectedResult_col = var_w 

        actualResult =  solve._solve(inputDict)
        self.assertEqual(expectedResult_col, (actualResult.get('cube'))[45])
        self.assertEqual(expectedResult_col, (actualResult.get('cube'))[46])
        self.assertEqual(expectedResult_col, (actualResult.get('cube'))[47])
        self.assertEqual(expectedResult_col, (actualResult.get('cube'))[48])
        self.assertEqual(expectedResult_col, (actualResult.get('cube'))[49])
        self.assertEqual(expectedResult_col, (actualResult.get('cube'))[50])
        self.assertEqual(expectedResult_col, (actualResult.get('cube'))[51])
        self.assertEqual(expectedResult_col, (actualResult.get('cube'))[52])
        self.assertEqual(expectedResult_col, (actualResult.get('cube'))[53])

        # #sides should also be solved
        self.assertEqual( (actualResult.get('cube'))[6],  (actualResult.get('cube'))[7],  (actualResult.get('cube'))[8])
        self.assertEqual( (actualResult.get('cube'))[15],  (actualResult.get('cube'))[16],  (actualResult.get('cube'))[17])
        self.assertEqual( (actualResult.get('cube'))[24],  (actualResult.get('cube'))[25],  (actualResult.get('cube'))[26])
        self.assertEqual( (actualResult.get('cube'))[33],  (actualResult.get('cube'))[34],  (actualResult.get('cube'))[35])
        
    def test_160_SolveLowerLayer(self):   
       
        inputDict = {}
        inputDict['cube'] = 'ooogboyyrgrbbrgwwroyrygbgbgygywowyrrbowoygbwwgbbywrorw'        
        inputDict['rotate'] = (solve._solve(inputDict)).get("solution")
        
        var_w = inputDict['cube'][-5]
        expectedResult_col = var_w 

        actualResult =  solve._solve(inputDict)
        self.assertEqual(expectedResult_col, (actualResult.get('cube'))[45])
        self.assertEqual(expectedResult_col, (actualResult.get('cube'))[46])
        self.assertEqual(expectedResult_col, (actualResult.get('cube'))[47])
        self.assertEqual(expectedResult_col, (actualResult.get('cube'))[48])
        self.assertEqual(expectedResult_col, (actualResult.get('cube'))[49])
        self.assertEqual(expectedResult_col, (actualResult.get('cube'))[50])
        self.assertEqual(expectedResult_col, (actualResult.get('cube'))[51])
        self.assertEqual(expectedResult_col, (actualResult.get('cube'))[52])
        self.assertEqual(expectedResult_col, (actualResult.get('cube'))[53])
        # #sides should also be solved
        self.assertEqual( (actualResult.get('cube'))[6],  (actualResult.get('cube'))[7],  (actualResult.get('cube'))[8])
        self.assertEqual( (actualResult.get('cube'))[15],  (actualResult.get('cube'))[16],  (actualResult.get('cube'))[17])
        self.assertEqual( (actualResult.get('cube'))[24],  (actualResult.get('cube'))[25],  (actualResult.get('cube'))[26])
        self.assertEqual( (actualResult.get('cube'))[33],  (actualResult.get('cube'))[34],  (actualResult.get('cube'))[35])
        
    def test_170_SolveMiddleLayer(self):   
     
        inputDict = {}
        inputDict['cube'] = 'L52255e5eLL2Le22ekkekek5wkewk52LkwL2LkLL22we55wkwww5we'        
        inputDict['rotate'] = (solve._solve(inputDict)).get("solution")
        
        var_w = inputDict['cube'][-5]
        expectedResult_col = var_w                    

        actualResult =  solve._solve(inputDict)
        self.assertEqual(expectedResult_col, (actualResult.get('cube'))[45])
        self.assertEqual(expectedResult_col, (actualResult.get('cube'))[46])
        self.assertEqual(expectedResult_col, (actualResult.get('cube'))[47])
        self.assertEqual(expectedResult_col, (actualResult.get('cube'))[48])
        self.assertEqual(expectedResult_col, (actualResult.get('cube'))[49])
        self.assertEqual(expectedResult_col, (actualResult.get('cube'))[50])
        self.assertEqual(expectedResult_col, (actualResult.get('cube'))[51])
        self.assertEqual(expectedResult_col, (actualResult.get('cube'))[52])
        self.assertEqual(expectedResult_col, (actualResult.get('cube'))[53])        
        
        # #sides should also be solved
        self.assertEqual( (actualResult.get('cube'))[3],  (actualResult.get('cube'))[4],  (actualResult.get('cube'))[5])
        self.assertEqual( (actualResult.get('cube'))[6],  (actualResult.get('cube'))[7],  (actualResult.get('cube'))[8])
        
        self.assertEqual( (actualResult.get('cube'))[12],  (actualResult.get('cube'))[13],  (actualResult.get('cube'))[14])
        self.assertEqual( (actualResult.get('cube'))[15],  (actualResult.get('cube'))[16],  (actualResult.get('cube'))[17])
        
        self.assertEqual( (actualResult.get('cube'))[21],  (actualResult.get('cube'))[22],  (actualResult.get('cube'))[23])
        self.assertEqual( (actualResult.get('cube'))[24],  (actualResult.get('cube'))[25],  (actualResult.get('cube'))[26])
        
        self.assertEqual( (actualResult.get('cube'))[30],  (actualResult.get('cube'))[31],  (actualResult.get('cube'))[32])   
        self.assertEqual( (actualResult.get('cube'))[33],  (actualResult.get('cube'))[34],  (actualResult.get('cube'))[35])

    def test_190_SolveMiddleLayer(self):   
     
        inputDict = {}
        inputDict['cube'] = 'fqxiAfAAiiiAqqffqAfAfiifqiqqfqAxxixxixxxfqAAcccxcccccc'        
        inputDict['rotate'] = (solve._solve(inputDict)).get("solution")
        
        var_w = inputDict['cube'][-5]
        expectedResult_col = var_w                    

        actualResult =  solve._solve(inputDict)
        self.assertEqual(expectedResult_col, (actualResult.get('cube'))[45])
        self.assertEqual(expectedResult_col, (actualResult.get('cube'))[46])
        self.assertEqual(expectedResult_col, (actualResult.get('cube'))[47])
        self.assertEqual(expectedResult_col, (actualResult.get('cube'))[48])
        self.assertEqual(expectedResult_col, (actualResult.get('cube'))[49])
        self.assertEqual(expectedResult_col, (actualResult.get('cube'))[50])
        self.assertEqual(expectedResult_col, (actualResult.get('cube'))[51])
        self.assertEqual(expectedResult_col, (actualResult.get('cube'))[52])
        self.assertEqual(expectedResult_col, (actualResult.get('cube'))[53])        
        
        # #sides should also be solved
        self.assertEqual( (actualResult.get('cube'))[3],  (actualResult.get('cube'))[4],  (actualResult.get('cube'))[5])
        self.assertEqual( (actualResult.get('cube'))[6],  (actualResult.get('cube'))[7],  (actualResult.get('cube'))[8])
        
        self.assertEqual( (actualResult.get('cube'))[12],  (actualResult.get('cube'))[13],  (actualResult.get('cube'))[14])
        self.assertEqual( (actualResult.get('cube'))[15],  (actualResult.get('cube'))[16],  (actualResult.get('cube'))[17])
        
        self.assertEqual( (actualResult.get('cube'))[21],  (actualResult.get('cube'))[22],  (actualResult.get('cube'))[23])
        self.assertEqual( (actualResult.get('cube'))[24],  (actualResult.get('cube'))[25],  (actualResult.get('cube'))[26])
        
        self.assertEqual( (actualResult.get('cube'))[30],  (actualResult.get('cube'))[31],  (actualResult.get('cube'))[32])   
        self.assertEqual( (actualResult.get('cube'))[33],  (actualResult.get('cube'))[34],  (actualResult.get('cube'))[35])


# Sad path tests

    def test_910_IncorrectCubeString(self):
    
        inputDict = {}
        inputDict['cube'] = '123456789'
        inputDict['op'] = 'solve'  
        inputDict['rotate'] = 'f'         
    
        expectedResult = {}
        expectedResult['status'] = 'error: cube string has to have 54 elements'
    
        actualResult = solve._solve(inputDict) #calling _solve and passing inputDict
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
    def test_920_CubeNotString(self):
    
        inputDict = {}
        inputDict['cube'] = 42
        inputDict['op'] = 'solve' 
        inputDict['rotate'] = ''            
    
        expectedResult = {}
        expectedResult['status'] = 'error: cube not a string'
    
        actualResult = solve._solve(inputDict) #calling _solve and passing inputDict
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
    
    def test_930_MissingCube(self):
        inputDict = {}
        inputDict['op'] = 'solve' 
        inputDict['rotate'] = ''          
    
        expectedResult = {}
        expectedResult['status'] = 'error: no cube found'
    
        actualResult = solve._solve(inputDict) #calling _solve and passing inputDict
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
    def test_940_InvalidRotation(self):
        inputDict = {}
        inputDict['cube'] = 'gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy'
        inputDict['rotate'] = 'w'
        inputDict['op'] = 'solve'
    
    
        expectedResult = {}
        expectedResult['status'] = 'error: optional rotate should be in [FfRrBbLlUuDd]'
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
    def test_941_IncorrectParmsRotateString(self):
        inputDict = {}
        inputDict['cube'] = 'rybbbrggryrybyoyyybgryggobbwwwwwwwwwgrrooybgooogrrboog'
        inputDict['rotate'] = '  '
        inputDict['op'] = 'solve'
    
        expectedResult = {}
        expectedResult['status'] = 'error: optional rotate should be in [FfRrBbLlUuDd]'
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status')) 
    
    def test_942_IncorrectParmsRotateString(self):
        inputDict = {}
        inputDict['cube'] = 'rybbbrggryrybyoyyybgryggobbwwwwwwwwwgrrooybgooogrrboog'
        inputDict['rotate'] = 'Ff Bb'
        inputDict['op'] = 'solve'
    
        expectedResult = {}
        expectedResult['status'] = 'error: optional rotate should be in [FfRrBbLlUuDd]'
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))  
    
    def test_943_IncorrectParmsRotateString(self):
        inputDict = {}
        inputDict['cube'] = 'rybbbrggryrybyoyyybgryggobbwwwwwwwwwgrrooybgooogrrboog'
        inputDict['rotate'] = 'Fx'
        inputDict['op'] = 'solve'
    
        expectedResult = {}
        expectedResult['status'] = 'error: optional rotate should be in [FfRrBbLlUuDd]'
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))        
    
    
    def test_950_CubeMoreThan54Elements(self):
        inputDict = {}
        inputDict['cube'] = 'rybbbrggryrybyoyyybgryggobbwwwwwwwwwgrrooybgooogrrboogo'
        inputDict['op'] = 'solve'
        inputDict['rotate'] = 'F'
    
        expectedResult = {}
        expectedResult['status'] = 'error: cube string has to have 54 elements'
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
    def test_960_CubeFewerThan54Elements(self):
        inputDict = {}
        inputDict['cube'] = 'rybbbrggryrybyoyyybgryggobbwwwwwwwwwgrrooybgooogrrboo'
        inputDict['op'] = 'solve'
        inputDict['rotate'] = 'F'
    
        expectedResult = {}
        expectedResult['status'] = 'error: cube string has to have 54 elements'
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
    def test_970_CubeNotSixColors(self):
        inputDict = {}
        inputDict['cube'] = 'bbbbbbbbbbbbbbbbbbgggggggggoooooooooyyyyyyyyywwwwwwwww'
        inputDict['op'] = 'solve'
        inputDict['rotate'] = 'F'
    
        expectedResult = {}
        expectedResult['status'] = 'error: there should be 6 colors'
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
    def test_980_CubeNineOccurencesOfSixColors(self):
        inputDict = {}
        inputDict['cube'] = 'bbbbbbbbbbrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        inputDict['op'] = 'solve'
        inputDict['rotate'] = 'F'
    
        expectedResult = {}
        expectedResult['status'] = 'error: one of the colors is more or less than 9 occurrences'
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
    def test_990_MiddleFaceDifferentColor(self):
        inputDict = {}
        inputDict['cube'] = 'bbbbrbbbbrrrrrrrbrgggggggggoooooooooyyyyyyyyywwwwwwwww'
        inputDict['op'] = 'solve'
        inputDict['rotate'] = 'f'
    
        expectedResult = {}
        expectedResult['status'] = 'error: two middle faces are the same colors'
        actualResult = solve._solve(inputDict)
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
    def test_9100_OnlyLettersAndNumbersInCubeString(self):
    
        inputDict = {}
        inputDict['cube'] = 'rrbbbbgggr????oro?ogr?ggobbwwwwwwwwwgrboorbb?o??rrgoog'
        inputDict['rotate'] = 'f'
        inputDict['op'] = 'solve'           
    
        expectedResult = {}
        expectedResult['status'] = 'error: only alphanumeric characters in the cube string'
    
        actualResult = solve._solve(inputDict) #calling _solve and passing inputDict
        self.assertEqual(expectedResult.get('status'), actualResult.get('status'))
    
   
       
# analysis of solve
#
#    inputs:
#        parms: dictionary input that is validated. Do not have to validate 
#        parms['op'] have to validate the keys ['op'] string, "solve", mandatory, arrives validated
#        parms['cube'] string; len = 54 chars [azAZ09], 9 occurences of each character, 6 distinct characters, 
#               middle will be one of the six; mandatory; arrives unvalidated
#        parms['rotate'] string; len >=0, [FfRrBbLlUuDd]; optional, defaulting to F if missing; arrives unvalidated

#    outputs:
#        side-effects: no state change; no external effects. No print statements
#        returns: dictionary
#        nominal: happy path
#            dictionary ['cube']: string len= 54
#            dictionary['status']: 'ok'

#        abnormal or sad path:
#            dictionary['status']: 'error: xxxx'
#        confidence level: written unittests to the level of boundary level analysis

#        happy path:
#            test 010: nominal valid cube with F rotation
#            test 020: nominal valid cube with f rotation
#            test 030: nominal valid cube with missing rotation
#            test 040: nominal valid cube with "" null string as rotation
#            test 050: boundary analysis for each of the rotations

#        sad path:
#            test 910: missing cube
#            test 920: valid cube, invalid rotation
#            test 930: have to test parms['cube'] and parms['rotate'] as they arrive unvalidated




