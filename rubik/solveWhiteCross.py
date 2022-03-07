from rubik.solveRotations import rotateCubeToLeft
from rubik.solveRotations import rotateCubeClock
from rubik.solveRotations import rotateIntoWhiteCross
from rubik.solveDaisy import solveDaisy


def solveWhiteCross(parms):
    
       
    # have the daisy now. match up colors and rotate sides down for white cross
    
    lst_cube = rotateIntoWhiteCross(solveDaisy(parms))
         
    #rotate the whole cube and do again  - make function later on
    lst_cube = rotateCubeClock(lst_cube)
    lst_cube = rotateIntoWhiteCross(lst_cube)
        
    #rotate the whole cube and do again  - make function later on
    lst_cube = rotateCubeClock(lst_cube)
    lst_cube = rotateIntoWhiteCross(lst_cube)
        
    #rotate the whole cube and do again  - make function later on
    lst_cube = rotateCubeClock(lst_cube)    
    lst_cube = rotateIntoWhiteCross(lst_cube)        
       
    #make white cross the front
    lst_cube =   rotateCubeToLeft(lst_cube)
    lst_cube =   rotateCubeToLeft(lst_cube)          

    
    return lst_cube 
