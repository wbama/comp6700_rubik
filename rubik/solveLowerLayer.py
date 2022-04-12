"""
    Created on 03/05/2022
    @author: Waldo du Toit
    program for solving the white cross
    03/31 - Solve lower layer
    04/04 - Finish solving lower layer
    
"""

from rubik.solveRotations import solve_top_w_corners, solve_bottom_w_corners, solve_top_white_cells
from rubik.solveWhiteCross import solveWhiteCross
from rubik.solveRotations import createYellowAndWhiteVariables


def solveLowerLayer(parms):
    
    var_w = createYellowAndWhiteVariables(parms)[1]    
    lst_cube = solveWhiteCross(parms)[0]
    
    str_rotations_long = "".join(solveWhiteCross(parms)[1]) 
            
    str_rotation_cleanup = str_rotations_long.replace("Dd", "")
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

    for _ in range(20): #run the whole thing 10 times, with the top and bottom white parts on its own each time
        # for _ in range(3):
        if lst_cube[0][0] == var_w or lst_cube[0][2] == var_w or lst_cube[1][0] == var_w or \
        lst_cube[1][2] == var_w or lst_cube[2][0] == var_w or lst_cube[2][2] == var_w or lst_cube[3][0] == var_w or \
        lst_cube[3][2] == var_w:
            lst_top_w_corners = solve_top_w_corners(lst_cube, lst_rotate)
            lst_cube = lst_top_w_corners[0]
            lst_rotate = lst_top_w_corners[1]

        if lst_cube[0][6] == var_w or lst_cube[0][8] == var_w or lst_cube[1][6] == var_w or \
        lst_cube[1][8] == var_w or lst_cube[2][6] == var_w or lst_cube[2][8] == var_w or lst_cube[3][6] == var_w or \
        lst_cube[3][8] == var_w:
            lst_bottom_w_corners = solve_bottom_w_corners(lst_cube, lst_rotate)
            lst_cube = lst_bottom_w_corners[0]
            lst_rotate = lst_bottom_w_corners[1]        
          
        if lst_cube[4][6] == var_w or lst_cube[4][8] == var_w or lst_cube[4][0] == var_w or lst_cube[4][2] == var_w:
            lst_top_white_cells = solve_top_white_cells(lst_cube, lst_rotate)
            lst_cube = lst_top_white_cells[0]
            lst_rotate = lst_top_white_cells[1]

    return lst_cube, lst_rotate

    

