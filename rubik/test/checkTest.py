from unittest import TestCase
import rubik.check as check 

class CheckTest(TestCase):
    
# Happy Path Tests
        
    def test_010_ShouldReturnOkOnSolvedCube(self):
        parm = {'op':'check', 'cube': 'gwrbbbwwyyybrrygogyowogyygorrogowbggbboyybwobrrrrwgwwo'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        
    def test_020_ShouldReturnOkOnSolvedCube(self):
        parm = {'op':'check', 'cube': 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        
    def test_030_ShouldReturnOkOnSolvedCube(self):
        parm = {'op':'check', 'cube': '11w11w11wrrrrrrrrryggyggyggaaaaaaaaayy1yy1yy1wwgwwgwwg'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        
    def test_040_ShouldReturnOkOnSolvedCube(self):
        parm = {'op':'check', 'cube': 'wyrwbbowwyrgyrwbrwyywggbggygoowoobyyrrrbybbobgrrgwgooo'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        
# Sad Path Tests
        
    def test_900_ReturnErrorOnSmallCube(self):
        parm = {'op':'check', 'cube': '123456789'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube string has to have 54 elements')
        
    def test_910_ReturnErrorOnNotStringCube(self):
        parm = {'op':'check', 'cube': 42}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube not a string')
        
    def test_920_ReturnErrorOnMissingCube(self):
        parm = {'op':'check'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: no cube found')
        
    def test_930_ReturnErrorOnMore54Elements(self):
        parm = {'op':'check', 'cube': 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyyffffffwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube string has to have 54 elements')
        
        
    def test_940_ReturnErrorOnLess54Elements(self):
        parm = {'op':'check', 'cube': 'bbbbbbbbbrrrrrrrrrgggggggggooooooooyyyyyyyyyfffffwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube string has to have 54 elements')
        
    def test_950_ReturnErrorOnNot6Colors(self):
        parm = {'op':'check', 'cube': 'bbbbbbbbbbbbbbbbbbgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: there should be 6 colors')
        
    def test_960_ReturnErrorOn9OccurencesOf6Colors(self):
        parm = {'op':'check', 'cube': 'bbbbbbbbbbrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: one of the colors is more or less than 9 occurrences')
        
    def test_970_ReturnErrorEachMiddleFaceDifferentColor(self):
        parm = {'op':'check', 'cube': 'bbbbrbbbbrrrrrrrbrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: two middle faces are the same colors')
        
    def test_980_ReturnErrorIncorrectAdjacentColor(self):
        parm = {'op':'check', 'cube': 'wwwbbbyyygggwrwbrbyyyrggwwwbobyoygogrrrgybrrrooobwgooo'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: adjacent color to color that would appear on opposite side')
        
    def test_990_ReturnErrorIncorrectAdjacentColor(self):
        parm = {'op':'check', 'cube': 'wyrwbbowwyggyrwbrwyywrgbggygoowoobyyrrrbybbobgrrgwgooo'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: adjacent color to color that would appear on opposite side')
        
    def test_9100_ReturnErrorIllegalCharacters(self):
        parm = {'op':'check', 'cube': 'rbbgbobbgrgw$r$w$obggrgg$wgor$$owoww$oob$rgw$rorrwbwob'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: only alphanumeric characters in the cube string')






