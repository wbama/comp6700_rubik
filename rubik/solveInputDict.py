# from rubik.solve import _solve
# from rubik import solveCheckInput
# from rubik.solveCheckInput import solveCheck
# from rubik.solveWhiteCross import solveWhiteCross
from rubik.solveRotations import rotateCubeClockwise
from rubik.solveRotations import createCubeListFromInputParms
from rubik.solveRotations import rotate_cube_to_left
from rubik.solveRotations import rotate_cube_to_right



inputDict = {}
inputDict['cube'] = "oogyowrwywgybyygwggbbbrrwbyoryyworybwrowgrbgowgrgbobor"
#inputDict['rotate'] = 'FLFFBUUdLfDrFLdRRdLLdRRu'
inputDict['op'] = 'solve' 

#print(_solve(inputDict))

#print(solveWhiteCross(inputDict))
lst_cube = createCubeListFromInputParms(inputDict)
print(lst_cube)
print(rotate_cube_to_left(lst_cube))



