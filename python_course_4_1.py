import unittest
from python_course_2_problem import Queue, Stack

# 測試我們之前寫的Stack的功能
# 1. push - 用作弊方式查看private attribute 
# 2. pop  - 有東西的Stack 必須回傳 我們想要的值 
# 3. pop  - 空的Stack 情況 必須 報錯
class StackTest(unittest.TestCase):

    # setUp函式 會在每一個test函式執行前被執行一次
    def setUp(self) -> None:
        self.s = Stack()
        return super().setUp()

    # test開頭的函式才會被當作測試
    def testStackPushOneElement(self):
        self.s.push(123)
        result = self.s._Stack__stack   # 這是一個作弊的方法，可以查看私有屬性 ( <object>._<class>__<attribute> )
        self.assertEqual(result, [123])

    def testStackPushThreeElements(self):
        self.pushThreeElements(self.s, [], {}, 3+4j)
        result = self.s._Stack__stack
        expected = [[], {}, 3+4j]
        self.assertEqual(result, expected)
        
    def testStackPopThreeElements(self):
        self.pushThreeElements(self.s, [], {}, 3+4j)
        self.assertEqual(self.s.pop(), 3+4j)
        self.assertEqual(self.s.pop(), {})
        self.assertEqual(self.s.pop(), [])

    # 這不是一個test開頭的函式，所以不會被執行。
    def pushThreeElements(self, stack:Stack, a, b, c):
        stack.push(a)
        stack.push(b)
        stack.push(c)

    # 這個函式是測試產品程式是否會報錯。
    def testPopEmptyStack(self):
        with self.assertRaises(Exception): 
            self.s.pop()

# 測試我們之前寫的Queue的功能
# 1. push - 用作弊方式查看private attribute 
# 2. pop  - 有東西的Queue 必須回傳 我們想要的值 
# 3. pop  - 空的Queue 情況 必須 報錯
class QueueTest(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Queue()
        return super().setUp()
    
    def testQueuePushThreeElements(self):
        self.pushThreeElements(self.s, 1, 2, 3)
        result = self.s._Queue__queue
        self.assertEqual(result, [1,2,3])
    
    def pushThreeElements(self, queue:Queue, a, b, c): 
        queue.push(a)
        queue.push(b)
        queue.push(c)

    def testPopThreeElements(self):
        self.pushThreeElements(self.s, 1, 2, 3)
        self.assertEqual(self.s.pop(), 1)
        self.assertEqual(self.s.pop(), 2)
        self.assertEqual(self.s.pop(), 3)

    def testPopEmptyQueue(self):
        with self.assertRaises(Exception):
            self.s.pop()


# 當本檔案被當作 main 去執行的時候，才要執行測試。
# verbosity = 4 是讓我們可以更清楚看到 測試執行 的詳細內容。
if __name__ == '__main__': 
    unittest.main(verbosity=4)
