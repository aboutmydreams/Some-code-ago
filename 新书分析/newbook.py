from bs4 import BeautifulSoup
import requests
import re
import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']

def en(x):
    return chr(int(x)+64)
# for i in range(1,26):
#     en(i)

# def geturl(letter):
#     url = 'http://210.35.251.243/newbook/newbook_cls_tree.php'
#     ans = requests.get(url)
#     Soup = BeautifulSoup(ans.text,'lxml')
#     leibie = Soup.select('#node{} > span'.format(letter))
#     #print(Soup)
#     print(leibie)
#     for item in leibie:
#         all_link = 'http://210.35.251.243/newbook/newbook_cls_book.php?back_days=15&s_doctype=ALL&loca_code=ALL&cls={}&clsname='.format(letter)+str(item.get("onclick"))[13:-2]
#         return all_link
# link_list = []
# for i in range(1,27):
#     aaa = en(i)
#     li_list = geturl(aaa)
#     link_list.append(li_list)
# print(link_list)
def name_num(ii):
    leibielink_list = ['http://210.35.251.243/newbook/newbook_cls_book.php?back_days=15&s_doctype=ALL&loca_code=ALL&cls=A&clsname=%E9%A9%AC%E5%88%97%E4%B8%BB%E4%B9%89%E3%80%81%E6%AF%9B%E6%B3%BD%E4%B8%9C%E6%80%9D%E6%83%B3%E3%80%81%E9%82%93%E5%B0%8F%E5%B9%B3%E7%90%86%E8%AE%BA', 'http://210.35.251.243/newbook/newbook_cls_book.php?back_days=15&s_doctype=ALL&loca_code=ALL&cls=B&clsname=%E5%93%B2%E5%AD%A6%E3%80%81%E5%AE%97%E6%95%99', 'http://210.35.251.243/newbook/newbook_cls_book.php?back_days=15&s_doctype=ALL&loca_code=ALL&cls=C&clsname=%E7%A4%BE%E4%BC%9A%E7%A7%91%E5%AD%A6%E6%80%BB%E8%AE%BA', 'http://210.35.251.243/newbook/newbook_cls_book.php?back_days=15&s_doctype=ALL&loca_code=ALL&cls=D&clsname=%E6%94%BF%E6%B2%BB%E3%80%81%E6%B3%95%E5%BE%8B', 'http://210.35.251.243/newbook/newbook_cls_book.php?back_days=15&s_doctype=ALL&loca_code=ALL&cls=E&clsname=%E5%86%9B%E4%BA%8B', 'http://210.35.251.243/newbook/newbook_cls_book.php?back_days=15&s_doctype=ALL&loca_code=ALL&cls=F&clsname=%E7%BB%8F%E6%B5%8E', 'http://210.35.251.243/newbook/newbook_cls_book.php?back_days=15&s_doctype=ALL&loca_code=ALL&cls=G&clsname=%E6%96%87%E5%8C%96%E3%80%81%E7%A7%91%E5%AD%A6%E3%80%81%E6%95%99%E8%82%B2%E3%80%81%E4%BD%93%E8%82%B2', 'http://210.35.251.243/newbook/newbook_cls_book.php?back_days=15&s_doctype=ALL&loca_code=ALL&cls=H&clsname=%E8%AF%AD%E8%A8%80%E3%80%81%E6%96%87%E5%AD%97', 'http://210.35.251.243/newbook/newbook_cls_book.php?back_days=15&s_doctype=ALL&loca_code=ALL&cls=I&clsname=%E6%96%87%E5%AD%A6', 'http://210.35.251.243/newbook/newbook_cls_book.php?back_days=15&s_doctype=ALL&loca_code=ALL&cls=J&clsname=%E8%89%BA%E6%9C%AF', 'http://210.35.251.243/newbook/newbook_cls_book.php?back_days=15&s_doctype=ALL&loca_code=ALL&cls=K&clsname=%E5%8E%86%E5%8F%B2%E3%80%81%E5%9C%B0%E7%90%86', 'http://210.35.251.243/newbook/newbook_cls_book.php?back_days=15&s_doctype=ALL&loca_code=ALL&cls=N&clsname=%E8%87%AA%E7%84%B6%E7%A7%91%E5%AD%A6%E6%80%BB%E8%AE%BA', 'http://210.35.251.243/newbook/newbook_cls_book.php?back_days=15&s_doctype=ALL&loca_code=ALL&cls=O&clsname=%E6%95%B0%E7%90%86%E7%A7%91%E5%AD%A6%E4%B8%8E%E5%8C%96%E5%AD%A6', 'http://210.35.251.243/newbook/newbook_cls_book.php?back_days=15&s_doctype=ALL&loca_code=ALL&cls=P&clsname=%E5%A4%A9%E6%96%87%E5%AD%A6%E3%80%81%E5%9C%B0%E7%90%83%E7%A7%91%E5%AD%A6', 'http://210.35.251.243/newbook/newbook_cls_book.php?back_days=15&s_doctype=ALL&loca_code=ALL&cls=Q&clsname=%E7%94%9F%E7%89%A9%E7%A7%91%E5%AD%A6', 'http://210.35.251.243/newbook/newbook_cls_book.php?back_days=15&s_doctype=ALL&loca_code=ALL&cls=R&clsname=%E5%8C%BB%E8%8D%AF%E3%80%81%E5%8D%AB%E7%94%9F', 'http://210.35.251.243/newbook/newbook_cls_book.php?back_days=15&s_doctype=ALL&loca_code=ALL&cls=S&clsname=%E5%86%9C%E4%B8%9A%E7%A7%91%E5%AD%A6', 'http://210.35.251.243/newbook/newbook_cls_book.php?back_days=15&s_doctype=ALL&loca_code=ALL&cls=T&clsname=%E5%B7%A5%E4%B8%9A%E6%8A%80%E6%9C%AF', 'http://210.35.251.243/newbook/newbook_cls_book.php?back_days=15&s_doctype=ALL&loca_code=ALL&cls=U&clsname=%E4%BA%A4%E9%80%9A%E8%BF%90%E8%BE%93', 'http://210.35.251.243/newbook/newbook_cls_book.php?back_days=15&s_doctype=ALL&loca_code=ALL&cls=V&clsname=%E8%88%AA%E7%A9%BA%E3%80%81%E8%88%AA%E5%A4%A9', 'http://210.35.251.243/newbook/newbook_cls_book.php?back_days=15&s_doctype=ALL&loca_code=ALL&cls=X&clsname=%E7%8E%AF%E5%A2%83%E7%A7%91%E5%AD%A6%2C%E5%AE%89%E5%85%A8%E7%A7%91%E5%AD%A6', 'http://210.35.251.243/newbook/newbook_cls_book.php?back_days=15&s_doctype=ALL&loca_code=ALL&cls=Z&clsname=%E7%BB%BC%E5%90%88%E6%80%A7%E5%9B%BE%E4%B9%A6']
    #print(len(leibielink_list))#22个 正确
    all_name = []
    all_num = []
    for i in range(ii):
        anss = requests.get(leibielink_list[i])
        Soup = BeautifulSoup(anss.text,'lxml')
        leibie1 = Soup.select('#titlenav > font:nth-of-type(1)')
        leibie2 = Soup.select('#titlenav > font:nth-of-type(2)')
        s = str(leibie2)
        print(s)
        if 'a' in s:
            word = "<a"
            place_a = [m.start() for m in re.finditer(word, s)][0]
            num = str(leibie2)[19:place_a-2]
        else:
            num = 0
        #print(place_a)
        #print(type(place_a))#int
        # print(str(leibie2)[19:place_a-2])#成功
        # print(str(leibie1)[38:-110])#成功
        name = str(leibie1)[38:-110]
        all_name.append(name)
        all_num.append(int(num))
    print(all_name,all_num)
    return all_name,all_num
if __name__=='__main__':
    x1_list,y1_list = name_num(22)
    new_x = ['A 马列毛邓论', 'B 哲学、宗教', 'C 社会科学总论', 'D 政治、法律', 'E 军事', 'F 经济', 'G 文化 教育 体育', 'H 语言、文字', 'I 文学', 'J 艺术', 'K 历史、地理', 'N 自然科学总论', 'O 数理化学', 'P 天文 地球科学', 'Q 生物科学', 'R 医药、卫生', 'S 农业科学', 'T 工业技术', 'U 交通运输', 'V 航空、航天', 'X 环境、安全科学', 'Z 综合性图书']
    avg = sum(y1_list)/len(new_x)
    #print(x1_list)
    #print(type(y1_list))#list
    plt.title('新书状况')
    plt.xlabel('类别')
    plt.xticks(rotation=20)
    plt.ylabel('数量')
    plt.plot(new_x,y1_list,'go:',label=str(avg*22))
    plt.plot(1,2)
    plt.legend()#显示lable标识
    plt.show()