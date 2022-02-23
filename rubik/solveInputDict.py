import rubik.cube as rubik
from rubik.solve import _solve
import rubik.solveCheckInput
from rubik.solveCheckInput import solveCheck



inputDict = {}
inputDict['cube'] = 'rrbbbbgggryyyyoroyogryggobbwwwwwwwwwgrboorbbyoyyrrgoog'
inputDict['rotate'] = ''   
inputDict['op'] = 'solve' 

print(_solve(inputDict))
#print(solveCheck(inputDict))

#    inputs:
#        parms: dictionary input that is validated. Do not have to validate 
#        parms['op'] have to validate the keys ['op'] string, "solve", mandatory, arrives validated
#        parms['cube'] string; len = 54 chars [azAZ09], 9 occurences of each character, 6 distinct characters, 
#               middle will be one of the six; mandatory; arrives unvalidated
#        parms['rotate'] string; len >=0, [FfRrBbLlUuDd]; optional, defaulting to F if missing; arrives unvalidated

#works

# 'rbywbwgbwrybrryrogyowogyygorrbgoobgwbboyybyrgowgrwgwwo'

#  parm = {'op':'check', 'cube': '11w11w11wrrrrrrrrryggyggyggaaaaaaaaayy1yy1yy1wwgwwgwwg'}
#  parms = {'op':'check', 'cube': 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
#  parm = {'op':'check', 'cube' : 'wyrwbbowwyrgyrwbrwyywggbggygoowoobyyrrrbybbobgrrgwgooo'}
#errors

#    parm = {'op':'check', 'cube': '123456789'}
#    parm = {'op':'check', 'cube': 42}
#    parm = {'op':'check'}

# is present 
#       parm = {'op':'check'}

#is a string  
#       parm = {'op':'check', 'cube': 42}

# has 55 elements
#       parm = {'op':'check', 'cube': 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyyffffffwwww'}

# has 53 elements
#       parm = {'op':'check', 'cube': 'bbbbbbbbbrrrrrrrrrgggggggggooooooooyyyyyyyyyfffffwwww'}

# has 6 colors
#       parm = {'op':'check', 'cube': 'bbbbbbbbbbbbbbbbbbgggggggggoooooooooyyyyyyyyywwwwwwwww'}

#       parm = {'op':'check', 'cube': 'bbbbbzzzzrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}

# has 9 occurrences of the 6 colors
#       parm = {'op':'check', 'cube': 'bbbbbbbbbbrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}

#each middle face is a different color
#     parm = {'op':'check', 'cube': 'bbbbrbbbbrrrrrrrbrgggggggggoooooooooyyyyyyyyywwwwwwwww'}

