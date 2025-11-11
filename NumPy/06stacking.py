import numpy as np
# 準備測試資料
arr1 = np.array([
    [1, 2, 3],
    [4, 5, 6]
]) # 2x3

arr2 = np.array([
    [7, 8, 9],
    [10, 11, 12]
]) # 2x3

arr3 = np.array([
    [13, 14],
    [15, 16]
])
# 合併第一個維度
result1 = np.vstack((arr1, arr2))
"""
    4x3
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12]
    ]
"""
print(result1)
# 合併第二個維度
result2 = np.hstack((arr1,arr2))
"""
    2x6
    [
        [1, 2, 3, 7, 8, 9],
        [4, 5, 6, 10, 11, 12]
    ]
"""
print(result2)

result3 = np.hstack((arr1, arr2, arr3))
"""
    2x8
    [
        [1, 2, 3, 7, 8, 9, 13, 14],
        [4, 5, 6, 10, 11, 12, 15, 16]
    ]
"""
print(result3)