"""
    Created on 02/05/2022
    @author: Waldo du Toit
    main solvec code
    
"""
from rubik.solveRotations import rotateSide_R, rotateSide_r, rotateSide_B, rotateSide_b
from rubik.solveRotations import rotateSide_L, rotateSide_l, rotateSide_U, rotateSide_u
from rubik.solveRotations import rotateSide_D, rotateSide_d, rotateSide_f, rotateSide_F
import rubik.solveCheckInput as ci
from rubik.solveRotations import createCubeListFromInputParms
from rubik.solveLowerLayer import solveLowerLayer


def _solve(parms):
    result = {}    
    str_cube = ''
    
    try:      
        #the test will give string input. Make a list cube    
        lst_cube = createCubeListFromInputParms(parms) 

        global rotate_length
        
        if ('rotate' in parms) and (parms.get('rotate')) == None:
            rotate_length = 0
        elif ('rotate' in parms) and (parms.get('rotate')) != None:
            rotate_length = len(parms.get('rotate'))
        elif 'rotate' not in parms:
            rotate_length = 0       
       
        if (rotate_length == 0 ):          
            str_rotations_long = "".join(solveLowerLayer(parms)[1])  
            print(f"string rotations {str_rotations_long}")
            str_rotation_cleanup = str_rotations_long.replace("Dd", "")
            str_rotation_cleanup = str_rotation_cleanup.replace("dD", "")
            str_rotation_cleanup = str_rotation_cleanup.replace("Rr", "")
            str_rotation_cleanup = str_rotation_cleanup.replace("rR", "")
            str_rotation_cleanup = str_rotation_cleanup.replace("Uu", "")
            str_rotation_cleanup = str_rotation_cleanup.replace("uU", "")
            str_rotation_cleanup = str_rotation_cleanup.replace("Ll", "")
            str_rotation_cleanup = str_rotation_cleanup.replace("lL", "")
            str_rotation_cleanup = str_rotation_cleanup.replace("bB", "")
            str_rotation_cleanup = str_rotation_cleanup.replace("Bb", "")
            str_rotation_cleanup = str_rotation_cleanup.replace("Ff", "")
            str_rotation_cleanup = str_rotation_cleanup.replace("fF", "")
            
 
            result['solution'] = str_rotation_cleanup
            result['status'] = 'ok' 
            
            s0=set(lst_cube[0])
            s1=set(lst_cube[1])
            s2=set(lst_cube[2])
            s3=set(lst_cube[3])
            s4=set(lst_cube[4])
            s5=set(lst_cube[5]) 
    
            #if all the sides only have one character, cube is solved, no solution
            if len(s0) == len(s1) == len(s2) == len(s3) == len(s4) == len(s5) == 1:
                result['solution'] = ""              
           
         
        if 'rotate' in parms and rotate_length > 0:
            for rotation in (parms.get('rotate')):   
            
                if rotation == 'F':
                        lst_cube = (rotateSide_F(lst_cube))                                   
                        
                elif rotation == 'f':
                    lst_cube = (rotateSide_f(lst_cube)) 
                         
                elif rotation == 'R':                   
                    lst_cube = rotateSide_R(lst_cube)     
                          
                elif rotation == 'r':
                    lst_cube = rotateSide_r(lst_cube)                          
                    
                elif rotation == 'B':
                    lst_cube = rotateSide_B(lst_cube)      
                 
                elif rotation == 'b':
                    lst_cube = rotateSide_b(lst_cube)                     
                     
                elif rotation == 'L':
                    lst_cube = rotateSide_L(lst_cube)                    
                    
                elif rotation == 'l':   
                    lst_cube = rotateSide_l(lst_cube)                       
                    
                elif rotation == 'U':
                    lst_cube = rotateSide_U(lst_cube)                      
                          
                elif rotation == 'u':
                    lst_cube = rotateSide_u(lst_cube)    
            
                elif rotation== 'D':
                    lst_cube = rotateSide_D(lst_cube) 
                    
                elif rotation == 'd':
                    lst_cube = rotateSide_d(lst_cube)      
           
            str1 = "".join(lst_cube[0])
            str2 = "".join(lst_cube[1])
            str3 = "".join(lst_cube[2])
            str4 = "".join(lst_cube[3])
            str5 = "".join(lst_cube[4])
            str6 = "".join(lst_cube[5])                       
         
            str_cube = str1+str2+str3+str4+str5+str6
                    
            result = {}
            result['cube'] = str_cube
            result['status'] = 'ok'   

       
    except:
        result = (ci.solveCheck(parms)) 
        
    else:
        if (ci.solveCheck(parms)['status']) == 'ok':
            result['cube'] = str_cube
        else:
            result = (ci.solveCheck(parms))   

    
    ######################################################
    # Cleanup
    ######################################################   
    
    #delete the cube string if giving solutions    
    if 'solution' in result:
        del result['cube'] 
    
    
    return result
 
 



