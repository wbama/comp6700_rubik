import unittest
from rubik.solveRotations import createCubeListFromInputParms
from rubik.solveRotations import rotateCubeToLeft, rotateCubeToRight
from rubik.solveRotations import rotateCubeDown
from rubik.solveRotations import rotateCubeUp
from rubik.solveRotations import rotateCubeClock
from rubik.solveRotations import putWhiteLeafPosition0_5
from rubik.solveDaisy import solveDaisy


class SolveDaisyTest(unittest.TestCase):   
            
  
        def test_010_WhiteLeafPos0_5NotMove(self):
            inputDict = {}
            #here yellow is in front
            inputDict['cube'] = 'byorywoogyobrgywoyrbrrwggbwbwowbggywwryboyybgbwrgrgoor'
 
    
            expectedResult = {}
            expectedResult['cube'] = 'byorywoogyobrgywoyrbrrwggbwbwowbggywwryboyybgbwrgrgoor'
            
            lst_cube = createCubeListFromInputParms(inputDict)  
            newCube = putWhiteLeafPosition0_5(lst_cube)
            
            str1 = "".join(newCube[0])
            str2 = "".join(newCube[1])
            str3 = "".join(newCube[2])
            str4 = "".join(newCube[3])
            str5 = "".join(newCube[4])
            str6 = "".join(newCube[5]) 

            str_cube = str1+str2+str3+str4+str5+str6  
                        
            self.assertEqual(expectedResult.get('cube'), str_cube)  
            
        def test_020_WhiteLeafPos4_5To0_5(self):
            inputDict = {}
            inputDict['cube'] = 'rwgrorryroorgbybgwgwbrrbggwybwwgboyworyoywbgygoybwyboo'
 
    
            expectedResult = {}
            expectedResult['cube'] = 'rwyrowryyrywobgogbowbyrbygwybwwgboyworgoyrbgggogbwrbor'
            
            lst_cube = createCubeListFromInputParms(inputDict)  
            newCube = putWhiteLeafPosition0_5(lst_cube)
            
            str1 = "".join(newCube[0])
            str2 = "".join(newCube[1])
            str3 = "".join(newCube[2])
            str4 = "".join(newCube[3])
            str5 = "".join(newCube[4])
            str6 = "".join(newCube[5]) 

            str_cube = str1+str2+str3+str4+str5+str6  
                        
            self.assertEqual(expectedResult.get('cube'), str_cube)  
            
        def test_030_WhiteLeafPos2_3To0_5(self):
            inputDict = {}
            inputDict['cube'] = 'rwgrorrygwgbybgroorwbrrbggwybwwgboyworyoyybgogoybwwboy'
 
    
            expectedResult = {}
            expectedResult['cube'] = 'rwyrowryyrywobgogbowbyrbygwybwwgboyworgoyrbgggogbwrbor'
            
            lst_cube = createCubeListFromInputParms(inputDict)  
            newCube = putWhiteLeafPosition0_5(lst_cube)
            
            str1 = "".join(newCube[0])
            str2 = "".join(newCube[1])
            str3 = "".join(newCube[2])
            str4 = "".join(newCube[3])
            str5 = "".join(newCube[4])
            str6 = "".join(newCube[5]) 

            str_cube = str1+str2+str3+str4+str5+str6  
                        
            self.assertEqual(expectedResult.get('cube'), str_cube) 
            
        def test_040_WhiteLeafPos1_3To0_5(self):
            inputDict = {}
            inputDict['cube'] = 'orwyygyowbgowoyrbrbbygwgbrbrywororyggwyrbrgboowgbgowwy'    
            expectedResult = {}
            expectedResult['cube'] = 'yyroywyobwbygogwyorywrwgyrboroorwrybgrgbbwgogrbobggwwb'            
            lst_cube = createCubeListFromInputParms(inputDict)  
            newCube = putWhiteLeafPosition0_5(lst_cube)            
            str1 = "".join(newCube[0])
            str2 = "".join(newCube[1])
            str3 = "".join(newCube[2])
            str4 = "".join(newCube[3])
            str5 = "".join(newCube[4])
            str6 = "".join(newCube[5]) 
            str_cube = str1+str2+str3+str4+str5+str6                          
            self.assertEqual(expectedResult.get('cube'), str_cube) 
            
        def test_050_WhiteLeafPos1_1To0_5(self):
            inputDict = {}
            inputDict['cube'] = 'bgbbyobbowwgyoryrrwwggwwygyryybrrogowrobbororwobygygwg'    
            expectedResult = {}
            expectedResult['cube'] = 'bgbbywbbgywgoororrryrgwwygyboybrrogowbwybrroowowygygwg'            
            lst_cube = createCubeListFromInputParms(inputDict)  
            newCube = putWhiteLeafPosition0_5(lst_cube)            
            str1 = "".join(newCube[0])
            str2 = "".join(newCube[1])
            str3 = "".join(newCube[2])
            str4 = "".join(newCube[3])
            str5 = "".join(newCube[4])
            str6 = "".join(newCube[5]) 
            str_cube = str1+str2+str3+str4+str5+str6                          
            self.assertEqual(expectedResult.get('cube'), str_cube) 
            

            
        


    
