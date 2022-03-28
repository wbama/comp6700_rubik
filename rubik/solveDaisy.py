"""
    Created on 03/05/2022
    @author: Waldo du Toit
    program for solving the daisy
    03/17 - Refactoring. Use _ instead of unused i
    
"""
from rubik.solveRotations import createCubeListFromInputParms
from rubik.solveRotations import y_4_SolveWhiteLeaves

def solveDaisy(parms):
    
    #find out where the yellow center is. Solve from that vantage point    
    lst_cube = (createCubeListFromInputParms(parms)) 
    lst_rotate = [] 

    for _ in range(20):
        lst_cube = (y_4_SolveWhiteLeaves(lst_cube, lst_rotate))[0]        

    return lst_cube, lst_rotate
