from rubik.solveRotations import createCubeListFromInputParms
from rubik.solveRotations import rotateCubeToLeft
from rubik.solveRotations import rotateCubeToRight
from rubik.solveRotations import rotateCubeDown
from rubik.solveRotations import rotateCubeUp
from rubik.solveRotations import putWhiteLeafPosition0_5
from rubik.solveRotations import rotateCubeClock



def solveDaisy(parms):
    
    #find out where the yellow center is. Solve from that vantage point
    
    #yellow is in front    
    if createCubeListFromInputParms(parms)[0][4] == 'y':
        lst_cube = (createCubeListFromInputParms(parms))  
                
    #find white leaves   
    if lst_cube[0][5] == 'w':
        lst_cube = lst_cube
    else:
        #inside cells
        lst_cube = putWhiteLeafPosition0_5(lst_cube)
        
    #rotate the whole cube and, do the yellow[0][5] again  
    lst_cube = rotateCubeClock(lst_cube)
        #find white leaves   
    if lst_cube[0][5] == 'w':
        lst_cube = lst_cube
    else:
        #inside cells
        lst_cube = putWhiteLeafPosition0_5(lst_cube)
        
    #rotate the whole cube and, do the yellow[0][5] again  
    lst_cube = rotateCubeClock(lst_cube)
        #find white leaves   
    if lst_cube[0][5] == 'w':
        lst_cube = lst_cube
    else:
        #inside cells
        lst_cube = putWhiteLeafPosition0_5(lst_cube)
        
    #rotate the whole cube and, do the yellow[0][5] again  
    lst_cube = rotateCubeClock(lst_cube)
        #find white leaves   
    if lst_cube[0][5] == 'w':
        lst_cube = lst_cube
    else:
        #inside cells
        lst_cube = putWhiteLeafPosition0_5(lst_cube)            

    
    return lst_cube 
