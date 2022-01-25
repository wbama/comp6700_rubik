from unittest import TestCase
import rubik.check as check 

class CheckTest(TestCase):
        
    def test_check_010_ShouldReturnOkOnSolvedCube(self):
        parm = {'op':'check', 'cube': 'bbbbbbbbbbbbbbbbbbgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')


# 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'
# is present 
#       parm = {'op':'check'}

#is a string  
#       parm = {'op':'check', 'cube': 42}


# has 54 elements
#       parm = {'op':'check', 'cube': 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyyffffffwwww'}

# has 6 colors
#       parm = {'op':'check', 'cube': 'bbbbbbbbbbbbbbbbbbgggggggggoooooooooyyyyyyyyywwwwwwwww'}

# has 9 occurrences of the 6 colors
# 'bbbbbbbbbbrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'

#each middle face is a different color
# 'bbbbrbbbbrrrrrrrbrgggggggggoooooooooyyyyyyyyywwwwwwwww'