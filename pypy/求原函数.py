while 1:
	pass
	a=input('输入您想求积分的函数：')
	if a.isdigit():
		if a[0]==0:
			print('ta的原函数是：C')
		elif a[0]==1:
			print('ta的原函数是：x')
		else:	
			print(a,'x')
	elif str(a)=='tanx' or str(a)=='tan(x)':
		pass
		print('(sec(x))^2+C')
	elif str(a)=='sinx' or str(a)=='sin(x)':
        pass
        print('ta的原函数是：cos(x)+C')
	else:
		if len(a)==1:
			pass
			if str(a)=='x':
				pass
				print('ta的原函数是：','(1/2)x^2','+C')
			elif int(a)==int(a)+0:
				print('ta的原函数是：',a,'x','+C')
			else:
				print('no')
		elif len(a)==2:
			pass
			a0=a[0]
			a1=a[1]
			k=(float(a0))/2
			if int(a0)==int(a0)+0 and str(a1)=='x':
				pass
				print('ta的原函数是：',k,'x^2','+C')
			else:
				print('no')
		else:
			print('开发ing')
