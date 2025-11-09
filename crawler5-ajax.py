# 抓取 kkday 首頁的文章標題  (原本要抓 medium.com ，但改版了，改版後的抓法見 crawler6-requestdata)
# 觀察載入頁面時，會先有一個框架出來，內容才出現，即非常可能是網頁前端利用了 ajax 技術 (或稱 XHR)
# 透過 F12 > Network > 篩選器選擇 XHR > 重新整理網頁 > 利用 preview 或 response 在各個連線中尋找可能包含文章標題的連線
# 找到之後查看該連線的 headers 中的 general ，就可以看到資料真正的網址

import urllib.request as req
url="https://www.kkday.com/zh-tw/home/ajax_get_homepage_setting?csrf_token_name=caf1173d0145cfcc8c965d295888c951" #如果直接連線到 https://www.kkday.com/ 是抓不到資料的
# 建立一個 request 物件，附加 Request Headers 的資訊
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
})
with req.urlopen(request) as response:  
    data=response.read().decode("utf-8") # 根據觀察，取得的資料是 JSON 格式

# 解析 JSON 格式的資料，取得每篇文章的標題
import json
data=json.loads(data) # 把原始的 JSON 資料解析成字典/列表的形式
# 取得 JSON 資料中的文章標題
posts=data["data"]["homepage_product_group"]
for key in posts:
    print(key["title"])

posts=data["data"]["top_products"]["prod_list"]
for key in posts:
    print(key["introduction"])