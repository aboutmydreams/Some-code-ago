import sys
import wi_bankss,time,keywordss

def get_timemin():
    now_time0 = '[\''+time.ctime().replace(':','\',\'').replace(' ','\',\'')+'\']'
    now_time = eval(now_time0)
    return now_time

def dendai():
    while 1:
        if get_timemin()[-4] not in ['08','07']:
            print(get_timemin()[-3],get_timemin(),111)
            print(keywordss.get_lastwd())
            time.sleep(3000)
        else:
            print(get_timemin()[-3],get_timemin(),233333)
            time.sleep(30)
            print(wi_bankss.all_title_and_link())
            time.sleep(30)
            print(keywordss.get_lastwd())
            time.sleep(700)


dendai()
# keywordss.last_wd()