
from rubik.solve import _solve
from rubik.solveDaisy import solveDaisy
from rubik.solveRotations import createCubeListFromInputParms, rotateCubeToRight, rotateCubeDown, rotateIntoWhiteCross_y_0, rotateIntoWhiteCross_y_1
from rubik.solveWhiteCross import solveWhiteCross

# inputDict['cube'] = "gwwboboyboygwbyyyrygwrrgwowggyogrowbrwrrygoogyorrwbbbb"

inputDict = {}
inputDict['cube'] = "wwwwwwwwwkkkkkkkkkYYYYYYYYYoooooooooeeeeeeeeeQQQQQQQQQ"
inputDict['op'] = 'solve' 
# inputDict['rotate'] = 'F'
lst_cube = (createCubeListFromInputParms(inputDict))
print(lst_cube)

if ("y") in (parms.get("cube").lower()):
    if ("y" in lst_cube[0][4] or "Y" in lst_cube[0][4]):
        var_w = lst_cube[2][4]
        var_y = lst_cube[0][4]
    elif ("y"  in lst_cube[1][4] or "Y" in lst_cube[1][4]):
        var_w = lst_cube[3][4]
        var_y = lst_cube[1][4]
    elif ("y" in lst_cube[2][4] or "Y" in lst_cube[2][4])  :
        var_w = lst_cube[0][4] 
        var_y = lst_cube[2][4]       
    elif ("y" in lst_cube[3][4] or "Y" in lst_cube[3][4])  :
        var_w = lst_cube[1][4]
        var_y = lst_cube[3][4]
    elif ("y" in lst_cube[4][4] or "Y" in lst_cube[4][4])  :
        var_w = lst_cube[5][4]
        var_y = lst_cube[4][4]
else:
    var_y = lst_cube[0][4]
    var_w = lst_cube[2][4]
# else:
#     VAR_Y = lst_cube[0][4]
#     VAR_W = lst_cube[2][4]

    
    
print(f"var yellow is:  {var_y}")
print(f"var white is: {var_w}")
# lst_rotate = []
# lst_cube = solveDaisy(inputDict)[0]
# rotations = solveDaisy(inputDict)[1]
#
# print(f"lst cube {lst_cube}")
# print(f"rotations {rotations}")
#
# print(f"WC {solveWhiteCross(inputDict)}")
#
# print(_solve(inputDict))
#
# lst_cube = createCubeListFromInputParms(parms)

#print(solveWhiteCross(inputDict))

# print(_solve(inputDict))
