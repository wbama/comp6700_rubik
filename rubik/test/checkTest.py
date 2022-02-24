from unittest import TestCase
import rubik.check as check 

class CheckTest(TestCase):
        
    def test_check_010_ShouldReturnOkOnSolvedCube(self):
        parm = {'op':'check', 'cube': 'gwrbbbwwyyybrrygogyowogyygorrogowbggbboyybwobrrrrwgwwo'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        
    def test_check_020_ShouldReturnOkOnSolvedCube(self):
        parm = {'op':'check', 'cube': 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        
# Sad Patch Tests
        
    def test_check_090_ReturnErrorOnSmallCube(self):
        parm = {'op':'check', 'cube': '123456789'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube string has to have 54 elements')
        
    def test_check_090_ReturnErrorOnNotStringCube(self):
        parm = {'op':'check', 'cube': 42}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube not a string')
        
    def test_check_090_ReturnErrorOnMissingCube(self):
        parm = {'op':'check'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: no cube found')
        
    def test_check_090_ReturnErrorOnMore54Elements(self):
        parm = {'op':'check', 'cube': 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyyffffffwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube string has to have 54 elements')
        
        
    def test_check_090_ReturnErrorOnLess54Elements(self):
        parm = {'op':'check', 'cube': 'bbbbbbbbbrrrrrrrrrgggggggggooooooooyyyyyyyyyfffffwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube string has to have 54 elements')
        
    def test_check_090_ReturnErrorOnNot6Colors(self):
        parm = {'op':'check', 'cube': 'bbbbbbbbbbbbbbbbbbgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: there should be 6 colors')
        
    def test_check_090_ReturnErrorOn9OccurencesOf6Colors(self):
        parm = {'op':'check', 'cube': 'bbbbbbbbbbrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: one of the colors is more or less than 9 occurrences')

#works

# 'rbywbwgbwrybrryrogyowogyygorrbgoobgwbboyybyrgowgrwgwwo'

#  parm = {'op':'check', 'cube': '11w11w11wrrrrrrrrryggyggyggaaaaaaaaayy1yy1yy1wwgwwgwwg'}
#  parms = {'op':'check', 'cube': 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
#  parm = {'op':'check', 'cube' : 'wyrwbbowwyrgyrwbrwyywggbggygoowoobyyrrrbybbobgrrgwgooo'}






# has 9 occurrences of the 6 colors
#       parm = {'op':'check', 'cube': 'bbbbbbbbbbrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}

#each middle face is a different color
#     parm = {'op':'check', 'cube': 'bbbbrbbbbrrrrrrrbrgggggggggoooooooooyyyyyyyyywwwwwwwww'}

#adjacent color
# parm = {'op':'check', 'cube':'wwwbbbyyygggwrwbrbyyyrggwwwbobyoygogrrrgybrrrooobwgooo'}
# parm = {'op':'check', 'cube' : 'wyrwbbowwyggyrwbrwyywrgbggygoowoobyyrrrbybbobgrrgwgooo'}





