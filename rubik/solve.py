import rubik.cube as rubik

def turn_clock(orig_side):
    new_cube = [[], [], [], [], [], []]
    #front
    new_cube[0].insert(0, orig_side [0][6])
    new_cube[0].insert(1, orig_side [0][3])
    new_cube[0].insert(2, orig_side [0][0])
    new_cube[0].insert(3, orig_side [0][7])
    new_cube[0].insert(4, orig_side [0][4])
    new_cube[0].insert(5, orig_side [0][1])
    new_cube[0].insert(6, orig_side [0][8])
    new_cube[0].insert(7, orig_side [0][5])
    new_cube[0].insert(8, orig_side [0][2])
    
    #right    
    new_cube[1].insert(0, orig_side [4][6])
    new_cube[1].insert(1, orig_side [1][1])
    new_cube[1].insert(2, orig_side [1][2])
    new_cube[1].insert(3, orig_side [4][7])
    new_cube[1].insert(4, orig_side [1][4])
    new_cube[1].insert(5, orig_side [1][5])
    new_cube[1].insert(6, orig_side [4][8])
    new_cube[1].insert(7, orig_side [1][7])
    new_cube[1].insert(8, orig_side [1][8])
    
    #back    
    new_cube[2].insert(0, orig_side [2][0])
    new_cube[2].insert(1, orig_side [2][1])
    new_cube[2].insert(2, orig_side [2][2])
    new_cube[2].insert(3, orig_side [2][3])
    new_cube[2].insert(4, orig_side [2][4])
    new_cube[2].insert(5, orig_side [2][5])
    new_cube[2].insert(6, orig_side [2][6])
    new_cube[2].insert(7, orig_side [2][7])
    new_cube[2].insert(8, orig_side [2][8])
    
    #left    
    new_cube[3].insert(0, orig_side [3][0])
    new_cube[3].insert(1, orig_side [3][1])
    new_cube[3].insert(2, orig_side [5][0])
    new_cube[3].insert(3, orig_side [3][3])
    new_cube[3].insert(4, orig_side [3][4])
    new_cube[3].insert(5, orig_side [5][1])
    new_cube[3].insert(6, orig_side [3][6])
    new_cube[3].insert(7, orig_side [3][7])
    new_cube[3].insert(8, orig_side [5][2])
    
    #top    
    new_cube[4].insert(0, orig_side [4][0])
    new_cube[4].insert(1, orig_side [4][1])
    new_cube[4].insert(2, orig_side [4][2])
    new_cube[4].insert(3, orig_side [4][3])
    new_cube[4].insert(4, orig_side [4][4])
    new_cube[4].insert(5, orig_side [4][5])
    new_cube[4].insert(6, orig_side [3][8])
    new_cube[4].insert(7, orig_side [3][5])
    new_cube[4].insert(8, orig_side [3][2])
    
    #bottom    
    new_cube[5].insert(0, orig_side [1][6])
    new_cube[5].insert(1, orig_side [1][3])
    new_cube[5].insert(2, orig_side [1][0])
    new_cube[5].insert(3, orig_side [5][3])
    new_cube[5].insert(4, orig_side [5][4])
    new_cube[5].insert(5, orig_side [5][5])
    new_cube[5].insert(6, orig_side [5][6])
    new_cube[5].insert(7, orig_side [5][7])
    new_cube[5].insert(8, orig_side [5][8])
    return new_cube

def turn_cclock(orig_side):
    new_cube = [[], [], [], [], [], []]
    #front
    new_cube[0].insert(0, orig_side [0][2])
    new_cube[0].insert(1, orig_side [0][5])
    new_cube[0].insert(2, orig_side [0][8])
    new_cube[0].insert(3, orig_side [0][1])
    new_cube[0].insert(4, orig_side [0][4])
    new_cube[0].insert(5, orig_side [0][7])
    new_cube[0].insert(6, orig_side [0][0])
    new_cube[0].insert(7, orig_side [0][3])
    new_cube[0].insert(8, orig_side [0][6])
    
    #right- takes from 5
    new_cube[1].insert(0, orig_side [5][2])
    new_cube[1].insert(1, orig_side [1][1])
    new_cube[1].insert(2, orig_side [1][2])
    new_cube[1].insert(3, orig_side [5][1])
    new_cube[1].insert(4, orig_side [1][4])
    new_cube[1].insert(5, orig_side [1][5])
    new_cube[1].insert(6, orig_side [5][0])
    new_cube[1].insert(7, orig_side [1][7])
    new_cube[1].insert(8, orig_side [1][8])
    
    #back  - stays same  
    new_cube[2].insert(0, orig_side [2][0])
    new_cube[2].insert(1, orig_side [2][1])
    new_cube[2].insert(2, orig_side [2][2])
    new_cube[2].insert(3, orig_side [2][3])
    new_cube[2].insert(4, orig_side [2][4])
    new_cube[2].insert(5, orig_side [2][5])
    new_cube[2].insert(6, orig_side [2][6])
    new_cube[2].insert(7, orig_side [2][7])
    new_cube[2].insert(8, orig_side [2][8])
    
    #left - takes from 4
    new_cube[3].insert(0, orig_side [3][0])
    new_cube[3].insert(1, orig_side [3][1])
    new_cube[3].insert(2, orig_side [4][8])
    new_cube[3].insert(3, orig_side [3][3])
    new_cube[3].insert(4, orig_side [3][4])
    new_cube[3].insert(5, orig_side [4][7])
    new_cube[3].insert(6, orig_side [3][6])
    new_cube[3].insert(7, orig_side [3][7])
    new_cube[3].insert(8, orig_side [4][6])
    
    #top - takes from 1  
    new_cube[4].insert(0, orig_side [4][0])
    new_cube[4].insert(1, orig_side [4][1])
    new_cube[4].insert(2, orig_side [4][2])
    new_cube[4].insert(3, orig_side [4][3])
    new_cube[4].insert(4, orig_side [4][4])
    new_cube[4].insert(5, orig_side [4][5])
    new_cube[4].insert(6, orig_side [1][0])
    new_cube[4].insert(7, orig_side [1][3])
    new_cube[4].insert(8, orig_side [1][6])
    
    #bottom - takes from 3
    new_cube[5].insert(0, orig_side [3][2])
    new_cube[5].insert(1, orig_side [3][5])
    new_cube[5].insert(2, orig_side [3][8])
    new_cube[5].insert(3, orig_side [5][3])
    new_cube[5].insert(4, orig_side [5][4])
    new_cube[5].insert(5, orig_side [5][5])
    new_cube[5].insert(6, orig_side [5][6])
    new_cube[5].insert(7, orig_side [5][7])
    new_cube[5].insert(8, orig_side [5][8])
    return new_cube

def _solve(parms):
    inputDict = {}
    inputDict['cube'] = 'rbywbwgbwrybrryrogyowogyygorrbgoobgwbboyybyrgowgrwgwwo'
    inputDict['rotate'] = 'F'
    inputDict['op'] = 'solve'
    
    result = {}
    result['cube'] = 'gwrbbbwwyyybrrygogyowogyygorrogowbggbboyybwobrrrrwgwwo'
    result['rotate'] = 'F'
    result['status'] = 'ok'
    return result    
    



# validate my parms, if invalid, need to return status with error
# if everything is valid, load parms into cube modell
# then rotate the cube model in the desired direction
# serialize the cube model in encoded cube into a string
# return the string result + status of "ok"


# but have to write the test code first


