import time
import xici,check_ip
while 1:
    xici.ip_pool()
    time.sleep(30)

    a = check_ip.last_good_ip()
    nowtime = str(time.localtime().tm_mon)+'月'+str(time.localtime().tm_mday)+'日'+str(time.localtime().tm_hour)+':'+str(time.localtime().tm_min)+':'+str(time.localtime().tm_sec)
    print (a,'\n---------------现在是------------'+nowtime)