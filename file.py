# 儲存檔案
file=open("data.txt", mode="w", encoding="utf-8") # 開啟   # mode=w 代表要寫入檔案
file.write("Hello File\nSecond Line\n測試中文") # 操作
file.close() #關閉

# 實務寫法：用 with 來開啟檔案，則最後不需寫 close，檔案就會自動安全且可靠的關閉
with open("data2.txt", mode="w", encoding="utf-8") as file:
    file.write("測試中文\n好棒棒")

# 讀取檔案 
with open("data.txt", mode="r", encoding="utf-8") as file: # 寫入檔案時可以寫入不存在的檔案，讀取檔案時則必須讀取已經存在的檔案
    data=file.read()
print(data)

# 當檔案為數字資料，想逐行讀取檔案，並計算總合
with open("datanum", mode="w", encoding="utf-8") as filenum:
    filenum.write("5\n3")
sum=0
with open("datanum", mode="r", encoding="utf-8") as filenum:
    for line in filenum:
        sum+=int(line)
print(sum)

# 使用 json 格式讀取、複寫檔案
import json
#從檔案中讀取 json 資料，放入變數 data 裡面
with open("config.json", mode="r") as file:
    data=json.load(file)
print(data) # data 會是一個字典資料
print("name:",data["name"])
data["name"]="New Name" # 修改變數中的資料
# 把最新的資料複寫回檔案中
with open("config.json", mode="w") as file:
    json.dump(data, file)
print("name:",data["name"])
