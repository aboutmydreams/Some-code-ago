import time
def write_qq(data):
    now_time =' '+time.ctime()[4:-4].replace('  ','-')#.replace(' ','')#:不能在文件名中出现
    with open('qq.txt','r') as f0:
        f00 = str(f0.read())
    if data not in f00:
        f = open('qq.txt','w+')
        f.write('{}'.format(f00+data+'\n'))#尾部写入
        f.flush()
        #f.close()#必要,json.loads()?
    with open('data/qq.txt','r') as file:
        what_read = str(file.read())
    f1 = open('data/qq.txt','w+')
    f1.write('{}'.format(what_read+data+now_time+'\n'+'<br>'))
    f1.flush()

#     f2=open('data/qq.txt','r')
#     print(f2.read())
#     f2.close()
# write_qq('1097977702')