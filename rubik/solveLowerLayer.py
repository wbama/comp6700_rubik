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
    
    print(var_w)
    
    return str_rotation_cleanup

    

