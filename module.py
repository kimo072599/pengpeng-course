# 載入內建的 sys 模組並取得資訊
import sys
print(sys.platform)
print(sys.maxsize)

# 建立 geometry 模組(見 geometry.py), 載入使用
import geometry
result=geometry.distance(1,1,5,5)
print(result)
result=geometry.slope(1,1,5,5)
print(result)

# 調整搜尋模組的路徑
import sys
print(sys.path) # 印出模組的搜尋路徑列表
sys.path.append("modules") # 在模組的搜尋濾鏡列表中[新增路徑]
                           # 可加入絕對路徑 / 相對路徑
print(sys.path)
import geometry2
print(geometry2.distance(1,1,5,5))