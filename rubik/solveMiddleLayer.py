"""
    Created on 03/05/2022
    @author: Waldo du Toit
    program for solving the white cross
    03/31 - Solve lower layer
    04/04 - Finish solving lower layer
    
"""
from rubik.solveRotations import createYellowAndWhiteVariables, rotateIntoT
from rubik.solveLowerLayer import solveLowerLayer


def solveMiddleLayer(parms):
    
    var_w = createYellowAndWhiteVariables(parms)[1]
    print(f"var_w is  {var_w}")
    #the input cube with the white cross
    
    lst_cube = solveLowerLayer(parms)[0]
    
    lst_rotate = solveLowerLayer(parms)[1]
            
    # str_rotation_cleanup = str_rotations_long.replace("Dd", "")
    # str_rotation_cleanup = str_rotation_cleanup.replace("dD", "")
    # str_rotation_cleanup = str_rotation_cleanup.replace("Rr", "")
    # str_rotation_cleanup = str_rotation_cleanup.replace("rR", "")
    # str_rotation_cleanup = str_rotation_cleanup.replace("Uu", "")
    # str_rotation_cleanup = str_rotation_cleanup.replace("uU", "")
    # str_rotation_cleanup = str_rotation_cleanup.replace("Ll", "")
    # str_rotation_cleanup = str_rotation_cleanup.replace("lL", "")
    # str_rotation_cleanup = str_rotation_cleanup.replace("bB", "")
    # str_rotation_cleanup = str_rotation_cleanup.replace("Bb", "")
    # str_rotation_cleanup = str_rotation_cleanup.replace("Ff", "")
    # str_rotation_cleanup = str_rotation_cleanup.replace("fF", "")    
    #get back the cleaned up rotations from making white cross. Append to this list

    
    rotateIntoT(lst_cube, lst_rotate)
    
    # print(f"input cube {lst_cube}")

    return lst_cube, lst_rotate

    

