# 載入 numpy 套件
import numpy as np
# 觀察資料形狀
data = np.ones(10)
print(data)
print(data.shape)
data = np.array([
    [3, 1, 5],
    [1, 2, 3]
])
print(data.shape)

# 資料的轉置 .T
data = np.array([
    [2, 4, 1],
    [1, 5, 0]
])
print(data.shape) # (2, 3)
print(data.T)
print(data.T.shape) # (3, 2)
# 如果對一維資料作轉置，結果會等於原本的資料
data = np.array([1, 2, 3])
print(f"一維資料轉置(.T)的結果:\n原始資料: {data}\n轉置後資料: {data.T}")

# 扁平化資料 .ravel()
data = np.array([
    [
        [2, 1, 3],[1, 2, 3]
    ],
    [
        [0, 2, 1],[8, 9, 10]
    ]
]) # (2, 2, 3)
newData = data.ravel() # .ravel() 方法需要用變數接，不會改變原始資料
print(newData)
print(newData.shape) # (12,)

# 重塑資料形狀 .reshape()
data = np.array([
    [
        [2, 1, 3],[1, 2, 3]
    ],
    [
        [0, 2, 1],[8, 9, 10]
    ]
]) # (2, 2, 3) # 2x2x3 = 12 !!!!!!
newData = data.reshape(3,4) # 3x4 = 12
# .reshape()也需要用變數接
print(newData)
# 重塑資料的時候要注意資料的數量，必須和原始資料數量相同
# newData = data.reshape(3,5) # 3x5 = 15
# ValueError: cannot reshape array of size 12 into shape (3,5)
newData = data.reshape(1, 2, 6) # 1x2x6 = 12
print(newData)
print(newData.shape)

# 資料的初始化
data = np.zeros(18).reshape(3, 6)
print(data)

data = np.arange(9).reshape(3, 3)
print(data)
print(data.T)


# 補充 .reshape() 用法
# 當賦予資料形狀數值為 -1 時，自動填入未除盡的量
a = np.arange(18).reshape((-1, 3, 2))
# 這邊 -1 就會被填入 36/3/2 = 3
# 也就相當於下面
b = np.arange(18).reshape((3, 3, 2))
print(a)
print(b)

# 因此如果要把一維橫向資料轉成二維直向，可用.reshape(-1, 1)
data = np.arange(5)
c = data.reshape(-1, 1)
print(c)
# 這個方法是創建新的陣列，修改新陣列不會影響原陣列
c[3,0] = 9
print(c)
print(data)

# 另一個做法是利用 np.newaxis 新增一個軸 (相當於新增一個維度)
# 一維變二維
data = np.arange(5)
d = data[:, np.newaxis]
print(d)
# 二維變三維
data = np.arange(8).reshape((2, 4))
print(data)
'''
[[0 1 2 3]
 [4 5 6 7]]
'''
e = data[:, np.newaxis, :] # 相當於 e = data.reshape(2, 1, 4)
print(e)
'''
[[[0 1 2 3]]

 [[4 5 6 7]]]
'''
f = data[:, :, np.newaxis] # 相當於 e = data.reshape(2, 4, 1)
print(f)
'''
[[[0]
  [1]
  [2]
  [3]]

 [[4]
  [5]
  [6]
  [7]]]
'''
# 這個方法屬於切片創建視圖，共享同一塊數據，因此修改視圖會影響原陣列
f[1, 0, 0] = 8
print(f)
print(data)