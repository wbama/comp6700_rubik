
from rubik.solve import turn_clock
from rubik.solve import turn_type1
from rubik.solve import turn_type2
from rubik.solve import turn_type3
import rubik.cube as rubik

inputDict = {}
inputDict['op'] = 'solve'
inputDict['rotate'] = 'F'
inputDict['cube'] = 'rrbbbbgggryyyyoroyogryggobbwwwwwwwwwgrboorbbyoyyrrgoog'

lst_cube = ([x for x in inputDict.get("cube")])
lst_in1, lst_in2, lst_in3, lst_in4, lst_in5, lst_in6 = ([] for i in range(6)) 

for i in range (1,7):
    for j in range(1,10):
        exec(f"lst_in{i}.append(lst_cube.pop(0))")  
        
#create list within a list of the cube.   
lst_opposite_cnt = []
for i in range(1,7):
    exec(f'lst_cube.append(lst_in{i})')
print(lst_cube)    


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
    
print(flip_cube_top_side(lst_cube))
