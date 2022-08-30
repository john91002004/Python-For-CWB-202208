# 練習寫函式、條件式、回傳正確的值
# Problem 1: 
# 兩個input參數: 複數、屬性
# 根據不同的屬性，回傳不同的output 
# Ex: 3+4j, real -> 3
def getAttributeFromComplexNumber(num, attr):
    if attr == 'real' : 
        return num.real 
    elif attr == 'imag': 
        return num.imag 
    elif attr == 'abs': 
        return abs(num)
    else: 
        return None 