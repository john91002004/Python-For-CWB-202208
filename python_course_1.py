# 初次練習寫函式
# 範例: 跟這個世界say Hi
def sayHelloToThisWorld(): 
    print('Hello, World!')

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

# 練習寫函式: 九九乘法表(sep= tab鍵)
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

# Problem: 產生MxN 複數陣列，並存成檔案，如以下形式:
# 0j, 1j, 2j, ... Mj 
# (1+0j), (1+1j), (1+2j), ... (1+Mj)
# ...
# (N+0j), (N+1j), (N+2j), ... (N+Mj)
def outputMxNComplexToFile(M, N):
    num_list = []
    for i in range(N+1): 
        tmp_list = [] 
        for j in range(M+1): 
            num = complex(i,j)
            tmp_list.append(str(num))
        tmp_str = ', '.join(tmp_list)
        num_list.append(tmp_str)
    content = '\n'.join(num_list)
    writeToFile(content, 'MxNComplex.txt')
    

# 重構(Refactoring)
# 通常開發程式碼的時候，想法非常亂，以至於Code也非常亂，
# 因此，我們必須在一段時間之後(通常是寫完一個函式或類別)，就重構。
# 重構的目的在於，使得往後程式碼開發變得更加容易、簡便，好閱讀。
# 重構後的特色: "Human-readable" "Human-readable" "Human-readable"
# 重構不一定會讓整體的程式碼變得更加簡短，而且通常會變得更長，但是會變得更容易閱讀、理解。

# 命名: 簡單明瞭地敘述該 函式 或 變數 是做什麼用的。 (通常 長命名 比 短命名 更具描述力)
# 函式內部結構: 清楚表達該函式的邏輯
# 降層法則: 當一個函式呼叫另一個函式的時候，被呼叫的函式通常會寫在呼叫他的函式下方。
#          這樣當你由上往下讀的時候，就好像在閱讀很有結構的文章一樣，先是說明大綱，再一步一步的拆解大綱，最後是細節。

# 這個函式是上一個函式重構之後的樣子，變得非常容易閱讀。
def outputMxNComplexToFile_Refactor(M, N):
    num_arr = generateComplexArray(M, N)
    s = convertArrayIntoString(num_arr)
    writeToFile(s, 'MxNComplex.txt')

def generateComplexArray(M, N):
    num_list = [] 
    for i in range(N+1): 
        tmp_list = []
        for j in range(M+1): 
            num = complex(i, j)
            tmp_list.append(num)
        num_list.append(tmp_list)
    return num_list 

def convertArrayIntoString(arr):
    tmp_list = [] 
    for item in arr: 
        str_item = [ str(num) for num in item ]
        tmp_str = ', '.join(str_item)
        tmp_list.append(tmp_str)
    return '\n'.join(tmp_list)

# 
import json 
def saveAsJson(data ,json_file): 
    json_str = json.dumps(data)
    writeToFile(json_str, json_file)

def loadFromJson(json_file): 
    json_str = readFromFile(json_file)
    return json.loads(json_str)

# 
def outputMxNComplexAsJson(M, N): 
    outputMxNComplexToFile(M, N)
    tmp_str = readFromFile('MxNComplex.txt')
    num_array = convertStringIntoArray(tmp_str) 
    num_dict = generateDictFromComplexArray(num_array) 
    saveAsJson(num_dict)

def convertStringIntoArray(s):
    tmp_dict = generateFirstLevelDict(s)
    for key in tmp_dict.keys(): 
        tmp_dict[key] = convertComplexIntoDict( complex(key) )
    return tmp_dict

def generateFirstLevelDict(s): 
    tmp_dict = {}
    tmp_list = convertStringIntoList(s)
    for item in tmp_list: 
        tmp_dict[item] = convertArrayIntoString( complex(item) ) 
    return tmp_dict 

def convertStringIntoList(s):
    new_list = []
    s = s.split('\n')
    for item in s: 
        tmp_str_list = item.split(', ')
        new_list.extend(tmp_str_list)
        
    


