# 載入 numpy 套件
import numpy as np
# 建立一維陣列
data = np.array([3, 2, 6, 4])
print(data)
data = np.empty(4) # 創造一個有四個資料的一維陣列，資料未指定，但也不保證是零，而是印出記憶體殘值
print(data) # Numpy 1.26 之後，記憶體會先清零才分配出來，所以會看到結果是[0. 0. 0. 0.]
data = np.zeros(3)
print(data) # 會輸出[0. 0. 0.]，因為預設是使用浮點數建立陣列
data = np.arange(5)
print(data)

# 建立二維陣列
data = np.array([   # 創造一個 3x3 的二維陣列
    [2, 3, 2],
    [1, 5, 2],
    [4, 2, 1]
])
print(data)
# 利用 empty、ones、zeros 建立二維陣列時，參數指定的是資料結構，而不是資料的值
data = np.empty([3,3]) # 創造一個 3x3 的二維陣列，資料未指定
print(data)
data = np.ones([2,3])
print(data)

# 建立三維陣列
data = np.array([   # 根據列表創造一個 2x2x2 的三維陣列
    [
        [3, 1], [1, 2]
    ],
    [
        [2, 5], [10, 2]
    ]
])
print(data)
data = np.zeros([3, 1, 3]) # 創造一個 3x1x3 的三維陣列，資料都是 0
print(data)

# 建立高維陣列
data = np.array([  # 創造一個 1x1x2x3 的四維陣列
    [
        [
            [3, 2, 1],
            [5, 5, 5]
        ]
    ]
])
print(data)
data = np.ones([2, 1, 1, 2]) # 創造一個 2x1x1x2 的四維陣列，資料都是 1
print(data)