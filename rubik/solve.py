from rubik.solveRotations import rotate_cube_to_right
from rubik.solveRotations import flip_cube_top_side
from rubik.solveRotations import turn_clock
from rubik.solveRotations import turn_cclock
import rubik.solveCheckInput as ci


def _solve(parms):
    result = {}    
      
    try:           

        lst_cube = ([x for x in parms.get("cube")])
        lst_in1, lst_in2, lst_in3, lst_in4, lst_in5, lst_in6 = ([] for i in range(6)) 
    
        for i in range (1,7):
            for j in range(1,10):
                exec(f"lst_in{i}.append(lst_cube.pop(0))")  
            
        # lst_opposite_cnt = []
        for i in range(1,7):
            exec(f'lst_cube.append(lst_in{i})')
            
       
        if  parms.get("rotate") == '':
                c_rotate_cube = (turn_clock(lst_cube)) 
        
        elif parms.get("rotate") == 'F':
                c_rotate_cube = (turn_clock(lst_cube))               
            
        elif parms.get("rotate") == 'f':
            c_rotate_cube = (turn_cclock(lst_cube))          
                 
        elif parms.get("rotate") == 'R':
           
            rotate_cube_to_right(lst_cube)
            
            #rotate Right side clockwise
            c_rotate_cube = (turn_clock(lst_cube)) 
            
            rotate_cube_to_right(c_rotate_cube)
            rotate_cube_to_right(c_rotate_cube)
            rotate_cube_to_right(c_rotate_cube)          
                  
        elif parms.get("rotate") == 'r':
            c_rotate_cube = (turn_cclock(lst_cube))        
          
            rotate_cube_to_right(lst_cube)
            
            #rotate Right side clockwise
            c_rotate_cube = (turn_cclock(lst_cube)) 
            
            rotate_cube_to_right(c_rotate_cube)
            rotate_cube_to_right(c_rotate_cube)
            rotate_cube_to_right(c_rotate_cube)  
                  
            
        elif parms.get("rotate") == 'B':
            
            rotate_cube_to_right(lst_cube)
            rotate_cube_to_right(lst_cube)
            
            #rotate Right side clockwise
            c_rotate_cube = (turn_clock(lst_cube))         
            
            rotate_cube_to_right(c_rotate_cube)
            rotate_cube_to_right(c_rotate_cube)          
         
        elif parms.get("rotate") == 'b':
            rotate_cube_to_right(lst_cube)
            rotate_cube_to_right(lst_cube)
            
            #rotate Right side clockwise
            c_rotate_cube = (turn_cclock(lst_cube))         
            
            rotate_cube_to_right(c_rotate_cube)
            rotate_cube_to_right(c_rotate_cube) 
           
             
        elif parms.get("rotate") == 'L':
          
            rotate_cube_to_right(lst_cube)
            rotate_cube_to_right(lst_cube)
            rotate_cube_to_right(lst_cube)
            
            #rotate Right side clockwise
            c_rotate_cube = (turn_clock(lst_cube))       
            
            rotate_cube_to_right(c_rotate_cube)     
            
            
        elif parms.get("rotate") == 'l':        
            
            rotate_cube_to_right(lst_cube)
            rotate_cube_to_right(lst_cube)
            rotate_cube_to_right(lst_cube)
            
            #rotate Right side clockwise
            c_rotate_cube = (turn_cclock(lst_cube))       
            
            rotate_cube_to_right(c_rotate_cube)  
               
            
        elif parms.get("rotate") == 'U':
            
            flip_cube_one = flip_cube_top_side(lst_cube)
            c_rotate_cube = (turn_clock(flip_cube_one)) 
            flip_cube_two = flip_cube_top_side(c_rotate_cube)
            flip_cube_three= flip_cube_top_side(flip_cube_two)
            c_rotate_cube= flip_cube_top_side(flip_cube_three)   
              
                  
        elif parms.get("rotate") == 'u':
            
            flip_cube_one = flip_cube_top_side(lst_cube)
            c_rotate_cube = (turn_cclock(flip_cube_one)) 
            flip_cube_two = flip_cube_top_side(c_rotate_cube)
            flip_cube_three= flip_cube_top_side(flip_cube_two)
            c_rotate_cube= flip_cube_top_side(flip_cube_three)        
    
        elif parms.get("rotate") == 'D':
             
            flip_cube_one = flip_cube_top_side(lst_cube)        
            flip_cube_two = flip_cube_top_side(flip_cube_one)
            flip_cube_three = flip_cube_top_side(flip_cube_two)
            c_rotate_cube = (turn_clock(flip_cube_three))
            flip_cube_four = flip_cube_top_side(c_rotate_cube)
            c_rotate_cube= flip_cube_four
            
        elif parms.get("rotate") == 'd':
            flip_cube_one = flip_cube_top_side(lst_cube)        
            flip_cube_two = flip_cube_top_side(flip_cube_one)
            flip_cube_three = flip_cube_top_side(flip_cube_two)
            c_rotate_cube = (turn_cclock(flip_cube_three)) 
            flip_cube_four = flip_cube_top_side(c_rotate_cube)
            c_rotate_cube= flip_cube_four
            
        else:
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
        if 'rotate' in parms:
            result['rotate'] = parms.get("rotate")
        result['op'] = 'solve'
        result['status'] = 'ok'   

       
    except:
        result = (ci.solveCheck(parms)) 
        
    else:
        if (ci.solveCheck(parms)['status']) == 'ok':
            result['cube'] = str_cube
            if 'rotate' in parms:
                result['rotate'] = (parms.get("rotate"))
            result['op'] = 'solve'
        else:
            result = (ci.solveCheck(parms))             
        
    
    return result
 
 
 
 

#    inputs:
#        parms: dictionary input that is validated. Do not have to validate i
#        parms['op'] have to validate the keys ['op'] string, "solve", mandatory, arrives validated
#        parms['cube'] string; len = 54 chars [azAZ09], 9 occurences of each character, 6 distinct characters, 
#               middle will be one of the six; mandatory; arrives unvalidated
#        parms['rotate'] string; len >=0, [FfRrBbLlUuDd]; optional, defaulting to F if missing; arrives unvalidated

# validate my parms, if invalid, need to return status with error
# if everything is valid, load parms into cube model
# then rotate the cube model in the desired direction
# serialize the cube model in encoded cube into a string
# return the string result + status of "ok"


# but have to write the test code first


