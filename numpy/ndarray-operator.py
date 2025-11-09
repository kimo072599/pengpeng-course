# 載入 numpy 模組
import numpy as np
# 逐元運算 (elementwise)
data1 = np.array([3, 2, 40])
data2 = np.array([1, 3, 6])
result = data1 + data2
print("加法：", result)
result = data1 * data2
print("乘法：", result)
result = data1 > data2
print("是否大於：", result)
result = data1 == data2
print("是否相等：", result)
# 逐元運算的前提，陣列內的資料量必須相等
# data1 = np.array([3, 2, 40, 1])
# data2 = np.array([1, 3, 6])
# result = data1 + data2
# ValueError: operands could not be broadcast together with shapes (4,) (3,)

# 矩陣運算 (matrix)
data1 = np.array([
    [1, 3]
]) # 1x2
data2 = np.array([
    [2, -1, 3],
    [-2, 4, 1]
]) # 2x3
# 內積
print("內積")
result = data1.dot(data2) # 1x3
print(result)

result = data1@data2
print(result)
# 外積
print("外積")
result = np.outer(data1, data2) # 2x6
print(result)
# 矩陣運算時要注意矩陣形狀，必須為可運算的矩陣

# 統計運算 (statistics)
# 可做單元運算
data = np.array([
    [2, 1, 7],
    [-5, 3, 8]
]) # 2x3
# 一般統計計算
result = data.sum()
print("總和", result)
result = data.max()
print("最大值", result)
result = data.mean()
print("平均值", result)
result = data.std()
print("標準差", result)
# 可針對不同維度分開處理
result = data.sum(axis = 0) # 針對第一個維度做總和 (在二維表格可以視為針對欄 column)
print(result)
result = data.sum(axis = 1) # 針對第二個維度做總和 (在二維表格可以視為針對列 row)
print(result)
result = data.max(axis = 0)
print(result)
result = data.mean(axis = 1)
print(result)

# 逐值累加
result = data.cumsum()
print("逐值累加", result)
result = data.cumsum(axis = 0)
print("針對欄逐值累加", result)
result = data.cumsum(axis = 1)
print("針對列逐值累加", result)