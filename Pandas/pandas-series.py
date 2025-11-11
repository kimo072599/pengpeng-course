# 載入 pandas 模組
import pandas as pd
# 資料索引
data=pd.Series([5, 4, -2, 3, 7])
print(data)
data=pd.Series([5, 4, -2, 3, 7], index=["a","b","c","d","e"])
print(data)
# 觀察資料
print("資料型態", data.dtype)
print("資料數量", data.size)
print("資料索引", data.index)
# 取得資料
# print(data[2], data[0]) # 根據順序，此方法即將遭棄用(20250519留)
print(data.iloc[2], data.iloc[0]) # 根據順序
print(data["e"],data["d"]) # 根據索引
# 數字運算: 基本、統計、順序
print("最大值", data.max())
print("總和", data.sum())
print("標準差", data.std())
print("中位數", data.median())
print("最大的三個數", data.nlargest(3))
# 字串運算: 基本、串接、搜尋、取代
data=pd.Series(["您好", "Python", "Pandas"])
print(data.str.lower()) # 全部變小寫
print(data.str.len()) # 算出每個字串的長度
print(data.str.cat(sep=",")) # 把字串串起來，可以自訂串接的符號
print(data.str.cat(sep="-"))
print(data.str.contains("P")) # 判斷每個字串是否包含特定的字元
print(data.str.contains("好"))
print(data.str.replace("您好","Hello")) # 取代