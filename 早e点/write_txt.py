from flask import jsonify
import time
import json
#import sys 
#sys.path.append('C:\Users\T-bao\Desktop\早e点\test\')


def save_data(data):
	f0 =  open('test.txt','r')
	f00 = f0.read()
	if data not in f00:
		f = open('test.txt','w+')
		f.write('{}'.format(f00+data+'\n'))#尾部写入
		f.flush()
		#f.close()#必要,json.loads()?
		f1 = open('data\\test.txt','r')
		#print(f1.read())
		da_log = f1.read()
		#print(type(da_log))
		now_time = f'{time.ctime()[-4:]}-' + time.ctime()[4:-4].replace(':',' , ')
		with open('data_log\\'+now_time+'.txt','w') as output:
			output.write(da_log)
			#print(da_log)
	else:
		print('重复')
		return 'have'
	#time_now = str(time.localtime())[16:].strip('tm_wday=3, tm_yday=109, tm_isdst=0')
	#print(time_now)
	#aa = 'hhh--{}'.format(now_time)

#save_data('7901117101','666')

