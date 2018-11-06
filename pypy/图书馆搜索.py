from bs4 import BeautifulSoup
import requests
def book_titles(seachname):
    #seachname = input('please input the seaching book')
    url0 = 'http://210.35.251.243/opac/openlink.php?strSearchType=title&match_flag=forward&historyCount=1&strText={}&doctype=ALL&with_ebook=on&displaypg=20&showmode=list&sort=CATA_DATE&orderby=desc&dept=ALL'.format(str(seachname))#第一页
    # all2= "http://210.35.251.243/opac/openlink.php?dept=01&title=python&doctype=ALL&lang_code=ALL&match_flag=forward&displaypg=20&showmode=list&orderby=DESC&sort=CATA_DATE&onlylendable=no&count=103&with_ebook=on&page=2"第二页
    # kejian='http://210.35.251.243/opac/openlink.php?dept=01&title=python&doctype=ALL&lang_code=ALL&match_flag=forward&displaypg=20&showmode=list&orderby=DESC&sort=CATA_DATE&onlylendable=yes&with_ebook=on&with_ebook=on'
    # kejian2='http://210.35.251.243/opac/openlink.php?dept=01&title=python&doctype=ALL&lang_code=ALL&match_flag=forward&displaypg=20&showmode=list&orderby=DESC&sort=CATA_DATE&onlylendable=yes&count=45&with_ebook=on&page=2'
    wb_data = requests.get(url0)
    soup = BeautifulSoup(wb_data.text,'lxml')
    titles = soup.select('#search_book_list > li > h3')
    kejies = soup.select('#search_book_list > li > p > span')
    booknums = str(soup.select('strong.red')[0])[20:-9]
    print(booknums)
    #print(titles)#成功
    for title,kejie in zip(titles,kejies):
        atitle = str(title)
        data = {
            'titlesname' : list(title.stripped_strings)[1],
            'titlesspace' : list(title.stripped_strings)[2],
            'titleslink' : 'http://210.35.251.243/opac/item.php?marc_no='+atitle[47:57],
            'kejie' : str(list(kejie.stripped_strings)[1])[-1]+'/'+str(list(kejie.stripped_strings)[0])[-1]

        }
        print(data)
    #print(type(kejie))
book_titles()

