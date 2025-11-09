# 主程式
# 建立封包(見 geometry 資料夾)
# 封包功能可將模組進行分門別類
import geometry.point #載入封包
result=geometry.point.distance(3,4)
print("距離", result)
import geometry.line
result=geometry.line.slope(1,1,3,3)
print("斜率", result)