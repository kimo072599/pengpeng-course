#數字運算
x=3+6
x=3-6
x=3*6
x=3/6 #小數除法
x=3//6 #整數除法，結果只顯示到整數，小數無條件捨去
x=2**3 #2的3次方
x=7%3 #取餘數
print(x)
#特殊語法
x+=1 #x=x=1
x-=1 #x=x-1
x/=1 #x=x/1
x*=1 #x=x*1
#字串運算
s="Hello"
print(s)
s='Hello' #文字可用單引號或雙引號
s="\"Hello\"" #在引號前輸入\可跳脫，使得該引號被視為文字
print(s)
s="Hello"+"World"
print(s)
s="Hello" "World" #可用一個空格表示字串的串接
print(s)
s="Hello\nWorld" #輸入\n可換行
print(s)
s="""Hello

World""" #也可使用三個單引號或雙引號，即可任意換行
print(s)
s="Hello"*3+"World"
print(s)
#字串匯兌內部的字元編號，從0開始
s="Hello"
print(s[0]) #顯示第一個字元
print(s[1:4]) #顯示編號1~4-1，也就是編號1~3的字元，也就是第二到第四個字元
print(s[1:]) #從第二個字元到結尾
print(s[:5]) #從開頭到第五個字元