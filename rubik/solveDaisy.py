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
from rubik.solveRotations import y_0_WhiteLeafPos0_5, y_1_WhiteLeafPos1_5, y_2_WhiteLeafPos2_5, y_3_WhiteLeafPos3_5


def solveDaisy(parms):
    
    #find out where the yellow center is. Solve from that vantage point    

    lst_cube = (createCubeListFromInputParms(parms)) 
    lst_rotate = [] 

    #yellow is in front    
    if createCubeListFromInputParms(parms)[0][4] == 'y': 
        #just run through the code 20 times. Take out the no movements in the end
        for i in range(20):
            lst_cube = (y_0_WhiteLeafPos0_5(lst_cube, lst_rotate))[0]         
 
    if createCubeListFromInputParms(parms)[1][4] == 'y': 
        #just run through the code 20 times. Take out the no movements in the end
        for i in range(20):
            lst_cube = (y_1_WhiteLeafPos1_5(lst_cube, lst_rotate))[0] 

    if createCubeListFromInputParms(parms)[2][4] == 'y': 
        #just run through the code 20 times. Take out the no movements in the end
        for i in range(20):
            lst_cube = (y_2_WhiteLeafPos2_5(lst_cube, lst_rotate))[0]    
            
    if createCubeListFromInputParms(parms)[3][4] == 'y': 
        #just run through the code 20 times. Take out the no movements in the end
        for i in range(20):
            lst_cube = (y_3_WhiteLeafPos3_5(lst_cube, lst_rotate))[0]             

    return lst_cube, lst_rotate
