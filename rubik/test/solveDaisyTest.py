import unittest
from rubik.solveWhiteCross import solveWhiteCross
from rubik.solveRotations import createCubeListFromInputParms
from rubik.solveRotations import rotateCubeToLeft, rotateCubeToRight
from rubik.solveRotations import rotateCubeDown
from rubik.solveRotations import rotateCubeUp
from rubik.solveRotations import rotateCubeClock
from rubik.solveRotations import putWhiteLeafPosition0_5
from rubik.solveDaisy import solveDaisy


class SolveDaisyTest(unittest.TestCase):
    
        def test_010_RotateYellowCenterToFront(self):
        
            inputDict = {}
            inputDict['cube'] = 'ygbwwwrygyywogoorwbbbbygrgyryoobbgybyroorggwowbwrowrrg'    
            expectedResult = 'y'           
            actualResult = solveDaisy(inputDict)
            self.assertEqual(expectedResult, actualResult.get('cube')[4])
            
            
        def test_020_RotateWholeCubeClockwise(self):
            inputDict = {}
            inputDict['cube'] = 'bgbgyrywgogyygywooggrbwywrobwyobrywrwworoorywgbrorbbbg'
            inputDict['op'] = 'solve'  
            
            expectedResult = {} 
            expectedResult['cube'] = 'ygbwyggrbrrwyowwooryogwrgbwbogbrbgbryobwbwrrywyooggoyy'
            
            lst_cube = createCubeListFromInputParms(inputDict)           
            rotatedCube = rotateCubeClock(lst_cube)
            
            str1 = "".join(rotatedCube[0])
            str2 = "".join(rotatedCube[1])
            str3 = "".join(rotatedCube[2])
            str4 = "".join(rotatedCube[3])
            str5 = "".join(rotatedCube[4])
            str6 = "".join(rotatedCube[5]) 

            str_cube = str1+str2+str3+str4+str5+str6              
            self.assertEqual(expectedResult.get('cube'), str_cube)           

            
        def test_040_TestRotateCubeToRight(self):
            inputDict = {}
            inputDict['cube'] = 'rgbwywgooybwrgybbyggbrwbgygrowybbyowywrgoobrooywwrrogr'
 
    
            expectedResult = {}
            expectedResult['cube'] = 'rowybbyowrgbwywgooybwrgybbyggbrwbgygrooworygbowogryrrw'
            
            lst_cube = createCubeListFromInputParms(inputDict)  
            rotatedCube = rotateCubeToRight(lst_cube)
            
            str1 = "".join(rotatedCube[0])
            str2 = "".join(rotatedCube[1])
            str3 = "".join(rotatedCube[2])
            str4 = "".join(rotatedCube[3])
            str5 = "".join(rotatedCube[4])
            str6 = "".join(rotatedCube[5]) 

            str_cube = str1+str2+str3+str4+str5+str6  
                        
            self.assertEqual(expectedResult.get('cube'), str_cube)  
            
        def test_050_TestRotateCubeToLeft(self):
            inputDict = {}
            inputDict['cube'] = 'rgbwywgooybwrgybbyggbrwbgygrowybbyowywrgoobrooywwrrogr'
 
    
            expectedResult = {}
            expectedResult['cube'] = 'ybwrgybbyggbrwbgygrowybbyowrgbwywgoobgyrowoorwrryrgowo'
            
            lst_cube = createCubeListFromInputParms(inputDict)  
            rotatedCube = rotateCubeToLeft(lst_cube)
            
            str1 = "".join(rotatedCube[0])
            str2 = "".join(rotatedCube[1])
            str3 = "".join(rotatedCube[2])
            str4 = "".join(rotatedCube[3])
            str5 = "".join(rotatedCube[4])
            str6 = "".join(rotatedCube[5]) 

            str_cube = str1+str2+str3+str4+str5+str6  
                        
            self.assertEqual(expectedResult.get('cube'), str_cube) 
            
        def test_060_TestRotateCubeUp(self):
            inputDict = {}
            inputDict['cube'] = 'byygbowygbygbobrgowwywgoybogbrwrobggororwrworrgywyrwyb'
 
    
            expectedResult = {}
            expectedResult['cube'] = 'rgywyrwybrbbgoyobgrowrwrororogbrggwbbyygbowygobyogwyww'
            
            lst_cube = createCubeListFromInputParms(inputDict)  
            rotatedCube = rotateCubeUp(lst_cube)
            
            str1 = "".join(rotatedCube[0])
            str2 = "".join(rotatedCube[1])
            str3 = "".join(rotatedCube[2])
            str4 = "".join(rotatedCube[3])
            str5 = "".join(rotatedCube[4])
            str6 = "".join(rotatedCube[5]) 

            str_cube = str1+str2+str3+str4+str5+str6  
                        
            self.assertEqual(expectedResult.get('cube'), str_cube) 
            
        def test_070_TestRotateCubeDown(self):
            inputDict = {}
            inputDict['cube'] = 'rgywyrwybrbbgoyobgrowrwrororogbrggwbbyygbowygobyogwyww'
 
    
            expectedResult = {}
            expectedResult['cube'] = 'byygbowygbygbobrgowwywgoybogbrwrobggororwrworrgywyrwyb'
            
            lst_cube = createCubeListFromInputParms(inputDict)  
            rotatedCube = rotateCubeDown(lst_cube)
            
            str1 = "".join(rotatedCube[0])
            str2 = "".join(rotatedCube[1])
            str3 = "".join(rotatedCube[2])
            str4 = "".join(rotatedCube[3])
            str5 = "".join(rotatedCube[4])
            str6 = "".join(rotatedCube[5]) 

            str_cube = str1+str2+str3+str4+str5+str6  
                        
            self.assertEqual(expectedResult.get('cube'), str_cube) 
            
        def test_060_WhiteLeafPos0_5NotMove(self):
            inputDict = {}
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
            
        def test_060_WhiteLeafPos4_5To0_5(self):
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
            
        def test_060_WhiteLeafPos2_3To0_5(self):
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
            
        def test_060_WhiteLeafPos1_3To0_5(self):
            inputDict = {}
            inputDict['cube'] = 'bgwbyrbbygrywoyobborrowgroogwywrrwgoygbbbyrorwogygygww'    
            expectedResult = {}
            expectedResult['cube'] = 'bgrbywbbgbrrrorwyygwyywgboogyywrrwgoobybbgrowworygogwo'            
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
            
        def test_060_WhiteLeafPos1_1To0_5(self):
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
            

            
        


    
