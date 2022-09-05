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


