#-*- coding: utf-8 -*-

'''
1、读取指定目录下的所有文件
2、读取指定文件，输出文件内容
3、创建一个文件并保存到指定目录
'''
import os
# 遍历指定目录，显示目录下的所有文件名
filenames = []
def eachFile(filepath):
    pathDir =  os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s%s' % (filepath,  allDir))
        filenames.append(child)
        # print (type(child)) # .decode('gbk')是解决中文显示乱码问题encode

# if __name__ == '__main__':
#     filePath = "D:\\FileDemo\\Java\\myJava.txt"
#     filePathI = "D:\\FileDemo\\Python\\pt.py"

eachFile("qundata815/")
f = open('all.txt','w', encoding="utf-8")

for i, txt_file in enumerate(filenames):
    # if i >= 1:
    #     continue
    print(txt_file)
    a_txt = open('{}'.format(txt_file),'r', errors='ignore')
    aread = a_txt.read()
    f.write(aread + '\n')
    # f.flush()
    # aaa = a_txt.readlines()
    # for x in aaa:
    #     print(x)
    a_txt.close()
