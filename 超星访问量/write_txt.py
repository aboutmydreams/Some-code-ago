from flask import jsonify
import time
import json
#import sys 
#sys.path.append('C:\Users\T-bao\Desktop\早e点\test\')

'''
def save_data(data):
	f0 =  open('line.txt','r')
	f00 = f0.read()
	aa=0
	for line in 
	else:
		print('重复')
		return 'have'
	#time_now = str(time.localtime())[16:].strip('tm_wday=3, tm_yday=109, tm_isdst=0')
	#print(time_now)
	#aa = 'hhh--{}'.format(now_time)

#save_data('7901117101','666')

'''
file = open("line.txt")
n = 0
r = 0
while 1:
    line = file.readline()
    print(f'{str(line)}----{str(n)}')
    n+=1
    if len(line) == 4:
        r+=1
    if not line:
    	print('准确率小于：',r/n)
    	break