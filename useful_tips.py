# Tip 1:
# 如果要對list裡面的所有元素做操作，可以用以下簡便的方法:
# 例如: 將數字轉換成字串 (注意字串跟數字的差別是單引號)
int_list = [1,2,3,4,5,6,7]
str_list = [ str(item) for item in int_list]
print(str_list) 
print("="*30)

# Tip 2:
# 用無限迴圈讀取檔案，並設定終止條件。
# (Python裡面沒有EOF符號，結束符號是""，也就是空字串。)
with open('test.txt') as fr: 
    content = ''
    s = fr.readline()
    while s != '': 
        content += s
        s = fr.readline() 
print(content)
print("="*30)

# Tip 3:
# 在函式的參數欄，用冒號賦予變數特定類型，會使Visual Code的intellisense能夠辨別該變數的類型。
# 進而能夠讓寫程式的人，更方便調用它的方法或屬性。
# (屬性就是物件的變數，方法就是物件的函式。)
def funcWithParamType(num:complex):
    return num.imag     # <- imag是藍色的，因為VS Code辨認出來num是complex。

def funcWithoutParamType(num):
    return num.imag     # <- imag是白色的，因為VS Code辨認不出來num是甚麼類型。

# Tip 4:
# 將list裡面的所有元素用逗號連起來，可以使用join。
# 注意: list裡面的元素類型必須是 str，如果不是，可以先用Tip 1做轉換。
s_list = [1,2,3,4,5, 'a', 'b', 'c'] 
new_list = [ str(item) for item in s_list]  # 先將其轉換成字串list
new_str = ','.join(new_list) 
print(new_str)
print("="*30)

# Tip 5: 
# 在python裡，所有的東西都是物件。只要是物件，就會有屬性和方法。
# 例如: 
a = 3 + 4j  # 這是一個複數
# 當我們鍵入 a. 的時候，intellisense會跳出一排可以選擇的屬性和方法給你使用。
# 扳手符號是屬性，立方盒符號是方法。
# 如此一來，你便可以知道這個物件有甚麼樣的屬性和方法可以調用。

# Tip 6: 
# 字串操作
# strip() 可以將該字串前後的空白格、換行符、TAB等等的空白全部移除。
s = "    Ha Ha Ha \n\n\t"
s = s.strip() 
print(s)
print("="*30)

# Tip 7: 
# 想要重複輸入 某個字串 或 某個字元，可以用 * (乘號)
print("-o-"*10)
