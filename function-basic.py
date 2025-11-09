# 定義函式
def multiply(n1,n2):
    print(n1*n2)
# 函式內部的程式碼，若是沒有被呼叫，就不會執行
# 呼叫函式
multiply(3,4)
multiply(10,8)

def multiply2(n1,n2):
    print(n1*n2)
    return 10
value=multiply2(3,4)
print(value)

def multiply3(n1,n2):
    print(n1*n2)
    return n1*n2
value=multiply2(3,4)+multiply3(8,10)
print(value)

# 程式的包裝
sum=0
for n in range(11):
    sum+=n
print(sum)

sum=0
for n in range(21):
    sum+=n
print(sum)
#函世可以用來做程式的包裝，同樣的邏輯可以重複利用
def calculate(max):
    sum=0
    for n in range(1,max+1):
        sum+=n
    print(sum)
calculate(10)
calculate(20)