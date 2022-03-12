#BbLlUuDd

def rotateSide_F(orig_cube):
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
    new_cube[1].insert(1, orig_cube [1][1])
    new_cube[1].insert(2, orig_cube [1][2])
    new_cube[1].insert(3, orig_cube [4][7])
    new_cube[1].insert(4, orig_cube [1][4])
    new_cube[1].insert(5, orig_cube [1][5])
    new_cube[1].insert(6, orig_cube [4][8])
    new_cube[1].insert(7, orig_cube [1][7])
    new_cube[1].insert(8, orig_cube [1][8])
    
    #back    
    new_cube[2].insert(0, orig_cube [2][0])
    new_cube[2].insert(1, orig_cube [2][1])
    new_cube[2].insert(2, orig_cube [2][2])
    new_cube[2].insert(3, orig_cube [2][3])
    new_cube[2].insert(4, orig_cube [2][4])
    new_cube[2].insert(5, orig_cube [2][5])
    new_cube[2].insert(6, orig_cube [2][6])
    new_cube[2].insert(7, orig_cube [2][7])
    new_cube[2].insert(8, orig_cube [2][8])
    
    #left    
    new_cube[3].insert(0, orig_cube [3][0])
    new_cube[3].insert(1, orig_cube [3][1])
    new_cube[3].insert(2, orig_cube [5][0])
    new_cube[3].insert(3, orig_cube [3][3])
    new_cube[3].insert(4, orig_cube [3][4])
    new_cube[3].insert(5, orig_cube [5][1])
    new_cube[3].insert(6, orig_cube [3][6])
    new_cube[3].insert(7, orig_cube [3][7])
    new_cube[3].insert(8, orig_cube [5][2])
    
    #top    
    new_cube[4].insert(0, orig_cube [4][0])
    new_cube[4].insert(1, orig_cube [4][1])
    new_cube[4].insert(2, orig_cube [4][2])
    new_cube[4].insert(3, orig_cube [4][3])
    new_cube[4].insert(4, orig_cube [4][4])
    new_cube[4].insert(5, orig_cube [4][5])
    new_cube[4].insert(6, orig_cube [3][8])
    new_cube[4].insert(7, orig_cube [3][5])
    new_cube[4].insert(8, orig_cube [3][2])
    
    #bottom    
    new_cube[5].insert(0, orig_cube [1][6])
    new_cube[5].insert(1, orig_cube [1][3])
    new_cube[5].insert(2, orig_cube [1][0])
    new_cube[5].insert(3, orig_cube [5][3])
    new_cube[5].insert(4, orig_cube [5][4])
    new_cube[5].insert(5, orig_cube [5][5])
    new_cube[5].insert(6, orig_cube [5][6])
    new_cube[5].insert(7, orig_cube [5][7])
    new_cube[5].insert(8, orig_cube [5][8])
    return new_cube

def rotateSide_f(orig_cube):
    new_cube = [[], [], [], [], [], []]
    #front
    new_cube[0].insert(0, orig_cube [0][2])
    new_cube[0].insert(1, orig_cube [0][5])
    new_cube[0].insert(2, orig_cube [0][8])
    new_cube[0].insert(3, orig_cube [0][1])
    new_cube[0].insert(4, orig_cube [0][4])
    new_cube[0].insert(5, orig_cube [0][7])
    new_cube[0].insert(6, orig_cube [0][0])
    new_cube[0].insert(7, orig_cube [0][3])
    new_cube[0].insert(8, orig_cube [0][6])
    
    #right- takes from 5
    new_cube[1].insert(0, orig_cube [5][2])
    new_cube[1].insert(1, orig_cube [1][1])
    new_cube[1].insert(2, orig_cube [1][2])
    new_cube[1].insert(3, orig_cube [5][1])
    new_cube[1].insert(4, orig_cube [1][4])
    new_cube[1].insert(5, orig_cube [1][5])
    new_cube[1].insert(6, orig_cube [5][0])
    new_cube[1].insert(7, orig_cube [1][7])
    new_cube[1].insert(8, orig_cube [1][8])
    
    #back  - stays same  
    new_cube[2].insert(0, orig_cube [2][0])
    new_cube[2].insert(1, orig_cube [2][1])
    new_cube[2].insert(2, orig_cube [2][2])
    new_cube[2].insert(3, orig_cube [2][3])
    new_cube[2].insert(4, orig_cube [2][4])
    new_cube[2].insert(5, orig_cube [2][5])
    new_cube[2].insert(6, orig_cube [2][6])
    new_cube[2].insert(7, orig_cube [2][7])
    new_cube[2].insert(8, orig_cube [2][8])
    
    #left - takes from 4
    new_cube[3].insert(0, orig_cube [3][0])
    new_cube[3].insert(1, orig_cube [3][1])
    new_cube[3].insert(2, orig_cube [4][8])
    new_cube[3].insert(3, orig_cube [3][3])
    new_cube[3].insert(4, orig_cube [3][4])
    new_cube[3].insert(5, orig_cube [4][7])
    new_cube[3].insert(6, orig_cube [3][6])
    new_cube[3].insert(7, orig_cube [3][7])
    new_cube[3].insert(8, orig_cube [4][6])
    
    #top - takes from 1  
    new_cube[4].insert(0, orig_cube [4][0])
    new_cube[4].insert(1, orig_cube [4][1])
    new_cube[4].insert(2, orig_cube [4][2])
    new_cube[4].insert(3, orig_cube [4][3])
    new_cube[4].insert(4, orig_cube [4][4])
    new_cube[4].insert(5, orig_cube [4][5])
    new_cube[4].insert(6, orig_cube [1][0])
    new_cube[4].insert(7, orig_cube [1][3])
    new_cube[4].insert(8, orig_cube [1][6])
    
    #bottom - takes from 3
    new_cube[5].insert(0, orig_cube [3][2])
    new_cube[5].insert(1, orig_cube [3][5])
    new_cube[5].insert(2, orig_cube [3][8])
    new_cube[5].insert(3, orig_cube [5][3])
    new_cube[5].insert(4, orig_cube [5][4])
    new_cube[5].insert(5, orig_cube [5][5])
    new_cube[5].insert(6, orig_cube [5][6])
    new_cube[5].insert(7, orig_cube [5][7])
    new_cube[5].insert(8, orig_cube [5][8])
    return new_cube

def rotateSide_R(orig_cube):
    new_cube = [[], [], [], [], [], []]

    new_cube[0].insert(0, orig_cube [0][0])
    new_cube[0].insert(1, orig_cube [0][1])
    new_cube[0].insert(2, orig_cube [5][2])
    new_cube[0].insert(3, orig_cube [0][3])
    new_cube[0].insert(4, orig_cube [0][4])
    new_cube[0].insert(5, orig_cube [5][5])
    new_cube[0].insert(6, orig_cube [0][6])
    new_cube[0].insert(7, orig_cube [0][7])
    new_cube[0].insert(8, orig_cube [5][8])
    
    new_cube[1].insert(0, orig_cube [1][6])
    new_cube[1].insert(1, orig_cube [1][3])
    new_cube[1].insert(2, orig_cube [1][0])
    new_cube[1].insert(3, orig_cube [1][7])
    new_cube[1].insert(4, orig_cube [1][4])
    new_cube[1].insert(5, orig_cube [1][1])
    new_cube[1].insert(6, orig_cube [1][8])
    new_cube[1].insert(7, orig_cube [1][5])
    new_cube[1].insert(8, orig_cube [1][2])
    
    new_cube[2].insert(0, orig_cube [4][8])
    new_cube[2].insert(1, orig_cube [2][1])
    new_cube[2].insert(2, orig_cube [2][2])
    new_cube[2].insert(3, orig_cube [4][5])
    new_cube[2].insert(4, orig_cube [2][4])
    new_cube[2].insert(5, orig_cube [2][5])
    new_cube[2].insert(6, orig_cube [4][2])
    new_cube[2].insert(7, orig_cube [2][7])
    new_cube[2].insert(8, orig_cube [2][8])    

    new_cube[3].insert(0, orig_cube [3][0])
    new_cube[3].insert(1, orig_cube [3][1])
    new_cube[3].insert(2, orig_cube [3][2])
    new_cube[3].insert(3, orig_cube [3][3])
    new_cube[3].insert(4, orig_cube [3][4])
    new_cube[3].insert(5, orig_cube [3][5])
    new_cube[3].insert(6, orig_cube [3][6])
    new_cube[3].insert(7, orig_cube [3][7])
    new_cube[3].insert(8, orig_cube [3][8])   

    new_cube[4].insert(0, orig_cube [4][0])
    new_cube[4].insert(1, orig_cube [4][1])
    new_cube[4].insert(2, orig_cube [0][2])
    new_cube[4].insert(3, orig_cube [4][3])
    new_cube[4].insert(4, orig_cube [4][4])
    new_cube[4].insert(5, orig_cube [0][5])
    new_cube[4].insert(6, orig_cube [4][6])
    new_cube[4].insert(7, orig_cube [4][7])
    new_cube[4].insert(8, orig_cube [0][8])
    
    new_cube[5].insert(0, orig_cube [5][0])
    new_cube[5].insert(1, orig_cube [5][1])
    new_cube[5].insert(2, orig_cube [2][6])
    new_cube[5].insert(3, orig_cube [5][3])
    new_cube[5].insert(4, orig_cube [5][4])
    new_cube[5].insert(5, orig_cube [2][3])
    new_cube[5].insert(6, orig_cube [5][6])
    new_cube[5].insert(7, orig_cube [5][7])
    new_cube[5].insert(8, orig_cube [2][0])
    return new_cube

def rotateSide_r(orig_cube):
    new_cube = [[], [], [], [], [], []]
    new_cube[0].insert(0, orig_cube [0][0])
    new_cube[0].insert(1, orig_cube [0][1])
    new_cube[0].insert(2, orig_cube [4][2])
    new_cube[0].insert(3, orig_cube [0][3])
    new_cube[0].insert(4, orig_cube [0][4])
    new_cube[0].insert(5, orig_cube [4][5])
    new_cube[0].insert(6, orig_cube [0][6])
    new_cube[0].insert(7, orig_cube [0][7])
    new_cube[0].insert(8, orig_cube [4][8])
    #side that rotates cc
    new_cube[1].insert(0, orig_cube [1][2])
    new_cube[1].insert(1, orig_cube [1][5])
    new_cube[1].insert(2, orig_cube [1][8])
    new_cube[1].insert(3, orig_cube [1][1])
    new_cube[1].insert(4, orig_cube [1][4])
    new_cube[1].insert(5, orig_cube [1][7])
    new_cube[1].insert(6, orig_cube [1][0])
    new_cube[1].insert(7, orig_cube [1][3])
    new_cube[1].insert(8, orig_cube [1][6])
    
    new_cube[2].insert(0, orig_cube [5][8])
    new_cube[2].insert(1, orig_cube [2][1])
    new_cube[2].insert(2, orig_cube [2][2])
    new_cube[2].insert(3, orig_cube [5][5])
    new_cube[2].insert(4, orig_cube [2][4])
    new_cube[2].insert(5, orig_cube [2][5])
    new_cube[2].insert(6, orig_cube [5][2])
    new_cube[2].insert(7, orig_cube [2][7])
    new_cube[2].insert(8, orig_cube [2][8])    

    new_cube[3].insert(0, orig_cube [3][0])
    new_cube[3].insert(1, orig_cube [3][1])
    new_cube[3].insert(2, orig_cube [3][2])
    new_cube[3].insert(3, orig_cube [3][3])
    new_cube[3].insert(4, orig_cube [3][4])
    new_cube[3].insert(5, orig_cube [3][5])
    new_cube[3].insert(6, orig_cube [3][6])
    new_cube[3].insert(7, orig_cube [3][7])
    new_cube[3].insert(8, orig_cube [3][8])   

    new_cube[4].insert(0, orig_cube [4][0])
    new_cube[4].insert(1, orig_cube [4][1])
    new_cube[4].insert(2, orig_cube [2][6])
    new_cube[4].insert(3, orig_cube [4][3])
    new_cube[4].insert(4, orig_cube [4][4])
    new_cube[4].insert(5, orig_cube [2][3])
    new_cube[4].insert(6, orig_cube [4][6])
    new_cube[4].insert(7, orig_cube [4][7])
    new_cube[4].insert(8, orig_cube [2][0])
    
    new_cube[5].insert(0, orig_cube [5][0])
    new_cube[5].insert(1, orig_cube [5][1])
    new_cube[5].insert(2, orig_cube [0][2])
    new_cube[5].insert(3, orig_cube [5][3])
    new_cube[5].insert(4, orig_cube [5][4])
    new_cube[5].insert(5, orig_cube [0][5])
    new_cube[5].insert(6, orig_cube [5][6])
    new_cube[5].insert(7, orig_cube [5][7])
    new_cube[5].insert(8, orig_cube [0][8])
    return new_cube


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

def rotateSide_b(orig_cube): #rotates cc
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
    parm_string = parms.get("cube")  #get the string
    
    lst_cube = ([x for x in parms.get("cube")])
    lst_in1, lst_in2, lst_in3, lst_in4, lst_in5, lst_in6 = ([] for i in range(6)) 
    
    for i in range (1,7):
        for j in range(1,10):
            exec(f"lst_in{i}.append(lst_cube.pop(0))")  
            
    for i in range(1,7):
        exec(f'lst_cube.append(lst_in{i})') 
    
    return lst_cube

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


def turn_type1(orig_cube):
    turned_side = []
    turned_side.insert(0, orig_cube [6])
    turned_side.insert(1, orig_cube [3])
    turned_side.insert(2, orig_cube [0])
    turned_side.insert(3, orig_cube [7])
    turned_side.insert(4, orig_cube [4])
    turned_side.insert(5, orig_cube [1])
    turned_side.insert(6, orig_cube [8])
    turned_side.insert(7, orig_cube [5])
    turned_side.insert(8, orig_cube [2])
    return turned_side
        
def turn_type2(orig_cube):
    turned_side = []
    turned_side.insert(0, orig_cube [2])
    turned_side.insert(1, orig_cube [5])
    turned_side.insert(2, orig_cube [8])
    turned_side.insert(3, orig_cube [1])
    turned_side.insert(4, orig_cube [4])
    turned_side.insert(5, orig_cube [7])
    turned_side.insert(6, orig_cube [0])
    turned_side.insert(7, orig_cube [3])
    turned_side.insert(8, orig_cube [6])
    return turned_side
        
def turn_type3(orig_cube):
    turned_side = []
    turned_side.insert(0, orig_cube [8])
    turned_side.insert(1, orig_cube [7])
    turned_side.insert(2, orig_cube [6])
    turned_side.insert(3, orig_cube [5])
    turned_side.insert(4, orig_cube [4])
    turned_side.insert(5, orig_cube [3])
    turned_side.insert(6, orig_cube [2])
    turned_side.insert(7, orig_cube [1])
    turned_side.insert(8, orig_cube [0])
    return turned_side

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
        #rotate cube to right
        first_side = cube.pop(0)
        cube.insert(3, first_side)        
        # rotate the top
        orig_cube = cube.pop(4)
        cube.insert(4, turn_type1(orig_cube))        
        #now rotate the bottom
        orig_cube = cube.pop(5) 
        cube.insert(5, turn_type2(orig_cube))
        return cube
 
 
def y_0_WhiteLeafPos0_5(lst_cube, lst_rotate):
        
        #one line
        if lst_cube[0][5] == "w":
            lst_cube = lst_cube
            lst_rotate.append("") 
        
        elif lst_cube[5][5] == 'w': 
            lst_cube = rotateSide_R(lst_cube)
            lst_rotate.append("R")   
        elif lst_cube[4][5] == 'w':
            lst_cube = rotateSide_r(lst_cube)
            lst_rotate.append("r") 
        #two lines of movement
        elif lst_cube[2][3] == 'w':
            lst_cube = rotateSide_R(lst_cube)
            lst_cube = rotateSide_R(lst_cube)
            lst_rotate.append("RR")               
        elif lst_cube[4][7] == 'w':
            lst_cube = rotateSide_u(lst_cube)
            lst_cube = rotateSide_r(lst_cube)
            lst_rotate.append("ur")  
        elif lst_cube[5][1] == 'w': 
            lst_cube = rotateSide_D(lst_cube)
            lst_cube = rotateSide_R(lst_cube)
            lst_rotate.append("DR")             
        #three lines of movement
        elif lst_cube[1][1] == 'w':
            lst_cube = rotateSide_f(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_F(lst_cube)  
            lst_rotate.append("fUF")  
        #four lines of movement  
        elif lst_cube[1][3] == 'w':
            lst_cube = rotateSide_R(lst_cube)
            lst_cube = rotateSide_f(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_F(lst_cube)  
            lst_rotate.append("RfUF")  
        elif lst_cube[1][5] == 'w':
            lst_cube = rotateSide_r(lst_cube)
            lst_cube = rotateSide_f(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_F(lst_cube)  
            lst_rotate.append("rfUF")
        elif lst_cube[2][1] == 'w':
            lst_cube = rotateSide_f(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_F(lst_cube)
            lst_rotate.append("fUUF")             
            
        #five lines of movement     
        elif lst_cube[4][1] == 'w':
            lst_cube = rotateSide_b(lst_cube)
            lst_cube = rotateSide_r(lst_cube)
            lst_cube = rotateSide_f(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_F(lst_cube)   
            lst_rotate.append("brfUF")             
        elif lst_cube[1][7] == 'w': 
            lst_cube = rotateSide_r(lst_cube)
            lst_cube = rotateSide_r(lst_cube)
            lst_cube = rotateSide_f(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_F(lst_cube)
            lst_rotate.append("rrfUF")    
        elif lst_cube[2][5] == 'w':
            lst_cube = rotateSide_b(lst_cube)
            lst_cube = rotateSide_f(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_F(lst_cube)
            lst_rotate.append("bfUUF") 
        elif lst_cube[4][3] == 'w':
            lst_cube = rotateSide_f(lst_cube)
            lst_cube = rotateSide_f(lst_cube)
            lst_cube = rotateSide_L(lst_cube)
            lst_cube = rotateSide_F(lst_cube)
            lst_cube = rotateSide_F(lst_cube) 
            lst_rotate.append("ffLFF")     
            
        #six lines of movement  
        elif lst_cube[2][7] == 'w':
            lst_cube = rotateSide_b(lst_cube)
            lst_cube = rotateSide_b(lst_cube)
            lst_cube = rotateSide_f(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_F(lst_cube)
            lst_rotate.append("bbfUUF")  
        elif lst_cube[3][3] == 'w':
            lst_cube = rotateSide_b(lst_cube)
            lst_cube = rotateSide_b(lst_cube)
            lst_cube = rotateSide_r(lst_cube)
            lst_cube = rotateSide_f(lst_cube) 
            lst_cube = rotateSide_U(lst_cube) 
            lst_cube = rotateSide_F(lst_cube) 
            lst_rotate.append("bbrfUF") 
        elif lst_cube[5][7] == 'w':
            lst_cube = rotateSide_B(lst_cube)
            lst_cube = rotateSide_r(lst_cube)
            lst_cube = rotateSide_f(lst_cube) 
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_F(lst_cube) 
            lst_rotate.append("brfUF") 
            
        elif lst_cube[5][3] == 'w':
            lst_cube = rotateSide_F(lst_cube)
            lst_cube = rotateSide_F(lst_cube)
            lst_cube = rotateSide_l(lst_cube)
            lst_cube = rotateSide_F(lst_cube) 
            lst_cube = rotateSide_F(lst_cube) 
            lst_rotate.append("FFlFF")   
            
        #more than six
        elif lst_cube[3][1] == 'w':
            lst_cube = rotateSide_l(lst_cube)
            lst_cube = rotateSide_b(lst_cube)
            lst_cube = rotateSide_L(lst_cube)
            lst_cube = rotateSide_b(lst_cube)
            lst_cube = rotateSide_r(lst_cube)
            lst_cube = rotateSide_f(lst_cube) 
            lst_cube = rotateSide_U(lst_cube) 
            lst_cube = rotateSide_F(lst_cube) 
            lst_rotate.append("lbLbrfUF")             
        elif lst_cube[3][5] == 'w':
            lst_cube = rotateSide_l(lst_cube)
            lst_cube = rotateSide_l(lst_cube)
            lst_cube = rotateSide_b(lst_cube)
            lst_cube = rotateSide_b(lst_cube)
            lst_cube = rotateSide_r(lst_cube)
            lst_cube = rotateSide_f(lst_cube) 
            lst_cube = rotateSide_U(lst_cube) 
            lst_cube = rotateSide_F(lst_cube) 
            lst_rotate.append("llbbrfUF")             
        elif lst_cube[3][7] == 'w':
            lst_cube = rotateSide_L(lst_cube)
            lst_cube = rotateSide_b(lst_cube)
            lst_cube = rotateSide_l(lst_cube)
            lst_cube = rotateSide_b(lst_cube)
            lst_cube = rotateSide_r(lst_cube)
            lst_cube = rotateSide_f(lst_cube) 
            lst_cube = rotateSide_U(lst_cube) 
            lst_cube = rotateSide_F(lst_cube) 
            lst_rotate.append("lblbrfUF")   
        else:
            lst_cube = lst_cube     
            lst_rotate.append("")         
        return lst_cube, lst_rotate
    
def y_1_WhiteLeafPos1_5(lst_cube, lst_rotate):

        if lst_cube[1][5] == "w":
            lst_cube = lst_cube
            lst_rotate.append("")         
        elif lst_cube[5][7] == 'w': 
            lst_cube = rotateSide_B(lst_cube)
            lst_rotate.append("B")   
        elif lst_cube[4][1] == 'w':
            lst_cube = rotateSide_b(lst_cube)
            lst_rotate.append("b") 
        #two lines of movement
        elif lst_cube[3][3] == 'w':
            lst_cube = rotateSide_B(lst_cube)
            lst_cube = rotateSide_B(lst_cube)
            lst_rotate.append("BB")               
        elif lst_cube[4][5] == 'w':
            lst_cube = rotateSide_u(lst_cube)
            lst_cube = rotateSide_b(lst_cube)
            lst_rotate.append("ub")  
        elif lst_cube[5][5] == 'w': 
            lst_cube = rotateSide_D(lst_cube)
            lst_cube = rotateSide_B(lst_cube)
            lst_rotate.append("DB")             
        #three lines of movement
        elif lst_cube[2][1] == 'w':
            lst_cube = rotateSide_r(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_R(lst_cube)  
            lst_rotate.append("rUR")  
        #four lines of movement  
        elif lst_cube[2][3] == 'w':
            lst_cube = rotateSide_B(lst_cube)
            lst_cube = rotateSide_r(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_R(lst_cube)  
            lst_rotate.append("BrUR")  
        elif lst_cube[2][5] == 'w':
            lst_cube = rotateSide_b(lst_cube)
            lst_cube = rotateSide_r(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_R(lst_cube)  
            lst_rotate.append("brUR")
        elif lst_cube[3][1] == 'w':
            lst_cube = rotateSide_r(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_R(lst_cube)
            lst_rotate.append("rUUR")             
            
        #five lines of movement     
        elif lst_cube[4][3] == 'w':
            lst_cube = rotateSide_l(lst_cube)
            lst_cube = rotateSide_b(lst_cube)
            lst_cube = rotateSide_r(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_R(lst_cube)   
            lst_rotate.append("lbrUR")             
        elif lst_cube[2][7] == 'w': 
            lst_cube = rotateSide_b(lst_cube)
            lst_cube = rotateSide_b(lst_cube)
            lst_cube = rotateSide_r(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_R(lst_cube)
            lst_rotate.append("bbrUF")    
        elif lst_cube[3][5] == 'w':
            lst_cube = rotateSide_l(lst_cube)
            lst_cube = rotateSide_r(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_R(lst_cube)
            lst_rotate.append("lrUUR") 
            
        elif lst_cube[5][1] == 'w':
            lst_cube = rotateSide_R(lst_cube)
            lst_cube = rotateSide_d(lst_cube)
            lst_cube = rotateSide_r(lst_cube)
            lst_cube = rotateSide_L(lst_cube)
            lst_cube = rotateSide_L(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_b(lst_cube)
            lst_rotate.append("RdrLLUb") 
        elif lst_cube[4][7] == 'w':
            lst_cube = rotateSide_r(lst_cube)
            lst_cube = rotateSide_r(lst_cube)
            lst_cube = rotateSide_F(lst_cube)
            lst_cube = rotateSide_R(lst_cube)
            lst_cube = rotateSide_R(lst_cube) 
            lst_rotate.append("rrFRR")      
        elif lst_cube[5][3] == 'w':
            lst_cube = rotateSide_l(lst_cube)
            lst_cube = rotateSide_l(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_b(lst_cube) 
            lst_rotate.append("llUb")   
        elif lst_cube[0][7] == 'w':
            lst_cube = rotateSide_R(lst_cube)
            lst_cube = rotateSide_d(lst_cube)
            lst_cube = rotateSide_L(lst_cube)
            lst_cube = rotateSide_b(lst_cube)
            lst_cube = rotateSide_b(lst_cube)
            lst_rotate.append("RdLbb")  
        elif lst_cube[0][3] == 'w':
            lst_cube = rotateSide_l(lst_cube)
            lst_cube = rotateSide_l(lst_cube)
            lst_cube = rotateSide_b(lst_cube)
            lst_cube = rotateSide_r(lst_cube) 
            lst_cube = rotateSide_U(lst_cube) 
            lst_cube = rotateSide_R(lst_cube) 
            lst_rotate.append("llbrUR")            
        elif lst_cube[0][1] == 'w':
            lst_cube = rotateSide_f(lst_cube)
            lst_cube = rotateSide_l(lst_cube)
            lst_cube = rotateSide_F(lst_cube)
            lst_cube = rotateSide_l(lst_cube)
            lst_cube = rotateSide_b(lst_cube)
            lst_cube = rotateSide_r(lst_cube) 
            lst_cube = rotateSide_U(lst_cube) 
            lst_cube = rotateSide_R(lst_cube) 
            lst_rotate.append("flFlbrUR")      
        elif lst_cube[0][5] == 'w':
            lst_cube = rotateSide_f(lst_cube)
            lst_cube = rotateSide_f(lst_cube)
            lst_cube = rotateSide_l(lst_cube)
            lst_cube = rotateSide_l(lst_cube)
            lst_cube = rotateSide_b(lst_cube)
            lst_cube = rotateSide_r(lst_cube) 
            lst_cube = rotateSide_U(lst_cube) 
            lst_cube = rotateSide_R(lst_cube) 
            lst_rotate.append("ffllbrUR")             
        elif lst_cube[3][7] == 'w':
            lst_cube = rotateSide_L(lst_cube)
            lst_cube = rotateSide_b(lst_cube)
            lst_cube = rotateSide_b(lst_cube)
            lst_rotate.append("Lbb")   
        else:
            lst_cube = lst_cube     
            lst_rotate.append("")         
        return lst_cube, lst_rotate
    

def y_2_WhiteLeafPos2_5(lst_cube, lst_rotate):
           if lst_cube[2][5] == "w":
            lst_cube = lst_cube
            lst_rotate.append("")         
        elif lst_cube[5][3] == 'w': 
            lst_cube = rotateSide_B(lst_cube)
            lst_rotate.append("B")   
        elif lst_cube[4][3] == 'w':
            lst_cube = rotateSide_b(lst_cube)
            lst_rotate.append("b") 
        #two lines of movement
        elif lst_cube[0][3] == 'w':
            lst_cube = rotateSide_B(lst_cube)
            lst_cube = rotateSide_B(lst_cube)
            lst_rotate.append("BB")               
        elif lst_cube[4][1] == 'w':
            lst_cube = rotateSide_u(lst_cube)
            lst_cube = rotateSide_b(lst_cube)
            lst_rotate.append("ub")  
        elif lst_cube[5][7] == 'w': 
            lst_cube = rotateSide_D(lst_cube)
            lst_cube = rotateSide_B(lst_cube)
            lst_rotate.append("DB")             
        #three lines of movement
        elif lst_cube[3][1] == 'w':
            lst_cube = rotateSide_r(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_R(lst_cube)  
            lst_rotate.append("rUR")  
        #four lines of movement  
        elif lst_cube[3][3] == 'w':
            lst_cube = rotateSide_B(lst_cube)
            lst_cube = rotateSide_r(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_R(lst_cube)  
            lst_rotate.append("BrUR")  
        elif lst_cube[3][5] == 'w':
            lst_cube = rotateSide_b(lst_cube)
            lst_cube = rotateSide_r(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_R(lst_cube)  
            lst_rotate.append("brUR")
        elif lst_cube[0][1] == 'w':
            lst_cube = rotateSide_r(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_R(lst_cube)
            lst_rotate.append("rUUR")             
            
        #five lines of movement     
        elif lst_cube[4][7] == 'w':
            lst_cube = rotateSide_l(lst_cube)
            lst_cube = rotateSide_b(lst_cube)
            lst_cube = rotateSide_r(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_R(lst_cube)   
            lst_rotate.append("lbrUR")             
        elif lst_cube[3][7] == 'w': 
            lst_cube = rotateSide_b(lst_cube)
            lst_cube = rotateSide_b(lst_cube)
            lst_cube = rotateSide_r(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_R(lst_cube)
            lst_rotate.append("bbrUF")    
        elif lst_cube[0][5] == 'w':
            lst_cube = rotateSide_l(lst_cube)
            lst_cube = rotateSide_r(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_R(lst_cube)
            lst_rotate.append("lrUUR") 
            
        elif lst_cube[5][5] == 'w':
            lst_cube = rotateSide_R(lst_cube)
            lst_cube = rotateSide_d(lst_cube)
            lst_cube = rotateSide_r(lst_cube)
            lst_cube = rotateSide_L(lst_cube)
            lst_cube = rotateSide_L(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_b(lst_cube)
            lst_rotate.append("RdrLLUb") 
        elif lst_cube[4][5] == 'w':
            lst_cube = rotateSide_r(lst_cube)
            lst_cube = rotateSide_r(lst_cube)
            lst_cube = rotateSide_F(lst_cube)
            lst_cube = rotateSide_R(lst_cube)
            lst_cube = rotateSide_R(lst_cube) 
            lst_rotate.append("rrFRR")      
        elif lst_cube[5][1] == 'w':
            lst_cube = rotateSide_l(lst_cube)
            lst_cube = rotateSide_l(lst_cube)
            lst_cube = rotateSide_U(lst_cube)
            lst_cube = rotateSide_b(lst_cube) 
            lst_rotate.append("llUb")   
        elif lst_cube[1][7] == 'w':
            lst_cube = rotateSide_R(lst_cube)
            lst_cube = rotateSide_d(lst_cube)
            lst_cube = rotateSide_L(lst_cube)
            lst_cube = rotateSide_b(lst_cube)
            lst_cube = rotateSide_b(lst_cube)
            lst_rotate.append("RdLbb")  
        elif lst_cube[1][3] == 'w':
            lst_cube = rotateSide_l(lst_cube)
            lst_cube = rotateSide_l(lst_cube)
            lst_cube = rotateSide_b(lst_cube)
            lst_cube = rotateSide_r(lst_cube) 
            lst_cube = rotateSide_U(lst_cube) 
            lst_cube = rotateSide_R(lst_cube) 
            lst_rotate.append("llbrUR")            
        elif lst_cube[1][1] == 'w':
            lst_cube = rotateSide_f(lst_cube)
            lst_cube = rotateSide_l(lst_cube)
            lst_cube = rotateSide_F(lst_cube)
            lst_cube = rotateSide_l(lst_cube)
            lst_cube = rotateSide_b(lst_cube)
            lst_cube = rotateSide_r(lst_cube) 
            lst_cube = rotateSide_U(lst_cube) 
            lst_cube = rotateSide_R(lst_cube) 
            lst_rotate.append("flFlbrUR")      
        elif lst_cube[1][5] == 'w':
            lst_cube = rotateSide_f(lst_cube)
            lst_cube = rotateSide_f(lst_cube)
            lst_cube = rotateSide_l(lst_cube)
            lst_cube = rotateSide_l(lst_cube)
            lst_cube = rotateSide_b(lst_cube)
            lst_cube = rotateSide_r(lst_cube) 
            lst_cube = rotateSide_U(lst_cube) 
            lst_cube = rotateSide_R(lst_cube) 
            lst_rotate.append("ffllbrUR")             
        elif lst_cube[0][7] == 'w':
            lst_cube = rotateSide_L(lst_cube)
            lst_cube = rotateSide_b(lst_cube)
            lst_cube = rotateSide_b(lst_cube)
            lst_rotate.append("Lbb")   
        else:
            lst_cube = lst_cube     
            lst_rotate.append("")         
        return lst_cube, lst_rotate

def y_3_WhiteLeafPos3_5(lst_cube, lst_rotate):
    pass

def y_4_WhiteLeafPos4_1(lst_cube, lst_rotate):
    pass

def y_5_WhiteLeafPos5_5(lst_cube, lst_rotate):
    pass
    
    
def rotateIntoWhiteCross_y_0(lst_cube, lst_rotate):
    #if statements. Can have more than one outcome
    if lst_cube[0][5] == "w" and (lst_cube[1][3] == lst_cube[1][4]):
        lst_cube = rotateSide_R(lst_cube)
        lst_cube = rotateSide_R(lst_cube)
        lst_rotate.append("RR")
    if lst_cube[0][1] == "w" and (lst_cube[4][7] == lst_cube[4][4]):
        lst_cube = rotateSide_U(lst_cube)
        lst_cube = rotateSide_U(lst_cube)
        lst_rotate.append("UU")   
    if lst_cube[0][3] == "w" and (lst_cube[3][5] == lst_cube[3][4]):
        lst_cube = rotateSide_L(lst_cube)
        lst_cube = rotateSide_L(lst_cube)
        lst_rotate.append("LL") 
    if lst_cube[0][7] == "w" and (lst_cube[5][1] == lst_cube[5][4]):
        lst_cube = rotateSide_D(lst_cube)
        lst_cube = rotateSide_D(lst_cube)
        lst_rotate.append("DD")  
    lst_cube = rotateSide_F(lst_cube)
    lst_rotate.append("F")  
    
    #if statements. Can have more than one outcome
    if lst_cube[0][5] == "w" and (lst_cube[1][3] == lst_cube[1][4]):
        lst_cube = rotateSide_R(lst_cube)
        lst_cube = rotateSide_R(lst_cube)
        lst_rotate.append("RR")
    if lst_cube[0][1] == "w" and (lst_cube[4][7] == lst_cube[4][4]):
        lst_cube = rotateSide_U(lst_cube)
        lst_cube = rotateSide_U(lst_cube)
        lst_rotate.append("UU")   
    if lst_cube[0][3] == "w" and (lst_cube[3][5] == lst_cube[3][4]):
        lst_cube = rotateSide_L(lst_cube)
        lst_cube = rotateSide_L(lst_cube)
        lst_rotate.append("LL") 
    if lst_cube[0][7] == "w" and (lst_cube[5][1] == lst_cube[5][4]):
        lst_cube = rotateSide_D(lst_cube)
        lst_cube = rotateSide_D(lst_cube)
        lst_rotate.append("DD")  
    lst_cube = rotateSide_F(lst_cube)
    lst_rotate.append("F") 
    
    #if statements. Can have more than one outcome
    if lst_cube[0][5] == "w" and (lst_cube[1][3] == lst_cube[1][4]):
        lst_cube = rotateSide_R(lst_cube)
        lst_cube = rotateSide_R(lst_cube)
        lst_rotate.append("RR")
    if lst_cube[0][1] == "w" and (lst_cube[4][7] == lst_cube[4][4]):
        lst_cube = rotateSide_U(lst_cube)
        lst_cube = rotateSide_U(lst_cube)
        lst_rotate.append("UU")   
    if lst_cube[0][3] == "w" and (lst_cube[3][5] == lst_cube[3][4]):
        lst_cube = rotateSide_L(lst_cube)
        lst_cube = rotateSide_L(lst_cube)
        lst_rotate.append("LL") 
    if lst_cube[0][7] == "w" and (lst_cube[5][1] == lst_cube[5][4]):
        lst_cube = rotateSide_D(lst_cube)
        lst_cube = rotateSide_D(lst_cube)
        lst_rotate.append("DD")  
    lst_cube = rotateSide_F(lst_cube)
    lst_rotate.append("F") 
    
    
    #if statements. Can have more than one outcome
    if lst_cube[0][5] == "w" and (lst_cube[1][3] == lst_cube[1][4]):
        lst_cube = rotateSide_R(lst_cube)
        lst_cube = rotateSide_R(lst_cube)
        lst_rotate.append("RR")
    if lst_cube[0][1] == "w" and (lst_cube[4][7] == lst_cube[4][4]):
        lst_cube = rotateSide_U(lst_cube)
        lst_cube = rotateSide_U(lst_cube)
        lst_rotate.append("UU")   
    if lst_cube[0][3] == "w" and (lst_cube[3][5] == lst_cube[3][4]):
        lst_cube = rotateSide_L(lst_cube)
        lst_cube = rotateSide_L(lst_cube)
        lst_rotate.append("LL") 
    if lst_cube[0][7] == "w" and (lst_cube[5][1] == lst_cube[5][4]):
        lst_cube = rotateSide_D(lst_cube)
        lst_cube = rotateSide_D(lst_cube)
        lst_rotate.append("DD")  
    lst_cube = rotateSide_F(lst_cube)
    lst_rotate.append("F") 
        
 
        
    return lst_cube, lst_rotate
        
        
        