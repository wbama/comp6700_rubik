"""
    Created on 03/05/2022
    @author: Waldo du Toit
    program for solving the white cross
    03/31 - Solve lower layer
    04/04 - Finish solving lower layer
    
"""
from rubik.solveRotations import createYellowAndWhiteVariables, rotateIntoTSolve, solve_top_w_corners
from rubik.solveRotations import right_left_trigger, back_left_trigger, left_left_trigger, front_left_trigger
from rubik.solveLowerLayer import solveLowerLayer


def solveMiddleLayer(parms):
    
    var_y = createYellowAndWhiteVariables(parms)[0]
    var_w = createYellowAndWhiteVariables(parms)[1]
    #the input cube with the white cross    
    lst_cube = solveLowerLayer(parms)[0]    
    lst_rotate = solveLowerLayer(parms)[1]
            
    for _ in range(50):
        
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
        
        #no edge pieces without yellow, but middle layer not solved. If middle layer solved, would break
        if (lst_cube[4][3]  == var_y or lst_cube[3][1]  == var_y) and \
            (lst_cube[4][1] == var_y or lst_cube[2][1]  == var_y) and \
            (lst_cube[4][5] == var_y or lst_cube[1][1] == var_y ) and \
            (lst_cube[4][7] == var_y or lst_cube[0][1] == var_y ):
            print("edge piece not yellow")
            print(lst_cube)
            print("")
            if (lst_cube[0][3] ==  lst_cube[0][4] and lst_cube[0][5] != lst_cube[0][4]):
                print("lst_cube[0][3]")
                lst_cube = right_left_trigger(lst_cube, lst_rotate)[0]
            elif (lst_cube[1][3] ==  lst_cube[1][4] and lst_cube[1][5] != lst_cube[1][4]):
                lst_cube = back_left_trigger(lst_cube, lst_rotate)[0]
                lst_top_w_corners = solve_top_w_corners(lst_cube, lst_rotate)
                lst_cube = lst_top_w_corners[0]
                lst_rotate = lst_top_w_corners[1] 
                print(f"lst_cube[1][3] {lst_cube}")
            elif (lst_cube[2][3] ==  lst_cube[2][4] and lst_cube[2][5] != lst_cube[2][4]):
                lst_cube = left_left_trigger(lst_cube, lst_rotate)[0]
            elif (lst_cube[3][3] ==  lst_cube[3][4] and lst_cube[3][5] != lst_cube[3][4]):
                lst_cube = front_left_trigger(lst_cube, lst_rotate)[0]
                
                
    
    return lst_cube, lst_rotate

    

