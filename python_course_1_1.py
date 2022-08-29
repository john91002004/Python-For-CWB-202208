# Problem 1 
def getAttributeFromComplexNumber(num, attr):
    if attr == 'real' : 
        return num.real 
    elif attr == 'imag': 
        return num.imag 
    elif attr == 'abs': 
        return abs(num)
    else: 
        return None 