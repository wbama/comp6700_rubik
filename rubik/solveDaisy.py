"""
    Created on 03/05/2022
    @author: Waldo du Toit
    program for solving the daisy
    03/17 - Refactoring. Use _ instead of unused i
    
"""
from rubik.solveRotations import createCubeListFromInputParms
from rubik.solveRotations import y_0_SolveWhiteLeaves, y_1_SolveWhiteLeaves, y_2_SolveWhiteLeaves, y_3_SolveWhiteLeaves, y_4_SolveWhiteLeaves, y_5_SolveWhiteLeaves
from rubik.solveRotations import createYellowAndWhiteVariables

def solveDaisy(parms):
    
    #find out where the yellow center is. Solve from that vantage point    
    lst_cube = (createCubeListFromInputParms(parms)) 
    var_y = createYellowAndWhiteVariables(parms)[0]
    lst_rotate = [] 

    # #yellow is in front    
    # if createCubeListFromInputParms(parms)[0][4] == var_y: 
    #     #just run through the code 20 times. Take out the no movements in the end
    #     for _ in range(20):
    #         lst_cube = (y_0_SolveWhiteLeaves(lst_cube, lst_rotate))[0]         
    #
    # if createCubeListFromInputParms(parms)[1][4] == var_y: 
    #     #just run through the code 20 times. Take out the no movements in the end
    #     for _ in range(20):
    #         lst_cube = (y_1_SolveWhiteLeaves(lst_cube, lst_rotate))[0] 
    #
    # if createCubeListFromInputParms(parms)[2][4] == var_y: 
    #     #just run through the code 20 times. Take out the no movements in the end
    #     for _ in range(20):
    #         lst_cube = (y_2_SolveWhiteLeaves(lst_cube, lst_rotate))[0]    
    #
    # if createCubeListFromInputParms(parms)[3][4] == var_y: 
    #     #just run through the code 20 times. Take out the no movements in the end
    #     for _ in range(20):
    #         lst_cube = (y_3_SolveWhiteLeaves(lst_cube, lst_rotate))[0]    
            
    # if createCubeListFromInputParms(parms)[4][4] == var_y: 
        #just run through the code 20 times. Take out the no movements in the end
    for _ in range(20):
        lst_cube = (y_4_SolveWhiteLeaves(lst_cube, lst_rotate))[0] 
            
    # if createCubeListFromInputParms(parms)[5][4] == var_y: 
    #     #just run through the code 20 times. Take out the no movements in the end
    #     for _ in range(20):
    #         lst_cube = (y_5_SolveWhiteLeaves(lst_cube, lst_rotate))[0]              

    return lst_cube, lst_rotate
