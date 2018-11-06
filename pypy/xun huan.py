# -*- coding: utf-8 -*-
errortimes=0
while errortimes<3:
    user=raw_input("user:")
    password=raw_input("password:")
    if user=='123' and password=='456':
        #正确后允许进入并退出循环
        print ("OK")
        pass
        qinhao=input('请填写你的完整寝室号,医学部请标记Y，例如Y010511\n寝室号=')
print('几食堂的呀？？')
shitang=input()
qin=int(qinhao)
shi=int(shitang)
if qinhao[0] in ['y','Y']:
	a1=int(qinhao[1:2])
elif:
	b1=int(qinhao[0:-1])
	print(b1)
	print('登入')
elif:
    #错误时，出错计数加1
    print "Error , enter again:"
    errortimes+=1
else:
    #错误达到三次,结束循环
    print "You are not allowed to enter!"
name=input("please input your name:")
if not name:
	pass
	name="player01"
print('hi',name)
