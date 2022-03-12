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
from rubik.solveRotations import y_0_WhiteLeafPos0_5, y_1_WhiteLeafPos1_5 


def solveDaisy(parms):
    
    #find out where the yellow center is. Solve from that vantage point    

    lst_cube = (createCubeListFromInputParms(parms)) 
    lst_rotate = [] 

    #yellow is in front        
    if createCubeListFromInputParms(parms)[0][4] == 'y':
              
    #first leaf position [0][5]
    #solve only this position. Then rotate the front edge and solve it again and again
        for i in range(5):
            while (lst_cube[0][5] != "w" or  lst_cube[0][1] != "w" or lst_cube[0][3] != "w" or lst_cube[0][7] != "w") and lst_cube[0][5] == "w":
                lst_cube = rotateSide_F(lst_cube)
                lst_rotate.append("F")
            else:
                lst_cube = (y_0_WhiteLeafPos0_5(lst_cube, lst_rotate))[0]            
 
            

    return lst_cube, lst_rotate
