# 裝飾器(Decorator)：特殊設計的函式，用來"輔助"其他的函式
# 定義裝飾器
def myDeco(callback):
    def run():
        print("裝飾器中的程式碼")
        callback() # 這個回呼函式就是要被裝式的函式
    return run
# 使用裝飾器
def test():
    print("普通函式的程式碼")

print("test")
test()

@myDeco
def test2():
    print("帶有裝飾器的函式的程式碼")

print("test2")
test2()