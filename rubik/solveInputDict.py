"""
    Created on 03/05/2022
    @author: Waldo du Toit
    code to feed in cube strings
    
"""
from rubik.solve import _solve

from rubik.solveRotations import createCubeListFromInputParms, rotateCubeToRight, rotateCubeDown
from rubik.solveWhiteCross import solveWhiteCross
from rubik.solveRotations import createYellowAndWhiteVariables, createStringFromCube, createYellowAndWhiteVariables
from rubik.solveLowerLayer import solveLowerLayer
from rubik.solveDaisy import solveDaisy
from rubik.solveMiddleLayer import solveMiddleLayer


#inputDict['cube'] = 'xy54Ra5ax4RxRxxa545445yxayy54RR4RaxxRayya5aayRxyy5445R'

inputDict = {}
#inputDict['cube'] = "ryrbboogywyogrwrygybrggbowbbyyoowoowwrggybgogbrbwwryrw"
#inputDict['cube'] = 'ybbbbwggboywrrbygwrgoygyroggobrorryowwbwygowwyrrowoybg'
#inputDict['cube'] = 'rrbbbbgggryyyyoroyogryggobbwwwwwwwwwgrboorbbyoyyrrgoog'
inputDict['cube'] = 'rrwobgbrrbwworbywyrgwygoorgobbboywrygybwygybooggyworwg'
inputDict['op'] = 'solve' 
#inputDict['rotate'] = 'uRRfuuubuLUURRBBuFFUULLLUlubuuBUbuBRUUrFUfUUfuF'

# print(solveWhiteCross(inputDict))
print(solveMiddleLayer(inputDict))

#print(_solve(inputDict))
