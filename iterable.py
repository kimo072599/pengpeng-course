# Iterable (可疊代)資料型態：可以被一個一個分開取出的資料
# 字串、列表、集合、字典

# for 迴圈
# for 變數名稱 in 可疊代的資料：
for x in [3, 5, 2]:
    print(x)
for x in "abc":
    print(x)
for x in {"a", "test", 3, 10}: # 注意集合的資料沒有順序性，所以印出來的順序是隨機的
    print(x)
for x in {"a":3, "t":5}:
    print(x)
dic={"a":3, "t":5}
for x in dic:
    print(x)
    print(dic[x])

# 內建函式
# max(可疊代資料)
result=max([10, 2, 30, 1])
print(result)
result=max("xaz")
print(result)
result=max({10, 200, 30, 1})
print(result)
result=max({"x":3, "a":4})
print(result)

# sorted(可疊代資料)
result=sorted([10, 2, 30, 1])
print(result)
result=sorted("xaz")
print(result)
result=sorted({10, 200, 30, 1})
print(result)
result=sorted({"x":3, "a":4})
print(result)