from rubik.solveRotations import createCubeListFromInputParms
from rubik.solveRotations import rotateCubeToLeft
from rubik.solveRotations import rotateCubeToRight
from rubik.solveRotations import rotateCubeDown
from rubik.solveRotations import rotateCubeUp
from rubik.solveRotations import rotateCubeClock
from rubik.solveRotations import rotateSide_F, rotateSide_f
from rubik.solveRotations import rotateSide_R, rotateSide_r
from rubik.solveRotations import rotateSide_B, rotateSide_b
from rubik.solveRotations import rotateSide_L, rotateSide_l
from rubik.solveRotations import rotateSide_U, rotateSide_u
from rubik.solveRotations import rotateSide_D, rotateSide_d
from rubik.solveRotations import y_0_SolveWhiteLeaves, y_1_SolveWhiteLeaves, y_2_SolveWhiteLeaves, y_3_SolveWhiteLeaves, y_4_SolveWhiteLeaves, y_5_SolveWhiteLeaves
from rubik.solveRotations import y_0_SolveWhiteLeaves, y_1_SolveWhiteLeaves, y_2_SolveWhiteLeaves, y_3_SolveWhiteLeaves, y_4_SolveWhiteLeaves, y_5_SolveWhiteLeaves
from rubik.solveRotations import createYellowAndWhiteSides

def solveDaisy(parms):
    
    #find out where the yellow center is. Solve from that vantage point    

    lst_cube = (createCubeListFromInputParms(parms)) 
    var_y = createYellowAndWhiteSides(parms)[0]
    var_w = createYellowAndWhiteSides(parms)[1]
    lst_rotate = [] 

    #yellow is in front    
    if createCubeListFromInputParms(parms)[0][4] == createYellowAndWhiteSides(parms)[0]: 
        #just run through the code 20 times. Take out the no movements in the end
        for i in range(20):
            lst_cube = (y_0_SolveWhiteLeaves(lst_cube, lst_rotate))[0]         
 
    if createCubeListFromInputParms(parms)[1][4] == 'y': 
        #just run through the code 20 times. Take out the no movements in the end
        for i in range(20):
            lst_cube = (y_1_SolveWhiteLeaves(lst_cube, lst_rotate))[0] 

    if createCubeListFromInputParms(parms)[2][4] == 'y': 
        #just run through the code 20 times. Take out the no movements in the end
        for i in range(20):
            lst_cube = (y_2_SolveWhiteLeaves(lst_cube, lst_rotate))[0]    
            
    if createCubeListFromInputParms(parms)[3][4] == 'y': 
        #just run through the code 20 times. Take out the no movements in the end
        for i in range(20):
            lst_cube = (y_3_SolveWhiteLeaves(lst_cube, lst_rotate))[0]    
            
    if createCubeListFromInputParms(parms)[4][4] == 'y': 
        #just run through the code 20 times. Take out the no movements in the end
        for i in range(20):
            lst_cube = (y_4_SolveWhiteLeaves(lst_cube, lst_rotate))[0] 
            
    if createCubeListFromInputParms(parms)[5][4] == 'y': 
        #just run through the code 20 times. Take out the no movements in the end
        for i in range(20):
            lst_cube = (y_5_SolveWhiteLeaves(lst_cube, lst_rotate))[0]              

    return lst_cube, lst_rotate
