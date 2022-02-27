def stringjoins(lst_cube):
    c_rotate_cube = (turn_clock(lst_cube)) 
    str1 = "".join(c_rotate_cube[0])
    str2 = "".join(c_rotate_cube[1])
    str3 = "".join(c_rotate_cube[2])
    str4 = "".join(c_rotate_cube[3])
    str5 = "".join(c_rotate_cube[4])
    str6 = "".join(c_rotate_cube[5])                       
         
    str_cube = str1+str2+str3+str4+str5+str6     
    return str_cube 

