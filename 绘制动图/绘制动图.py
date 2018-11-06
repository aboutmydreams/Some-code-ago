import matplotlib.pyplot as plt
import time
#相当于是一个排序函数
def insert_sort(lst):
    lsts = []
    for i in range(len(lst)):
        temp = lst[i]
        j = i-1
        while j>=0 and lst[j]>temp:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = temp
        l = lst[:]
        lsts.append(l)
    return lsts


if __name__ == "__main__":
    lst = [13,32,42,1,53,4,66,2,5,7,74,23]
    lsts = insert_sort(lst)
    plt.ion()#打开交互模式
    fig = plt.figure()#新建绘图窗口
    ax  = plt.gca()#获取当前子图
    bars = ax.bar(range(len(lst)),height=lst)#绘制条形图
    for l in lsts:
        print(l)
        bars.remove()#删除条形图
        bars = ax.bar(range(len(lst)),height=l)#绘制条形图
        plt.pause(0.5)
    while True:#防止图片关闭
        plt.pause(1)