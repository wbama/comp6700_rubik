from rubik.solveRotations import createCubeListFromInputParms
import rubik.solveWhiteCross as swc


inputDict = {}
inputDict['cube'] = "rrbbbbgggryyyyoroyogryggobbwwwwwwwwwgrboorbbyoyyrrgoog"
#inputDict['rotate'] = 'FLFFBUUdLfDrFLdRRdLLdRRu'
inputDict['op'] = 'solve' 

print(createCubeListFromInputParms(inputDict))