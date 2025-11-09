import pandas as pd
# 讀取資料
data=pd.read_csv("googleplaystore.csv") # 把 csv 格式的檔案讀取成一個 DataFrame
# 觀察資料
print(data)
print("資料數量",data.shape)
print("資料欄位",data.columns)

# 分析資料：評分的各種統計數據
print(data["Rating"])
print("平均數", data["Rating"].mean())
print("中位數", data["Rating"].median())
print("取得評分前 100 名應用程式的平均", data["Rating"].nlargest(100).mean()) # 會發現結果 > 5，不太正常，所以要進行資料處理
condition=data["Rating"]>5
datawrong=data[condition]
print(datawrong) # 會找出一個評分不正常的數據
condition=data["Rating"]<=5
dataright=data[condition]
print("平均數", dataright["Rating"].mean())
print("中位數", dataright["Rating"].median())
print("取得評分前 100 名應用程式的平均", dataright["Rating"].nlargest(100).mean())

# 分析資料：安裝數量的各種數據
# print("平均數",data["Installs"].mean()) # 試圖了解安裝數量的數據，會發現怪怪的
# print(data["Installs"]) # 發現原來 Installs 欄位裡的不是數值，而是字串
# data["Installs"]=pd.to_numeric(data["Installs"]) # 發生無法處理的狀況因此需要處理數據：ValueError: Unable to parse string "10,000+"
# data["Installs"]=pd.to_numeric(data["Installs"].str.replace("[,+]","",regex=True)) # 還是處理失敗：ValueError: Unable to parse string "Free" at position 10472
# print(data["Installs"][10472]) # 得到 Free，這是原始資料的不乾淨，再次進行處理
data["Installs"]=pd.to_numeric(data["Installs"].str.replace("[,+]","",regex=True).replace("Free","",regex=True))
print(data["Installs"])
print("平均數",data["Installs"].mean())
condition=data["Installs"]>100000
print("安裝數量大於 100000 的應用程式有幾個",data[condition].shape)
print("安裝數量大於 100000 的應用程式有幾個",data[condition].shape[0])

# 基於資料的應用：關鍵字搜尋應用程式名稱
keyword=input("請輸入關鍵字：")
condition=data["App"].str.contains(keyword)
print(data[condition]["App"])
print("包含關鍵字的應用程式數量",data[condition]["App"].shape[0])
condition=data["App"].str.contains(keyword, case=False) # 忽略大小寫
print("包含關鍵字的應用程式數量",data[condition]["App"].shape[0])