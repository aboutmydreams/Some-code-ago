import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
import seaborn as sns


#显示数据，返回数据列表
def show_data():
	dataopen = open('data.txt', 'r',encoding="utf-8")
	data = dataopen.read().replace('\n','a').replace('	','a').replace('aa','a').replace('a',',').replace(' ','')
	dataopen.close()
	return eval('['+data+']')
#print(len(show_data()))

data = show_data()
#print(data)


#计算数据中相同地点货物数量，返回25个数量的列表
def all_count():
	def same(i):
		i_count = data.count(i)
		return i_count
	all_num = []
	for i in range(1,26):
		i_num = same(i)
		all_num.append(i_num)
	return all_num
	#print(len(all_num))
print(all_count())

data1 =[41, 36, 48, 36, 21, 45, 43, 41, 40, 46, 43, 42, 44, 55, 55, 45, 28, 40, 44, 40, 17, 43, 32, 41, 34]
print(abs(-5))

#货物地点的坐标
dian1 = [[2, 6], [2, 3], [2, 0], [2, -3], [2, -6], [4, 6], [4, 3], [4, 0], [4, -3], [4, -6], [6, 6], [6, 3], [6, 0], [6, -3], [6, -6], [8, 6], [8, 3], [8, 0], [8, -3], [8, -6], [10, 6], [10, 3], [10, 0], [10, -3], [10, -6]]


#可卸货坐标地，传入目的地坐标点，输出周边4个点，可输入0
def could_done(dian):
	point1 = [dian1[dian][0]+1,dian1[dian][1]]
	point2 = [dian1[dian][0]-1,dian1[dian][1]]
	point3 = [dian1[dian][0],dian1[dian][1]+1]
	point3 = [dian1[dian][0],dian1[dian][1]-1]
	return [point1,point2,point3,point4]


#最少的转弯用时
def less_turn_time():
	time_list = []
	for i in range(0,25):
		if i in [1,2,4,5,8,13,18,23]:
			time = 2
		elif i == 3:
			time = 0
		else:
			time = 4
		time_list.append(time)
	return time_list
print(less_turn_time())

#最少的路程时间
def less_distance_time():
	time_list = []
	for i in range(0,25):
		if i in [8,13,18,23]:
			time_one = 2*(dian1[i][0]+abs(dian1[i][1])+1)#加一是因为绕路了
		else:
			time_one = 2*(dian1[i][0]+abs(dian1[i][1]))#路程上一米每秒
		time_list.append(time_one)
	return time_list
print(less_distance_time())

#测试一个机器人搬运完货物的时间
def test_less_time():
	all_time = 0
	for i in range(0,25):
		must_time = 3500#1000*(2+1+0.5)装货时间 卸货时间 扫码时间
		every_num = all_count()
		less_turntime = less_turn_time()
		less_distancetime = less_distance_time()
		time = every_num[i]*(less_turntime[i]+less_distancetime[i])#个数乘以最小时间
		all_time = all_time+time
	return all_time+must_time
print(test_less_time())



def lu(i):
	time_li = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
	



def robot():
	the_data = show_data()
	time = 0
	had_done = 0 #货物序号
	this_done = 0 #是否卸货，0为没有，1为已经卸货
	aim_num = the_data[had_done]-1 #货物的目的地序号
	aim_place = dian1[aim_num] #目的地坐标
	starting_point = (0,0) #机器人起点
	while time<less_turntime[aim_num]+less_distancetime[aim_num]+8:#8是最大延时，额外转弯2次，等待避让3次
		pass
		if aim_place[0] in [8,13,18,23]:
			while x:
				pass
			time +=1
			x = starting_point[0]+1


#背景
sns.set_style('darkgrid')


#绘制目的地坐标
xl = [0]
yl = [0]
for i in range(0,25):
	x = dian1[i][0]
	y = dian1[i][1]
	xl.append(x)
	yl.append(y)
pl.plot(xl, yl,'s',color='#C5D9F1')# use pylab to plot x and y(o是点，r是red)

#绘制边界
xbian = [0.5,11.5,11.5,0.5,0.5,0.5,-1.5,-1.5,0.5]
ybian = [7.5,7.5,-7.5,-7.5,7.5,1.5,1.5,-1.5,-1.5]
pl.plot(xbian, ybian,'-k')

#绘制路线
'''
xlu = [1,1,3,3,5,5,7,7,9,9,11,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1]
ylu = [-7,7,7,-7,-7,7,7,-7,-7,7,7,-7,-7,-5,-5,-4,-4,-2,-2,-1,-1,1,1,2,2,4,4,5,5,7,7]
pl.plot(xlu, ylu,':','#f0f0f0')
'''



pl.show()# show the plot on the screen