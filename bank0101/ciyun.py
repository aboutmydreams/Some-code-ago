import wordcloud #导入词云
from wordcloud import STOPWORDS  # 停止词
import jieba
import numpy as np  # 科学计算
import matplotlib  # 数据可视化
from matplotlib import pyplot as plt
from PIL import Image  # 图片处理

def getYesterday():
    today=datetime.date.today()
    oneday=datetime.timedelta(days=1)
    return str(today-oneday).replace('-','')

# 读取文本
pythonInfo = open('all_yes_title.txt', 'r', encoding='utf-8', errors='ignore').read()
# print(pythonInfo)
# 切割
pythonCut = jieba.cut(pythonInfo, cut_all=True)
pythonInfoList = ' '.join(pythonCut)  # 返回一个生成器对象
print(pythonInfoList)
backgroud = np.array(Image.open('猫.jpg'))  # 将图片格式化成RBG数组
myCloudword = wordcloud.WordCloud(font_path='simkai.ttf',  # 字体路径
                                  width=400, height=200,
                                  mask=backgroud,  # 字体颜色
                                  scale=1,  # 比例
                                  max_words=200,  # 最大字数
                                  min_font_size=4,  # 最小字体
                                  stopwords=STOPWORDS,  # 默认停止词
                                  random_state=50,  # 随机角度
                                  background_color='black',  # 背景颜色
                                  max_font_size=100  # 最大字体
                                  ).generate(pythonInfoList)
plt.imshow(myCloudword)
plt.show() #图片展示
print(myCloudword)
plt.figimage(myCloudword)   #绘制图片
plt.imsave(f'keyimg/{getYesterday()}.png', myCloudword)

# ---------------------

# 本文来自 why1673 的CSDN 博客 ，全文地址请点击：https://blog.csdn.net/weixin_41829272/article/details/80864396?utm_source=copy
