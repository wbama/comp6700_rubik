from rubik.solveRotations import rotate_cube_to_right
from rubik.solveRotations import flip_cube_top_side
from rubik.solveRotations import turn_clock
from rubik.solveRotations import turn_cclock
from rubik.solveRotations import stringjoins
import rubik.solveCheckInput as ci


def _solve(parms):
    result = {}    
    str_cube = ''
      
    try:         

        lst_cube = ([x for x in parms.get("cube")])
        lst_in1, lst_in2, lst_in3, lst_in4, lst_in5, lst_in6 = ([] for i in range(6)) 
    
        for i in range (1,7):
            for j in range(1,10):
                exec(f"lst_in{i}.append(lst_cube.pop(0))")  
            
        for i in range(1,7):
            exec(f'lst_cube.append(lst_in{i})')            
       
       
        if 'rotate' not in parms:
                # c_rotate_cube = (turn_clock(lst_cube)) 
                # str1 = "".join(c_rotate_cube[0])
                # str2 = "".join(c_rotate_cube[1])
                # str3 = "".join(c_rotate_cube[2])
                # str4 = "".join(c_rotate_cube[3])
                # str5 = "".join(c_rotate_cube[4])
                # str6 = "".join(c_rotate_cube[5])                       
                #
                # str_cube = str1+str2+str3+str4+str5+str6  
                print(str_cube)                 
                result = {}
                result['cube'] = stringjoins(lst_cube)
                result['status'] = 'ok' 
                
        if 'rotate' in parms and (parms.get('rotate')) == None:
                c_rotate_cube = (turn_clock(lst_cube)) 
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
            
            c_rotate_cube = (turn_clock(lst_cube)) 
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
                        lst_cube = (turn_clock(lst_cube))                                   
                        
                elif rotation == 'f':
                    lst_cube = (turn_cclock(lst_cube)) 
                         
                elif rotation == 'R':
                   
                    rotate_cube_to_right(lst_cube)
                    
                    #rotate Right side clockwise
                    c_rotate_cube = (turn_clock(lst_cube)) 
                    
                    rotate_cube_to_right(c_rotate_cube)
                    rotate_cube_to_right(c_rotate_cube)
                    rotate_cube_to_right(c_rotate_cube)   
                    lst_cube =  c_rotate_cube      
                          
                elif rotation == 'r':
                    c_rotate_cube = (turn_cclock(lst_cube))        
                  
                    rotate_cube_to_right(lst_cube)
                    
                    #rotate Right side clockwise
                    c_rotate_cube = (turn_cclock(lst_cube)) 
                    
                    rotate_cube_to_right(c_rotate_cube)
                    rotate_cube_to_right(c_rotate_cube)
                    rotate_cube_to_right(c_rotate_cube) 
                    lst_cube =  c_rotate_cube
                          
                    
                elif rotation == 'B':
                    
                    rotate_cube_to_right(lst_cube)
                    rotate_cube_to_right(lst_cube)
                    
                    #rotate Right side clockwise
                    c_rotate_cube = (turn_clock(lst_cube))         
                    
                    rotate_cube_to_right(c_rotate_cube)
                    rotate_cube_to_right(c_rotate_cube) 
                    lst_cube =  c_rotate_cube         
                 
                elif rotation == 'b':
                    rotate_cube_to_right(lst_cube)
                    rotate_cube_to_right(lst_cube)
                    
                    #rotate Right side clockwise
                    c_rotate_cube = (turn_cclock(lst_cube))         
                    
                    rotate_cube_to_right(c_rotate_cube)
                    rotate_cube_to_right(c_rotate_cube)
                    lst_cube =  c_rotate_cube 
                   
                     
                elif rotation == 'L':
                  
                    rotate_cube_to_right(lst_cube)
                    rotate_cube_to_right(lst_cube)
                    rotate_cube_to_right(lst_cube)
                    
                    #rotate Right side clockwise
                    c_rotate_cube = (turn_clock(lst_cube))       
                    
                    rotate_cube_to_right(c_rotate_cube) 
                    lst_cube =  c_rotate_cube    
                    
                    
                elif rotation == 'l':        
                    
                    rotate_cube_to_right(lst_cube)
                    rotate_cube_to_right(lst_cube)
                    rotate_cube_to_right(lst_cube)
                    
                    #rotate Right side clockwise
                    c_rotate_cube = (turn_cclock(lst_cube))       
                    
                    rotate_cube_to_right(c_rotate_cube)  
                    lst_cube =  c_rotate_cube
                       
                    
                elif rotation == 'U':
                    
                    flip_cube_one = flip_cube_top_side(lst_cube)
                    c_rotate_cube = (turn_clock(flip_cube_one)) 
                    flip_cube_two = flip_cube_top_side(c_rotate_cube)
                    flip_cube_three= flip_cube_top_side(flip_cube_two)
                    c_rotate_cube= flip_cube_top_side(flip_cube_three)  
                    lst_cube =  c_rotate_cube 
                      
                          
                elif rotation == 'u':
                    
                    flip_cube_one = flip_cube_top_side(lst_cube)
                    c_rotate_cube = (turn_cclock(flip_cube_one)) 
                    flip_cube_two = flip_cube_top_side(c_rotate_cube)
                    flip_cube_three= flip_cube_top_side(flip_cube_two)
                    c_rotate_cube= flip_cube_top_side(flip_cube_three) 
                    lst_cube =  c_rotate_cube       
            
                elif rotation== 'D':
                     
                    flip_cube_one = flip_cube_top_side(lst_cube)        
                    flip_cube_two = flip_cube_top_side(flip_cube_one)
                    flip_cube_three = flip_cube_top_side(flip_cube_two)
                    c_rotate_cube = (turn_clock(flip_cube_three))
                    flip_cube_four = flip_cube_top_side(c_rotate_cube)
                    c_rotate_cube= flip_cube_four
                    lst_cube =  c_rotate_cube
                    
                elif rotation == 'd':
                    flip_cube_one = flip_cube_top_side(lst_cube)        
                    flip_cube_two = flip_cube_top_side(flip_cube_one)
                    flip_cube_three = flip_cube_top_side(flip_cube_two)
                    c_rotate_cube = (turn_cclock(flip_cube_three)) 
                    flip_cube_four = flip_cube_top_side(c_rotate_cube)
                    c_rotate_cube= flip_cube_four
                    lst_cube =  c_rotate_cube
            
                # else:
                #     c_rotate_cube = (turn_clock(lst_cube))         
           
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
 
 



