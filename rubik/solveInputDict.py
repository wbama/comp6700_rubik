# from rubik.solve import _solve
# from rubik import solveCheckInput
# from rubik.solveCheckInput import solveCheck
# from rubik.solveWhiteCross import solveWhiteCross
from rubik.solveRotations import rotateCubeClockwise
from rubik.solveRotations import createCubeListFromInputParms




inputDict = {}
inputDict['cube'] = "ggrggoggoyroyyygbrbbbgbbybbwwwwwwwwwrryrryrrbooyooyoog"
#inputDict['rotate'] = 'FLFFBUUdLfDrFLdRRdLLdRRu'
inputDict['op'] = 'solve' 

#print(_solve(inputDict))

#print(solveWhiteCross(inputDict))
lst_cube = createCubeListFromInputParms(inputDict)
print(rotateCubeClockwise(lst_cube))



