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
                
        if lst_cube[5][0] == var_w and lst_cube[5][1] == var_w and lst_cube[5][2] == var_w and lst_cube[5][3] == var_w and \
        lst_cube[5][4] == var_w and lst_cube[5][5] == var_w and lst_cube[5][6] == var_w and lst_cube[5][7] == var_w and \
        lst_cube[5][8] == var_w and \
        (lst_cube[0][3] == lst_cube[0][4] == lst_cube[0][5] == lst_cube[0][6] == lst_cube[0][7] == lst_cube[0][8]) and \
        (lst_cube[1][3] == lst_cube[1][4] == lst_cube[1][5] == lst_cube[1][6] == lst_cube[1][7] == lst_cube[1][8]) and \
        (lst_cube[2][3] == lst_cube[2][4] == lst_cube[2][5] == lst_cube[2][6] == lst_cube[2][7] == lst_cube[2][8]) and \
        (lst_cube[3][3] == lst_cube[3][4] == lst_cube[3][5] == lst_cube[3][6] == lst_cube[3][7] == lst_cube[3][8]):
            break
    
    return lst_cube, lst_rotate

    

