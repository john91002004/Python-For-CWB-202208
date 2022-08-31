# 練習寫函式、條件式、回傳正確的值
# Problem 1: 
# 兩個input參數: 複數、屬性
# 根據不同的屬性，回傳不同的output 
# Ex: 3+4j, real -> 3
def getAttrFromComplex(num:complex, attr): 
    if attr == 'real': 
        return num.real
    elif attr == 'imag': 
        return num.imag
    elif attr == 'abs': 
        return abs(num)
    else: 
        return None 

# 練習寫函式
# Problem 2: 
# 輸入一個複數，回傳一個字典，包含三個key value pair
def convertComplexIntoDict(num:complex): 
    return {'real': num.real, 'imag': num.imag, 'abs': abs(num)}

# 練習寫函式
# Problem 3: 
# 輸入兩個非負整數，回傳一個字串，字串中的各個複數用", "將連起來
# Ex: funcName(1,2) -> '0, 0+1j, 0+2j, 1, 1+1j, 1+2j'
# 小技巧: ', '.join(['hello', 'world']) -> 'hello, world'
def generateComplexString(n, m): 
    num_list = [] 
    for i in range(n+1): 
        for j in range(m+1): 
            num = complex(i, j)
            if num.imag == 0: 
                complex_str = str( int(num.real) )
            else:
                complex_str = f'{int(num.real)}+{int(num.imag)}j'
            num_list.append( complex_str )
    return ', '.join(num_list)

# 這是另一種寫法，直接用字串的方式產生output。
def generateComplexString2(n, m):
    s = '' 
    for i in range(n+1): 
        for j in range(m+1):
            num_string = f'{i}+{j}j'

            if num_string == '0+0j': 
                s += '0'
            elif num_string.count('0j') != 0: 
                s += f'{i}'
            else:
                s += num_string

            if i == n and j == m: 
                pass
            else: 
                s += ', '
    return s 

# Practice: 九九乘法表(sep= tab鍵)
# 1x1=1 1x2=2 1x3=3 ... 1x9=9
# 2x1=2 2x2=4 2x3=6 ... 2x9=18
# ...
def print9x9Table():
    for i in range(1,10):
        for j in range(1,10):
            print(f"{i}x{j}={i*j}", end='\t')
        print()

# Problem: 檔案操作
# 讀取檔案中的內容，每一行是一個元素，存成一個list。
# Ex: ['Hello, world!', 'How are you doing? ' ...]
def readFileAsList(file): 
    with open(file=file) as fr: 
        str_list = fr.readlines()
    return str_list 


# Problem: 讀取和寫入
def writeToFile(content, file):
    with open(file, 'w') as fw: 
        fw.write(content)

def readFromFile(file): 
    with open(file) as fr: 
        s = fr.read()
    return s 
