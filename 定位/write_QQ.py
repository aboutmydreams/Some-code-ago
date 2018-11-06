import time
def write_qq(data):
    now_time =' '+time.ctime()[4:-4].replace('  ','-')#.replace(' ','')#:不能在文件名中出现
    f0 =  open('qq.txt','r')
    f00 = str(f0.read())
    f0.close()
    if data not in f00:
        f = open('qq.txt','w+')
        f.write('{}'.format(f00+data+'\n'))#尾部写入
        f.flush()
        #f.close()#必要,json.loads()?
    file = open('data/qq.txt','r')
    what_read = str(file.read())
    file.close()
    f1 = open('data/qq.txt','w+')
    f1.write('{}'.format(what_read+data+now_time+'\n'+'<br>'))
    f1.flush()

#     f2=open('data/qq.txt','r')
#     print(f2.read())
#     f2.close()
# write_qq('1097977702')