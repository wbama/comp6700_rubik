"""
    Created on 03/05/2022
    @author: Waldo du Toit
    program for solving the white cross
    03/31 - Solve lower layer
    
"""

from rubik.solveRotations import solve_top_w_corners, solve_bottom_w_corners, solve_top_white_cells
from rubik.solveWhiteCross import solveWhiteCross
from rubik.solveRotations import createYellowAndWhiteVariables


def solveLowerLayer(parms):
    
    var_w = createYellowAndWhiteVariables(parms)[1]
    #the input cube with the white cross
    lst_cube = solveWhiteCross(parms)[0]
    print(f"first list {lst_cube}") 
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
    
    #the cross color will be whatever is at the bottom. Not always white. use var_w    
    # if no side-top corners or side-bottom corners, solve top matched to bottom, do whole thing again    
    #if no top corners, solve the bottom corners. Run once, then run top corners            
    #solve the side-top corners

    
    for _ in range(50): #run the whole thing 10 times, with the top and bottom white parts on its own each time
        # for _ in range(3):
        if lst_cube[0][0] == var_w or lst_cube[0][2] == var_w or lst_cube[1][0] == var_w or \
        lst_cube[1][2] == var_w or lst_cube[2][0] == var_w or lst_cube[2][2] == var_w or lst_cube[3][0] == var_w or \
        lst_cube[3][2] == var_w:
            print(f"input list {lst_cube}") 
            lst_top_w_corners = solve_top_w_corners(lst_cube, lst_rotate)
            lst_cube = lst_top_w_corners[0]
            lst_rotate = lst_top_w_corners[1]
            str_rotate = "".join(lst_rotate) 
            print(f"rotate_top_w_corners {str_rotate}")   
            print(f"after 1st rotate {lst_cube}")   
        
        # if no side-top corners, put side-bottom corners on top, then solve side-top corners   
        # just do the rotate once, then split up, else will do twice
        if lst_cube[0][0] != var_w and lst_cube[0][2] != var_w and lst_cube[1][0] != var_w and \
        lst_cube[1][2] != var_w and lst_cube[2][0] != var_w and lst_cube[2][2] != var_w and lst_cube[3][0] != var_w and \
        lst_cube[3][2] != var_w:
            lst_bottom_w_corners = solve_bottom_w_corners(lst_cube, lst_rotate)
            lst_cube = lst_bottom_w_corners[0]
            lst_rotate = lst_bottom_w_corners[1]
            print(f"after bottom white rotate {lst_bottom_w_corners}")
                
            # if lst_cube[5][0] == var_w and lst_cube[5][1] == var_w and lst_cube[5][2] == var_w and lst_cube[5][3] == var_w and \
            # lst_cube[5][4] == var_w and lst_cube[5][5] == var_w and lst_cube[5][6] == var_w and lst_cube[5][7] == var_w and \
            # lst_cube[5][8] == var_w and (lst_cube[0][6] == lst_cube[0][7] == lst_cube[0][8]) and \
            # (lst_cube[1][6] == lst_cube[1][7] == lst_cube[1][8]) and   (lst_cube[2][6] == lst_cube[2][7] == lst_cube[2][8]) and \
            #  (lst_cube[3][6] == lst_cube[3][7] == lst_cube[3][8]):
            #     break
            
        if lst_cube[4][6] == var_w or lst_cube[4][8] == var_w or lst_cube[4][0] == var_w or lst_cube[4][2] == var_w:
            print("top white somewhere")
            lst_top_white_cells = solve_top_white_cells(lst_cube, lst_rotate)
            lst_cube = lst_top_white_cells[0]
            lst_rotate = lst_top_white_cells[1]
            print(f"after top rotate {lst_cube}")           
            
        if lst_cube[5][0] == var_w and lst_cube[5][1] == var_w and lst_cube[5][2] == var_w and lst_cube[5][3] == var_w and \
        lst_cube[5][4] == var_w and lst_cube[5][5] == var_w and lst_cube[5][6] == var_w and lst_cube[5][7] == var_w and \
        lst_cube[5][8] == var_w and (lst_cube[0][6] == lst_cube[0][7] == lst_cube[0][8]) and \
        (lst_cube[1][6] == lst_cube[1][7] == lst_cube[1][8]) and   (lst_cube[2][6] == lst_cube[2][7] == lst_cube[2][8]) and \
         (lst_cube[3][6] == lst_cube[3][7] == lst_cube[3][8]):
            break

    # if no side-top corners or side-bottom corners, solve top matched to bottom, do whole thing again
    print(f"final lst_cube {lst_cube}")
    print("".join(lst_rotate))  
    return lst_cube, lst_rotate

    

