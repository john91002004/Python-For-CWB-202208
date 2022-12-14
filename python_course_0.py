# Course 0: 
# 了解變數的兩個種類: 穩定具體變數、指標型變數

# 查看類別: 穩定具體變數
a = 1 
b = 3.14
c = 3+4j 
print("type(a) =", type(a))
print("type(b) =", type(b))
print("type(c) =", type(c))
print("="*30)

# 查看類別: 指標型變數
a = [1,2,3]
b = {1:2, 2:3}
c = (1,2,4,5,6)
print("type(a) =", type(a))
print("type(b) =", type(b)) 
print("type(c) =", type(c))
print("="*30)

# 指標型變數: list, dict, tuple 
a = [1,2,3,4,5]
b = a 
# 此時的b是指向a所指向的物件，也就是[1,2,3,4,5]
a.append(6)
print("a =", a)
print("b =", b)
# 因為對a操作，等同於對指向物件的操作，所以b也會跟著一起改變: b == [1,2,3,4,5,6]
print("="*30)

# 如果要對a做改變，卻不對b做改變，就拷貝一份新的物件:
a = [1,2,3,4,5]
b = a.copy()
a.append(6)
print("a =", a)
print("b =", b)

