f = open('sas.txt','a')
f.write('hhh')
f.close()


f1 = open('sas.txt','r')
print(f1.read())