from rubik.solveRotations import rotateCubeToLeft
from rubik.solveRotations import rotateCubeClock
from rubik.solveRotations import rotateIntoWhiteCross_y_0, rotateIntoWhiteCross_y_1, rotateIntoWhiteCross_y_2, rotateIntoWhiteCross_y_3
from rubik.solveRotations import rotateIntoWhiteCross_y_4, rotateIntoWhiteCross_y_5
from rubik.solveRotations import createCubeListFromInputParms
from rubik.solveDaisy import solveDaisy


def solveWhiteCross(parms):
    
       
    # have the daisy now. match up colors and rotate sides down for white cross
    if createCubeListFromInputParms(parms)[0][4] == 'y': 
        lst_cube_from_daisy = ((rotateIntoWhiteCross_y_0(solveDaisy(parms)[0], solveDaisy(parms)[1])))[0]
        rotation_from_daisy = ((rotateIntoWhiteCross_y_0(solveDaisy(parms)[0], solveDaisy(parms)[1])))[1]        
        whiteCrossCube = (rotateIntoWhiteCross_y_0(lst_cube_from_daisy, rotation_from_daisy ))      
        for i in range(20):
            whiteCrossCube = (rotateIntoWhiteCross_y_0(whiteCrossCube[0], whiteCrossCube[1]))        
        
    elif createCubeListFromInputParms(parms)[1][4] == 'y': 
        lst_cube_from_daisy = ((rotateIntoWhiteCross_y_1(solveDaisy(parms)[0], solveDaisy(parms)[1])))[0]
        rotation_from_daisy = ((rotateIntoWhiteCross_y_1(solveDaisy(parms)[0], solveDaisy(parms)[1])))[1]        
        whiteCrossCube = (rotateIntoWhiteCross_y_1(lst_cube_from_daisy, rotation_from_daisy ))             
        for i in range(20):
            whiteCrossCube = (rotateIntoWhiteCross_y_1(whiteCrossCube[0], whiteCrossCube[1])) 
            
    elif createCubeListFromInputParms(parms)[2][4] == 'y': 
        lst_cube_from_daisy = ((rotateIntoWhiteCross_y_2(solveDaisy(parms)[0], solveDaisy(parms)[1])))[0]
        rotation_from_daisy = ((rotateIntoWhiteCross_y_2(solveDaisy(parms)[0], solveDaisy(parms)[1])))[1]        
        whiteCrossCube = (rotateIntoWhiteCross_y_2(lst_cube_from_daisy, rotation_from_daisy ))             
        for i in range(20):
            whiteCrossCube = (rotateIntoWhiteCross_y_2(whiteCrossCube[0], whiteCrossCube[1])) 
            
    elif createCubeListFromInputParms(parms)[3][4] == 'y': 
        lst_cube_from_daisy = ((rotateIntoWhiteCross_y_3(solveDaisy(parms)[0], solveDaisy(parms)[1])))[0]
        rotation_from_daisy = ((rotateIntoWhiteCross_y_3(solveDaisy(parms)[0], solveDaisy(parms)[1])))[1]        
        whiteCrossCube = (rotateIntoWhiteCross_y_3(lst_cube_from_daisy, rotation_from_daisy ))      
        for i in range(20):
            whiteCrossCube = (rotateIntoWhiteCross_y_3(whiteCrossCube[0], whiteCrossCube[1]))        
        
    elif createCubeListFromInputParms(parms)[4][4] == 'y': 
        lst_cube_from_daisy = ((rotateIntoWhiteCross_y_4(solveDaisy(parms)[0], solveDaisy(parms)[1])))[0]
        rotation_from_daisy = ((rotateIntoWhiteCross_y_4(solveDaisy(parms)[0], solveDaisy(parms)[1])))[1]        
        whiteCrossCube = (rotateIntoWhiteCross_y_4(lst_cube_from_daisy, rotation_from_daisy ))             
        for i in range(20):
            whiteCrossCube = (rotateIntoWhiteCross_y_4(whiteCrossCube[0], whiteCrossCube[1])) 
            
    elif createCubeListFromInputParms(parms)[5][4] == 'y': 
        lst_cube_from_daisy = ((rotateIntoWhiteCross_y_5(solveDaisy(parms)[0], solveDaisy(parms)[1])))[0]
        rotation_from_daisy = ((rotateIntoWhiteCross_y_5(solveDaisy(parms)[0], solveDaisy(parms)[1])))[1]        
        whiteCrossCube = (rotateIntoWhiteCross_y_5(lst_cube_from_daisy, rotation_from_daisy ))             
        for i in range(20):
            whiteCrossCube = (rotateIntoWhiteCross_y_5(whiteCrossCube[0], whiteCrossCube[1]))                  
    
    return whiteCrossCube 
