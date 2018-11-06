import pymongo
client = pymongo.MongoClient('localhost',27011)
duixiang = client['duixiang']#前者是python中的对象，后者是数据库中的对象，最好保持一致。
sheet_tab = duixiang['sheet_tab']#建立一个sheet

# path = 'duixiang.txt'
# with open(path,'r') as f:
#     lines = f.readlines()#这一文件内容,如果是这一段 用readline()
#     for index,line in enumerate(lines):
#         data = {
#             'index':index,#行数
#             'line':line,#这一行的内容
#             'words':len(line.split())
#         }
#         print(data)
#     #print(lines.split('\
#         sheet_tab.insert_one(data)
for item in sheet_tab.find():
     print(item)