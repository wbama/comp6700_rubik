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
    # print(rotation_from_daisy)        
    # whiteCrossCubeRotation = (rotateIntoWhiteCross(lst_cube_from_daisy, rotation_from_daisy ))
      
    lst_cube = solveDaisy(parms)[0]
    lst_rotate = solveDaisy(parms)[1]
               
    for _ in range(50):
        lst_cube_rotate = rotateIntoWhiteCross(lst_cube, lst_rotate)   
        lst_cube = lst_cube_rotate[0]
        lst_rotate = lst_cube_rotate[1]   
                
        if lst_cube[5][1] == var_w and lst_cube[5][3] == var_w and lst_cube[5][4] == var_w and \
        lst_cube[5][5] == var_w and lst_cube[5][7] == var_w:
            break
        else:
            lst_cube = rotateSide_U(lst_cube)
            lst_rotate.append("U")
            
    # print("".join(lst_rotate))     
    return [lst_cube, lst_rotate] 
