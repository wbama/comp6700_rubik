"""
    Created on 03/05/2022
    @author: Waldo du Toit
    program for solving the white cross
    03/31 - Solve lower layer
    04/04 - Finish solving lower layer
    04/17 - Upper layer construction
    
"""
from rubik.solveRotations import createYellowAndWhiteVariables, rotateIntoTSolve, solve_top_w_corners
from rubik.solveRotations import right_left_trigger, back_left_trigger, left_left_trigger, front_left_trigger
from rubik.solveMiddleLayer import solveMiddleLayer

def solveUpperLayer(parms):
    
    var_y = createYellowAndWhiteVariables(parms)[0]
    var_w = createYellowAndWhiteVariables(parms)[1]
    #the input cube with the white cross    
    lst_cube = solveMiddleLayer(parms)[0]    
    lst_rotate = solveMiddleLayer(parms)[1]
            
    for _ in range(20):        
        pass

    return lst_cube, lst_rotate

    

