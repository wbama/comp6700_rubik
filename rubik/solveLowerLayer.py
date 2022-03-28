"""
    Created on 03/05/2022
    @author: Waldo du Toit
    program for solving the white cross
    03/26 - Solve lower layer
    
"""

from rubik.solveWhiteCross import solveWhiteCross
from rubik.solveRotations import createYellowAndWhiteVariables
from rubik.solveRotations import rotateSide_R, rotateSide_r, rotateSide_B, rotateSide_b
from rubik.solveRotations import rotateSide_L, rotateSide_l, rotateSide_U, rotateSide_u
from rubik.solveRotations import rotateSide_D, rotateSide_d, rotateSide_f, rotateSide_F
from rubik.solveRotations import front_left_trigger, front_right_trigger, right_left_trigger, right_right_trigger
from rubik.solveRotations import back_left_trigger, back_right_trigger, left_left_trigger, left_right_trigger

def solveLowerLayer(parms):
    
    var_w = createYellowAndWhiteVariables(parms)[1]
    #the input cube with the white cross
    lst_cube = solveWhiteCross(parms)[0]
    print(f"beginning cube {lst_cube}")

    str_rotations_long = "".join(solveWhiteCross(parms)[1])  
            
    last_x = str_rotations_long.rfind('x')
    str_rotations_short = str_rotations_long[:last_x]
    str_rotations_no_x = str_rotations_short.replace("x", "")
    str_rotations_no_y = str_rotations_no_x.replace("y", "")
    str_rotation_cleanup = str_rotations_no_y.replace("Dd", "")
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
    
    #get back the cleaned up rotations from making white cross. Append to this list
    lst_rotate = list(str_rotation_cleanup) 

    
    #the cross color will be whatever is at the bottom. Not always white. use var_w
    print(f"The cross color will be {var_w}")
    

    #solve the top corners
    if lst_cube[0][0] == var_w or lst_cube[0][2] == var_w or lst_cube[1][0] == var_w or \
        lst_cube[1][2] == var_w or lst_cube[2][0] == var_w or lst_cube[2][2] == var_w or \
        lst_cube[3][0] == var_w or lst_cube[3][2] == var_w:
        
        #[3][2] 
        if lst_cube[3][2] == var_w and lst_cube[0][0] == lst_cube[0][4]:
            lst_rotate.append("") 
            lst_cube = left_right_trigger(lst_cube, lst_rotate)
            
        elif lst_cube[3][2] == var_w and lst_cube[0][0] == lst_cube[3][4]:
            lst_cube = rotateSide_U(lst_cube)
            lst_rotate.append("U") 
            lst_cube = back_right_trigger(lst_cube, lst_rotate)
            
        elif lst_cube[3][2] == var_w and lst_cube[0][0] == lst_cube[2][4]:
            lst_cube = rotateSide_u(lst_cube)
            lst_cube = rotateSide_u(lst_cube)
            lst_rotate.append("uu") 
            lst_cube = right_right_trigger(lst_cube, lst_rotate)
        elif lst_cube[3][2] == var_w and lst_cube[0][0] == lst_cube[1][4]:
            lst_cube = rotateSide_u(lst_cube)
            lst_rotate.append("u") 
            lst_cube = front_right_trigger(lst_cube, lst_rotate)
        #[3][0]
        elif lst_cube[3][0] == var_w and lst_cube[2][2] == lst_cube[2][4]:
            lst_rotate.append("") 
            lst_cube = back_right_trigger(lst_cube, lst_rotate)
        elif lst_cube[3][0] == var_w and lst_cube[2][2] == lst_cube[1][4]:
            lst_cube = rotateSide_U(lst_cube)
            lst_rotate.append("U")          
            lst_cube = back_left_trigger(lst_cube, lst_rotate)

        elif lst_cube[3][0] == var_w and lst_cube[2][2] == lst_cube[0][4]:
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_rotate.append("UU") 
            lst_cube = right_left_trigger(lst_cube, lst_rotate)
        elif lst_cube[3][0] == var_w and lst_cube[2][2] == lst_cube[3][4]:
            lst_cube = rotateSide_u(lst_cube)
            lst_rotate.append("u")              
            lst_cube = front_left_trigger(lst_cube, lst_rotate)
        #[0][0] 
        elif lst_cube[0][0] == var_w and lst_cube[3][2] == lst_cube[0][4]:
            lst_cube = rotateSide_u(lst_cube)
            lst_rotate.append("u") 
            lst_cube = right_left_trigger(lst_cube, lst_rotate)
        elif lst_cube[0][0] == var_w and lst_cube[3][2] == lst_cube[1][4]:
            lst_cube = rotateSide_u(lst_cube)
            lst_cube = rotateSide_u(lst_cube)
            lst_rotate.append("uu") 
            lst_cube = back_left_trigger(lst_cube, lst_rotate)
        elif lst_cube[0][0] == var_w and lst_cube[3][2] == lst_cube[2][4]:
            lst_cube = rotateSide_U(lst_cube)
            lst_rotate.append("U") 
            lst_cube = left_left_trigger(lst_cube, lst_rotate)
        elif lst_cube[0][0] == var_w and lst_cube[3][2] == lst_cube[3][4]:
            lst_rotate.append("")     
            lst_cube = front_left_trigger(lst_cube, lst_rotate)        
        #[0][2]
        elif lst_cube[0][2] == var_w and lst_cube[1][0] == lst_cube[0][4]:
            lst_cube = rotateSide_U(lst_cube)
            lst_rotate.append("U") 
        elif lst_cube[2][2] == var_w and lst_cube[1][0] == lst_cube[1][4]:
            lst_rotate.append("") 
        elif lst_cube[0][2] == var_w and lst_cube[1][0] == lst_cube[2][4]:
            lst_cube = rotateSide_u(lst_cube)
            lst_rotate.append("u") 
        elif lst_cube[0][2] == var_w and lst_cube[1][0] == lst_cube[3][4]:
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_rotate.append("UU")                
            
        #[1][0] 
        elif lst_cube[1][0] == var_w and lst_cube[0][2] == lst_cube[0][4]:
            lst_rotate.append("") 
        elif lst_cube[1][0] == var_w and lst_cube[0][2] == lst_cube[1][4]:
            lst_cube = rotateSide_u(lst_cube)
            lst_rotate.append("u") 
        elif lst_cube[1][0] == var_w and lst_cube[0][2] == lst_cube[2][4]:
            lst_cube = rotateSide_u(lst_cube)
            lst_cube = rotateSide_u(lst_cube)
            lst_rotate.append("uu") 
        elif lst_cube[1][0] == var_w and lst_cube[0][2] == lst_cube[3][4]:
            lst_cube = rotateSide_U(lst_cube)
            lst_rotate.append("U")             
        #[1][2]
        elif lst_cube[1][2] == var_w and lst_cube[2][0] == lst_cube[0][4]:
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_rotate.append("UU") 
        elif lst_cube[1][2] == var_w and lst_cube[2][0] == lst_cube[1][4]:
            lst_cube = rotateSide_U(lst_cube)
            lst_rotate.append("U") 
            lst_cube = front_right_trigger(lst_cube, lst_rotate)
            
        elif lst_cube[1][2] == var_w and lst_cube[2][0] == lst_cube[2][4]:
            lst_rotate.append("") 
        elif lst_cube[1][2] == var_w and lst_cube[2][0] == lst_cube[3][4]:
            lst_cube = rotateSide_U(lst_cube)
            lst_rotate.append("U")  
            
            
        #[2][0] 
        elif lst_cube[2][0] == var_w and lst_cube[1][2] == lst_cube[0][4]:
            lst_cube = rotateSide_U(lst_cube)
            lst_rotate.append("U")   
        elif lst_cube[2][0] == var_w and lst_cube[1][2] == lst_cube[1][4]:
            lst_rotate.append("") 
        elif lst_cube[2][0] == var_w and lst_cube[1][2] == lst_cube[2][4]:
            lst_cube = rotateSide_u(lst_cube)
            lst_rotate.append("u") 
        elif lst_cube[2][0] == var_w and lst_cube[1][2] == lst_cube[3][4]:
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_rotate.append("UU")             
        #[2][2]
        elif lst_cube[2][2] == var_w and lst_cube[3][0] == lst_cube[0][4]:
            lst_cube = rotateSide_u(lst_cube)
            lst_rotate.append("U") 
        elif lst_cube[2][2] == var_w and lst_cube[3][0] == lst_cube[1][4]:
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_rotate.append("UU") 
        elif lst_cube[2][2] == var_w and lst_cube[3][0] == lst_cube[2][4]:
            lst_cube = rotateSide_U(lst_cube)
            lst_rotate.append("U") 
        elif lst_cube[2][2] == var_w and lst_cube[3][0] == lst_cube[3][4]:
            lst_rotate.append("")   
            
                      
        
        
    print(lst_cube)
    print(lst_rotate)    
    
    return str_rotation_cleanup

    

