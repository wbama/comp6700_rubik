"""
    Created on 03/05/2022
    @author: Waldo du Toit
    all functions used to solve the white cross, daisy or final solve
    
"""
        #this function looks at the colors around the edge and compares to the back colors to add to counter
        
def verifyAdjacentColors(lst_cube):

    ctr = 0     

    if ((lst_cube[0][0]) == lst_cube[0][4] and lst_cube[2][4] in [lst_cube[3][2],lst_cube[4][6]]):
        ctr = 1        
    elif ((lst_cube[0][1]) == lst_cube[0][4] and lst_cube[2][4] == lst_cube[4][7]):
        ctr = 1
    elif ((lst_cube[0][2]) == lst_cube[0][4] and lst_cube[2][4] in [lst_cube[4][8],lst_cube[1][0]]):
        ctr = 1
    elif ((lst_cube[0][3]) == lst_cube[0][4] and lst_cube[2][4] == lst_cube[3][5]):
        ctr = 1
    elif ((lst_cube[0][5]) == lst_cube[0][4] and lst_cube[2][4] == lst_cube[1][3]):
        ctr = 1
    elif ((lst_cube[0][6]) == lst_cube[0][4] and lst_cube[2][4] in [lst_cube[3][8],lst_cube[5][0]]):
        ctr = 1   
    elif ((lst_cube[0][7]) == lst_cube[0][4] and lst_cube[2][4] == lst_cube[5][1]):
        ctr = 1
    elif ((lst_cube[0][8]) == lst_cube[0][4] and lst_cube[2][4] in [lst_cube[1][6],lst_cube[5][2]]):
        ctr = 1

    #top right corner
    elif ((lst_cube[4][8]) == lst_cube[0][4] and lst_cube[2][4] == lst_cube[1][0]):
        ctr = 1   
    elif ((lst_cube[4][8]) == lst_cube[2][4] and lst_cube[0][4] == lst_cube[1][0]):
        ctr = 1   
    elif ((lst_cube[4][5]) == lst_cube[0][4] and lst_cube[2][4] == lst_cube[1][1]):
        ctr = 1   
    elif ((lst_cube[4][5]) == lst_cube[2][4] and lst_cube[0][4] == lst_cube[1][1]):
        ctr = 1            
    elif ((lst_cube[4][2]) == lst_cube[0][4] and lst_cube[2][4] == lst_cube[1][2]):
        ctr = 1   
    elif ((lst_cube[4][2]) == lst_cube[2][4] and lst_cube[0][4] == lst_cube[1][2]):
        ctr = 1   

    #top left corner    
    elif ((lst_cube[4][6]) == lst_cube[0][4] and lst_cube[2][4] == lst_cube[3][2]):
        ctr = 1   
    elif ((lst_cube[4][6]) == lst_cube[2][4] and lst_cube[0][4] == lst_cube[3][2]):
        ctr = 1   
    elif ((lst_cube[4][3]) == lst_cube[0][4] and lst_cube[2][4] == lst_cube[3][1]):
        ctr = 1    
    elif ((lst_cube[4][3]) == lst_cube[2][4] and lst_cube[0][4] == lst_cube[3][1]):
        ctr = 1    
    elif ((lst_cube[4][0]) == lst_cube[0][4] and lst_cube[2][4] == lst_cube[3][0]):
        ctr = 1   
    elif ((lst_cube[4][0]) == lst_cube[2][4] and lst_cube[0][4] == lst_cube[3][0]):
        ctr = 1   

    #bottom right row
    elif ((lst_cube[5][2]) == lst_cube[0][4] and lst_cube[2][4] == lst_cube[1][6]):
        ctr = 1  
    elif ((lst_cube[5][2]) == lst_cube[2][4] and lst_cube[0][4] == lst_cube[1][6]):
        ctr = 1  
    elif ((lst_cube[5][5]) == lst_cube[0][4] and lst_cube[2][4] == lst_cube[1][7]):
        ctr = 1   
    elif ((lst_cube[5][5]) == lst_cube[2][4] and lst_cube[0][4] == lst_cube[1][7]):
        ctr = 1          
    elif ((lst_cube[5][8]) == lst_cube[0][4] and lst_cube[2][4] == lst_cube[1][8]):
        ctr = 1   
    elif ((lst_cube[5][8]) == lst_cube[2][4] and lst_cube[0][4] == lst_cube[1][8]):
        ctr = 1   

    #bottom left row        
    elif ((lst_cube[5][0]) == lst_cube[0][4] and lst_cube[2][4] == lst_cube[3][8]):
        ctr = 1  
    elif ((lst_cube[5][0]) == lst_cube[2][4] and lst_cube[0][4] == lst_cube[3][8]):
        ctr = 1  
    elif ((lst_cube[5][3]) == lst_cube[0][4] and lst_cube[2][4] == lst_cube[3][7]):
        ctr = 1    
    elif ((lst_cube[5][3]) == lst_cube[2][4] and lst_cube[0][4] == lst_cube[3][7]):
        ctr = 1 
    elif ((lst_cube[5][6]) == lst_cube[0][4] and lst_cube[2][4] == lst_cube[3][6]):
        ctr = 1 
    elif ((lst_cube[5][6]) == lst_cube[2][4] and lst_cube[0][4] == lst_cube[3][6]):
        ctr = 1           

    return ctr   

# here y is always top, w is always bottom. Easier
def createYellowAndWhiteVariables(parms):
    global var_y, var_w
    lst_cube = createCubeListFromInputParms(parms)
    var_y = lst_cube[4][4]
    var_w = lst_cube[5][4]

    return var_y, var_w

#rotate the front side clockwise
def rotateSide_F_front (new_cube, orig_cube):
    new_cube[0].insert(0, orig_cube [0][6])
    new_cube[0].insert(1, orig_cube [0][3])
    new_cube[0].insert(2, orig_cube [0][0])
    new_cube[0].insert(3, orig_cube [0][7])
    new_cube[0].insert(4, orig_cube [0][4])
    new_cube[0].insert(5, orig_cube [0][1])
    new_cube[0].insert(6, orig_cube [0][8])
    new_cube[0].insert(7, orig_cube [0][5])
    new_cube[0].insert(8, orig_cube [0][2])
    
def rotateSide_F_right (new_cube, orig_cube):
    new_cube[1].insert(0, orig_cube [4][6])
    new_cube[1].insert(1, orig_cube [1][1])
    new_cube[1].insert(2, orig_cube [1][2])
    new_cube[1].insert(3, orig_cube [4][7])
    new_cube[1].insert(4, orig_cube [1][4])
    new_cube[1].insert(5, orig_cube [1][5])
    new_cube[1].insert(6, orig_cube [4][8])
    new_cube[1].insert(7, orig_cube [1][7])
    new_cube[1].insert(8, orig_cube [1][8])
    
def rotateSide_F_back (new_cube, orig_cube):
    new_cube[2].insert(0, orig_cube [2][0])
    new_cube[2].insert(1, orig_cube [2][1])
    new_cube[2].insert(2, orig_cube [2][2])
    new_cube[2].insert(3, orig_cube [2][3])
    new_cube[2].insert(4, orig_cube [2][4])
    new_cube[2].insert(5, orig_cube [2][5])
    new_cube[2].insert(6, orig_cube [2][6])
    new_cube[2].insert(7, orig_cube [2][7])
    new_cube[2].insert(8, orig_cube [2][8])
    
def rotateSide_F_left (new_cube, orig_cube):
    new_cube[3].insert(0, orig_cube [3][0])
    new_cube[3].insert(1, orig_cube [3][1])
    new_cube[3].insert(2, orig_cube [5][0])
    new_cube[3].insert(3, orig_cube [3][3])
    new_cube[3].insert(4, orig_cube [3][4])
    new_cube[3].insert(5, orig_cube [5][1])
    new_cube[3].insert(6, orig_cube [3][6])
    new_cube[3].insert(7, orig_cube [3][7])
    new_cube[3].insert(8, orig_cube [5][2])
    
def rotateSide_F_top (new_cube, orig_cube):
    new_cube[4].insert(0, orig_cube [4][0])
    new_cube[4].insert(1, orig_cube [4][1])
    new_cube[4].insert(2, orig_cube [4][2])
    new_cube[4].insert(3, orig_cube [4][3])
    new_cube[4].insert(4, orig_cube [4][4])
    new_cube[4].insert(5, orig_cube [4][5])
    new_cube[4].insert(6, orig_cube [3][8])
    new_cube[4].insert(7, orig_cube [3][5])
    new_cube[4].insert(8, orig_cube [3][2])
    
def rotateSide_F_bottom (new_cube, orig_cube):
    new_cube[5].insert(0, orig_cube [1][6])
    new_cube[5].insert(1, orig_cube [1][3])
    new_cube[5].insert(2, orig_cube [1][0])
    new_cube[5].insert(3, orig_cube [5][3])
    new_cube[5].insert(4, orig_cube [5][4])
    new_cube[5].insert(5, orig_cube [5][5])
    new_cube[5].insert(6, orig_cube [5][6])
    new_cube[5].insert(7, orig_cube [5][7])
    new_cube[5].insert(8, orig_cube [5][8])
    
def rotateSide_F(orig_cube):
    new_cube = [[], [], [], [], [], []]
    #front
    rotateSide_F_front (new_cube, orig_cube)    
    #right    
    rotateSide_F_right (new_cube, orig_cube)    
    #back    
    rotateSide_F_back (new_cube, orig_cube)    
    #left    
    rotateSide_F_left (new_cube, orig_cube)    
    #top    
    rotateSide_F_top (new_cube, orig_cube)    
    #bottom    
    rotateSide_F_bottom (new_cube, orig_cube)
    return new_cube

def rotateSide_f_front(new_cube, orig_cube):
    new_cube[0].insert(0, orig_cube [0][2])
    new_cube[0].insert(1, orig_cube [0][5])
    new_cube[0].insert(2, orig_cube [0][8])
    new_cube[0].insert(3, orig_cube [0][1])
    new_cube[0].insert(4, orig_cube [0][4])
    new_cube[0].insert(5, orig_cube [0][7])
    new_cube[0].insert(6, orig_cube [0][0])
    new_cube[0].insert(7, orig_cube [0][3])
    new_cube[0].insert(8, orig_cube [0][6])
    
def rotateSide_f_right(new_cube, orig_cube):
    new_cube[1].insert(0, orig_cube [5][2])
    new_cube[1].insert(1, orig_cube [1][1])
    new_cube[1].insert(2, orig_cube [1][2])
    new_cube[1].insert(3, orig_cube [5][1])
    new_cube[1].insert(4, orig_cube [1][4])
    new_cube[1].insert(5, orig_cube [1][5])
    new_cube[1].insert(6, orig_cube [5][0])
    new_cube[1].insert(7, orig_cube [1][7])
    new_cube[1].insert(8, orig_cube [1][8])
    
def rotateSide_f_back(new_cube, orig_cube):
    new_cube[2].insert(0, orig_cube [2][0])
    new_cube[2].insert(1, orig_cube [2][1])
    new_cube[2].insert(2, orig_cube [2][2])
    new_cube[2].insert(3, orig_cube [2][3])
    new_cube[2].insert(4, orig_cube [2][4])
    new_cube[2].insert(5, orig_cube [2][5])
    new_cube[2].insert(6, orig_cube [2][6])
    new_cube[2].insert(7, orig_cube [2][7])
    new_cube[2].insert(8, orig_cube [2][8])
    
def rotateSide_f_left(new_cube, orig_cube):
    new_cube[3].insert(0, orig_cube [3][0])
    new_cube[3].insert(1, orig_cube [3][1])
    new_cube[3].insert(2, orig_cube [4][8])
    new_cube[3].insert(3, orig_cube [3][3])
    new_cube[3].insert(4, orig_cube [3][4])
    new_cube[3].insert(5, orig_cube [4][7])
    new_cube[3].insert(6, orig_cube [3][6])
    new_cube[3].insert(7, orig_cube [3][7])
    new_cube[3].insert(8, orig_cube [4][6])
    
def rotateSide_f_top(new_cube, orig_cube):
    new_cube[4].insert(0, orig_cube [4][0])
    new_cube[4].insert(1, orig_cube [4][1])
    new_cube[4].insert(2, orig_cube [4][2])
    new_cube[4].insert(3, orig_cube [4][3])
    new_cube[4].insert(4, orig_cube [4][4])
    new_cube[4].insert(5, orig_cube [4][5])
    new_cube[4].insert(6, orig_cube [1][0])
    new_cube[4].insert(7, orig_cube [1][3])
    new_cube[4].insert(8, orig_cube [1][6])
    
def rotateSide_f_bottom(new_cube, orig_cube):
    new_cube[5].insert(0, orig_cube [3][2])
    new_cube[5].insert(1, orig_cube [3][5])
    new_cube[5].insert(2, orig_cube [3][8])
    new_cube[5].insert(3, orig_cube [5][3])
    new_cube[5].insert(4, orig_cube [5][4])
    new_cube[5].insert(5, orig_cube [5][5])
    new_cube[5].insert(6, orig_cube [5][6])
    new_cube[5].insert(7, orig_cube [5][7])
    new_cube[5].insert(8, orig_cube [5][8])

def rotateSide_f(orig_cube):
    new_cube = [[], [], [], [], [], []]
    #front
    rotateSide_f_front(new_cube, orig_cube)    
    #right- takes from 5
    rotateSide_f_right(new_cube, orig_cube)    
    #back  - stays same  
    rotateSide_f_back(new_cube, orig_cube)    
    #left - takes from 4
    rotateSide_f_left(new_cube, orig_cube)    
    #top - takes from 1  
    rotateSide_f_top(new_cube, orig_cube)    
    #bottom - takes from 3
    rotateSide_f_bottom(new_cube, orig_cube)
    return new_cube

def rotateSide_R_front(new_cube, orig_cube):
    new_cube[0].insert(0, orig_cube [0][0])
    new_cube[0].insert(1, orig_cube [0][1])
    new_cube[0].insert(2, orig_cube [5][2])
    new_cube[0].insert(3, orig_cube [0][3])
    new_cube[0].insert(4, orig_cube [0][4])
    new_cube[0].insert(5, orig_cube [5][5])
    new_cube[0].insert(6, orig_cube [0][6])
    new_cube[0].insert(7, orig_cube [0][7])
    new_cube[0].insert(8, orig_cube [5][8])
    
def rotateSide_R_right(new_cube, orig_cube):
    new_cube[1].insert(0, orig_cube [1][6])
    new_cube[1].insert(1, orig_cube [1][3])
    new_cube[1].insert(2, orig_cube [1][0])
    new_cube[1].insert(3, orig_cube [1][7])
    new_cube[1].insert(4, orig_cube [1][4])
    new_cube[1].insert(5, orig_cube [1][1])
    new_cube[1].insert(6, orig_cube [1][8])
    new_cube[1].insert(7, orig_cube [1][5])
    new_cube[1].insert(8, orig_cube [1][2])    
    
def rotateSide_R_back(new_cube, orig_cube):   
    new_cube[2].insert(0, orig_cube [4][8])
    new_cube[2].insert(1, orig_cube [2][1])
    new_cube[2].insert(2, orig_cube [2][2])
    new_cube[2].insert(3, orig_cube [4][5])
    new_cube[2].insert(4, orig_cube [2][4])
    new_cube[2].insert(5, orig_cube [2][5])
    new_cube[2].insert(6, orig_cube [4][2])
    new_cube[2].insert(7, orig_cube [2][7])
    new_cube[2].insert(8, orig_cube [2][8])  
     
def rotateSide_R_left(new_cube, orig_cube):  
    new_cube[3].insert(0, orig_cube [3][0])
    new_cube[3].insert(1, orig_cube [3][1])
    new_cube[3].insert(2, orig_cube [3][2])
    new_cube[3].insert(3, orig_cube [3][3])
    new_cube[3].insert(4, orig_cube [3][4])
    new_cube[3].insert(5, orig_cube [3][5])
    new_cube[3].insert(6, orig_cube [3][6])
    new_cube[3].insert(7, orig_cube [3][7])
    new_cube[3].insert(8, orig_cube [3][8])  
    
def rotateSide_R_top(new_cube, orig_cube): 
    new_cube[4].insert(0, orig_cube [4][0])
    new_cube[4].insert(1, orig_cube [4][1])
    new_cube[4].insert(2, orig_cube [0][2])
    new_cube[4].insert(3, orig_cube [4][3])
    new_cube[4].insert(4, orig_cube [4][4])
    new_cube[4].insert(5, orig_cube [0][5])
    new_cube[4].insert(6, orig_cube [4][6])
    new_cube[4].insert(7, orig_cube [4][7])
    new_cube[4].insert(8, orig_cube [0][8]) 
    
def rotateSide_R_bottom(new_cube, orig_cube):      
    new_cube[5].insert(0, orig_cube [5][0])
    new_cube[5].insert(1, orig_cube [5][1])
    new_cube[5].insert(2, orig_cube [2][6])
    new_cube[5].insert(3, orig_cube [5][3])
    new_cube[5].insert(4, orig_cube [5][4])
    new_cube[5].insert(5, orig_cube [2][3])
    new_cube[5].insert(6, orig_cube [5][6])
    new_cube[5].insert(7, orig_cube [5][7])
    new_cube[5].insert(8, orig_cube [2][0])
    
#rotate right side clockwise
def rotateSide_R(orig_cube):
    new_cube = [[], [], [], [], [], []]
    
    rotateSide_R_front(new_cube, orig_cube)     
    rotateSide_R_right(new_cube, orig_cube)         
    rotateSide_R_back(new_cube, orig_cube)         
    rotateSide_R_left(new_cube, orig_cube)             
    rotateSide_R_top(new_cube, orig_cube)            
    rotateSide_R_bottom(new_cube, orig_cube) 
    return new_cube


def rotateSide_r_front(new_cube, orig_cube):
    new_cube[0].insert(0, orig_cube [0][0])
    new_cube[0].insert(1, orig_cube [0][1])
    new_cube[0].insert(2, orig_cube [4][2])
    new_cube[0].insert(3, orig_cube [0][3])
    new_cube[0].insert(4, orig_cube [0][4])
    new_cube[0].insert(5, orig_cube [4][5])
    new_cube[0].insert(6, orig_cube [0][6])
    new_cube[0].insert(7, orig_cube [0][7])
    new_cube[0].insert(8, orig_cube [4][8])
    
def rotateSide_r_right(new_cube, orig_cube):
    new_cube[1].insert(0, orig_cube [1][2])
    new_cube[1].insert(1, orig_cube [1][5])
    new_cube[1].insert(2, orig_cube [1][8])
    new_cube[1].insert(3, orig_cube [1][1])
    new_cube[1].insert(4, orig_cube [1][4])
    new_cube[1].insert(5, orig_cube [1][7])
    new_cube[1].insert(6, orig_cube [1][0])
    new_cube[1].insert(7, orig_cube [1][3])
    new_cube[1].insert(8, orig_cube [1][6])   
    
def rotateSide_r_back(new_cube, orig_cube):   
    new_cube[2].insert(0, orig_cube [5][8])
    new_cube[2].insert(1, orig_cube [2][1])
    new_cube[2].insert(2, orig_cube [2][2])
    new_cube[2].insert(3, orig_cube [5][5])
    new_cube[2].insert(4, orig_cube [2][4])
    new_cube[2].insert(5, orig_cube [2][5])
    new_cube[2].insert(6, orig_cube [5][2])
    new_cube[2].insert(7, orig_cube [2][7])
    new_cube[2].insert(8, orig_cube [2][8])  
     
def rotateSide_r_left(new_cube, orig_cube):  
    new_cube[3].insert(0, orig_cube [3][0])
    new_cube[3].insert(1, orig_cube [3][1])
    new_cube[3].insert(2, orig_cube [3][2])
    new_cube[3].insert(3, orig_cube [3][3])
    new_cube[3].insert(4, orig_cube [3][4])
    new_cube[3].insert(5, orig_cube [3][5])
    new_cube[3].insert(6, orig_cube [3][6])
    new_cube[3].insert(7, orig_cube [3][7])
    new_cube[3].insert(8, orig_cube [3][8])   
    
def rotateSide_r_top(new_cube, orig_cube): 
    new_cube[4].insert(0, orig_cube [4][0])
    new_cube[4].insert(1, orig_cube [4][1])
    new_cube[4].insert(2, orig_cube [2][6])
    new_cube[4].insert(3, orig_cube [4][3])
    new_cube[4].insert(4, orig_cube [4][4])
    new_cube[4].insert(5, orig_cube [2][3])
    new_cube[4].insert(6, orig_cube [4][6])
    new_cube[4].insert(7, orig_cube [4][7])
    new_cube[4].insert(8, orig_cube [2][0])
    
def rotateSide_r_bottom(new_cube, orig_cube):      
    new_cube[5].insert(0, orig_cube [5][0])
    new_cube[5].insert(1, orig_cube [5][1])
    new_cube[5].insert(2, orig_cube [0][2])
    new_cube[5].insert(3, orig_cube [5][3])
    new_cube[5].insert(4, orig_cube [5][4])
    new_cube[5].insert(5, orig_cube [0][5])
    new_cube[5].insert(6, orig_cube [5][6])
    new_cube[5].insert(7, orig_cube [5][7])
    new_cube[5].insert(8, orig_cube [0][8])

#rotate the right side cc
def rotateSide_r(orig_cube):
    new_cube = [[], [], [], [], [], []]

    rotateSide_r_front(new_cube, orig_cube)        
    rotateSide_r_right(new_cube, orig_cube)        
    rotateSide_r_back(new_cube, orig_cube)         
    rotateSide_r_left(new_cube, orig_cube)        
    rotateSide_r_top(new_cube, orig_cube)        
    rotateSide_r_bottom(new_cube, orig_cube) 

    return new_cube

#rotate the back clockwise
def rotateSide_B(orig_cube): #rotates clock
    new_cube = [[], [], [], [], [], []]
    #front
    new_cube[0].insert(0, orig_cube [0][0])
    new_cube[0].insert(1, orig_cube [0][1])
    new_cube[0].insert(2, orig_cube [0][2])
    new_cube[0].insert(3, orig_cube [0][3])
    new_cube[0].insert(4, orig_cube [0][4])
    new_cube[0].insert(5, orig_cube [0][5])
    new_cube[0].insert(6, orig_cube [0][6])
    new_cube[0].insert(7, orig_cube [0][7])
    new_cube[0].insert(8, orig_cube [0][8])
    
    new_cube[1].insert(0, orig_cube [1][0])
    new_cube[1].insert(1, orig_cube [1][1])
    new_cube[1].insert(2, orig_cube [5][8])
    new_cube[1].insert(3, orig_cube [1][3])
    new_cube[1].insert(4, orig_cube [1][4])
    new_cube[1].insert(5, orig_cube [5][7])
    new_cube[1].insert(6, orig_cube [1][6])
    new_cube[1].insert(7, orig_cube [1][7])
    new_cube[1].insert(8, orig_cube [5][6])
    #rotates clock
    new_cube[2].insert(0, orig_cube [2][6])
    new_cube[2].insert(1, orig_cube [2][3])
    new_cube[2].insert(2, orig_cube [2][0])
    new_cube[2].insert(3, orig_cube [2][7])
    new_cube[2].insert(4, orig_cube [2][4])
    new_cube[2].insert(5, orig_cube [2][1])
    new_cube[2].insert(6, orig_cube [2][8])
    new_cube[2].insert(7, orig_cube [2][5])
    new_cube[2].insert(8, orig_cube [2][2])
    
    new_cube[3].insert(0, orig_cube [4][2])
    new_cube[3].insert(1, orig_cube [3][1])
    new_cube[3].insert(2, orig_cube [3][2])
    new_cube[3].insert(3, orig_cube [4][1])
    new_cube[3].insert(4, orig_cube [3][4])
    new_cube[3].insert(5, orig_cube [3][5])
    new_cube[3].insert(6, orig_cube [4][0])
    new_cube[3].insert(7, orig_cube [3][7])
    new_cube[3].insert(8, orig_cube [3][8])
    
    new_cube[4].insert(0, orig_cube [1][2])
    new_cube[4].insert(1, orig_cube [1][5])
    new_cube[4].insert(2, orig_cube [1][8])
    new_cube[4].insert(3, orig_cube [4][3])
    new_cube[4].insert(4, orig_cube [4][4])
    new_cube[4].insert(5, orig_cube [4][5])
    new_cube[4].insert(6, orig_cube [4][6])
    new_cube[4].insert(7, orig_cube [4][7])
    new_cube[4].insert(8, orig_cube [4][8])
    
    new_cube[5].insert(0, orig_cube [5][0])
    new_cube[5].insert(1, orig_cube [5][1])
    new_cube[5].insert(2, orig_cube [5][2])
    new_cube[5].insert(3, orig_cube [5][3])
    new_cube[5].insert(4, orig_cube [5][4])
    new_cube[5].insert(5, orig_cube [5][5])
    new_cube[5].insert(6, orig_cube [3][0])
    new_cube[5].insert(7, orig_cube [3][3])
    new_cube[5].insert(8, orig_cube [3][6])
    return new_cube

#rotate the back cc
def rotateSide_b(orig_cube): 
    new_cube = [[], [], [], [], [], []]
    #front says same
    new_cube[0].insert(0, orig_cube [0][0])
    new_cube[0].insert(1, orig_cube [0][1])
    new_cube[0].insert(2, orig_cube [0][2])
    new_cube[0].insert(3, orig_cube [0][3])
    new_cube[0].insert(4, orig_cube [0][4])
    new_cube[0].insert(5, orig_cube [0][5])
    new_cube[0].insert(6, orig_cube [0][6])
    new_cube[0].insert(7, orig_cube [0][7])
    new_cube[0].insert(8, orig_cube [0][8])
    
    new_cube[1].insert(0, orig_cube [1][0])
    new_cube[1].insert(1, orig_cube [1][1])
    new_cube[1].insert(2, orig_cube [4][0])
    new_cube[1].insert(3, orig_cube [1][3])
    new_cube[1].insert(4, orig_cube [1][4])
    new_cube[1].insert(5, orig_cube [4][1])
    new_cube[1].insert(6, orig_cube [1][6])
    new_cube[1].insert(7, orig_cube [1][7])
    new_cube[1].insert(8, orig_cube [4][2])
    #rotates cc
    new_cube[2].insert(0, orig_cube [2][2])
    new_cube[2].insert(1, orig_cube [2][5])
    new_cube[2].insert(2, orig_cube [2][8])
    new_cube[2].insert(3, orig_cube [2][1])
    new_cube[2].insert(4, orig_cube [2][4])
    new_cube[2].insert(5, orig_cube [2][7])
    new_cube[2].insert(6, orig_cube [2][0])
    new_cube[2].insert(7, orig_cube [2][3])
    new_cube[2].insert(8, orig_cube [2][6])   
       
    
    new_cube[3].insert(0, orig_cube [5][6])
    new_cube[3].insert(1, orig_cube [3][1])
    new_cube[3].insert(2, orig_cube [3][2])
    new_cube[3].insert(3, orig_cube [5][7])
    new_cube[3].insert(4, orig_cube [3][4])
    new_cube[3].insert(5, orig_cube [3][5])
    new_cube[3].insert(6, orig_cube [5][8])
    new_cube[3].insert(7, orig_cube [3][7])
    new_cube[3].insert(8, orig_cube [3][8])
    
    new_cube[4].insert(0, orig_cube [3][6])
    new_cube[4].insert(1, orig_cube [3][3])
    new_cube[4].insert(2, orig_cube [3][0])
    new_cube[4].insert(3, orig_cube [4][3])
    new_cube[4].insert(4, orig_cube [4][4])
    new_cube[4].insert(5, orig_cube [4][5])
    new_cube[4].insert(6, orig_cube [4][6])
    new_cube[4].insert(7, orig_cube [4][7])
    new_cube[4].insert(8, orig_cube [4][8])
    
    new_cube[5].insert(0, orig_cube [5][0])
    new_cube[5].insert(1, orig_cube [5][1])
    new_cube[5].insert(2, orig_cube [5][2])
    new_cube[5].insert(3, orig_cube [5][3])
    new_cube[5].insert(4, orig_cube [5][4])
    new_cube[5].insert(5, orig_cube [5][5])
    new_cube[5].insert(6, orig_cube [1][8])
    new_cube[5].insert(7, orig_cube [1][5])
    new_cube[5].insert(8, orig_cube [1][2])
    return new_cube

#rotate the left clockwise
def rotateSide_L(orig_cube):
    new_cube = [[], [], [], [], [], []]
    #front
    new_cube[0].insert(0, orig_cube [4][0])
    new_cube[0].insert(1, orig_cube [0][1])
    new_cube[0].insert(2, orig_cube [0][2])
    new_cube[0].insert(3, orig_cube [4][3])
    new_cube[0].insert(4, orig_cube [0][4])
    new_cube[0].insert(5, orig_cube [0][5])
    new_cube[0].insert(6, orig_cube [4][6])
    new_cube[0].insert(7, orig_cube [0][7])
    new_cube[0].insert(8, orig_cube [0][8])
    
    #stays the same
    new_cube[1].insert(0, orig_cube [1][0])
    new_cube[1].insert(1, orig_cube [1][1])
    new_cube[1].insert(2, orig_cube [1][2])
    new_cube[1].insert(3, orig_cube [1][3])
    new_cube[1].insert(4, orig_cube [1][4])
    new_cube[1].insert(5, orig_cube [1][5])
    new_cube[1].insert(6, orig_cube [1][6])
    new_cube[1].insert(7, orig_cube [1][7])
    new_cube[1].insert(8, orig_cube [1][8])
    
    new_cube[2].insert(0, orig_cube [2][0])
    new_cube[2].insert(1, orig_cube [2][1])
    new_cube[2].insert(2, orig_cube [5][6])
    new_cube[2].insert(3, orig_cube [2][3])
    new_cube[2].insert(4, orig_cube [2][4])
    new_cube[2].insert(5, orig_cube [5][3])
    new_cube[2].insert(6, orig_cube [2][6])
    new_cube[2].insert(7, orig_cube [2][7])
    new_cube[2].insert(8, orig_cube [5][0])
    
    #side that rotates clock
    new_cube[3].insert(0, orig_cube [3][6])
    new_cube[3].insert(1, orig_cube [3][3])
    new_cube[3].insert(2, orig_cube [3][0])
    new_cube[3].insert(3, orig_cube [3][7])
    new_cube[3].insert(4, orig_cube [3][4])
    new_cube[3].insert(5, orig_cube [3][1])
    new_cube[3].insert(6, orig_cube [3][8])
    new_cube[3].insert(7, orig_cube [3][5])
    new_cube[3].insert(8, orig_cube [3][2])    
    
    new_cube[4].insert(0, orig_cube [2][8])
    new_cube[4].insert(1, orig_cube [4][1])
    new_cube[4].insert(2, orig_cube [4][2])
    new_cube[4].insert(3, orig_cube [2][5])
    new_cube[4].insert(4, orig_cube [4][4])
    new_cube[4].insert(5, orig_cube [4][5])
    new_cube[4].insert(6, orig_cube [2][2])
    new_cube[4].insert(7, orig_cube [4][7])
    new_cube[4].insert(8, orig_cube [4][8])
    
    new_cube[5].insert(0, orig_cube [0][0])
    new_cube[5].insert(1, orig_cube [5][1])
    new_cube[5].insert(2, orig_cube [5][2])
    new_cube[5].insert(3, orig_cube [0][3])
    new_cube[5].insert(4, orig_cube [5][4])
    new_cube[5].insert(5, orig_cube [5][5])
    new_cube[5].insert(6, orig_cube [0][6])
    new_cube[5].insert(7, orig_cube [5][7])
    new_cube[5].insert(8, orig_cube [5][8])
    return new_cube

#rotate the left cc
def rotateSide_l(orig_cube):
    new_cube = [[], [], [], [], [], []]
    #front
    new_cube[0].insert(0, orig_cube [5][0])
    new_cube[0].insert(1, orig_cube [0][1])
    new_cube[0].insert(2, orig_cube [0][2])
    new_cube[0].insert(3, orig_cube [5][3])
    new_cube[0].insert(4, orig_cube [0][4])
    new_cube[0].insert(5, orig_cube [0][5])
    new_cube[0].insert(6, orig_cube [5][6])
    new_cube[0].insert(7, orig_cube [0][7])
    new_cube[0].insert(8, orig_cube [0][8])
    
    #stays the same
    new_cube[1].insert(0, orig_cube [1][0])
    new_cube[1].insert(1, orig_cube [1][1])
    new_cube[1].insert(2, orig_cube [1][2])
    new_cube[1].insert(3, orig_cube [1][3])
    new_cube[1].insert(4, orig_cube [1][4])
    new_cube[1].insert(5, orig_cube [1][5])
    new_cube[1].insert(6, orig_cube [1][6])
    new_cube[1].insert(7, orig_cube [1][7])
    new_cube[1].insert(8, orig_cube [1][8])
    
    new_cube[2].insert(0, orig_cube [2][0])
    new_cube[2].insert(1, orig_cube [2][1])
    new_cube[2].insert(2, orig_cube [4][6])
    new_cube[2].insert(3, orig_cube [2][3])
    new_cube[2].insert(4, orig_cube [2][4])
    new_cube[2].insert(5, orig_cube [4][3])
    new_cube[2].insert(6, orig_cube [2][6])
    new_cube[2].insert(7, orig_cube [2][7])
    new_cube[2].insert(8, orig_cube [4][0])
    
    #side that rotates counterc
    new_cube[3].insert(0, orig_cube [3][2])
    new_cube[3].insert(1, orig_cube [3][5])
    new_cube[3].insert(2, orig_cube [3][8])
    new_cube[3].insert(3, orig_cube [3][1])
    new_cube[3].insert(4, orig_cube [3][4])
    new_cube[3].insert(5, orig_cube [3][7])
    new_cube[3].insert(6, orig_cube [3][0])
    new_cube[3].insert(7, orig_cube [3][3])
    new_cube[3].insert(8, orig_cube [3][6])      
   
    new_cube[4].insert(0, orig_cube [0][0])
    new_cube[4].insert(1, orig_cube [4][1])
    new_cube[4].insert(2, orig_cube [4][2])
    new_cube[4].insert(3, orig_cube [0][3])
    new_cube[4].insert(4, orig_cube [4][4])
    new_cube[4].insert(5, orig_cube [4][5])
    new_cube[4].insert(6, orig_cube [0][6])
    new_cube[4].insert(7, orig_cube [4][7])
    new_cube[4].insert(8, orig_cube [4][8])
    
    new_cube[5].insert(0, orig_cube [2][8])
    new_cube[5].insert(1, orig_cube [5][1])
    new_cube[5].insert(2, orig_cube [5][2])
    new_cube[5].insert(3, orig_cube [2][5])
    new_cube[5].insert(4, orig_cube [5][4])
    new_cube[5].insert(5, orig_cube [5][5])
    new_cube[5].insert(6, orig_cube [2][2])
    new_cube[5].insert(7, orig_cube [5][7])
    new_cube[5].insert(8, orig_cube [5][8])
    return new_cube

#rotate upper side clockwise
def rotateSide_U(orig_cube):

    new_cube = [[], [], [], [], [], []]
    #front
    new_cube[0].insert(0, orig_cube [1][0])
    new_cube[0].insert(1, orig_cube [1][1])
    new_cube[0].insert(2, orig_cube [1][2])
    new_cube[0].insert(3, orig_cube [0][3])
    new_cube[0].insert(4, orig_cube [0][4])
    new_cube[0].insert(5, orig_cube [0][5])
    new_cube[0].insert(6, orig_cube [0][6])
    new_cube[0].insert(7, orig_cube [0][7])
    new_cube[0].insert(8, orig_cube [0][8])
    
    new_cube[1].insert(0, orig_cube [2][0])
    new_cube[1].insert(1, orig_cube [2][1])
    new_cube[1].insert(2, orig_cube [2][2])
    new_cube[1].insert(3, orig_cube [1][3])
    new_cube[1].insert(4, orig_cube [1][4])
    new_cube[1].insert(5, orig_cube [1][5])
    new_cube[1].insert(6, orig_cube [1][6])
    new_cube[1].insert(7, orig_cube [1][7])
    new_cube[1].insert(8, orig_cube [1][8])
    
    new_cube[2].insert(0, orig_cube [3][0])
    new_cube[2].insert(1, orig_cube [3][1])
    new_cube[2].insert(2, orig_cube [3][2])
    new_cube[2].insert(3, orig_cube [2][3])
    new_cube[2].insert(4, orig_cube [2][4])
    new_cube[2].insert(5, orig_cube [2][5])
    new_cube[2].insert(6, orig_cube [2][6])
    new_cube[2].insert(7, orig_cube [2][7])
    new_cube[2].insert(8, orig_cube [2][8])
    

    new_cube[3].insert(0, orig_cube [0][0])
    new_cube[3].insert(1, orig_cube [0][1])
    new_cube[3].insert(2, orig_cube [0][2])
    new_cube[3].insert(3, orig_cube [3][3])
    new_cube[3].insert(4, orig_cube [3][4])
    new_cube[3].insert(5, orig_cube [3][5])
    new_cube[3].insert(6, orig_cube [3][6])
    new_cube[3].insert(7, orig_cube [3][7])
    new_cube[3].insert(8, orig_cube [3][8])      
   
    #side that rotates clock
    new_cube[4].insert(0, orig_cube [4][6])
    new_cube[4].insert(1, orig_cube [4][3])
    new_cube[4].insert(2, orig_cube [4][0])
    new_cube[4].insert(3, orig_cube [4][7])
    new_cube[4].insert(4, orig_cube [4][4])
    new_cube[4].insert(5, orig_cube [4][1])
    new_cube[4].insert(6, orig_cube [4][8])
    new_cube[4].insert(7, orig_cube [4][5])
    new_cube[4].insert(8, orig_cube [4][2])   
   
    #stays the same
    new_cube[5].insert(0, orig_cube [5][0])
    new_cube[5].insert(1, orig_cube [5][1])
    new_cube[5].insert(2, orig_cube [5][2])
    new_cube[5].insert(3, orig_cube [5][3])
    new_cube[5].insert(4, orig_cube [5][4])
    new_cube[5].insert(5, orig_cube [5][5])
    new_cube[5].insert(6, orig_cube [5][6])
    new_cube[5].insert(7, orig_cube [5][7])
    new_cube[5].insert(8, orig_cube [5][8])
    return new_cube

#rotate upper cc
def rotateSide_u(orig_cube):

    new_cube = [[], [], [], [], [], []]
    #front
    new_cube[0].insert(0, orig_cube [3][0])
    new_cube[0].insert(1, orig_cube [3][1])
    new_cube[0].insert(2, orig_cube [3][2])
    new_cube[0].insert(3, orig_cube [0][3])
    new_cube[0].insert(4, orig_cube [0][4])
    new_cube[0].insert(5, orig_cube [0][5])
    new_cube[0].insert(6, orig_cube [0][6])
    new_cube[0].insert(7, orig_cube [0][7])
    new_cube[0].insert(8, orig_cube [0][8])
    
    new_cube[1].insert(0, orig_cube [0][0])
    new_cube[1].insert(1, orig_cube [0][1])
    new_cube[1].insert(2, orig_cube [0][2])
    new_cube[1].insert(3, orig_cube [1][3])
    new_cube[1].insert(4, orig_cube [1][4])
    new_cube[1].insert(5, orig_cube [1][5])
    new_cube[1].insert(6, orig_cube [1][6])
    new_cube[1].insert(7, orig_cube [1][7])
    new_cube[1].insert(8, orig_cube [1][8])
    
    new_cube[2].insert(0, orig_cube [1][0])
    new_cube[2].insert(1, orig_cube [1][1])
    new_cube[2].insert(2, orig_cube [1][2])
    new_cube[2].insert(3, orig_cube [2][3])
    new_cube[2].insert(4, orig_cube [2][4])
    new_cube[2].insert(5, orig_cube [2][5])
    new_cube[2].insert(6, orig_cube [2][6])
    new_cube[2].insert(7, orig_cube [2][7])
    new_cube[2].insert(8, orig_cube [2][8])
    

    new_cube[3].insert(0, orig_cube [2][0])
    new_cube[3].insert(1, orig_cube [2][1])
    new_cube[3].insert(2, orig_cube [2][2])
    new_cube[3].insert(3, orig_cube [3][3])
    new_cube[3].insert(4, orig_cube [3][4])
    new_cube[3].insert(5, orig_cube [3][5])
    new_cube[3].insert(6, orig_cube [3][6])
    new_cube[3].insert(7, orig_cube [3][7])
    new_cube[3].insert(8, orig_cube [3][8])      
   
    #side that rotates cclock
    new_cube[4].insert(0, orig_cube [4][2])
    new_cube[4].insert(1, orig_cube [4][5])
    new_cube[4].insert(2, orig_cube [4][8])
    new_cube[4].insert(3, orig_cube [4][1])
    new_cube[4].insert(4, orig_cube [4][4])
    new_cube[4].insert(5, orig_cube [4][7])
    new_cube[4].insert(6, orig_cube [4][0])
    new_cube[4].insert(7, orig_cube [4][3])
    new_cube[4].insert(8, orig_cube [4][6]) 
    
    
    #stays the same
    new_cube[5].insert(0, orig_cube [5][0])
    new_cube[5].insert(1, orig_cube [5][1])
    new_cube[5].insert(2, orig_cube [5][2])
    new_cube[5].insert(3, orig_cube [5][3])
    new_cube[5].insert(4, orig_cube [5][4])
    new_cube[5].insert(5, orig_cube [5][5])
    new_cube[5].insert(6, orig_cube [5][6])
    new_cube[5].insert(7, orig_cube [5][7])
    new_cube[5].insert(8, orig_cube [5][8])
    return new_cube

#rotate bottom clockwise
def rotateSide_D(orig_cube):
    new_cube = [[], [], [], [], [], []]
    #front
    new_cube[0].insert(0, orig_cube [0][0])
    new_cube[0].insert(1, orig_cube [0][1])
    new_cube[0].insert(2, orig_cube [0][2])
    new_cube[0].insert(3, orig_cube [0][3])
    new_cube[0].insert(4, orig_cube [0][4])
    new_cube[0].insert(5, orig_cube [0][5])
    new_cube[0].insert(6, orig_cube [3][6])
    new_cube[0].insert(7, orig_cube [3][7])
    new_cube[0].insert(8, orig_cube [3][8])
    
    new_cube[1].insert(0, orig_cube [1][0])
    new_cube[1].insert(1, orig_cube [1][1])
    new_cube[1].insert(2, orig_cube [1][2])
    new_cube[1].insert(3, orig_cube [1][3])
    new_cube[1].insert(4, orig_cube [1][4])
    new_cube[1].insert(5, orig_cube [1][5])
    new_cube[1].insert(6, orig_cube [0][6])
    new_cube[1].insert(7, orig_cube [0][7])
    new_cube[1].insert(8, orig_cube [0][8])
    
    new_cube[2].insert(0, orig_cube [2][0])
    new_cube[2].insert(1, orig_cube [2][1])
    new_cube[2].insert(2, orig_cube [2][2])
    new_cube[2].insert(3, orig_cube [2][3])
    new_cube[2].insert(4, orig_cube [2][4])
    new_cube[2].insert(5, orig_cube [2][5])
    new_cube[2].insert(6, orig_cube [1][6])
    new_cube[2].insert(7, orig_cube [1][7])
    new_cube[2].insert(8, orig_cube [1][8])
    

    new_cube[3].insert(0, orig_cube [3][0])
    new_cube[3].insert(1, orig_cube [3][1])
    new_cube[3].insert(2, orig_cube [3][2])
    new_cube[3].insert(3, orig_cube [3][3])
    new_cube[3].insert(4, orig_cube [3][4])
    new_cube[3].insert(5, orig_cube [3][5])
    new_cube[3].insert(6, orig_cube [2][6])
    new_cube[3].insert(7, orig_cube [2][7])
    new_cube[3].insert(8, orig_cube [2][8])      
   
    #stays the same
    new_cube[4].insert(0, orig_cube [4][0])
    new_cube[4].insert(1, orig_cube [4][1])
    new_cube[4].insert(2, orig_cube [4][2])
    new_cube[4].insert(3, orig_cube [4][3])
    new_cube[4].insert(4, orig_cube [4][4])
    new_cube[4].insert(5, orig_cube [4][5])
    new_cube[4].insert(6, orig_cube [4][6])
    new_cube[4].insert(7, orig_cube [4][7])
    new_cube[4].insert(8, orig_cube [4][8])   
   
    #side that rotates clock
    new_cube[5].insert(0, orig_cube [5][6])
    new_cube[5].insert(1, orig_cube [5][3])
    new_cube[5].insert(2, orig_cube [5][0])
    new_cube[5].insert(3, orig_cube [5][7])
    new_cube[5].insert(4, orig_cube [5][4])
    new_cube[5].insert(5, orig_cube [5][1])
    new_cube[5].insert(6, orig_cube [5][8])
    new_cube[5].insert(7, orig_cube [5][5])
    new_cube[5].insert(8, orig_cube [5][2])    
  
    return new_cube

#rotate bottom cc
def rotateSide_d(orig_cube):
    new_cube = [[], [], [], [], [], []]
    #front
    new_cube[0].insert(0, orig_cube [0][0])
    new_cube[0].insert(1, orig_cube [0][1])
    new_cube[0].insert(2, orig_cube [0][2])
    new_cube[0].insert(3, orig_cube [0][3])
    new_cube[0].insert(4, orig_cube [0][4])
    new_cube[0].insert(5, orig_cube [0][5])
    new_cube[0].insert(6, orig_cube [1][6])
    new_cube[0].insert(7, orig_cube [1][7])
    new_cube[0].insert(8, orig_cube [1][8])
    
    new_cube[1].insert(0, orig_cube [1][0])
    new_cube[1].insert(1, orig_cube [1][1])
    new_cube[1].insert(2, orig_cube [1][2])
    new_cube[1].insert(3, orig_cube [1][3])
    new_cube[1].insert(4, orig_cube [1][4])
    new_cube[1].insert(5, orig_cube [1][5])
    new_cube[1].insert(6, orig_cube [2][6])
    new_cube[1].insert(7, orig_cube [2][7])
    new_cube[1].insert(8, orig_cube [2][8])
    
    new_cube[2].insert(0, orig_cube [2][0])
    new_cube[2].insert(1, orig_cube [2][1])
    new_cube[2].insert(2, orig_cube [2][2])
    new_cube[2].insert(3, orig_cube [2][3])
    new_cube[2].insert(4, orig_cube [2][4])
    new_cube[2].insert(5, orig_cube [2][5])
    new_cube[2].insert(6, orig_cube [3][6])
    new_cube[2].insert(7, orig_cube [3][7])
    new_cube[2].insert(8, orig_cube [3][8])
    

    new_cube[3].insert(0, orig_cube [3][0])
    new_cube[3].insert(1, orig_cube [3][1])
    new_cube[3].insert(2, orig_cube [3][2])
    new_cube[3].insert(3, orig_cube [3][3])
    new_cube[3].insert(4, orig_cube [3][4])
    new_cube[3].insert(5, orig_cube [3][5])
    new_cube[3].insert(6, orig_cube [0][6])
    new_cube[3].insert(7, orig_cube [0][7])
    new_cube[3].insert(8, orig_cube [0][8])      
   
    #stays the same
    new_cube[4].insert(0, orig_cube [4][0])
    new_cube[4].insert(1, orig_cube [4][1])
    new_cube[4].insert(2, orig_cube [4][2])
    new_cube[4].insert(3, orig_cube [4][3])
    new_cube[4].insert(4, orig_cube [4][4])
    new_cube[4].insert(5, orig_cube [4][5])
    new_cube[4].insert(6, orig_cube [4][6])
    new_cube[4].insert(7, orig_cube [4][7])
    new_cube[4].insert(8, orig_cube [4][8])   
   
    #side that rotates cc
    new_cube[5].insert(0, orig_cube [5][2])
    new_cube[5].insert(1, orig_cube [5][5])
    new_cube[5].insert(2, orig_cube [5][8])
    new_cube[5].insert(3, orig_cube [5][1])
    new_cube[5].insert(4, orig_cube [5][4])
    new_cube[5].insert(5, orig_cube [5][7])
    new_cube[5].insert(6, orig_cube [5][0])
    new_cube[5].insert(7, orig_cube [5][3])
    new_cube[5].insert(8, orig_cube [5][6])    
  
  
    return new_cube

#create a string from a cube list. for testing
def createStringFromCube(lst_cube):
    str1 = "".join(lst_cube[0])
    str2 = "".join(lst_cube[1])
    str3 = "".join(lst_cube[2])
    str4 = "".join(lst_cube[3])
    str5 = "".join(lst_cube[4])
    str6 = "".join(lst_cube[5])                       
         
    str_cube = str1+str2+str3+str4+str5+str6
    return str_cube


def createCubeListFromInputParms(parms):
    # parm_string = parms.get("cube")  
    
    lst_cube = ([x for x in parms.get("cube")])
    lst_in1, lst_in2, lst_in3, lst_in4, lst_in5, lst_in6 = ([] for i in range(6)) 
    
    for i in range (1,7):
        for _ in range(1,10):
            exec(f"lst_in{i}.append((lst_cube.pop(0)))")  
            
    for i in range(1,7):
        exec(f'lst_cube.append(lst_in{i})') 
    
    return lst_cube

#rotate the whole cube clockwise. Used in testing. 
def rotateCubeClock(orig_cube):
    new_cube = [[], [], [], [], [], []]
    
    #front
    new_cube[0].insert(0, orig_cube [0][6])
    new_cube[0].insert(1, orig_cube [0][3])
    new_cube[0].insert(2, orig_cube [0][0])
    new_cube[0].insert(3, orig_cube [0][7])
    new_cube[0].insert(4, orig_cube [0][4])
    new_cube[0].insert(5, orig_cube [0][1])
    new_cube[0].insert(6, orig_cube [0][8])
    new_cube[0].insert(7, orig_cube [0][5])
    new_cube[0].insert(8, orig_cube [0][2])
    
    #right    
    new_cube[1].insert(0, orig_cube [4][6])
    new_cube[1].insert(1, orig_cube [4][3])
    new_cube[1].insert(2, orig_cube [4][0])
    new_cube[1].insert(3, orig_cube [4][7])
    new_cube[1].insert(4, orig_cube [4][4])
    new_cube[1].insert(5, orig_cube [4][1])
    new_cube[1].insert(6, orig_cube [4][8])
    new_cube[1].insert(7, orig_cube [4][5])
    new_cube[1].insert(8, orig_cube [4][2])
    
    #back    
    new_cube[2].insert(0, orig_cube [2][2])
    new_cube[2].insert(1, orig_cube [2][5])
    new_cube[2].insert(2, orig_cube [2][8])
    new_cube[2].insert(3, orig_cube [2][1])
    new_cube[2].insert(4, orig_cube [2][4])
    new_cube[2].insert(5, orig_cube [2][7])
    new_cube[2].insert(6, orig_cube [2][0])
    new_cube[2].insert(7, orig_cube [2][3])
    new_cube[2].insert(8, orig_cube [2][6])
    
    #left    
    new_cube[3].insert(0, orig_cube [5][6])
    new_cube[3].insert(1, orig_cube [5][3])
    new_cube[3].insert(2, orig_cube [5][0])
    new_cube[3].insert(3, orig_cube [5][7])
    new_cube[3].insert(4, orig_cube [5][4])
    new_cube[3].insert(5, orig_cube [5][1])
    new_cube[3].insert(6, orig_cube [5][8])
    new_cube[3].insert(7, orig_cube [5][5])
    new_cube[3].insert(8, orig_cube [5][2])
    
    #top    
    new_cube[4].insert(0, orig_cube [3][6])
    new_cube[4].insert(1, orig_cube [3][3])
    new_cube[4].insert(2, orig_cube [3][0])
    new_cube[4].insert(3, orig_cube [3][7])
    new_cube[4].insert(4, orig_cube [3][4])
    new_cube[4].insert(5, orig_cube [3][1])
    new_cube[4].insert(6, orig_cube [3][8])
    new_cube[4].insert(7, orig_cube [3][5])
    new_cube[4].insert(8, orig_cube [3][2])
    
    #bottom    
    new_cube[5].insert(0, orig_cube [1][6])
    new_cube[5].insert(1, orig_cube [1][3])
    new_cube[5].insert(2, orig_cube [1][0])
    new_cube[5].insert(3, orig_cube [1][7])
    new_cube[5].insert(4, orig_cube [1][4])
    new_cube[5].insert(5, orig_cube [1][1])
    new_cube[5].insert(6, orig_cube [1][8])
    new_cube[5].insert(7, orig_cube [1][5])
    new_cube[5].insert(8, orig_cube [1][2])
    
    return new_cube

#front side goes to the right
def rotateCubeToRight(cube):
        new_cube = [[], [], [], [], [], []]
        
        new_cube[0] = cube[3]
        new_cube[1] = cube[0]
        new_cube[2] = cube[1]
        new_cube[3] = cube[2]
        
        new_cube[4].insert(0, cube [4][2])
        new_cube[4].insert(1, cube [4][5])
        new_cube[4].insert(2, cube [4][8])
        new_cube[4].insert(3, cube [4][1])
        new_cube[4].insert(4, cube [4][4])
        new_cube[4].insert(5, cube [4][7])
        new_cube[4].insert(6, cube [4][0])
        new_cube[4].insert(7, cube [4][3])
        new_cube[4].insert(8, cube [4][6])     

        new_cube[5].insert(0, cube [5][6])
        new_cube[5].insert(1, cube [5][3])
        new_cube[5].insert(2, cube [5][0])
        new_cube[5].insert(3, cube [5][7])
        new_cube[5].insert(4, cube [5][4])
        new_cube[5].insert(5, cube [5][1])
        new_cube[5].insert(6, cube [5][8])
        new_cube[5].insert(7, cube [5][5])
        new_cube[5].insert(8, cube [5][2])  

        return new_cube
    
#font side goes up   
def rotateCubeUp(cube):
        new_cube = [[], [], [], [], [], []]       
        
        new_cube[0] = cube[5]
        
        new_cube[1].insert(0, cube [1][6])
        new_cube[1].insert(1, cube [1][3])
        new_cube[1].insert(2, cube [1][0])
        new_cube[1].insert(3, cube [1][7])
        new_cube[1].insert(4, cube [1][4])
        new_cube[1].insert(5, cube [1][1])
        new_cube[1].insert(6, cube [1][8])
        new_cube[1].insert(7, cube [1][5])
        new_cube[1].insert(8, cube [1][2])  
                 
        new_cube[2].insert(0, cube [4][8])
        new_cube[2].insert(1, cube [4][7])
        new_cube[2].insert(2, cube [4][6])
        new_cube[2].insert(3, cube [4][5])
        new_cube[2].insert(4, cube [4][4])
        new_cube[2].insert(5, cube [4][3])
        new_cube[2].insert(6, cube [4][2])
        new_cube[2].insert(7, cube [4][1])
        new_cube[2].insert(8, cube [4][0]) 
        
        new_cube[3].insert(0, cube [3][2])
        new_cube[3].insert(1, cube [3][5])
        new_cube[3].insert(2, cube [3][8])
        new_cube[3].insert(3, cube [3][1])
        new_cube[3].insert(4, cube [3][4])
        new_cube[3].insert(5, cube [3][7])
        new_cube[3].insert(6, cube [3][0])
        new_cube[3].insert(7, cube [3][3])
        new_cube[3].insert(8, cube [3][6]) 
           
        new_cube[4] = cube[0]   
        
        new_cube[5].insert(0, cube [2][8])
        new_cube[5].insert(1, cube [2][7])
        new_cube[5].insert(2, cube [2][6])
        new_cube[5].insert(3, cube [2][5])
        new_cube[5].insert(4, cube [2][4])
        new_cube[5].insert(5, cube [2][3])
        new_cube[5].insert(6, cube [2][2])
        new_cube[5].insert(7, cube [2][1])
        new_cube[5].insert(8, cube [2][0]) 

        return new_cube
    
#front side goes down    
def rotateCubeDown(cube):
        new_cube = [[], [], [], [], [], []]       
        
        new_cube[0] = cube[4]
        
        new_cube[1].insert(0, cube [1][2])
        new_cube[1].insert(1, cube [1][5])
        new_cube[1].insert(2, cube [1][8])
        new_cube[1].insert(3, cube [1][1])
        new_cube[1].insert(4, cube [1][4])
        new_cube[1].insert(5, cube [1][7])
        new_cube[1].insert(6, cube [1][0])
        new_cube[1].insert(7, cube [1][3])
        new_cube[1].insert(8, cube [1][6])  
                 
        new_cube[2].insert(0, cube [5][8])
        new_cube[2].insert(1, cube [5][7])
        new_cube[2].insert(2, cube [5][6])
        new_cube[2].insert(3, cube [5][5])
        new_cube[2].insert(4, cube [5][4])
        new_cube[2].insert(5, cube [5][3])
        new_cube[2].insert(6, cube [5][2])
        new_cube[2].insert(7, cube [5][1])
        new_cube[2].insert(8, cube [5][0]) 
        
        new_cube[3].insert(0, cube [3][6])
        new_cube[3].insert(1, cube [3][3])
        new_cube[3].insert(2, cube [3][0])
        new_cube[3].insert(3, cube [3][7])
        new_cube[3].insert(4, cube [3][4])
        new_cube[3].insert(5, cube [3][1])
        new_cube[3].insert(6, cube [3][8])
        new_cube[3].insert(7, cube [3][5])
        new_cube[3].insert(8, cube [3][2]) 
        
        new_cube[4].insert(0, cube [2][8])
        new_cube[4].insert(1, cube [2][7])
        new_cube[4].insert(2, cube [2][6])
        new_cube[4].insert(3, cube [2][5])
        new_cube[4].insert(4, cube [2][4])
        new_cube[4].insert(5, cube [2][3])
        new_cube[4].insert(6, cube [2][2])
        new_cube[4].insert(7, cube [2][1])
        new_cube[4].insert(8, cube [2][0])            

        new_cube[5] = cube[0]  

        return new_cube

#front side goes to the left
def rotateCubeToLeft(cube):
        new_cube = [[], [], [], [], [], []]
        
        new_cube[0] = cube[1]
        new_cube[1] = cube[2]
        new_cube[2] = cube[3]
        new_cube[3] = cube[0]
        
        new_cube[4].insert(0, cube [4][6])
        new_cube[4].insert(1, cube [4][3])
        new_cube[4].insert(2, cube [4][0])
        new_cube[4].insert(3, cube [4][7])
        new_cube[4].insert(4, cube [4][4])
        new_cube[4].insert(5, cube [4][1])
        new_cube[4].insert(6, cube [4][8])
        new_cube[4].insert(7, cube [4][5])
        new_cube[4].insert(8, cube [4][2])     

        new_cube[5].insert(0, cube [5][2])
        new_cube[5].insert(1, cube [5][5])
        new_cube[5].insert(2, cube [5][8])
        new_cube[5].insert(3, cube [5][1])
        new_cube[5].insert(4, cube [5][4])
        new_cube[5].insert(5, cube [5][7])
        new_cube[5].insert(6, cube [5][0])
        new_cube[5].insert(7, cube [5][3])
        new_cube[5].insert(8, cube [5][6])  

        return new_cube    

def SolveWhiteLeaves(lst_cube, lst_rotate): # working on this one    

        #rotate non white to into [4][5]        
        if lst_cube[4][5] == var_w and lst_cube[4][7] != var_w:
            lst_cube = rotateSide_u(lst_cube)
            lst_rotate.append("u")  
        elif lst_cube[4][5] == var_w and lst_cube[4][3] != var_w:
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_rotate.append("UU")  
        elif lst_cube[4][5] == var_w and lst_cube[4][1] != var_w:
            lst_cube = rotateSide_U(lst_cube)
            lst_rotate.append("U")  
    
    #first and easiest now solve [4][5]
        if lst_cube[0][5] == var_w and lst_cube[4][5] != var_w:
            lst_cube = rotateSide_R(lst_cube)
            lst_rotate.append("R") 
        elif lst_cube[5][5] == var_w and lst_cube[4][5] != var_w:
            lst_cube = rotateSide_R(lst_cube)
            lst_cube = rotateSide_R(lst_cube)
            lst_rotate.append("RR")            
        elif lst_cube[2][3] == var_w and lst_cube[4][5] != var_w:
            lst_cube = rotateSide_r(lst_cube)
            lst_rotate.append("r")      
        
        elif lst_cube[0][1] == var_w and lst_cube[4][5] != var_w:
            lst_cube = rotateSide_F(lst_cube)
            lst_cube = rotateSide_R(lst_cube)
            lst_rotate.append("FR")             
        elif lst_cube[0][3] == var_w and lst_cube[4][5] != var_w:
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_l(lst_cube)
            lst_cube = rotateSide_u(lst_cube)
            lst_cube = rotateSide_u(lst_cube)
            lst_rotate.append("UUluu") 
        elif lst_cube[0][7] == var_w and lst_cube[4][5] != var_w:
            lst_cube = rotateSide_D(lst_cube)
            lst_cube = rotateSide_r(lst_cube)
            lst_cube = rotateSide_u(lst_cube)
            lst_cube = rotateSide_B(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_rotate.append("DruBU") 
            
        elif lst_cube[1][1] == var_w and lst_cube[4][5] != var_w:
            lst_cube = rotateSide_r(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_f(lst_cube)
            lst_cube = rotateSide_u(lst_cube)
            lst_rotate.append("rUfu")             
        elif lst_cube[1][3] == var_w and lst_cube[4][5] != var_w:
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_f(lst_cube)
            lst_cube = rotateSide_u(lst_cube)
            lst_rotate.append("Ufu")  
        elif lst_cube[1][5] == var_w and lst_cube[4][5] != var_w:
            lst_cube = rotateSide_r(lst_cube)
            lst_cube = rotateSide_r(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_f(lst_cube)
            lst_cube = rotateSide_u(lst_cube)
            lst_rotate.append("rrUfu")   
        elif lst_cube[1][7] == var_w and lst_cube[4][5] != var_w:
            lst_cube = rotateSide_R(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_f(lst_cube)
            lst_cube = rotateSide_u(lst_cube)
            lst_rotate.append("RUfu")  
            
        elif lst_cube[2][1] == var_w and lst_cube[4][5] != var_w:
            lst_cube = rotateSide_b(lst_cube)
            lst_cube = rotateSide_r(lst_cube)
            lst_rotate.append("br")             
        elif lst_cube[2][7] == var_w and lst_cube[4][5] != var_w:
            lst_cube = rotateSide_u(lst_cube)
            lst_cube = rotateSide_b(lst_cube)
            lst_cube = rotateSide_u(lst_cube)
            lst_cube = rotateSide_L(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_rotate.append("ubuLUU") 
        elif lst_cube[2][5] == var_w and lst_cube[4][5] != var_w:
            lst_cube = rotateSide_u(lst_cube)
            lst_cube = rotateSide_u(lst_cube)
            lst_cube = rotateSide_L(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_rotate.append("uuLUU") 
            
        elif lst_cube[3][1] == var_w and lst_cube[4][5] != var_w:
            lst_cube = rotateSide_l(lst_cube)
            lst_cube = rotateSide_u(lst_cube)
            lst_cube = rotateSide_b(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_rotate.append("lubU")             
        elif lst_cube[3][3] == var_w and lst_cube[4][5] != var_w:
            lst_cube = rotateSide_u(lst_cube)
            lst_cube = rotateSide_b(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_rotate.append("ubU") 
        elif lst_cube[3][5] == var_w and lst_cube[4][5] != var_w:
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_f(lst_cube)
            lst_cube = rotateSide_u(lst_cube)
            lst_rotate.append("Ufu") 
        elif lst_cube[3][7] == var_w and lst_cube[4][5] != var_w:
            lst_cube = rotateSide_D(lst_cube)
            lst_cube = rotateSide_D(lst_cube)
            lst_cube = rotateSide_R(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_f(lst_cube)
            lst_cube = rotateSide_u(lst_cube)
            lst_rotate.append("DDRUfu") 
            
        elif lst_cube[5][1] == var_w and lst_cube[4][5] != var_w:
            lst_cube = rotateSide_D(lst_cube)
            lst_cube = rotateSide_R(lst_cube)
            lst_cube = rotateSide_R(lst_cube)
            lst_rotate.append("DRR")             
        elif lst_cube[5][3] == var_w and lst_cube[4][5] != var_w:
            lst_cube = rotateSide_D(lst_cube)
            lst_cube = rotateSide_D(lst_cube)
            lst_cube = rotateSide_R(lst_cube)
            lst_cube = rotateSide_R(lst_cube)
            lst_rotate.append("DDRR")   
        elif lst_cube[5][7] == var_w and lst_cube[4][5] != var_w:
            lst_cube = rotateSide_d(lst_cube)
            lst_cube = rotateSide_R(lst_cube)
            lst_cube = rotateSide_R(lst_cube)
            lst_rotate.append("dRR")   
        # else:
        #     lst_cube = lst_cube
        #     lst_rotate.append("")
            
        return [lst_cube, lst_rotate]

def rotateIntoWhiteCross(lst_cube, lst_rotate):
    #if statements. Can have more than one outcome
    #move the top to match the middle first.
    #solve all for [4][5] first
    if lst_cube[4][5] == var_w and (lst_cube[1][1] == lst_cube[0][4]):
        lst_cube = rotateSide_U(lst_cube)
        lst_cube = rotateSide_F(lst_cube)
        lst_cube = rotateSide_F(lst_cube)
        lst_rotate.append("UFF")      

    elif lst_cube[4][5] == var_w and (lst_cube[1][1] == lst_cube[3][4]):
        lst_cube = rotateSide_U(lst_cube)
        lst_cube = rotateSide_U(lst_cube)
        lst_cube = rotateSide_L(lst_cube)
        lst_cube = rotateSide_L(lst_cube)
        lst_rotate.append("UULL") 

    elif lst_cube[4][5] == var_w and (lst_cube[1][1] == lst_cube[2][4]):
        lst_cube = rotateSide_u(lst_cube)
        lst_cube = rotateSide_B(lst_cube)
        lst_cube = rotateSide_B(lst_cube)
        lst_rotate.append("uBB")   

    elif lst_cube[4][5] == var_w and (lst_cube[1][1] == lst_cube[1][4]):
        lst_cube = rotateSide_R(lst_cube)
        lst_cube = rotateSide_R(lst_cube)
        lst_rotate.append("RR")  

##################################################
            # [4][1]
    if lst_cube[4][1] == var_w and (lst_cube[2][1] == lst_cube[0][4]):
        lst_cube = rotateSide_U(lst_cube)
        lst_cube = rotateSide_U(lst_cube)
        lst_cube = rotateSide_F(lst_cube)
        lst_cube = rotateSide_F(lst_cube)
        lst_rotate.append("UUFF")      

    elif lst_cube[4][1] == var_w and (lst_cube[2][1] == lst_cube[3][4]):
        lst_cube = rotateSide_u(lst_cube)
        lst_cube = rotateSide_L(lst_cube)
        lst_cube = rotateSide_L(lst_cube)
        lst_rotate.append("uLL") 

    elif lst_cube[4][1] == var_w and (lst_cube[2][1] == lst_cube[2][4]):
        lst_cube = rotateSide_B(lst_cube)
        lst_cube = rotateSide_B(lst_cube)
        lst_rotate.append("BB")   

    elif lst_cube[4][1] == var_w and (lst_cube[2][1] == lst_cube[1][4]):
        lst_cube = rotateSide_U(lst_cube)
        lst_cube = rotateSide_R(lst_cube)
        lst_cube = rotateSide_R(lst_cube)
        lst_rotate.append("URR")  

##################################################
            # [4][3]
    if lst_cube[4][3] == var_w and (lst_cube[3][1] == lst_cube[0][4]):
        lst_cube = rotateSide_u(lst_cube)
        lst_cube = rotateSide_F(lst_cube)
        lst_cube = rotateSide_F(lst_cube)
        lst_rotate.append("uFF")      

    elif lst_cube[4][3] == var_w and (lst_cube[3][1] == lst_cube[3][4]):
            lst_cube = rotateSide_L(lst_cube)
            lst_cube = rotateSide_L(lst_cube)
            lst_rotate.append("LL") 

    elif lst_cube[4][3] == var_w and (lst_cube[3][1] == lst_cube[2][4]):
        lst_cube = rotateSide_U(lst_cube)
        lst_cube = rotateSide_B(lst_cube)
        lst_cube = rotateSide_B(lst_cube)
        lst_rotate.append("UBB")   

    elif lst_cube[4][3] == var_w and (lst_cube[3][1] == lst_cube[1][4]):
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_R(lst_cube)
            lst_cube = rotateSide_R(lst_cube)
            lst_rotate.append("UURR")          

##################################################
            # [4][7]
    if lst_cube[4][7] == var_w and (lst_cube[0][1] == lst_cube[0][4]):
            lst_cube = rotateSide_F(lst_cube)
            lst_cube = rotateSide_F(lst_cube)
            lst_rotate.append("FF")      

    elif lst_cube[4][7] == var_w and (lst_cube[0][1] == lst_cube[3][4]):
        lst_cube = rotateSide_U(lst_cube)
        lst_cube = rotateSide_L(lst_cube)
        lst_cube = rotateSide_L(lst_cube)
        lst_rotate.append("ULL") 

    elif lst_cube[4][7] == var_w and (lst_cube[0][1] == lst_cube[2][4]):
        lst_cube = rotateSide_u(lst_cube)
        lst_cube = rotateSide_u(lst_cube)
        lst_cube = rotateSide_B(lst_cube)
        lst_cube = rotateSide_B(lst_cube)
        lst_rotate.append("uuBB")   

    elif lst_cube[4][7] == var_w and (lst_cube[0][1] == lst_cube[1][4]):
        lst_cube = rotateSide_u(lst_cube)
        lst_cube = rotateSide_R(lst_cube)
        lst_cube = rotateSide_R(lst_cube)
        lst_rotate.append("uRR")  
    else:
        lst_cube = rotateSide_U(lst_cube) 
        lst_rotate.append("U")  


    return [lst_cube, lst_rotate]


# def rotateIntoWhiteCross(lst_cube, lst_rotate):
#     #if statements. Can have more than one outcome
#     if lst_cube[4][5] == var_w and (lst_cube[1][1] == lst_cube[1][4]):
#         lst_cube = rotateSide_R(lst_cube)
#         lst_cube = rotateSide_R(lst_cube)
#         lst_rotate.append("RR")
#     if lst_cube[4][1] == var_w and (lst_cube[2][1] == lst_cube[2][4]):
#         lst_cube = rotateSide_B(lst_cube)
#         lst_cube = rotateSide_B(lst_cube)
#         lst_rotate.append("BB")   
#     if lst_cube[4][3] == var_w and (lst_cube[3][1] == lst_cube[3][4]):
#         lst_cube = rotateSide_L(lst_cube)
#         lst_cube = rotateSide_L(lst_cube)
#         lst_rotate.append("LL") 
#     if lst_cube[4][7] == var_w and (lst_cube[0][4] == lst_cube[0][1]):
#         lst_cube = rotateSide_F(lst_cube)
#         lst_cube = rotateSide_F(lst_cube)
#         lst_rotate.append("FF")  
#     lst_cube = rotateSide_U(lst_cube)
#     lst_rotate.append("U")      
#
#     return lst_cube, lst_rotate

#######
def front_left_trigger(lst_cube, lst_rotate):
    lst_cube = rotateSide_F(lst_cube)
    lst_cube = rotateSide_U(lst_cube)
    lst_cube = rotateSide_f(lst_cube)   
    lst_rotate.append("FUf")  
    
    return [lst_cube, lst_rotate]

def front_right_trigger(lst_cube, lst_rotate):
    lst_cube = rotateSide_f(lst_cube)
    lst_cube = rotateSide_u(lst_cube)
    lst_cube = rotateSide_F(lst_cube)   
    lst_rotate.append("fuF")  
    
    return [lst_cube, lst_rotate]
#######
def right_left_trigger(lst_cube, lst_rotate):
    lst_cube = rotateSide_R(lst_cube)
    lst_cube = rotateSide_U(lst_cube)
    lst_cube = rotateSide_r(lst_cube)   
    lst_rotate.append("RUr")  
    
    return [lst_cube, lst_rotate]

def right_right_trigger(lst_cube, lst_rotate):
    lst_cube = rotateSide_r(lst_cube)
    lst_cube = rotateSide_u(lst_cube)
    lst_cube = rotateSide_R(lst_cube)   
    lst_rotate.append("ruR")  
    
    return [lst_cube, lst_rotate]

#######
def back_left_trigger(lst_cube, lst_rotate):
    lst_cube = rotateSide_B(lst_cube)
    lst_cube = rotateSide_U(lst_cube)
    lst_cube = rotateSide_b(lst_cube)   
    lst_rotate.append("BUb")  
    
    return [lst_cube, lst_rotate]

def back_right_trigger(lst_cube, lst_rotate):
    lst_cube = rotateSide_b(lst_cube)
    lst_cube = rotateSide_u(lst_cube)
    lst_cube = rotateSide_B(lst_cube)   
    lst_rotate.append("buB")  
    
    return [lst_cube, lst_rotate]

#######
def left_left_trigger(lst_cube, lst_rotate):
    lst_cube = rotateSide_L(lst_cube)
    lst_cube = rotateSide_U(lst_cube)
    lst_cube = rotateSide_l(lst_cube)   
    lst_rotate.append("LUl")  
    
    return [lst_cube, lst_rotate]

def left_right_trigger(lst_cube, lst_rotate):
    lst_cube = rotateSide_l(lst_cube)
    lst_cube = rotateSide_u(lst_cube)
    lst_cube = rotateSide_L(lst_cube)   
    lst_rotate.append("luL")  
    
    return [lst_cube, lst_rotate]

def solve_top_w_corners(lst_cube, lst_rotate):
    
    if lst_cube[3][2] == var_w and lst_cube[0][0] == lst_cube[0][4]:
        lst_rotate.append("") 
        lst_cube = left_right_trigger(lst_cube, lst_rotate)[0]
        
    elif lst_cube[3][2] == var_w and lst_cube[0][0] == lst_cube[3][4]:###
        lst_cube = rotateSide_U(lst_cube)
        lst_rotate.append("U") 
        lst_cube = back_right_trigger(lst_cube, lst_rotate)[0]
        
    elif lst_cube[3][2] == var_w and lst_cube[0][0] == lst_cube[2][4]:
        lst_cube = rotateSide_u(lst_cube)
        lst_cube = rotateSide_u(lst_cube)
        lst_rotate.append("uu")         
        lst_cube = right_right_trigger(lst_cube, lst_rotate)[0]
        
    elif lst_cube[3][2] == var_w and lst_cube[0][0] == lst_cube[1][4]:
        lst_cube = rotateSide_u(lst_cube)
        lst_rotate.append("u") 
        lst_cube = front_right_trigger(lst_cube, lst_rotate)[0]
        
    #[3][0]
    elif lst_cube[3][0] == var_w and lst_cube[2][2] == lst_cube[2][4]:
        lst_cube = back_right_trigger(lst_cube, lst_rotate)[0]  
              
    elif lst_cube[3][0] == var_w and lst_cube[2][2] == lst_cube[1][4]:
        lst_cube = rotateSide_U(lst_cube)
        lst_rotate.append("U")          
        lst_cube = back_left_trigger(lst_cube, lst_rotate)[0]    
    elif lst_cube[3][0] == var_w and lst_cube[2][2] == lst_cube[0][4]:
        lst_cube = rotateSide_U(lst_cube)
        lst_cube = rotateSide_U(lst_cube)
        lst_rotate.append("UU") 
        lst_cube = right_left_trigger(lst_cube, lst_rotate)[0]
    elif lst_cube[3][0] == var_w and lst_cube[2][2] == lst_cube[3][4]:
        lst_cube = rotateSide_u(lst_cube)
        lst_rotate.append("u")              
        lst_cube = left_right_trigger(lst_cube, lst_rotate)[0]
        
    #[0][0] 
    elif lst_cube[0][0] == var_w and lst_cube[3][2] == lst_cube[0][4]:
        lst_cube = rotateSide_u(lst_cube)
        lst_rotate.append("u") 
        lst_cube = right_left_trigger(lst_cube, lst_rotate)[0]
        
    elif lst_cube[0][0] == var_w and lst_cube[3][2] == lst_cube[1][4]:
        lst_cube = rotateSide_u(lst_cube)
        lst_cube = rotateSide_u(lst_cube)
        lst_rotate.append("uu") 
        lst_cube = back_left_trigger(lst_cube, lst_rotate)[0]
        
    elif lst_cube[0][0] == var_w and lst_cube[3][2] == lst_cube[2][4]:
        lst_cube = rotateSide_U(lst_cube)
        lst_rotate.append("U") 
        lst_cube = left_left_trigger(lst_cube, lst_rotate)[0]
        
    elif lst_cube[0][0] == var_w and lst_cube[3][2] == lst_cube[3][4]:
        lst_cube = front_left_trigger(lst_cube, lst_rotate)[0]   
            
    #[0][2]
    elif lst_cube[0][2] == var_w and lst_cube[1][0] == lst_cube[0][4]:
        lst_cube = rotateSide_U(lst_cube)
        lst_rotate.append("U") 
        lst_cube = left_right_trigger(lst_cube, lst_rotate)[0]       

    elif lst_cube[0][2] == var_w and lst_cube[1][0] == lst_cube[1][4]:
        lst_cube = front_right_trigger(lst_cube, lst_rotate)[0]
        
    elif lst_cube[0][2] == var_w and lst_cube[1][0] == lst_cube[2][4]:
        lst_cube = rotateSide_u(lst_cube)
        lst_rotate.append("u") 
        lst_cube = right_right_trigger(lst_cube, lst_rotate)[0]   

    elif lst_cube[0][2] == var_w and lst_cube[1][0] == lst_cube[3][4]:
        lst_cube = rotateSide_U(lst_cube)
        lst_cube = rotateSide_U(lst_cube)
        lst_rotate.append("UU")    
        lst_cube = back_right_trigger(lst_cube, lst_rotate)[0]  
   
        
    #[1][0] 
    elif lst_cube[1][0] == var_w and lst_cube[0][2] == lst_cube[0][4]:
        lst_cube = right_left_trigger(lst_cube, lst_rotate)[0]  
    elif lst_cube[1][0] == var_w and lst_cube[0][2] == lst_cube[1][4]:
        lst_cube = rotateSide_u(lst_cube)
        lst_rotate.append("u") 
        lst_cube = back_left_trigger(lst_cube, lst_rotate)[0]  
    elif lst_cube[1][0] == var_w and lst_cube[0][2] == lst_cube[2][4]:
        lst_cube = rotateSide_u(lst_cube)
        lst_cube = rotateSide_u(lst_cube)
        lst_rotate.append("uu") 
        lst_cube = left_left_trigger(lst_cube, lst_rotate)[0]  
    elif lst_cube[1][0] == var_w and lst_cube[0][2] == lst_cube[3][4]:
        lst_cube = rotateSide_U(lst_cube)
        lst_rotate.append("U")   
        lst_cube = front_left_trigger(lst_cube, lst_rotate)[0]      
                
    #[1][2]
    elif lst_cube[1][2] == var_w and lst_cube[2][0] == lst_cube[0][4]:
        lst_cube = rotateSide_U(lst_cube)
        lst_cube = rotateSide_U(lst_cube)
        lst_rotate.append("UU") 
        lst_cube = left_right_trigger(lst_cube, lst_rotate)[0]     
    
    elif lst_cube[1][2] == var_w and lst_cube[2][0] == lst_cube[1][4]:
        lst_cube = rotateSide_U(lst_cube)
        lst_rotate.append("U") 
        lst_cube = front_right_trigger(lst_cube, lst_rotate)[0]
    
    elif lst_cube[1][2] == var_w and lst_cube[2][0] == lst_cube[2][4]:
        lst_cube = right_right_trigger(lst_cube, lst_rotate)[0]
        
    elif lst_cube[1][2] == var_w and lst_cube[2][0] == lst_cube[3][4]:
        lst_cube = rotateSide_u(lst_cube)
        lst_rotate.append("u")        
        lst_cube = back_right_trigger(lst_cube, lst_rotate)[0]
        
    #[2][0] 
    elif lst_cube[2][0] == var_w and lst_cube[1][2] == lst_cube[0][4]:
        lst_cube = rotateSide_U(lst_cube)
        lst_rotate.append("U")   
        lst_cube = right_left_trigger(lst_cube, lst_rotate)[0]
        
    elif lst_cube[2][0] == var_w and lst_cube[1][2] == lst_cube[1][4]:
        lst_cube = back_left_trigger(lst_cube, lst_rotate)[0]
        
    elif lst_cube[2][0] == var_w and lst_cube[1][2] == lst_cube[2][4]:
        lst_cube = rotateSide_u(lst_cube)
        lst_rotate.append("u") 
        lst_cube = left_left_trigger(lst_cube, lst_rotate)[0]
        
    elif lst_cube[2][0] == var_w and lst_cube[1][2] == lst_cube[3][4]:
        lst_cube = rotateSide_U(lst_cube)
        lst_cube = rotateSide_U(lst_cube)
        lst_rotate.append("UU") 
        lst_cube = front_left_trigger(lst_cube, lst_rotate)[0]
                    
    #[2][2]
    elif lst_cube[2][2] == var_w and lst_cube[3][0] == lst_cube[0][4]: ##
        lst_cube = rotateSide_u(lst_cube)
        lst_rotate.append("u") 
        lst_cube = left_right_trigger(lst_cube, lst_rotate)[0]
        
    elif lst_cube[2][2] == var_w and lst_cube[3][0] == lst_cube[1][4]:
        lst_cube = rotateSide_U(lst_cube)
        lst_cube = rotateSide_U(lst_cube)
        lst_rotate.append("UU") 
        
        lst_cube = front_right_trigger(lst_cube, lst_rotate)[0]
    elif lst_cube[2][2] == var_w and lst_cube[3][0] == lst_cube[2][4]:
        lst_cube = rotateSide_U(lst_cube)
        lst_rotate.append("U") 
        lst_cube = right_right_trigger(lst_cube, lst_rotate)[0]
        
    elif lst_cube[2][2] == var_w and lst_cube[3][0] == lst_cube[3][4]:
        lst_cube = back_right_trigger(lst_cube, lst_rotate)[0] 
        
    return [lst_cube, lst_rotate]

def solve_bottom_w_corners(lst_cube, lst_rotate):
    if lst_cube[0][6] == var_w:
        lst_cube = left_right_trigger(lst_cube, lst_rotate)[0]
    elif lst_cube[0][8] == var_w:
        lst_cube = right_left_trigger(lst_cube, lst_rotate)[0]
    elif lst_cube[1][6] == var_w:
        lst_cube = front_right_trigger(lst_cube, lst_rotate)[0]
    elif lst_cube[1][8] == var_w:
        lst_cube = back_left_trigger(lst_cube, lst_rotate)[0]
    elif lst_cube[2][6] == var_w:
        lst_cube = right_right_trigger(lst_cube, lst_rotate)[0]
    elif lst_cube[2][8] == var_w:
        lst_cube = left_left_trigger(lst_cube, lst_rotate)[0]
    elif lst_cube[3][6] == var_w:
        lst_cube = back_right_trigger(lst_cube, lst_rotate)[0]
    elif lst_cube[3][8] == var_w:
        lst_cube = front_left_trigger(lst_cube, lst_rotate)[0]
        
    return [lst_cube, lst_rotate]


def solve_top_white_cells(lst_cube, lst_rotate):
    if lst_cube[4][6] == var_w and lst_cube[5][0] != var_w:
            lst_cube = rotateSide_l(lst_cube)
            lst_cube = rotateSide_u(lst_cube)
            lst_cube = rotateSide_L(lst_cube) 
            lst_cube = rotateSide_l(lst_cube)
            lst_cube = rotateSide_u(lst_cube)
            lst_cube = rotateSide_L(lst_cube)   
            lst_rotate.append("luLluL")  
    elif lst_cube[4][6] == var_w and lst_cube[5][2] != var_w:
            lst_cube = rotateSide_u(lst_cube)
            lst_cube = rotateSide_R(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_r(lst_cube) 
            lst_cube = rotateSide_R(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_r(lst_cube)   
            lst_rotate.append("uRUrRUr")  
    elif lst_cube[4][6] == var_w and lst_cube[5][8] != var_w:
            lst_cube = rotateSide_u(lst_cube)
            lst_cube = rotateSide_u(lst_cube)
            lst_cube = rotateSide_B(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_b(lst_cube) 
            lst_cube = rotateSide_B(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_b(lst_cube)   
            lst_rotate.append("uuBUbBUb")  
    elif lst_cube[4][6] == var_w and lst_cube[5][6] != var_w:
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_b(lst_cube)
            lst_cube = rotateSide_u(lst_cube)
            lst_cube = rotateSide_B(lst_cube) 
            lst_cube = rotateSide_b(lst_cube)
            lst_cube = rotateSide_u(lst_cube)
            lst_cube = rotateSide_B(lst_cube)   
            lst_rotate.append("UbuBbuB")            
            
    elif lst_cube[4][8] == var_w and lst_cube[5][2] != var_w:
            lst_cube = rotateSide_R(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_r(lst_cube) 
            lst_cube = rotateSide_R(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_r(lst_cube)   
            lst_rotate.append("RUrRUr")      
    elif lst_cube[4][8] == var_w and lst_cube[5][0] != var_w:
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_l(lst_cube)
            lst_cube = rotateSide_u(lst_cube)
            lst_cube = rotateSide_L(lst_cube) 
            lst_cube = rotateSide_l(lst_cube)
            lst_cube = rotateSide_u(lst_cube)
            lst_cube = rotateSide_L(lst_cube)   
            lst_rotate.append("UluLluL")  

    elif lst_cube[4][8] == var_w and lst_cube[5][8] != var_w:
            lst_cube = rotateSide_u(lst_cube)
            lst_cube = rotateSide_u(lst_cube)
            lst_cube = rotateSide_B(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_b(lst_cube) 
            lst_cube = rotateSide_B(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_b(lst_cube)   
            lst_rotate.append("uuBUbBUb")   
    elif lst_cube[4][8] == var_w and lst_cube[5][6] != var_w:
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_b(lst_cube)
            lst_cube = rotateSide_u(lst_cube)
            lst_cube = rotateSide_B(lst_cube) 
            lst_cube = rotateSide_b(lst_cube)
            lst_cube = rotateSide_u(lst_cube)
            lst_cube = rotateSide_B(lst_cube)   
            lst_rotate.append("UUbuBbuB") 
    ###here
    elif lst_cube[4][0] == var_w and lst_cube[5][6] != var_w:
            lst_cube = rotateSide_b(lst_cube)
            lst_cube = rotateSide_u(lst_cube)
            lst_cube = rotateSide_B(lst_cube) 
            lst_cube = rotateSide_b(lst_cube)
            lst_cube = rotateSide_u(lst_cube)
            lst_cube = rotateSide_B(lst_cube)   
            lst_rotate.append("buBbuB") 
    elif lst_cube[4][0] == var_w and lst_cube[5][0] != var_w:
            lst_cube = rotateSide_u(lst_cube)
            lst_cube = rotateSide_l(lst_cube)
            lst_cube = rotateSide_u(lst_cube)
            lst_cube = rotateSide_L(lst_cube) 
            lst_cube = rotateSide_l(lst_cube)
            lst_cube = rotateSide_u(lst_cube)
            lst_cube = rotateSide_L(lst_cube)   
            lst_rotate.append("uluLluL") 
    elif lst_cube[4][0] == var_w and lst_cube[5][8] != var_w:
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_B(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_b(lst_cube) 
            lst_cube = rotateSide_B(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_b(lst_cube)   
            lst_rotate.append("UBUbBUb")   
    elif lst_cube[4][0] == var_w and lst_cube[5][2] != var_w:
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_R(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_r(lst_cube) 
            lst_cube = rotateSide_R(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_r(lst_cube)   
            lst_rotate.append("UURUrRUr") 
            
    elif lst_cube[4][2] == var_w and lst_cube[5][8] != var_w:
            lst_cube = rotateSide_B(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_b(lst_cube) 
            lst_cube = rotateSide_B(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_b(lst_cube)   
            lst_rotate.append("BUbBUb")
            
    elif lst_cube[4][2] == var_w and lst_cube[5][0] != var_w:
            lst_cube = rotateSide_u(lst_cube)
            lst_cube = rotateSide_u(lst_cube)
            lst_cube = rotateSide_l(lst_cube)
            lst_cube = rotateSide_u(lst_cube)
            lst_cube = rotateSide_L(lst_cube) 
            lst_cube = rotateSide_l(lst_cube)
            lst_cube = rotateSide_u(lst_cube)
            lst_cube = rotateSide_L(lst_cube)   
            lst_rotate.append("uuluLluL") 
    elif lst_cube[4][2] == var_w and lst_cube[5][6] != var_w:
            lst_cube = rotateSide_u(lst_cube)
            lst_cube = rotateSide_b(lst_cube)
            lst_cube = rotateSide_u(lst_cube)
            lst_cube = rotateSide_B(lst_cube) 
            lst_cube = rotateSide_b(lst_cube)
            lst_cube = rotateSide_u(lst_cube)
            lst_cube = rotateSide_B(lst_cube)   
            lst_rotate.append("ubuBbuB") 

    elif lst_cube[4][2] == var_w and lst_cube[5][2] != var_w:
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_R(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_r(lst_cube) 
            lst_cube = rotateSide_R(lst_cube)
            lst_cube = rotateSide_u(lst_cube)
            lst_cube = rotateSide_r(lst_cube)   
            lst_rotate.append("URUrRur") 
        
    return [lst_cube, lst_rotate]

def rotateIntoTSolve(lst_cube, lst_rotate):
    #top piece with no yellow. Then matches the side with one of center colors
    if lst_cube[4][7] != var_y and lst_cube[0][1] != var_y:
        if lst_cube[0][1] == lst_cube[0][4] == lst_cube[0][7]:
            if lst_cube[4][7] == lst_cube[1][4]:
                lst_cube = rotateSide_U(lst_cube)
                lst_rotate.append("U") 
                lst_cube = right_left_trigger(lst_cube, lst_rotate)[0]            
            elif lst_cube[4][7] == lst_cube[3][4]:                                            
                lst_cube = rotateSide_u(lst_cube) 
                lst_rotate.append("u")  
                lst_cube = left_right_trigger(lst_cube, lst_rotate)[0]
                
        elif lst_cube[0][1] == lst_cube[1][4] == lst_cube[1][7]:
            lst_cube = rotateSide_u(lst_cube)
            lst_rotate.append("u")            
            if lst_cube[4][5] == lst_cube[2][4]:
                lst_cube = rotateSide_U(lst_cube)
                lst_rotate.append("U") 
                lst_cube = back_left_trigger(lst_cube, lst_rotate)[0]            
            elif lst_cube[4][5] == lst_cube[0][4]:                                            
                lst_cube = rotateSide_u(lst_cube) 
                lst_rotate.append("u")  
                lst_cube = front_right_trigger(lst_cube, lst_rotate)[0]   
            
        elif lst_cube[0][1] == lst_cube[2][4] == lst_cube[2][7]:
            lst_cube = rotateSide_u(lst_cube)
            lst_cube = rotateSide_u(lst_cube)
            lst_rotate.append("uu") 
            if lst_cube[4][1] == lst_cube[3][4]:
                lst_cube = rotateSide_U(lst_cube)
                lst_rotate.append("U") 
                lst_cube = left_left_trigger(lst_cube, lst_rotate)[0]            
            elif lst_cube[4][1] == lst_cube[1][4]:                                            
                lst_cube = rotateSide_u(lst_cube) 
                lst_rotate.append("u")  
                lst_cube = right_right_trigger(lst_cube, lst_rotate)[0]  
    
        elif lst_cube[0][1] == lst_cube[3][4] == lst_cube[3][7]:
            lst_cube = rotateSide_U(lst_cube)
            lst_rotate.append("U")            
            if lst_cube[4][3] == lst_cube[0][4]:
                lst_cube = rotateSide_U(lst_cube)
                lst_rotate.append("U") 
                lst_cube = front_left_trigger(lst_cube, lst_rotate)[0]            
            elif lst_cube[4][3] == lst_cube[2][4]:                                            
                lst_cube = rotateSide_u(lst_cube) 
                lst_rotate.append("u")  
                lst_cube = back_right_trigger(lst_cube, lst_rotate)[0]  
            
#############################################   

    elif lst_cube[4][5] != var_y and lst_cube[1][1] != var_y:
        if lst_cube[1][1] == lst_cube[0][4] == lst_cube[0][7]:
            lst_cube = rotateSide_U(lst_cube)
            lst_rotate.append("U") 
            if lst_cube[4][7] == lst_cube[1][4]:
                lst_cube = rotateSide_U(lst_cube)
                lst_rotate.append("U") 
                lst_cube = right_left_trigger(lst_cube, lst_rotate)[0] 
            elif lst_cube[4][7] == lst_cube[2][4]:                                            
                lst_cube = rotateSide_u(lst_cube) 
                lst_rotate.append("u")  
                lst_cube = left_right_trigger(lst_cube, lst_rotate)[0]              
            
        elif lst_cube[1][1] == lst_cube[1][4] == lst_cube[1][7]:
            if lst_cube[4][5] == lst_cube[2][4]:
                lst_cube = rotateSide_U(lst_cube)
                lst_rotate.append("U") 
                lst_cube = back_left_trigger(lst_cube, lst_rotate)[0]            
            elif lst_cube[4][5] == lst_cube[0][4]:                                            
                lst_cube = rotateSide_u(lst_cube) 
                lst_rotate.append("u")  
                lst_cube = front_right_trigger(lst_cube, lst_rotate)[0]                

        elif lst_cube[1][1] == lst_cube[2][4] == lst_cube[2][7]:
            lst_cube = rotateSide_u(lst_cube)
            lst_rotate.append("u") 
            if lst_cube[4][1] == lst_cube[3][4]:
                lst_cube = rotateSide_U(lst_cube)
                lst_rotate.append("U") 
                lst_cube = left_left_trigger(lst_cube, lst_rotate)[0]            
            elif lst_cube[4][1] == lst_cube[1][4]:                                            
                lst_cube = rotateSide_u(lst_cube) 
                lst_rotate.append("u")  
                lst_cube = right_right_trigger(lst_cube, lst_rotate)[0]      
            
            
        elif lst_cube[1][1] == lst_cube[3][4] == lst_cube[3][7]:
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_rotate.append("UU") 
            if lst_cube[4][3] == lst_cube[0][4]:
                lst_cube = rotateSide_U(lst_cube)
                lst_rotate.append("U") 
                lst_cube = front_left_trigger(lst_cube, lst_rotate)[0]            
            elif lst_cube[4][3] == lst_cube[2][4]:                                            
                lst_cube = rotateSide_u(lst_cube) 
                lst_rotate.append("u")  
                lst_cube = back_right_trigger(lst_cube, lst_rotate)[0]             
            
            
#############################################            
    elif lst_cube[4][1] != var_y and lst_cube[2][1] != var_y:
        if lst_cube[2][1] == lst_cube[0][4] == lst_cube[0][7]:
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_rotate.append("UU")             
            if lst_cube[4][7] == lst_cube[1][4]:
                lst_cube = rotateSide_U(lst_cube)
                lst_rotate.append("U") 
                lst_cube = right_left_trigger(lst_cube, lst_rotate)[0]            
            elif lst_cube[4][7] == lst_cube[3][4]:                                            
                lst_cube = rotateSide_u(lst_cube) 
                lst_rotate.append("u")  
                lst_cube = left_right_trigger(lst_cube, lst_rotate)[0]                
            
        elif lst_cube[2][1] == lst_cube[1][4] == lst_cube[1][7]:
            lst_cube = rotateSide_U(lst_cube)
            lst_rotate.append("U") 
            if lst_cube[4][5] == lst_cube[2][4]:
                lst_cube = rotateSide_U(lst_cube)
                lst_rotate.append("U") 
                lst_cube = back_left_trigger(lst_cube, lst_rotate)[0]            
            elif lst_cube[4][5] == lst_cube[0][4]:                                            
                lst_cube = rotateSide_u(lst_cube) 
                lst_rotate.append("u")  
                lst_cube = front_right_trigger(lst_cube, lst_rotate)[0]   
            
            
        elif lst_cube[2][1] == lst_cube[2][4] == lst_cube[2][7]:
            if lst_cube[4][1] == lst_cube[3][4]:
                lst_cube = rotateSide_U(lst_cube)
                lst_rotate.append("U") 
                lst_cube = left_left_trigger(lst_cube, lst_rotate)[0]            
            elif lst_cube[4][1] == lst_cube[1][4]:                                            
                lst_cube = rotateSide_u(lst_cube) 
                lst_rotate.append("u")  
                lst_cube = right_right_trigger(lst_cube, lst_rotate)[0]             
            
        elif lst_cube[2][1] == lst_cube[3][4] == lst_cube[3][7]:
            lst_cube = rotateSide_u(lst_cube)
            lst_rotate.append("u") 
            if lst_cube[4][3] == lst_cube[0][4]:
                lst_cube = rotateSide_U(lst_cube)
                lst_rotate.append("U") 
                lst_cube = front_left_trigger(lst_cube, lst_rotate)[0]            
            elif lst_cube[4][3] == lst_cube[1][4]:                                            
                lst_cube = rotateSide_u(lst_cube) 
                lst_rotate.append("u")  
                lst_cube = back_right_trigger(lst_cube, lst_rotate)[0]            
            
            
#############################################
           
    elif lst_cube[4][3] != var_y :
        if lst_cube[3][1] == lst_cube[0][4] == lst_cube[0][7]:
            lst_cube = rotateSide_u(lst_cube)
            lst_rotate.append("u") 
            if lst_cube[4][7] == lst_cube[1][4]:
                lst_cube = rotateSide_U(lst_cube)
                lst_rotate.append("U") 
                lst_cube = right_left_trigger(lst_cube, lst_rotate)[0]            
            elif lst_cube[4][7] == lst_cube[3][4]:                                            
                lst_cube = rotateSide_u(lst_cube) 
                lst_rotate.append("u")  
                lst_cube = left_right_trigger(lst_cube, lst_rotate)[0]    
            
            
        elif lst_cube[3][1] == lst_cube[1][4] == lst_cube[1][7]:
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_rotate.append("UU") 
            if lst_cube[4][5] == lst_cube[2][4]:
                lst_cube = rotateSide_U(lst_cube)
                lst_rotate.append("U") 
                lst_cube = back_left_trigger(lst_cube, lst_rotate)[0]            
            elif lst_cube[4][5] == lst_cube[0][4]:                                            
                lst_cube = rotateSide_u(lst_cube) 
                lst_rotate.append("u")  
                lst_cube = front_right_trigger(lst_cube, lst_rotate)[0]   
            
            
        elif lst_cube[3][1] == lst_cube[2][4] == lst_cube[2][7]:
            lst_cube = rotateSide_U(lst_cube)
            lst_rotate.append("U")
            if lst_cube[4][1] == lst_cube[3][4]:
                lst_cube = rotateSide_U(lst_cube)
                lst_rotate.append("U") 
                lst_cube = left_left_trigger(lst_cube, lst_rotate)[0]            
            elif lst_cube[4][1] == lst_cube[1][4]:                                            
                lst_cube = rotateSide_u(lst_cube) 
                lst_rotate.append("u")  
                lst_cube = right_right_trigger(lst_cube, lst_rotate)[0]   
            
            
        elif lst_cube[3][1] == lst_cube[3][4] == lst_cube[3][7]:
            if lst_cube[4][3] == lst_cube[0][4]:
                lst_cube = rotateSide_U(lst_cube)
                lst_rotate.append("U") 
                lst_cube = front_left_trigger(lst_cube, lst_rotate)[0]            
            elif lst_cube[4][3] == lst_cube[2][4]:                                            
                lst_cube = rotateSide_u(lst_cube) 
                lst_rotate.append("u")  
                lst_cube = back_right_trigger(lst_cube, lst_rotate)[0]   
            
    return [lst_cube, lst_rotate]
            

                




        
        
        
        