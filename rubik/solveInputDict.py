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
inputDict['cube'] = 'BeReRrAReeeBBerBttrArRBtBrRRtrrrBeRRtBtRttAAtreAAABAAe'
inputDict['op'] = 'solve' 
inputDict['rotate'] = 'uRRfuuubuLUURRBBuFFUULLLUlubuBbuBUbuBRUrRUrFUfUUfuF'

# print(solveWhiteCross(inputDict))
print(solveLowerLayer(inputDict))
print("")
print("")
print("")
#print(_solve(inputDict))

#print(_solve(inputDict))
