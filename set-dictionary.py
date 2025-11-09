# 集合的運算
s1={3,4,5}
print(3 in s1)
print(10 in s1)
print(10 not in s1)
s2={4,5,6,7}
s3=s1&s2 #交集:取兩個集合中相同的資料
print(s3)
s3=s1|s2 #聯集:取兩個集合中的所有資料，但不重複
print(s3)
s3=s1-s2 #差集:從s1中減去和s2重複的部分
print(s3)
s3=s1^s2 #反交集:取兩個集合中不重複的部分
print(s3)
s=set("Hello") #set(字串)
print(s)
print("H" in s)
print("A" in s)
print("He" in s)
print("HH" in s)
#字典的運算
dic={"apple":"蘋果","bug":"蟲蟲"}
print(dic["apple"])
dic["apple"]="小蘋果" #更改字典的value
print(dic["apple"])
dic={"apple":"蘋果","bug":"蟲蟲"}
print("apple" in dic) #判斷key是否存在
print(dic)
del dic["apple"] #以key做代表刪除字典中的鍵值對(key-value pair)
print(dic)
# dic={x:x*2 for x in 列表}
dic={x:x*2 for x in [3,4,5]} #從列表的資料產生字典
print(dic)
