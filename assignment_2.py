

inputDict = {}
inputDict['op'] = 'solve'
inputDict['rotate'] = 'F'
inputDict['cube'] = 'rrbbbbgggryyyyoroyogryggobbwwwwwwwwwgrboorbbyoyyrrgoog'



lst_cube = ([x for x in inputDict.get("cube")])
print(lst_cube)

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


def turn_clock(orig_side):
    zero_side = [[], [], [], [], [], []]
    #front
    zero_side[0].insert(0, orig_side [0][6])
    zero_side[0].insert(1, orig_side [0][3])
    zero_side[0].insert(2, orig_side [0][0])
    zero_side[0].insert(3, orig_side [0][7])
    zero_side[0].insert(4, orig_side [0][4])
    zero_side[0].insert(5, orig_side [0][1])
    zero_side[0].insert(6, orig_side [0][8])
    zero_side[0].insert(7, orig_side [0][5])
    zero_side[0].insert(8, orig_side [0][2])
    
    #right    
    zero_side[1].insert(0, orig_side [4][6])
    zero_side[1].insert(1, orig_side [1][1])
    zero_side[1].insert(2, orig_side [1][2])
    zero_side[1].insert(3, orig_side [4][7])
    zero_side[1].insert(4, orig_side [1][4])
    zero_side[1].insert(5, orig_side [1][5])
    zero_side[1].insert(6, orig_side [4][8])
    zero_side[1].insert(7, orig_side [1][7])
    zero_side[1].insert(8, orig_side [1][8])
    
    #back    
    zero_side[2].insert(0, orig_side [2][0])
    zero_side[2].insert(1, orig_side [2][1])
    zero_side[2].insert(2, orig_side [2][2])
    zero_side[2].insert(3, orig_side [2][3])
    zero_side[2].insert(4, orig_side [2][4])
    zero_side[2].insert(5, orig_side [2][5])
    zero_side[2].insert(6, orig_side [2][6])
    zero_side[2].insert(7, orig_side [2][7])
    zero_side[2].insert(8, orig_side [2][8])
    
    #left    
    zero_side[3].insert(0, orig_side [3][0])
    zero_side[3].insert(1, orig_side [3][1])
    zero_side[3].insert(2, orig_side [5][0])
    zero_side[3].insert(3, orig_side [3][3])
    zero_side[3].insert(4, orig_side [3][4])
    zero_side[3].insert(5, orig_side [5][1])
    zero_side[3].insert(6, orig_side [3][6])
    zero_side[3].insert(7, orig_side [3][7])
    zero_side[3].insert(8, orig_side [5][2])
    
    #top    
    zero_side[4].insert(0, orig_side [4][0])
    zero_side[4].insert(1, orig_side [4][1])
    zero_side[4].insert(2, orig_side [4][2])
    zero_side[4].insert(3, orig_side [4][3])
    zero_side[4].insert(4, orig_side [4][4])
    zero_side[4].insert(5, orig_side [4][5])
    zero_side[4].insert(6, orig_side [3][8])
    zero_side[4].insert(7, orig_side [3][5])
    zero_side[4].insert(8, orig_side [3][2])
    
    #bottom    
    zero_side[5].insert(0, orig_side [1][6])
    zero_side[5].insert(1, orig_side [1][3])
    zero_side[5].insert(2, orig_side [1][0])
    zero_side[5].insert(3, orig_side [5][3])
    zero_side[5].insert(4, orig_side [5][4])
    zero_side[5].insert(5, orig_side [5][5])
    zero_side[5].insert(6, orig_side [5][6])
    zero_side[5].insert(7, orig_side [5][7])
    zero_side[5].insert(8, orig_side [5][8])
    return zero_side

turned = turn_clock(lst_cube)
print("original cube")
print(lst_cube)
print("turned_cube")
print(turned)


def turn_cclock(orig_side):
    zero_side = [[], [], [], [], [], []]
    #front
    zero_side[0].insert(0, orig_side [0][2])
    zero_side[0].insert(1, orig_side [0][5])
    zero_side[0].insert(2, orig_side [0][8])
    zero_side[0].insert(3, orig_side [0][1])
    zero_side[0].insert(4, orig_side [0][4])
    zero_side[0].insert(5, orig_side [0][7])
    zero_side[0].insert(6, orig_side [0][0])
    zero_side[0].insert(7, orig_side [0][3])
    zero_side[0].insert(8, orig_side [0][6])
    
    #right- takes from 5
    zero_side[1].insert(0, orig_side [5][2])
    zero_side[1].insert(1, orig_side [1][1])
    zero_side[1].insert(2, orig_side [1][2])
    zero_side[1].insert(3, orig_side [5][1])
    zero_side[1].insert(4, orig_side [1][4])
    zero_side[1].insert(5, orig_side [1][5])
    zero_side[1].insert(6, orig_side [5][0])
    zero_side[1].insert(7, orig_side [1][7])
    zero_side[1].insert(8, orig_side [1][8])
    
    #back  - stays same  
    zero_side[2].insert(0, orig_side [2][0])
    zero_side[2].insert(1, orig_side [2][1])
    zero_side[2].insert(2, orig_side [2][2])
    zero_side[2].insert(3, orig_side [2][3])
    zero_side[2].insert(4, orig_side [2][4])
    zero_side[2].insert(5, orig_side [2][5])
    zero_side[2].insert(6, orig_side [2][6])
    zero_side[2].insert(7, orig_side [2][7])
    zero_side[2].insert(8, orig_side [2][8])
    
    #left - takes from 4
    zero_side[3].insert(0, orig_side [3][0])
    zero_side[3].insert(1, orig_side [3][1])
    zero_side[3].insert(2, orig_side [4][8])
    zero_side[3].insert(3, orig_side [3][3])
    zero_side[3].insert(4, orig_side [3][4])
    zero_side[3].insert(5, orig_side [4][7])
    zero_side[3].insert(6, orig_side [3][6])
    zero_side[3].insert(7, orig_side [3][7])
    zero_side[3].insert(8, orig_side [4][6])
    
    #top - takes from 1  
    zero_side[4].insert(0, orig_side [4][0])
    zero_side[4].insert(1, orig_side [4][1])
    zero_side[4].insert(2, orig_side [4][2])
    zero_side[4].insert(3, orig_side [4][3])
    zero_side[4].insert(4, orig_side [4][4])
    zero_side[4].insert(5, orig_side [4][5])
    zero_side[4].insert(6, orig_side [1][0])
    zero_side[4].insert(7, orig_side [1][3])
    zero_side[4].insert(8, orig_side [1][6])
    
    #bottom - takes from 3
    zero_side[5].insert(0, orig_side [3][2])
    zero_side[5].insert(1, orig_side [3][5])
    zero_side[5].insert(2, orig_side [3][8])
    zero_side[5].insert(3, orig_side [5][3])
    zero_side[5].insert(4, orig_side [5][4])
    zero_side[5].insert(5, orig_side [5][5])
    zero_side[5].insert(6, orig_side [5][6])
    zero_side[5].insert(7, orig_side [5][7])
    zero_side[5].insert(8, orig_side [5][8])
    return zero_side



turned = turn_cclock(lst_cube)
print("original cube")
print(lst_cube)
print("turned_cube")
print(turned)





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

for i in range(0,6):
    exec(f'str{i}="".join(c_rotate_cube[{i}])')
    
str_cube = str1+str2+str3+str4+str5
print(str_cube)
    

lst_cube = ['1', '2', '3']
str1 = "".join(lst_cube[0])
print(str1)
    
print(string)
    
print(lst_cube2)
    
def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    
    # return string  
    return str1 
        
        
# Driver code    
s = lst_cube
print(listToString(s)) 
