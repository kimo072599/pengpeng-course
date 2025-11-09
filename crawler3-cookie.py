# 抓取 PTT 八卦版的網頁原始碼 (HTML)
import urllib.request as req
url="https://www.ptt.cc/bbs/Gossiping/index.html"
# 建立一個 request 物件，附加 Request Headers 的資訊
request=req.Request(url, headers={
    "cookie":"over18=1",  #見下個註解
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
})
with req.urlopen(request) as response:  
    data=response.read().decode("utf-8")

import bs4
root=bs4.BeautifulSoup(data, "html.parser") 
titles=root.find_all("div", class_="title") 
for title in titles:
    if title.a != None: 
        print(title.a.string)
# 以上部分幾乎與抓取電影版的程式碼相同，唯一不同是需要多給一個 cookie 資料
# 當網頁有年齡確認頁面時，常需要透過此方法才能抓取資料，否則將抓取到年齡確認頁面的原始碼
# 然而 PTT 後端政策改動後(2023-2024 年間)，雖然年齡確認頁面仍然存在，但當使用程式碼抓取標題頁面原始碼時其實可以不需要有 over18=1 的 cookie
# 但為了爬蟲的穩定性，最好不要將此行程式碼刪除，否則若網頁後端政策又改動，還是得加上

# 現在想抓取不只是第一頁的標題
# 在"上頁"(或"下頁")按鈕上按右鍵 > 檢查，複製按鈕的名稱
# 抓取上一頁的連結
nextLink=root.find("a", string="‹ 上頁") # 找到內文是 "‹ 上頁" 的 a 標籤
print(nextLink)
print(nextLink["href"])