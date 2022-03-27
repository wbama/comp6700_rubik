"""
    Created on 03/05/2022
    @author: Waldo du Toit
    program for solving the white cross
    03/26 - Solve lower layer
    
"""

from rubik.solveWhiteCross import solveWhiteCross
from rubik.solveRotations import createYellowAndWhiteVariables


def solveLowerLayer(parms):
    
    var_w = createYellowAndWhiteVariables(parms)[1]
    #the input cube with the white cross
    lst_cube = solveWhiteCross(parms)[0]

    str_rotations_long = "".join(solveWhiteCross(parms)[1])  
            
    last_x = str_rotations_long.rfind('x')
    str_rotations_short = str_rotations_long[:last_x]
    str_rotations_no_x = str_rotations_short.replace("x", "")
    str_rotations_no_y = str_rotations_no_x.replace("y", "")
    str_rotation_cleanup = str_rotations_no_y.replace("Dd", "")
    str_rotation_cleanup = str_rotation_cleanup.replace("dD", "")
    str_rotation_cleanup = str_rotation_cleanup.replace("Rr", "")
    str_rotation_cleanup = str_rotation_cleanup.replace("rR", "")
    str_rotation_cleanup = str_rotation_cleanup.replace("Uu", "")
    str_rotation_cleanup = str_rotation_cleanup.replace("uU", "")
    str_rotation_cleanup = str_rotation_cleanup.replace("Ll", "")
    str_rotation_cleanup = str_rotation_cleanup.replace("lL", "")
    str_rotation_cleanup = str_rotation_cleanup.replace("bB", "")
    str_rotation_cleanup = str_rotation_cleanup.replace("Bb", "")
    str_rotation_cleanup = str_rotation_cleanup.replace("Ff", "")
    str_rotation_cleanup = str_rotation_cleanup.replace("fF", "")
    
    #get back the cleaned up rotations from making white cross. Append to this list
    lst_rotate = list(str_rotation_cleanup)
    print(lst_cube)
    print(lst_rotate)
    

    
    #the cross color will be whatever is at the bottom. Not always white. use var_w
    print(f"The cross color will be {var_w}")
    
    if lst_cube[0][1] == var_w or lst_cube[0][2] == var_w or lst_cube[1][0] == var_w or \
        lst_cube[1][2] == var_w or lst_cube[2][0] == var_w or lst_cube[2][2] == var_w or \
        lst_cube[3][0] == var_w or lst_cube[3][2] == var_w:
        print("corner cross")
        
        
    
    return str_rotation_cleanup

    

