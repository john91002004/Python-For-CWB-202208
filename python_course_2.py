# 練習寫函式、條件式、回傳正確的值
# Problem 1: 
# 兩個input參數: 複數、屬性
# 根據不同的屬性，回傳不同的output 
# Ex: 3+4j, real -> 3
def getAttrFromComplex(num, attr): 
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
def convertComplexIntoDict(num): 
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
def generateComplexString2(n,m):
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
