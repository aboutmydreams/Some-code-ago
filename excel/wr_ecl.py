import xlrd
from xlrd import open_workbook
from xlutils.copy import copy
data = xlrd.open_workbook('1.xls', formatting_info=True)

table = data.sheets()[0]             #通过索引顺序获取
# table = data.sheet_by_index(0)       #通过索引顺序获取
# table = data.sheet_by_name(u'Sheet') #通过名称获取


w=copy(data)
w.get_sheet(0).write(0,0,"foo")
w.save('book2.xlsx')

data1 = xlrd.open_workbook('book2.xlsx')
table1 = data1.sheets()[0]
for i in range(16):
    a = table1.row_values(i)
    print(a)
