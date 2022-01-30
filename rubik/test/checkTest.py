from unittest import TestCase
import rubik.check as check 

class CheckTest(TestCase):
        
    def test_check_010_ShouldReturnOkOnSolvedCube(self):
        parm = {'op':'check', 'cube': 'wyrwbbwwwyrgyrwbrwyywggbggygoowoobyyrrrbybbobgrrgwgooo'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')

#works

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

#adjacent color
# parm = {'op':'check', 'cube':'wwwbbbyyygggwrwbrbyyyrggwwwbobyoygogrrrgybrrrooobwgooo'}
# parm = {'op':'check', 'cube' : 'wyrwbbowwyggyrwbrwyywrgbggygoowoobyyrrrbybbobgrrgwgooo'}





