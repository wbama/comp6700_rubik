
def turn_type1(orig_side):
    turned_side = []
    turned_side.insert(0, orig_side [6])
    turned_side.insert(1, orig_side [3])
    turned_side.insert(2, orig_side [0])
    turned_side.insert(3, orig_side [7])
    turned_side.insert(4, orig_side [4])
    turned_side.insert(5, orig_side [1])
    turned_side.insert(6, orig_side [8])
    turned_side.insert(7, orig_side [5])
    turned_side.insert(8, orig_side [2])
    return turned_side
        
def turn_type2(orig_side):
    turned_side = []
    turned_side.insert(0, orig_side [2])
    turned_side.insert(1, orig_side [5])
    turned_side.insert(2, orig_side [8])
    turned_side.insert(3, orig_side [1])
    turned_side.insert(4, orig_side [4])
    turned_side.insert(5, orig_side [7])
    turned_side.insert(6, orig_side [0])
    turned_side.insert(7, orig_side [3])
    turned_side.insert(8, orig_side [6])
    return turned_side
        
def turn_type3(orig_side):
    turned_side = []
    turned_side.insert(0, orig_side [8])
    turned_side.insert(1, orig_side [7])
    turned_side.insert(2, orig_side [6])
    turned_side.insert(3, orig_side [5])
    turned_side.insert(4, orig_side [4])
    turned_side.insert(5, orig_side [3])
    turned_side.insert(6, orig_side [2])
    turned_side.insert(7, orig_side [1])
    turned_side.insert(8, orig_side [0])
    return turned_side

def rotate_cube_to_right(cube):
        #rotate cube to right
        first_side = cube.pop(0)
        cube.insert(3, first_side)        
        # rotate the top
        orig_side = cube.pop(4)
        cube.insert(4, turn_type1(orig_side))        
        #now rotate the bottom
        orig_side = cube.pop(5) 
        cube.insert(5, turn_type2(orig_side))
        return cube
    
def flip_cube_top_side(cube):
        side_0 = cube[4]

        side_1 = cube[1]
        #rotate it correctly
        side_1 = (turn_type2(side_1))
        side_2 = cube[5]
        #rotate side 2
        side_2 = (turn_type3(side_2))
        side_3 = cube[3]
        #rotate side 3
        side_3 = (turn_type1(side_3))
        #rotate side 4
        side_4 = cube[2]
        side_4 = (turn_type3(side_4))
        side_5 = cube[0]        
        cube = []
        for i in range(6):
            exec(f'cube.append(side_{i})') 
               
        return cube

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