import math
print('ax^2+bx+c=o','please write a,b,c')
sad=input('a=')
sad1=input('b=')
sad2=input('c=')
a=int(sad)
b=int(sad1)
c=int(sad2)
if b*b-4*a*c<0:
	pass
	print('this fangcheng wujie')
else:
	sad3=(-b-math.sqrt(b*b-4*a*c))/2*a
	sad4=(-b+math.sqrt(b*b-4*a*c))/2*a
	print('x1=',sad3)
	print('x2=',sad4)