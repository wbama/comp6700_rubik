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
        
    def test_check_030_ShouldReturnOkOnSolvedCube(self):
        parm = {'op':'check', 'cube': '11w11w11wrrrrrrrrryggyggyggaaaaaaaaayy1yy1yy1wwgwwgwwg'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'ok')
        
    def test_check_040_ShouldReturnOkOnSolvedCube(self):
        parm = {'op':'check', 'cube': 'wyrwbbowwyrgyrwbrwyywggbggygoowoobyyrrrbybbobgrrgwgooo'}
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
        
    def test_check_091_ReturnErrorOnNotStringCube(self):
        parm = {'op':'check', 'cube': 42}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube not a string')
        
    def test_check_092_ReturnErrorOnMissingCube(self):
        parm = {'op':'check'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: no cube found')
        
    def test_check_093_ReturnErrorOnMore54Elements(self):
        parm = {'op':'check', 'cube': 'bbbbbbbbbrrrrrrrrrgggggggggoooooooooyyyyyyyyyffffffwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube string has to have 54 elements')
        
        
    def test_check_094_ReturnErrorOnLess54Elements(self):
        parm = {'op':'check', 'cube': 'bbbbbbbbbrrrrrrrrrgggggggggooooooooyyyyyyyyyfffffwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: cube string has to have 54 elements')
        
    def test_check_095_ReturnErrorOnNot6Colors(self):
        parm = {'op':'check', 'cube': 'bbbbbbbbbbbbbbbbbbgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: there should be 6 colors')
        
    def test_check_096_ReturnErrorOn9OccurencesOf6Colors(self):
        parm = {'op':'check', 'cube': 'bbbbbbbbbbrrrrrrrrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: one of the colors is more or less than 9 occurrences')
        
    def test_check_097_ReturnErrorEachMiddleFaceDifferentColor(self):
        parm = {'op':'check', 'cube': 'bbbbrbbbbrrrrrrrbrgggggggggoooooooooyyyyyyyyywwwwwwwww'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: two middle faces are the same colors')
        
    def test_check_098_ReturnErrorIncorrectAdjacentColor(self):
        parm = {'op':'check', 'cube': 'wwwbbbyyygggwrwbrbyyyrggwwwbobyoygogrrrgybrrrooobwgooo'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: adjacent color to color that would appear on opposite side')
        
    def test_check_099_ReturnErrorIncorrectAdjacentColor(self):
        parm = {'op':'check', 'cube': 'wyrwbbowwyggyrwbrwyywrgbggygoowoobyyrrrbybbobgrrgwgooo'}
        result = check._check(parm)
        self.assertIn('status', result)
        status = result.get('status', None)
        self.assertEqual(status, 'error: adjacent color to color that would appear on opposite side')






