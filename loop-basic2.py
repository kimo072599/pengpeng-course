# while迴圈
n=1
while n<=3:
    print(n)
    n+=1
# 1+2+3+...+10
n=1
sum=0 #紀錄累加的結果
while n<=10:
    sum=sum+n
    n+=1
print(sum)
# for迴圈
for x in [3,5,1]:
    print(x)
for x in "Hello":
    print(x)
for x in range(3):
    print(x)
for x in range(7,10):
    print(x)
# 1+2+3+...+10
sum=0
for x in range(1,11): #雖然寫成range(11)結果也一樣，但實際意義與命題不太相同，會多+0
    sum=sum+x
print(sum)