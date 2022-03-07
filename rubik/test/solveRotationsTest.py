import unittest
from rubik.solveRotations import createCubeListFromInputParms
from rubik.solveRotations import rotateCubeToLeft, rotateCubeToRight
from rubik.solveRotations import rotateCubeUp, rotateCubeDown
from rubik.solveRotations import rotateCubeClock
from rubik.solveRotations import rotateSide_R, rotateSide_r
from rubik.solveRotations import rotateSide_B, rotateSide_b
from rubik.solveRotations import rotateSide_L, rotateSide_l
from rubik.solveRotations import rotateSide_U, rotateSide_u
from rubik.solveRotations import rotateSide_D, rotateSide_d

class SolveDaisyTest(unittest.TestCase):
            
        def test_010_RotateWholeCubeClockwise(self):
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

            
        def test_020_TestRotateCubeToRight(self):
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
            
        def test_030_TestRotateCubeToLeft(self):
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
            
        def test_040_TestRotateCubeUp(self):
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
            
        def test_050_TestRotateCubeDown(self):
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
            
        def test_060_TestRotateCube_R(self):
            inputDict = {}
            inputDict['cube'] = 'wwoywrgrbbbrbbrygwbwggywgbrooorgoybrygwgoyboywyrwrygoo'
 
    
            expectedResult = {}
            expectedResult['cube'] = 'wwrywygroybbgbbwrrywgyywwbrooorgoybrygogorbobwygwrggob'
            
            lst_cube = createCubeListFromInputParms(inputDict)  
            rotatedCube = rotateSide_R(lst_cube)
            
            str1 = "".join(rotatedCube[0])
            str2 = "".join(rotatedCube[1])
            str3 = "".join(rotatedCube[2])
            str4 = "".join(rotatedCube[3])
            str5 = "".join(rotatedCube[4])
            str6 = "".join(rotatedCube[5]) 

            str_cube = str1+str2+str3+str4+str5+str6  
                        
            self.assertEqual(expectedResult.get('cube'), str_cube) 
            
            
        def test_070_TestRotateCube_r(self):
            inputDict = {}
            inputDict['cube'] = 'wwrywygroybbgbbwrrywgyywwbrooorgoybrygogorbobwygwrggob'
 
    
            expectedResult = {}
            expectedResult['cube'] = 'wwoywrgrbbbrbbrygwbwggywgbrooorgoybrygwgoyboywyrwrygoo'
            
            lst_cube = createCubeListFromInputParms(inputDict)  
            rotatedCube = rotateSide_r(lst_cube)
            
            str1 = "".join(rotatedCube[0])
            str2 = "".join(rotatedCube[1])
            str3 = "".join(rotatedCube[2])
            str4 = "".join(rotatedCube[3])
            str5 = "".join(rotatedCube[4])
            str6 = "".join(rotatedCube[5]) 

            str_cube = str1+str2+str3+str4+str5+str6  
                        
            self.assertEqual(expectedResult.get('cube'), str_cube) 
            
        def test_080_TestRotateCube_B(self):
            inputDict = {}
            inputDict['cube'] = 'gwrwybbgggwworyoyrgywrwwbrobgyoogyywoorogboryrrwbbgbby'
 
    
            expectedResult = {}
            expectedResult['cube'] = 'gwrwybbgggwyorboybbrgrwyowwrgyoogoywwyrogboryrrwbbgboy'
            
            lst_cube = createCubeListFromInputParms(inputDict)  
            rotatedCube = rotateSide_B(lst_cube)
            
            str1 = "".join(rotatedCube[0])
            str2 = "".join(rotatedCube[1])
            str3 = "".join(rotatedCube[2])
            str4 = "".join(rotatedCube[3])
            str5 = "".join(rotatedCube[4])
            str6 = "".join(rotatedCube[5]) 

            str_cube = str1+str2+str3+str4+str5+str6  
                        
            self.assertEqual(expectedResult.get('cube'), str_cube) 
            
        def test_090_TestRotateCube_b(self):
            inputDict = {}
            inputDict['cube'] = 'gwrwybbgggwyorboybbrgrwyowwrgyoogoywwyrogboryrrwbbgboy'
 
    
            expectedResult = {}
            expectedResult['cube'] = 'gwrwybbgggwworyoyrgywrwwbrobgyoogyywoorogboryrrwbbgbby'
            
            lst_cube = createCubeListFromInputParms(inputDict)  
            rotatedCube = rotateSide_b(lst_cube)
            
            str1 = "".join(rotatedCube[0])
            str2 = "".join(rotatedCube[1])
            str3 = "".join(rotatedCube[2])
            str4 = "".join(rotatedCube[3])
            str5 = "".join(rotatedCube[4])
            str6 = "".join(rotatedCube[5]) 

            str_cube = str1+str2+str3+str4+str5+str6  
                        
            self.assertEqual(expectedResult.get('cube'), str_cube) 
            
        def test_100_TestRotateCube_L(self):
            inputDict = {}
            inputDict['cube'] = 'rbrwwgbwbwywoggrbborbyygwyyrbyrbooryybgwrrgogogwwoygoo'
 
    
            expectedResult = {}
            expectedResult['cube'] = 'ybrwwggwbwywoggrbborgyywwyoorrrbbyoyybggrrbogrgwwoyboo'
            
            lst_cube = createCubeListFromInputParms(inputDict)  
            rotatedCube = rotateSide_L(lst_cube)
            
            str1 = "".join(rotatedCube[0])
            str2 = "".join(rotatedCube[1])
            str3 = "".join(rotatedCube[2])
            str4 = "".join(rotatedCube[3])
            str5 = "".join(rotatedCube[4])
            str6 = "".join(rotatedCube[5]) 

            str_cube = str1+str2+str3+str4+str5+str6  
                        
            self.assertEqual(expectedResult.get('cube'), str_cube) 
            
        def test_110_TestRotateCube_l(self):
            inputDict = {}
            inputDict['cube'] = 'ybrwwggwbwywoggrbborgyywwyoorrrbbyoyybggrrbogrgwwoyboo'
 
    
            expectedResult = {}
            expectedResult['cube'] = 'rbrwwgbwbwywoggrbborbyygwyyrbyrbooryybgwrrgogogwwoygoo'
            
            lst_cube = createCubeListFromInputParms(inputDict)  
            rotatedCube = rotateSide_l(lst_cube)
            
            str1 = "".join(rotatedCube[0])
            str2 = "".join(rotatedCube[1])
            str3 = "".join(rotatedCube[2])
            str4 = "".join(rotatedCube[3])
            str5 = "".join(rotatedCube[4])
            str6 = "".join(rotatedCube[5]) 

            str_cube = str1+str2+str3+str4+str5+str6  
                        
            self.assertEqual(expectedResult.get('cube'), str_cube) 
            
        def test_110_TestRotateCube_U(self):
            inputDict = {}
            inputDict['cube'] = 'rbrwwgbwbwywoggrbborbyygwyyrbyrbooryybgwrrgogogwwoygoo'
 
    
            expectedResult = {}
            expectedResult['cube'] = 'wywwwgbwborboggrbbrbyyygwyyrbrrboorygwyorbgrgogwwoygoo'
            
            lst_cube = createCubeListFromInputParms(inputDict)  
            rotatedCube = rotateSide_U(lst_cube)
            
            str1 = "".join(rotatedCube[0])
            str2 = "".join(rotatedCube[1])
            str3 = "".join(rotatedCube[2])
            str4 = "".join(rotatedCube[3])
            str5 = "".join(rotatedCube[4])
            str6 = "".join(rotatedCube[5]) 

            str_cube = str1+str2+str3+str4+str5+str6  
                        
            self.assertEqual(expectedResult.get('cube'), str_cube) 
            
 
        


    
