#-*- coding: UTF-8 -*-
import re,requests,sys,fileinput
import jieba
import jieba.analyse
import xlwt,xlrd
myqq = 3539347852
f = open('all.txt','r',encoding='utf-8')
lines = f.readlines()           # 调用文件的 readline()方法





def remove(text,topnum,weight=None):#分词、去停用词、前top n个关键词
    #第一步：分词，这里使用结巴分词全模式
    fenci_text = jieba.cut(text)
    #print("/ ".join(fenci_text))

    #第二步：去停用词
    #这里是有一个文件存放要改的文章，一个文件存放停用表，然后和停用表里的词比较，一样的就删掉，最后把结果存放在一个文件中
    stopwords = {}.fromkeys([ line.rstrip() for line in open('stopwd.txt') ])
    final = ""
    for word in fenci_text:
        if word not in stopwords:
            if (word != "。" and word != "，") :
                final = final + " " + word
    print(final)

    #第三步：提取关键词
    #a=jieba.analyse.extract_tags(text, topK = 5, withWeight = True, allowPOS = ())
    if weight:
        a=jieba.analyse.extract_tags(final, topK = topnum, withWeight = True,allowPOS = ())
        print('1')
        return a
    else:
        a=jieba.analyse.extract_tags(final, topK = topnum,allowPOS = ())
        return a
    #text (final)为待提取的文本
    # topK:返回几个 TF/IDF 权重最大的关键词，默认值为20。
    # withWeight:是否一并返回关键词权重值，默认值为False。
    # allowPOS:仅包括指定词性的词，默认值为空，即不进行筛选。


print(len(lines))
pbm =[]#疑问列表
for line in lines:
    line0 = line.strip().strip(' ').strip('')
    site = line0[::-1].find('】')
    line1 = line0[-site:]
    if ("?" in line1 or '吗' in line1 or '？' in line1 or '是不是' in line or '会不会' in line or '怎么' in line1) and line1[-1] != ')' and 5<len(line1)<20:
        pbm.append(line1)


toplong = len(pbm)//3
print(len(pbm))
pbmstr = ''.join(pbm)
keys = remove(pbmstr,toplong,1)#,1)
print(keys)


# someli = []
#
# for key in keys:
#     for pb in pbm:
#         if key in pb:
#



# def write_pbexcel():

workbook = xlwt.Workbook(encoding = 'ascii')
worksheet = workbook.add_sheet('My Worksheet', cell_overwrite_ok=True)
worksheet.write(0, 0, label = 'Row 0, Column 0 Value')
worksheet.write(3, 0, label = '')
print(worksheet.last_used_row)
workbook.save('Excel_Workbook.xls')

# wd = xlrd.open_workbook()















