"""
    Created on 03/05/2022
    @author: Waldo du Toit
    program for solving the white cross
    03/26 - Solve lower layer
    
"""

from rubik.solveWhiteCross import solveWhiteCross
from rubik.solveRotations import createYellowAndWhiteVariables,\
    solve_top_w_corners
from rubik.solveRotations import rotateSide_R, rotateSide_r, rotateSide_B, rotateSide_b
from rubik.solveRotations import rotateSide_L, rotateSide_l, rotateSide_U, rotateSide_u
from rubik.solveRotations import rotateSide_D, rotateSide_d, rotateSide_f, rotateSide_F
from rubik.solveRotations import front_left_trigger, front_right_trigger, right_left_trigger, right_right_trigger
from rubik.solveRotations import back_left_trigger, back_right_trigger, left_left_trigger, left_right_trigger
from rubik.solveRotations import solve_top_w_corners, solve_bottom_w_corners

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
    
    #the cross color will be whatever is at the bottom. Not always white. use var_w
    
    # if no side-top corners or side-bottom corners, solve top matched to bottom, do whole thing again
    
    #if no top corners, solve the bottom corners. Run once, then run top corners
            
    #solve the side-top corners
    while True:
        lst_cube = solve_top_w_corners(lst_cube, lst_rotate)[0]  
        lst_rotate =   solve_top_w_corners(lst_cube, lst_rotate)[1]
                            
        if lst_cube[0][0] != var_w and lst_cube[0][2] != var_w and lst_cube[1][0] != var_w and \
        lst_cube[1][2] != var_w and lst_cube[2][0] != var_w and lst_cube[2][2] != var_w and lst_cube[3][0] != var_w and \
        lst_cube[3][2] != var_w:
            break
    
    # if no side-top corners, put side-bottom corners on top, then solve side-top corners   
    lst_cube = solve_bottom_w_corners(lst_cube, lst_rotate)[0] 
    lst_rotate =   solve_bottom_w_corners(lst_cube, lst_rotate)[1]
        
    while True:
        lst_cube = solve_top_w_corners(lst_cube, lst_rotate)[0]  
        lst_rotate =   solve_top_w_corners(lst_cube, lst_rotate)[1]              
                      
        if lst_cube[0][0] != var_w and lst_cube[0][2] != var_w and lst_cube[1][0] != var_w and \
        lst_cube[1][2] != var_w and lst_cube[2][0] != var_w and lst_cube[2][2] != var_w and lst_cube[3][0] != var_w and \
        lst_cube[3][2] != var_w:
            break
    # if no side-top corners or side-bottom corners, solve top matched to bottom, do whole thing again
    
    return lst_cube, lst_rotate

    

