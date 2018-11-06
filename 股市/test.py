import time
now_time0 = '[\''+time.ctime().replace(':','\',\'').replace(' ','\',\'')+'\']'
now_time = eval(now_time0)
now_hour = now_time[3]
now_min = now_time[4]
print(now_time)