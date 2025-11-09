# 抓取 PTT 八卦版的網頁原始碼 (HTML)
def getData(url):
    import urllib.request as req
    # 注意這邊刪除了 url 的資料，將其移到外面了
    request=req.Request(url, headers={
        "cookie":"over18=1",  
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
    # 抓取上一頁的連結
    nextLink=root.find("a", string="‹ 上頁")
    return (nextLink["href"]) # 這裡改成 return，在外面印出來或取得上一頁按鈕連結

# 抓取一個頁面的標題
pageURL="https://www.ptt.cc/bbs/Gossiping/index.html"
pageURL=getData(pageURL)
print("\n上一頁按鈕連結:", pageURL,"\n")

# 抓取三頁標題
pageURL="https://www.ptt.cc/bbs/Gossiping/index.html"
count=0
while count<3:
    pageURL="https://www.ptt.cc"+getData(pageURL)
    count+=1