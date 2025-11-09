def test(arg):
    print(arg)

test(3)
test("Hello")

# 定義一個回呼函式
def handle():
    print(100)

test(handle) # python 會告訴我們 handle 是一個函式

def test2(arg):
    arg() # 呼叫回呼函式

test2(handle) # 這樣才會印出 100

def handle2(data):
    print(data)

# test2(handle2) # 會出錯誤，因為 handle2 需要一個 data，而 test2 中沒有給予data
def test3(arg):
    arg(50) # 呼叫回呼函數，並代入參數(當回呼函述需要參數)

test3(handle2)

# 整合練習
def add(n1, n2, callback):
    callback(n1+n2)

def handle1(result):
    print("結果是", result)

add(3, 4, handle1)

def handleEnglish(result):
    print("Result of add is", result)

add(5, 6, handleEnglish)
# 以上程式碼即可用不同的方式來顯示 add 的結果