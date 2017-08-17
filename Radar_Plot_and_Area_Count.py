
# coding: utf-8

# # 雷達圖面積計算及視覺化 - 用Jupyter notebook 
# ### Radar Plot and Area Count - Jupyter notebook 

# ## Area Count
# - 雷達圖常用來表達能力值，能力值總和高低可用雷達圖範圍面積計算，但網路上計算雷達圖面積多為座標(x,y)計算，不適用僅知各維度刻度的雷達圖，故特別分享本實作。
# - 計算雷達圖面積，雷達圖以多個等角三角形構成，透過雷達圖已知的各維度刻度即可計算雷達圖面積。
# - 三角形面積計算，如已知兩邊長及其夾角，可用三角函數1/2ABsinC求出，AB為兩邊邊長、C為AB之夾角，角度C為360/邊長求得，惟math.sin()所填入的值並非角度，這個坑本實作已解決如下。

# In[9]:


import math

def area_count(file_list):
    _m = file_list
    area = 0
    if len(_m) < 3:
        raise ("少於三維度，不成面積")
    else:
        for i in range(len(_m)):
            if i < len(_m)-1:
                area += _m[i]*_m[i+1]
            else:
                area += _m[len(_m)-1]*_m[0]
        area = area*math.sin(math.radians(360/len(_m)))/2
    print ('{} Area count = {}'.format(_m , area))
    return area


M1 = [25,100,48.47,16.67,16.67]
M2 = [50,48.78,0,100,58.35]
M3 = [100,50,30.57,0,0.84]

area_count(M1)
area_count(M2)
area_count(M3)


# ## Radar Plot
# 
# - Python可以採用Jupyter Notebook繪製雷達圖進行資料視覺化。

# In[8]:


from iplotter import ChartJSPlotter

plotter = ChartJSPlotter()

data = {
    "labels": ["Label-1", "Label-2", "Label-3", "Label-4","Label-5"],
    "datasets": [
        {
            "label": "File_1",
            "borderColor": "rgba(0,255,255,1)",
            "data": [25,100,48.47,16.67,16.67]
            
        }, {
            "label": "File_2",
            "borderColor": "rgba(0,0,255,1)",
            "data": [50,48.78,0,100,58.35]
        },
        {
            "label": "File_3",
            "borderColor": "rgba(255,99,132,1)",
            "data": [100,50,30.57,0,0.84]
        }
    ]
}

plotter.plot_and_save(data, 'radar', options=None)

