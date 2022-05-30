with open('sas.txt','a') as f:
    f.write('hhh')
f1 = open('sas.txt','r')
print(f1.read())