# 抓取 PTT 電影版的網頁原始碼 (HTML)
import urllib.request as req
url="https://www.ptt.cc/bbs/movie/index.html"
with req.urlopen(url) as response:
    data=response.read().decode("utf-8")
print(data)
# 會被拒絕，因為這不像是一般使用者的連線方式
# 進入想要訪問的頁面 > F12 > Network > 重新整理頁面 > (filter 設定為 all) > index.html > Headers > request headers
# 從上述操作就可以看到，當我們以一般使用者在瀏覽器訪問頁面時會附加的很多資訊，必須讓我們的程式也具備這些資訊