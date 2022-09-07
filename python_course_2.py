# 定義類別的關鍵字: class <class_name>
# 定義方法的關鍵字: def   <func_name>
class Person: 
    # __method__ 前後具有雙底線的方法，叫做Magic Method。
    # 注意: 命名時，不要命名成前後都有雙底線的名字，否則有可能會覆蓋掉原本的Magic Method。
    # __init__() 這個方法作用是初始化整個物件，是在物件被創建時，一定會執行的方法。
    def __init__(self, name, age, gender):
        self.name = name
        self.__age = age
        self.gender = gender
    
    def eat(self, food): 
        print(f'{self.name} is eating {food}')

    def hello(self, who):
        print(f'hello, {who}!')
    
    def introduceMyself(self):
        print(f'I am {self.name}, {self.__age} years old.')

    def getAge(self): 
        return self.__age
    # 私有成員，無論是屬性或方法，開頭一定有雙底線，才會被python判別成私有成員。
    # 公有成員，就隨意，只要沒有雙底線開頭，就是公有成員。
    # 注意: 唯一的例外是Magic Method，雖然有雙底線，但是都是公有方法。
    # 注意: 私有方法僅能在該類別"內部"使用，外部是無法使用的，連子類別都無法使用。
    def __addAge(self): # 私有方法
        self.__age += 1

    def birthday(self):
        self.__addAge()
    
# 物件導向語言三大特色:
# ---
# 1. 封裝(Encapsulation): 
#    用私有成員(private)的方式去達成不被外部存取或寫入的目的，其中包括屬性和方法。
# --- 
# 2. 繼承(Inheritance): 
#    父類別 parent class <-> 子類別 child class
# ---
# 3. 多型(Polymorphism)
#    用同樣名字的方法，把父類別的方法覆載(override)。(蓋掉的意思)

class Student(Person): 
    
    def __init__(self, name, age, gender, student_ID, school):
        self.studentID = student_ID
        self.school = school
        super().__init__(name, age, gender)

    def getAge(self): 
        print('Suck yourself.')

# 練習寫類別
# 父類別: Animal 
#   方法: sound, eat
# 子類別: Bird, Cat, Dog
class Animal:

    def __init__(self, age=0, length=1, weight=1):
        self.age = age
        self.length = length
        self.weight = weight

    def sound(self):
        pass

    def eat(self):
        pass 

class Dog(Animal): 

    def sound(self):
        print('汪汪!')

    def eat(self, food):
        if food != 'bones': 
            print('汪汪!真難吃!')  

class Cat(Animal):

    def sound(self):
        print('喵喵')
        
    def eat(self): 
        print('本喵准你進貢~')

class Bird(Animal):

    def sound(self):
        print('啾啾!')

    def eat(self): 
        print('不要餵我飼料')

# 練習寫類別
# 父類別: Geometry
#   方法: 計算面積
#   方法: 計算周長
# 子類別: 
#  1. 圓形
#  2. 長方形
#  3. 正方形
#  4. 三角形
from math import pi, sqrt 
class Geometry: 

    def __init__(self): 
        self.name = 'Geometry'
    
    def calArea(self): 
        pass
    
    def calPerimeter(self):
        pass
    
    def introduceMyself(self):
        print(f'I am {self.name}')

# 以下為子類別，全都繼承了Geometry父類別，並且擁有 introduceMyself 方法可以呼叫。
# 此時，不需要 override 這個方法，只需要 override 其中的 self.name 即可。
# 這樣，每一種幾何圖形，都會有不同的 introduceMyself 內容。
class Circle(Geometry):

    def __init__(self, radius):
        self.name = 'Circle'
        self.radius = radius
    
    def calArea(self):
        return pi * self.radius ** 2
    
    def calPerimeter(self):
        return 2 * pi * self.radius

class Rectangle(Geometry):

    def __init__(self, length, width):
        self.name = 'Rectangle'
        self.len = length
        self.wid = width
    
    def calArea(self):
        return self.len * self.wid
    
    def calPerimeter(self):
        return 2 * (self.len + self.wid)

class Square(Geometry): 
    
    def __init__(self, side):
        self.name = 'Square'
        self.side = side
    
    def calArea(self):
        return self.side * self.side
    
    def calPerimeter(self):
        return 4 * self.side 

class Triangle(Geometry): 
    
    def __init__(self, a, b, c):
        self.name = 'Triangle'
        self.a = a 
        self.b = b 
        self.c = c 
    
    def calArea(self): # 海龍公式
        s = (self.a + self.b + self.c) / 2
        return sqrt( s * (s-self.a) * (s-self.b) * (s-self.c) )
    
    def calPerimeter(self):
        return self.a + self.b + self.c

# 練習寫類別
# 練習Class super_complex 
class super_complex:

    def __init__(self, value): 
        self.value = self.__convertToComplex(value)
        self.real = self.__getRealPart()
        self.imag = self.__getImagPart()
        self.abs = self.__calAbs()
    
    def __convertToComplex(self, value):
        return complex(value)

    def __getRealPart(self):
        return self.value.real 
    
    def __getImagPart(self):
        return self.value.imag
    
    def __calAbs(self):
        return abs(self.value)

    # 以下兩個方法是Magic Method，我們重新定義它們來 override 原本的方法。
    # __repr__ 方法是用來表示(represent) 這個物件的，當我們在互動視窗執行這個物件時，就會調用這個函式。
    def __repr__(self):
        if self.value == 0: 
            return '0'
        elif self.value.imag == 0: 
            tmp = str(self.value).strip('()')
            return tmp.split('+')[0]
        else: 
            return str(self.value).strip(')(')

    # __str__ 方法是在呼叫 str() 時，會調用的函式。 
    def __str__(self):
        return self.__repr__()
    
    # __eq__ 例如: a==b 就等於self是a，other是b。
    def __eq__(self, other):
        if type(self) != type(other):   # 先判斷是不是同樣的type
            return False 
        elif self.value == other.value: # 再判斷是不是同樣的值
            return True 
        else:
            return False 

    # __add__ 例如: a+b 就等於self是a，other是b。
    def __add__(self, other):
        return super_complex(self.value + other.value)


# 用自定義的類別，重新練習之前寫過的函式
# Problem 3: 
# 輸入兩個非負整數，回傳一個字串，字串中的各個複數用", "將連起來
# Ex: funcName(1,2) -> '0, 1j, 2j, 1, 1+1j, 1+2j'
def generateComplexString3(N, M):
    tmp_list = []
    for i in range(N+1): 
        for j in range(M+1):
            num = complex(i, j)
            num_str = str( super_complex(num) )
            tmp_list.append( num_str )
    return ', '.join(tmp_list)




