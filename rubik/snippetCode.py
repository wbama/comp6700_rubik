from rubik.solveRotations import createCubeStringFromInputParms
import rubik.solveWhiteCross as swc


inputDict = {}
inputDict['cube'] = "rrbbbbgggryyyyoroyogryggobbwwwwwwwwwgrboorbbyoyyrrgoog"
#inputDict['rotate'] = 'FLFFBUUdLfDrFLdRRdLLdRRu'
inputDict['op'] = 'solve' 

print(createCubeStringFromInputParms(inputDict))