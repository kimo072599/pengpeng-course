#有序可變動的列表 List
grades=[12,60,15,70,90]
print(grades)
print(grades[0])
print(grades[3])
grades[0]=55
print(grades)
print(grades[1:4])
grades[1:4]=[]
print(grades)
grades=grades+[12,33]
print(grades)
length=len(grades) #取得列表長度 len(列表資料)
print(length)
print(len(grades))
data=[[3,4,5],[6,7,8]]
print(data[0][1])
data[0][0:2]=[5,5,5]
print(data)
#有序不可變動的列表 Tuple
data=(3,4,5)
data[0]=5 #會顯示錯誤
#除了不能更動tuple中的資料，其餘皆與list相同