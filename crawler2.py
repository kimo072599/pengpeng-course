# 抓取 PTT 電影版的網頁原始碼 (HTML)
import urllib.request as req
url="https://www.ptt.cc/bbs/movie/index.html"
# 建立一個 request 物件，附加 Request Headers 的資訊
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
})
with req.urlopen(request) as response:  # 改成用 request 的資料，而不是用 url
    data=response.read().decode("utf-8")
#print(data)

# 解析原始碼，取得每篇文章的標題
# 需要使用第三方套件 beautifulsoup4，因此需安裝: pip install beautifulsoup4
import bs4
root=bs4.BeautifulSoup(data, "html.parser") # 讓 BeautifulSoup 協助我們解析 HTML 格式文件
print(root.title)
print(root.title.string)
titles=root.find("div", class_="title") # 尋找 class="title" 的 div 標籤 # find 會幫我們找出其中一個符合條件的標籤
print(titles) # 印出一個標題，並包含 div 標籤
print(titles.a.string) # 去蕪存菁的取得 a 標籤內的文字
titles=root.find_all("div", class_="title") # 尋找"所有" class="title" 的 div 標籤
print(titles)
for title in titles:
    if title.a != None: # 如果標題含有 a 標籤(即沒有被刪除)，印出來
        print(title.a.string)