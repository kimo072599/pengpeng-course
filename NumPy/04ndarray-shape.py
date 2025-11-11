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

# 資料的轉置
data = np.array([
    [2, 4, 1],
    [1, 5, 0]
])
print(data.shape) # (2, 3)
print(data.T)
print(data.T.shape) # (3, 2)
# 如果對一維資料作轉置，結果會等於原本的資料

# 扁平化資料
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

# 重塑資料形狀
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