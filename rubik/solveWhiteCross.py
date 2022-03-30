"""
    Created on 03/05/2022
    @author: Waldo du Toit
    program for solving the white cross
    03/17 - Refactoring. Replace i in range with _
    
"""


from rubik.solveRotations import rotateIntoWhiteCross_y_4, createYellowAndWhiteVariables
from rubik.solveDaisy import solveDaisy

def solveWhiteCross(parms):  
    
    var_w = createYellowAndWhiteVariables(parms)[1]  

    lst_cube_from_daisy = ((rotateIntoWhiteCross_y_4(solveDaisy(parms)[0], solveDaisy(parms)[1])))[0]
    rotation_from_daisy = ((rotateIntoWhiteCross_y_4(solveDaisy(parms)[0], solveDaisy(parms)[1])))[1]  
          
    whiteCrossCube = (rotateIntoWhiteCross_y_4(lst_cube_from_daisy, rotation_from_daisy )) 
    
    while True:                   
    # for _ in range(20):
        whiteCrossCube = (rotateIntoWhiteCross_y_4(whiteCrossCube[0], whiteCrossCube[1])) 
        lst_cube = whiteCrossCube[0]
    
        if lst_cube[5][1] == var_w and lst_cube[5][3] == var_w and lst_cube[5][4] == var_w and \
        lst_cube[5][5] == var_w and lst_cube[5][7] == var_w:
            break
            
    return whiteCrossCube 
