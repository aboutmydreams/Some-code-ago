from bs4 import BeautifulSoup
import requests
import re
import matplotlib.pyplot as plt
from pylab import mpl
import seaborn as sns
mpl.rcParams['font.sans-serif'] = ['SimHei']

if __name__=='__main__':
    sns.set_style('darkgrid')
    xbian = [0.4,0.66,0.4,0.2,0,-0.2,-0.3,-0.4,-0.6,-0.68,-0.6,-0.4,-0.2,0,0.2,0.34,0.4]
    ybian = [0.008,0.032,0.026,0.026,0.018,0.01,0,-0.012,-0.028,-0.032,-0.03,-0.024,-0.026,-0.02,-0.02,0,0.008]
    plt.plot(xbian, ybian,'-k')
    #print(x1_list)
    #print(type(y1_list))#list
    plt.title('新书状况')
    plt.xlabel('类别')
    plt.xticks(rotation=20)
    plt.ylabel('数量')
    # plt.plot(new_x,y1_list,'go:',label=str(avg*22))
    # plt.plot(1,2)
    plt.legend()#显示lable标识
    plt.show()