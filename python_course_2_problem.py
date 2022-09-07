# 練習寫Stack
# 使用案例: 當我創建一個Stack物件: 
#   a = Stack() 
#   a.push(123) a.push(456) a.push([19302,'q'])
# 此時， a.pop() 應該要回傳 [19302, 'q'] 
class Stack: 

    def __init__(self): 
        self.__stack = [] 

    def push(self, value): 
        self.__stack.append(value)

    def pop(self):
#       return self.__stack.pop()       這是偷吃步的作法，直接使用其內建方法
        result = self.__stack[-1]
        self.__stack = self.__stack[:-1]
        return result

    def __repr__(self):
        return str(self.__stack)

# 練習寫Queue
# 使用案例: 當我創建一個Queue物件:
#   a = Queue()
#   a.push(123) a.push({}) a.push('hahaha')
# 此時， a.pop() 應該要回傳 123
class Queue:
    
    def __init__(self): 
        self.__queue = []

    def push(self, value): 
        self.__queue.append(value)
        
    def pop(self): 
        # return self.__queue.pop(0)    這是偷吃步的作法，直接使用其內建方法
        result = self.__queue[0]
        self.__queue = self.__queue[1:]
        return result 

