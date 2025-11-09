print("test")
# 定義建立生成器函式
def test():
    yield 3
# 呼叫並回傳生成器
gen=test()
# 直接嘗試印出 gen ，並不會有東西，只會提示是一個生成器
print(gen)
# 搭配 for 迴圈中使用
for d in gen:
    print(d)

print("test2")
# 函式中放入多個 yield 就會依序印出
def test2():
    yield 5
    yield 10
gen2=test2()
for d in gen2:
    print(d)

print("test3")
# 也可以用 next()來印出生成器中的值
def test3():
    yield 1
    yield 2
    yield 3
gen3=test3()
print(next(gen3)) # 1
print(next(gen3)) # 2
print(next(gen3)) # 3
# print(next(gen3)) # 出現錯誤：StopIteration

print("test4")
# 當函式中存在 yield，則呼叫函式時會與傳統函式呼叫不同，並不會執行函式中的程式碼
def test4():
    print("階段一")
    yield 6
    print("階段二")
    yield 11
gen4=test4() # 這邊呼叫時並不會印出階段一階段二，而是生成一個生成器放入變數中，函式中的程式碼暫時不會動
# for d in gen3:
#     print(d)

print("generateEven")
def generateEven():
    number=0
    yield number
    number+=2
    yield number
    number+=2
    yield number

evenGenerator=generateEven()
for data in evenGenerator:
    print(data)

print("generateEven2")
def generateEven2(maxnumber):
    number=0
    while number<=maxnumber:
        yield number
        number+=2

evenGenerator2=generateEven2(10)
for data in evenGenerator2:
    print(data)