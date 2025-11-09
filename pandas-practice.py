# 名稱不要取作 pandas，否則會和內建模組名稱衝突
# 安裝 pandas : pip install pandas
# 載入 pandas 模組
import pandas as pd
# 建立 Series
data=pd.Series([20,10,15])
# 基本 Series 操作
print(data)
print("Max", data.max())
print("Median", data.median())
data=data*2
print(data)
data=data==20
print(data)

# 建立 DataFrame
data=pd.DataFrame({
    "name":["Amy","John","Bob"],
    "salary":[30000,50000,40000]
})
# 基本 DataFrame 操作
print(data)
# 取得特定的欄位
print(data["salary"])
print("=================")
# 取得特定的列
print(data.iloc[0]) # ilocation # 雖然是取出列，但結果並不會以橫向顯示
print(data.iloc[1]) # 印出第 2 列