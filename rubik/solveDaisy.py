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
from rubik.solveRotations import y_0_WhiteLeafPos0_5, y_0_WhiteLeafPos0_1 


def solveDaisy(parms):
    
    #find out where the yellow center is. Solve from that vantage point
    

    lst_cube = (createCubeListFromInputParms(parms)) 
    lst_rotate = [] 

    #yellow is in front        
    if createCubeListFromInputParms(parms)[0][4] == 'y':
              
    #first leaf position [0][5]
    #solve only this position. Then rotate the front edge and solve it again and again
        print(f"lst_cube in {lst_cube}")
        while lst_cube[0][5] == "w":
            lst_cube = rotateSide_F(lst_cube)
            lst_rotate.append("F")
        else:
            lst_cube = (y_0_WhiteLeafPos0_5(lst_cube, lst_rotate))[0] #this output is a tuple
            print(f"lst_cube 1 {lst_cube}")
    #rotate the face, so that there is now non white leaf
        while lst_cube[0][5] == "w":
            lst_cube = rotateSide_F(lst_cube)
            lst_rotate.append("F")
        else:
            lst_cube = (y_0_WhiteLeafPos0_5(lst_cube, lst_rotate))[0] #this output is a tuple
            print(f"lst_cube 2 {lst_cube}")
            
        while lst_cube[0][5] == "w":
            lst_cube = rotateSide_F(lst_cube)
            lst_rotate.append("F")
        else:
            lst_cube = (y_0_WhiteLeafPos0_5(lst_cube, lst_rotate))[0] #this output is a tuple
            print(f"lst_cube 3 {lst_cube}")
    #rotate the face, so that there is now non white leaf
        while lst_cube[0][5] == "w":
            lst_cube = rotateSide_F(lst_cube)
            lst_rotate.append("F")
        else:
            lst_cube = (y_0_WhiteLeafPos0_5(lst_cube, lst_rotate))[0] #this output is a tuple
            print(f"lst_cube 4 {lst_cube}")     
   


         
    print(lst_rotate)
            
        

    return lst_cube 
