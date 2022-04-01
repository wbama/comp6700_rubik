"""
    Created on 03/05/2022
    @author: Waldo du Toit
    program for solving the white cross
    03/17 - Refactoring. Replace i in range with _
    
"""


from rubik.solveRotations import rotateIntoWhiteCross, createYellowAndWhiteVariables, rotateSide_U
from rubik.solveDaisy import solveDaisy

def solveWhiteCross(parms):  
    
    var_w = createYellowAndWhiteVariables(parms)[1]  

    lst_cube_from_daisy = ((rotateIntoWhiteCross(solveDaisy(parms)[0], solveDaisy(parms)[1])))[0]
    rotation_from_daisy = ((rotateIntoWhiteCross(solveDaisy(parms)[0], solveDaisy(parms)[1])))[1]           
    whiteCrossCube = (rotateIntoWhiteCross(lst_cube_from_daisy, rotation_from_daisy ))    
               
    for _ in range(20):
        whiteCrossCube = (rotateIntoWhiteCross(whiteCrossCube[0], whiteCrossCube[1])) 
        lst_cube = whiteCrossCube[0]
    
        if lst_cube[5][1] == var_w and lst_cube[5][3] == var_w and lst_cube[5][4] == var_w and \
        lst_cube[5][5] == var_w and lst_cube[5][7] == var_w:
            break
        else:
            lst_cube = rotateSide_U(lst_cube)
            rotation_from_daisy.append("U")
            
            
    return whiteCrossCube 
