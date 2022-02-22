
from rubik.solve import turn_clock

inputDict = {}
inputDict['op'] = 'solve'
inputDict['rotate'] = 'F'
inputDict['cube'] = 'rbywbwgbwrybrryrogyowogyygorrbgoobgwbboyybyrgowgrwgwwo'

lst_cube = ([x for x in inputDict.get("cube")])
lst_in1, lst_in2, lst_in3, lst_in4, lst_in5, lst_in6 = ([] for i in range(6)) 

for i in range (1,7):
    for j in range(1,10):
        exec(f"lst_in{i}.append(lst_cube.pop(0))")  
        
#create list within a list of the cube.   
lst_opposite_cnt = []
for i in range(1,7):
    exec(f'lst_cube.append(lst_in{i})')
    
print("\n")
print(lst_cube) #blue - front, yellow - right, green - back, yellow - top

c_rotate_cube = (turn_clock(lst_cube))
    
result = {}
result['cube'] = 'gwrbbbwwyyybrrygogyowogyygorrogowbggbboyybwobrrrrwgwwo'
result['rotate'] = 'F'
result['status'] = 'ok'

print('\nRotatedCube')
print(c_rotate_cube)

for i in range(1,6):
    exec(f'str{i}="".join(c_rotate_cube[{i-1}])')
    
str_cube = str1+str2+str3+str4+str5
print(str_cube)
    
