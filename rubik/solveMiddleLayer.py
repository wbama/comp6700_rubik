"""
    Created on 03/05/2022
    @author: Waldo du Toit
    program for solving the white cross
    03/31 - Solve lower layer
    04/04 - Finish solving lower layer
    
"""
from rubik.solveRotations import createYellowAndWhiteVariables, rotateIntoTSolve, solve_top_w_corners
from rubik.solveLowerLayer import solveLowerLayer


def solveMiddleLayer(parms):
    
    var_w = createYellowAndWhiteVariables(parms)[1]
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

    for _ in range(20):
        
        lst_cube_t = rotateIntoTSolve(lst_cube, lst_rotate)
        lst_cube = lst_cube_t[0]
        lst_rotate = lst_cube_t[1]
    
        if lst_cube[0][0] == var_w or lst_cube[0][2] == var_w or lst_cube[1][0] == var_w or \
            lst_cube[1][2] == var_w or lst_cube[2][0] == var_w or lst_cube[2][2] == var_w or lst_cube[3][0] == var_w or \
            lst_cube[3][2] == var_w:
                # print("top w corners")
                lst_top_w_corners = solve_top_w_corners(lst_cube, lst_rotate)
                lst_cube = lst_top_w_corners[0]
                lst_rotate = lst_top_w_corners[1]
    
    return lst_cube, lst_rotate

    

