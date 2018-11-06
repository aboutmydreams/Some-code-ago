import os
i=0
while 1:
	if os.path.isfile('lock.log'):
		print('it has been locked')
	username=input('username=')
	password=input('password=')
	i1=3-i
	pass
	if username=='milo' and password=='123':
		pass
		print('welcome')
	else:
		if i<3:
			print('The username or password is wrong and you have only' ,i1,' opinions')
			i+=1
			
		else:
			pass
			open('lock.log','w').write(username)
			print('you are locking hhhhhh','the last name is %s'%username,'You can delete the log file in the folder')
			break
		continue
print('welcome')
