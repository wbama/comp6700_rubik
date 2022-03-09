from rubik.solveRotations import rotateCubeToLeft
from rubik.solveRotations import rotateCubeDown
from rubik.solveRotations import rotateSide_F
from rubik.solveRotations import rotateSide_f
import rubik.solveCheckInput as ci
from rubik.solveRotations import createCubeListFromInputParms
from rubik.solveWhiteCross import solveWhiteCross


def _solve(parms):
    result = {}    
    str_cube = ''
      
    try:         

 
        lst_cube = createCubeListFromInputParms(parms)           
       
       
        if 'rotate' not in parms:
            lst_cube = solveWhiteCross(parms)[0]
            str1 = "".join(lst_cube[0])
            str2 = "".join(lst_cube[1])
            str3 = "".join(lst_cube[2])
            str4 = "".join(lst_cube[3])
            str5 = "".join(lst_cube[4])
            str6 = "".join(lst_cube[5])                       
         
            str_cube = str1+str2+str3+str4+str5+str6   
            str_rotations = "".join(solveWhiteCross(parms)[1])                  
            result = {}
            result['cube'] = str_cube
            result['status'] = 'ok' 
            result['rotate'] = str_rotations
                
        if 'rotate' in parms and (parms.get('rotate')) == None:
                c_rotate_cube = (rotateSide_F(lst_cube)) 
                str1 = "".join(c_rotate_cube[0])
                str2 = "".join(c_rotate_cube[1])
                str3 = "".join(c_rotate_cube[2])
                str4 = "".join(c_rotate_cube[3])
                str5 = "".join(c_rotate_cube[4])
                str6 = "".join(c_rotate_cube[5])                       
         
                str_cube = str1+str2+str3+str4+str5+str6                    
                result = {}
                result['cube'] = str_cube
                result['status'] = 'ok' 
                
        if ('rotate' in parms) and (parms.get('rotate')) == None:
            rotate_length = 0
        elif ('rotate' in parms) and (parms.get('rotate')) != None:
            rotate_length = len(parms.get('rotate'))
        elif 'rotate' not in parms:
            rotate_length = 0           
  
            
        if ('rotate' in parms and rotate_length == 0):
            
            c_rotate_cube = (rotateSide_F(lst_cube)) 
            str1 = "".join(c_rotate_cube[0])
            str2 = "".join(c_rotate_cube[1])
            str3 = "".join(c_rotate_cube[2])
            str4 = "".join(c_rotate_cube[3])
            str5 = "".join(c_rotate_cube[4])
            str6 = "".join(c_rotate_cube[5])                       
             
            str_cube = str1+str2+str3+str4+str5+str6                    
            result = {}
            result['cube'] = str_cube
            result['status'] = 'ok'   
        
        if 'rotate' in parms and rotate_length > 0:
            for rotation in (parms.get('rotate')):   
            
                if rotation == 'F':
                        lst_cube = (rotateSide_F(lst_cube))                                   
                        
                elif rotation == 'f':
                    lst_cube = (rotateSide_f(lst_cube)) 
                         
                elif rotation == 'R':
                   
                    rotateCubeToLeft(lst_cube)
                    
                    #rotate Right side clockwise
                    c_rotate_cube = (rotateSide_F(lst_cube)) 
                    
                    rotateCubeToLeft(c_rotate_cube)
                    rotateCubeToLeft(c_rotate_cube)
                    rotateCubeToLeft(c_rotate_cube)   
                    lst_cube =  c_rotate_cube      
                          
                elif rotation == 'r':
                    c_rotate_cube = (rotateSide_f(lst_cube))        
                  
                    rotateCubeToLeft(lst_cube)
                    
                    #rotate Right side clockwise
                    c_rotate_cube = (rotateSide_f(lst_cube)) 
                    
                    rotateCubeToLeft(c_rotate_cube)
                    rotateCubeToLeft(c_rotate_cube)
                    rotateCubeToLeft(c_rotate_cube) 
                    lst_cube =  c_rotate_cube
                          
                    
                elif rotation == 'B':
                    
                    rotateCubeToLeft(lst_cube)
                    rotateCubeToLeft(lst_cube)
                    
                    #rotate Right side clockwise
                    c_rotate_cube = (rotateSide_F(lst_cube))         
                    
                    rotateCubeToLeft(c_rotate_cube)
                    rotateCubeToLeft(c_rotate_cube) 
                    lst_cube =  c_rotate_cube         
                 
                elif rotation == 'b':
                    rotateCubeToLeft(lst_cube)
                    rotateCubeToLeft(lst_cube)
                    
                    #rotate Right side clockwise
                    c_rotate_cube = (rotateSide_f(lst_cube))         
                    
                    rotateCubeToLeft(c_rotate_cube)
                    rotateCubeToLeft(c_rotate_cube)
                    lst_cube =  c_rotate_cube 
                   
                     
                elif rotation == 'L':
                  
                    rotateCubeToLeft(lst_cube)
                    rotateCubeToLeft(lst_cube)
                    rotateCubeToLeft(lst_cube)
                    
                    #rotate Right side clockwise
                    c_rotate_cube = (rotateSide_F(lst_cube))       
                    
                    rotateCubeToLeft(c_rotate_cube) 
                    lst_cube =  c_rotate_cube    
                    
                    
                elif rotation == 'l':        
                    
                    rotateCubeToLeft(lst_cube)
                    rotateCubeToLeft(lst_cube)
                    rotateCubeToLeft(lst_cube)
                    
                    #rotate Right side clockwise
                    c_rotate_cube = (rotateSide_f(lst_cube))       
                    
                    rotateCubeToLeft(c_rotate_cube)  
                    lst_cube =  c_rotate_cube
                       
                    
                elif rotation == 'U':
                    
                    flip_cube_one = rotateCubeDown(lst_cube)
                    c_rotate_cube = (rotateSide_F(flip_cube_one)) 
                    flip_cube_two = rotateCubeDown(c_rotate_cube)
                    flip_cube_three= rotateCubeDown(flip_cube_two)
                    c_rotate_cube= rotateCubeDown(flip_cube_three)  
                    lst_cube =  c_rotate_cube 
                      
                          
                elif rotation == 'u':
                    
                    flip_cube_one = rotateCubeDown(lst_cube)
                    c_rotate_cube = (rotateSide_f(flip_cube_one)) 
                    flip_cube_two = rotateCubeDown(c_rotate_cube)
                    flip_cube_three= rotateCubeDown(flip_cube_two)
                    c_rotate_cube= rotateCubeDown(flip_cube_three) 
                    lst_cube =  c_rotate_cube       
            
                elif rotation== 'D':
                     
                    flip_cube_one = rotateCubeDown(lst_cube)        
                    flip_cube_two = rotateCubeDown(flip_cube_one)
                    flip_cube_three = rotateCubeDown(flip_cube_two)
                    c_rotate_cube = (rotateSide_F(flip_cube_three))
                    flip_cube_four = rotateCubeDown(c_rotate_cube)
                    c_rotate_cube= flip_cube_four
                    lst_cube =  c_rotate_cube
                    
                elif rotation == 'd':
                    flip_cube_one = rotateCubeDown(lst_cube)        
                    flip_cube_two = rotateCubeDown(flip_cube_one)
                    flip_cube_three = rotateCubeDown(flip_cube_two)
                    c_rotate_cube = (rotateSide_f(flip_cube_three)) 
                    flip_cube_four = rotateCubeDown(c_rotate_cube)
                    c_rotate_cube= flip_cube_four
                    lst_cube =  c_rotate_cube
            
                # else:
                #     c_rotate_cube = (rotateSide_F(lst_cube))         
           
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
        
    
    return result
 
 



