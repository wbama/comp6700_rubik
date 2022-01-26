from unittest import TestCase
import rubik.check as check 

class CheckTest(TestCase):
        
    def test_check_010_ShouldReturnOkOnSolvedCube(self):
        parm = {'op':'check', 'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')

#default
#parm = {'op':'check', 'cube': 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}

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
# parm = {'op':'check', 'cube':'bbbbbbbbbrrrrrrrrrgwgggggggoooooooooyyyyyyyyywwgwwwwww'}
# parm = {'op':'check', 'cube':'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}



