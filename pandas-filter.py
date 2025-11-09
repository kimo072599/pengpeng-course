# 載入 pandas 模組
import pandas as pd
# 篩選練習 - Series
data=pd.Series([30,15,20])
condition=[True, False, True]
filteredData=data[condition]
print(filteredData)

condition=data>18
print(condition) # 會看到 condition 其實就是個布林值列表
filteredData=data[condition]
print(filteredData)

data=pd.Series(["您好", "Python", "Pandas"])
condition=[True, False, True]
filteredData=data[condition]
print(filteredData)

condition=data.str.contains("P")
print(condition)
filteredData=data[condition]
print(filteredData)

# 篩選練習 - DataFrame
data=pd.DataFrame({
    "name":["Amy", "Bob", "Charles"],
    "salary":[30000,50000,40000]
})
print(data)
condition=[False, True, True]
filteredData=data[condition]
print(filteredData)

condition=data["salary"]>=40000
print(condition)
filteredData=data[condition]
print(filteredData)

condition=data["name"]=="Amy"
print(condition)
filteredData=data[condition]
print(filteredData)