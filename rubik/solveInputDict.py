from rubik.solve import _solve
from rubik import solveCheckInput
from rubik.solveCheckInput import solveCheck
from rubik.solveWhiteCross import solveWhiteCross



inputDict = {}
inputDict['cube'] = "ggrggoggoyroyyygbrbbbgbbybbwwwwwwwwwrryrryrrbooyooyoog"
#inputDict['rotate'] = 'FLFFBUUdLfDrFLdRRdLLdRRu'
inputDict['op'] = 'solve' 

#print(_solve(inputDict))

print(solveWhiteCross(inputDict))



