"""
    Created on 03/05/2022
    @author: Waldo du Toit
    codes to rotate cube strings. Then use those cube strings in unittests to test cube from different sides
    
"""
from rubik.solve import _solve
from rubik.solveDaisy import solveDaisy
from rubik.solveRotations import createCubeListFromInputParms, rotateCubeToRight, rotateCubeDown, rotateCubeUp
from rubik.solveWhiteCross import solveWhiteCross


inputDict = {}
inputDict['cube'] = "rryobggrwoyowrroybgybygoygwwwywobrborowryggbbygbwwbgor"
inputDict['op'] = 'solve' 
#inputDict['rotate'] = 'F'

lst_cube = createCubeListFromInputParms(inputDict)
print(lst_cube)
#rotate the cube
lst_cube = rotateCubeUp(lst_cube)
print(lst_cube)
str1 = "".join(lst_cube[0])
str2 = "".join(lst_cube[1])
str3 = "".join(lst_cube[2])
str4 = "".join(lst_cube[3])
str5 = "".join(lst_cube[4])
str6 = "".join(lst_cube[5])                       
         
str_cube = str1+str2+str3+str4+str5+str6
print(str_cube)