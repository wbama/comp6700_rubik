"""
    Created on 03/05/2022
    @author: Waldo du Toit
    program for solving the daisy
    03/17 - Refactoring. Use _ instead of unused i
    
"""
from rubik.solveRotations import createCubeListFromInputParms
from rubik.solveRotations import solveWhiteLeaves, createYellowAndWhiteVariables

def solveDaisy(parms):
    
    #find out where the yellow center is. Solve from that vantage point    
    lst_cube = (createCubeListFromInputParms(parms)) 
    lst_rotate = [] 
    var_w = createYellowAndWhiteVariables(parms)[1] 
    var_y =  createYellowAndWhiteVariables(parms)[0]

    for _ in range(50):
        lst_cube = (solveWhiteLeaves(lst_cube, lst_rotate))[0]   
        
        if lst_cube[4][4] == var_y and lst_cube[4][1] == var_w and lst_cube[4][3] == var_w and \
        lst_cube[4][5] == var_w and lst_cube[4][7] == var_w:
            break     

    return [lst_cube, lst_rotate]
