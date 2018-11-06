#-*- coding:utf-8 -*- 
from bs4 import BeautifulSoup
info=[]
with open('C:\Users\T-bao\Desktop\网页 文档\pypy\html文件\模板.html','r',encoding='utf-8') as wb_data:
	Soup = BeautifulSoup(wb_data.read())
	ps=Soup.select('body > div.container > div.habits_zone.row > div > div.type.col-xs-6 > p')
	spans=Soup.select('body > div.container > div.labels_zone.row > div > span')
	a=Soup.select('body > div.container > div.habits_zone.row > div > div.ipt_habit.col-xs-6 > input[type="text"]')
	print(ps,spans,a,sep='\n-----------------------\n')

for p in ps:
	print(p.get_text())#释放p标签所标记的信息


'''
for p,span,a in zip(ps,spans,a):
	data={
	'p'    : p.get_text(),#一定要加英文逗号啊啊啊
	'span':span.get_text(),
	'a'    : a.get_text()
	#如果有image，'image':images.get('src')
	#如果文本中存在多对一的关系，可以使用列表：'span' : list(span.stripped_strings),
	}
	print(data)
'''
for p in ps:
	data0={
	'p':p.get_text()
	}
	print(data0)
	info.append(data0)#将数据导入info（信息）
for i in info:#根据长度筛选
	pass
	if len(i['p'])>6:
		pass
		print(i['p'],len(i['p']))