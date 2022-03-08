
from rubik.solve import _solve
from rubik.solveDaisy import solveDaisy


inputDict = {}
inputDict['cube'] = "brorybgygggowobwbgbwwowrrobbyygrbrgoooygborwwyrrwgywyy"
inputDict['op'] = 'solve' 
#inputDict['rotate'] = 'F'

print(solveDaisy(inputDict))



