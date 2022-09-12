# 無須用到 Visual Code 的互動視窗，我們會用 Run Python File。
import unittest

class SimpleTest(unittest.TestCase): 
    
    def testOneEqualsOne(self): 
        self.assertEqual(1, 1)		# 因為 1等於1 所以斷言(assert)成功 >> OK

    def testOneGreaterThanOne(self):
        self.assertGreater(1, 1)		# 因為 1不大於1 所以斷言失敗 >> FAIL

    def testCompileFailure(self):
        self.assertF(1, 2) 			# 因為根本沒有assertF 的函式 所以編譯錯誤 >> ERROR

if __name__ == '__main__':
    unittest.main(verbosity=4)
