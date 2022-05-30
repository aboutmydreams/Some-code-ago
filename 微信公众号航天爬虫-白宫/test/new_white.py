# -*- coding: UTF-8 -*-
import requests,time,os
from bs4 import BeautifulSoup

HTML_DIR = "html"
TXT_PATH="whg_news.txt"
TYPEDIC={
    "presidential-action":"PRESIDENTIAL ACTIONS",
    "briefing-statement":"BRIEFINGS & STATEMENTS",
    "article":"ARTICLES"
}

s = requests.session()

#查看页数
def how_many_page():
    url = 'https://www.whitehouse.gov/news/'
    s = requests.session()
    page = s.get(url).text
    soup = BeautifulSoup(page,'lxml')
    last_pages = soup.select('#main-content > div.page-results > div > div > a')
    print(last_pages)
    print(last_pages[2].get_text())
    return last_pages[2].get_text()

last_page = how_many_page()




#存链接文档
def what_url(page_i):
    if page_i == 1:
        return 'https://www.whitehouse.gov/news/'
    if page_i > 1:
        return f'https://www.whitehouse.gov/news/page/{page_i}/'

page_list = []
with open("page.txt","w") as a:
    for i in range(1,int(last_page)+1):
        page_list.append(what_url(i))
        one_url = str(what_url(i))
        print(one_url)
        a.write(one_url)
    print(page_list)
with open("page.txt","r") as b:
    page_list = b.readlines()
    print(page_list)

def page_ten_link(i):
    page_list = ['https://www.whitehouse.gov/news/', 'https://www.whitehouse.gov/news/page/2/', 'https://www.whitehouse.gov/news/page/3/', 'https://www.whitehouse.gov/news/page/4/', 'https://www.whitehouse.gov/news/page/5/', 'https://www.whitehouse.gov/news/page/6/', 'https://www.whitehouse.gov/news/page/7/', 'https://www.whitehouse.gov/news/page/8/', 'https://www.whitehouse.gov/news/page/9/', 'https://www.whitehouse.gov/news/page/10/', 'https://www.whitehouse.gov/news/page/11/', 'https://www.whitehouse.gov/news/page/12/', 'https://www.whitehouse.gov/news/page/13/', 'https://www.whitehouse.gov/news/page/14/', 'https://www.whitehouse.gov/news/page/15/', 'https://www.whitehouse.gov/news/page/16/', 'https://www.whitehouse.gov/news/page/17/', 'https://www.whitehouse.gov/news/page/18/', 'https://www.whitehouse.gov/news/page/19/', 'https://www.whitehouse.gov/news/page/20/', 'https://www.whitehouse.gov/news/page/21/', 'https://www.whitehouse.gov/news/page/22/', 'https://www.whitehouse.gov/news/page/23/', 'https://www.whitehouse.gov/news/page/24/', 'https://www.whitehouse.gov/news/page/25/', 'https://www.whitehouse.gov/news/page/26/', 'https://www.whitehouse.gov/news/page/27/', 'https://www.whitehouse.gov/news/page/28/', 'https://www.whitehouse.gov/news/page/29/', 'https://www.whitehouse.gov/news/page/30/', 'https://www.whitehouse.gov/news/page/31/', 'https://www.whitehouse.gov/news/page/32/', 'https://www.whitehouse.gov/news/page/33/', 'https://www.whitehouse.gov/news/page/34/', 'https://www.whitehouse.gov/news/page/35/', 'https://www.whitehouse.gov/news/page/36/', 'https://www.whitehouse.gov/news/page/37/', 'https://www.whitehouse.gov/news/page/38/', 'https://www.whitehouse.gov/news/page/39/', 'https://www.whitehouse.gov/news/page/40/', 'https://www.whitehouse.gov/news/page/41/', 'https://www.whitehouse.gov/news/page/42/', 'https://www.whitehouse.gov/news/page/43/', 'https://www.whitehouse.gov/news/page/44/', 'https://www.whitehouse.gov/news/page/45/', 'https://www.whitehouse.gov/news/page/46/', 'https://www.whitehouse.gov/news/page/47/', 'https://www.whitehouse.gov/news/page/48/', 'https://www.whitehouse.gov/news/page/49/', 'https://www.whitehouse.gov/news/page/50/', 'https://www.whitehouse.gov/news/page/51/', 'https://www.whitehouse.gov/news/page/52/', 'https://www.whitehouse.gov/news/page/53/', 'https://www.whitehouse.gov/news/page/54/', 'https://www.whitehouse.gov/news/page/55/', 'https://www.whitehouse.gov/news/page/56/', 'https://www.whitehouse.gov/news/page/57/', 'https://www.whitehouse.gov/news/page/58/', 'https://www.whitehouse.gov/news/page/59/', 'https://www.whitehouse.gov/news/page/60/', 'https://www.whitehouse.gov/news/page/61/', 'https://www.whitehouse.gov/news/page/62/', 'https://www.whitehouse.gov/news/page/63/', 'https://www.whitehouse.gov/news/page/64/', 'https://www.whitehouse.gov/news/page/65/', 'https://www.whitehouse.gov/news/page/66/', 'https://www.whitehouse.gov/news/page/67/', 'https://www.whitehouse.gov/news/page/68/', 'https://www.whitehouse.gov/news/page/69/', 'https://www.whitehouse.gov/news/page/70/', 'https://www.whitehouse.gov/news/page/71/', 'https://www.whitehouse.gov/news/page/72/', 'https://www.whitehouse.gov/news/page/73/', 'https://www.whitehouse.gov/news/page/74/', 'https://www.whitehouse.gov/news/page/75/', 'https://www.whitehouse.gov/news/page/76/', 'https://www.whitehouse.gov/news/page/77/', 'https://www.whitehouse.gov/news/page/78/', 'https://www.whitehouse.gov/news/page/79/', 'https://www.whitehouse.gov/news/page/80/', 'https://www.whitehouse.gov/news/page/81/', 'https://www.whitehouse.gov/news/page/82/', 'https://www.whitehouse.gov/news/page/83/', 'https://www.whitehouse.gov/news/page/84/', 'https://www.whitehouse.gov/news/page/85/', 'https://www.whitehouse.gov/news/page/86/', 'https://www.whitehouse.gov/news/page/87/', 'https://www.whitehouse.gov/news/page/88/', 'https://www.whitehouse.gov/news/page/89/', 'https://www.whitehouse.gov/news/page/90/', 'https://www.whitehouse.gov/news/page/91/', 'https://www.whitehouse.gov/news/page/92/', 'https://www.whitehouse.gov/news/page/93/', 'https://www.whitehouse.gov/news/page/94/', 'https://www.whitehouse.gov/news/page/95/', 'https://www.whitehouse.gov/news/page/96/', 'https://www.whitehouse.gov/news/page/97/', 'https://www.whitehouse.gov/news/page/98/', 'https://www.whitehouse.gov/news/page/99/', 'https://www.whitehouse.gov/news/page/100/', 'https://www.whitehouse.gov/news/page/101/', 'https://www.whitehouse.gov/news/page/102/', 'https://www.whitehouse.gov/news/page/103/', 'https://www.whitehouse.gov/news/page/104/', 'https://www.whitehouse.gov/news/page/105/', 'https://www.whitehouse.gov/news/page/106/', 'https://www.whitehouse.gov/news/page/107/', 'https://www.whitehouse.gov/news/page/108/', 'https://www.whitehouse.gov/news/page/109/', 'https://www.whitehouse.gov/news/page/110/', 'https://www.whitehouse.gov/news/page/111/', 'https://www.whitehouse.gov/news/page/112/', 'https://www.whitehouse.gov/news/page/113/', 'https://www.whitehouse.gov/news/page/114/', 'https://www.whitehouse.gov/news/page/115/', 'https://www.whitehouse.gov/news/page/116/', 'https://www.whitehouse.gov/news/page/117/', 'https://www.whitehouse.gov/news/page/118/', 'https://www.whitehouse.gov/news/page/119/', 'https://www.whitehouse.gov/news/page/120/', 'https://www.whitehouse.gov/news/page/121/', 'https://www.whitehouse.gov/news/page/122/', 'https://www.whitehouse.gov/news/page/123/', 'https://www.whitehouse.gov/news/page/124/', 'https://www.whitehouse.gov/news/page/125/', 'https://www.whitehouse.gov/news/page/126/', 'https://www.whitehouse.gov/news/page/127/', 'https://www.whitehouse.gov/news/page/128/', 'https://www.whitehouse.gov/news/page/129/', 'https://www.whitehouse.gov/news/page/130/', 'https://www.whitehouse.gov/news/page/131/', 'https://www.whitehouse.gov/news/page/132/', 'https://www.whitehouse.gov/news/page/133/', 'https://www.whitehouse.gov/news/page/134/', 'https://www.whitehouse.gov/news/page/135/', 'https://www.whitehouse.gov/news/page/136/', 'https://www.whitehouse.gov/news/page/137/', 'https://www.whitehouse.gov/news/page/138/', 'https://www.whitehouse.gov/news/page/139/', 'https://www.whitehouse.gov/news/page/140/', 'https://www.whitehouse.gov/news/page/141/', 'https://www.whitehouse.gov/news/page/142/', 'https://www.whitehouse.gov/news/page/143/', 'https://www.whitehouse.gov/news/page/144/', 'https://www.whitehouse.gov/news/page/145/', 'https://www.whitehouse.gov/news/page/146/', 'https://www.whitehouse.gov/news/page/147/', 'https://www.whitehouse.gov/news/page/148/', 'https://www.whitehouse.gov/news/page/149/', 'https://www.whitehouse.gov/news/page/150/', 'https://www.whitehouse.gov/news/page/151/', 'https://www.whitehouse.gov/news/page/152/', 'https://www.whitehouse.gov/news/page/153/', 'https://www.whitehouse.gov/news/page/154/', 'https://www.whitehouse.gov/news/page/155/', 'https://www.whitehouse.gov/news/page/156/', 'https://www.whitehouse.gov/news/page/157/', 'https://www.whitehouse.gov/news/page/158/', 'https://www.whitehouse.gov/news/page/159/', 'https://www.whitehouse.gov/news/page/160/', 'https://www.whitehouse.gov/news/page/161/', 'https://www.whitehouse.gov/news/page/162/', 'https://www.whitehouse.gov/news/page/163/', 'https://www.whitehouse.gov/news/page/164/', 'https://www.whitehouse.gov/news/page/165/', 'https://www.whitehouse.gov/news/page/166/', 'https://www.whitehouse.gov/news/page/167/', 'https://www.whitehouse.gov/news/page/168/', 'https://www.whitehouse.gov/news/page/169/', 'https://www.whitehouse.gov/news/page/170/', 'https://www.whitehouse.gov/news/page/171/', 'https://www.whitehouse.gov/news/page/172/', 'https://www.whitehouse.gov/news/page/173/', 'https://www.whitehouse.gov/news/page/174/', 'https://www.whitehouse.gov/news/page/175/', 'https://www.whitehouse.gov/news/page/176/', 'https://www.whitehouse.gov/news/page/177/', 'https://www.whitehouse.gov/news/page/178/', 'https://www.whitehouse.gov/news/page/179/', 'https://www.whitehouse.gov/news/page/180/', 'https://www.whitehouse.gov/news/page/181/', 'https://www.whitehouse.gov/news/page/182/', 'https://www.whitehouse.gov/news/page/183/', 'https://www.whitehouse.gov/news/page/184/', 'https://www.whitehouse.gov/news/page/185/', 'https://www.whitehouse.gov/news/page/186/', 'https://www.whitehouse.gov/news/page/187/', 'https://www.whitehouse.gov/news/page/188/', 'https://www.whitehouse.gov/news/page/189/', 'https://www.whitehouse.gov/news/page/190/', 'https://www.whitehouse.gov/news/page/191/', 'https://www.whitehouse.gov/news/page/192/', 'https://www.whitehouse.gov/news/page/193/', 'https://www.whitehouse.gov/news/page/194/', 'https://www.whitehouse.gov/news/page/195/', 'https://www.whitehouse.gov/news/page/196/', 'https://www.whitehouse.gov/news/page/197/', 'https://www.whitehouse.gov/news/page/198/', 'https://www.whitehouse.gov/news/page/199/', 'https://www.whitehouse.gov/news/page/200/', 'https://www.whitehouse.gov/news/page/201/', 'https://www.whitehouse.gov/news/page/202/', 'https://www.whitehouse.gov/news/page/203/', 'https://www.whitehouse.gov/news/page/204/', 'https://www.whitehouse.gov/news/page/205/', 'https://www.whitehouse.gov/news/page/206/', 'https://www.whitehouse.gov/news/page/207/', 'https://www.whitehouse.gov/news/page/208/', 'https://www.whitehouse.gov/news/page/209/', 'https://www.whitehouse.gov/news/page/210/', 'https://www.whitehouse.gov/news/page/211/', 'https://www.whitehouse.gov/news/page/212/', 'https://www.whitehouse.gov/news/page/213/', 'https://www.whitehouse.gov/news/page/214/', 'https://www.whitehouse.gov/news/page/215/', 'https://www.whitehouse.gov/news/page/216/', 'https://www.whitehouse.gov/news/page/217/', 'https://www.whitehouse.gov/news/page/218/', 'https://www.whitehouse.gov/news/page/219/', 'https://www.whitehouse.gov/news/page/220/', 'https://www.whitehouse.gov/news/page/221/', 'https://www.whitehouse.gov/news/page/222/', 'https://www.whitehouse.gov/news/page/223/', 'https://www.whitehouse.gov/news/page/224/', 'https://www.whitehouse.gov/news/page/225/', 'https://www.whitehouse.gov/news/page/226/', 'https://www.whitehouse.gov/news/page/227/', 'https://www.whitehouse.gov/news/page/228/', 'https://www.whitehouse.gov/news/page/229/', 'https://www.whitehouse.gov/news/page/230/', 'https://www.whitehouse.gov/news/page/231/', 'https://www.whitehouse.gov/news/page/232/', 'https://www.whitehouse.gov/news/page/233/', 'https://www.whitehouse.gov/news/page/234/', 'https://www.whitehouse.gov/news/page/235/', 'https://www.whitehouse.gov/news/page/236/', 'https://www.whitehouse.gov/news/page/237/', 'https://www.whitehouse.gov/news/page/238/', 'https://www.whitehouse.gov/news/page/239/', 'https://www.whitehouse.gov/news/page/240/', 'https://www.whitehouse.gov/news/page/241/', 'https://www.whitehouse.gov/news/page/242/', 'https://www.whitehouse.gov/news/page/243/', 'https://www.whitehouse.gov/news/page/244/', 'https://www.whitehouse.gov/news/page/245/', 'https://www.whitehouse.gov/news/page/246/', 'https://www.whitehouse.gov/news/page/247/', 'https://www.whitehouse.gov/news/page/248/', 'https://www.whitehouse.gov/news/page/249/', 'https://www.whitehouse.gov/news/page/250/', 'https://www.whitehouse.gov/news/page/251/', 'https://www.whitehouse.gov/news/page/252/', 'https://www.whitehouse.gov/news/page/253/', 'https://www.whitehouse.gov/news/page/254/', 'https://www.whitehouse.gov/news/page/255/', 'https://www.whitehouse.gov/news/page/256/', 'https://www.whitehouse.gov/news/page/257/', 'https://www.whitehouse.gov/news/page/258/', 'https://www.whitehouse.gov/news/page/259/', 'https://www.whitehouse.gov/news/page/260/', 'https://www.whitehouse.gov/news/page/261/', 'https://www.whitehouse.gov/news/page/262/', 'https://www.whitehouse.gov/news/page/263/', 'https://www.whitehouse.gov/news/page/264/', 'https://www.whitehouse.gov/news/page/265/', 'https://www.whitehouse.gov/news/page/266/', 'https://www.whitehouse.gov/news/page/267/', 'https://www.whitehouse.gov/news/page/268/', 'https://www.whitehouse.gov/news/page/269/', 'https://www.whitehouse.gov/news/page/270/', 'https://www.whitehouse.gov/news/page/271/', 'https://www.whitehouse.gov/news/page/272/', 'https://www.whitehouse.gov/news/page/273/', 'https://www.whitehouse.gov/news/page/274/', 'https://www.whitehouse.gov/news/page/275/', 'https://www.whitehouse.gov/news/page/276/', 'https://www.whitehouse.gov/news/page/277/', 'https://www.whitehouse.gov/news/page/278/', 'https://www.whitehouse.gov/news/page/279/', 'https://www.whitehouse.gov/news/page/280/', 'https://www.whitehouse.gov/news/page/281/', 'https://www.whitehouse.gov/news/page/282/', 'https://www.whitehouse.gov/news/page/283/', 'https://www.whitehouse.gov/news/page/284/', 'https://www.whitehouse.gov/news/page/285/', 'https://www.whitehouse.gov/news/page/286/', 'https://www.whitehouse.gov/news/page/287/', 'https://www.whitehouse.gov/news/page/288/', 'https://www.whitehouse.gov/news/page/289/', 'https://www.whitehouse.gov/news/page/290/', 'https://www.whitehouse.gov/news/page/291/', 'https://www.whitehouse.gov/news/page/292/', 'https://www.whitehouse.gov/news/page/293/', 'https://www.whitehouse.gov/news/page/294/', 'https://www.whitehouse.gov/news/page/295/', 'https://www.whitehouse.gov/news/page/296/', 'https://www.whitehouse.gov/news/page/297/', 'https://www.whitehouse.gov/news/page/298/', 'https://www.whitehouse.gov/news/page/299/', 'https://www.whitehouse.gov/news/page/300/', 'https://www.whitehouse.gov/news/page/301/', 'https://www.whitehouse.gov/news/page/302/', 'https://www.whitehouse.gov/news/page/303/', 'https://www.whitehouse.gov/news/page/304/', 'https://www.whitehouse.gov/news/page/305/', 'https://www.whitehouse.gov/news/page/306/', 'https://www.whitehouse.gov/news/page/307/', 'https://www.whitehouse.gov/news/page/308/', 'https://www.whitehouse.gov/news/page/309/', 'https://www.whitehouse.gov/news/page/310/', 'https://www.whitehouse.gov/news/page/311/', 'https://www.whitehouse.gov/news/page/312/', 'https://www.whitehouse.gov/news/page/313/', 'https://www.whitehouse.gov/news/page/314/', 'https://www.whitehouse.gov/news/page/315/', 'https://www.whitehouse.gov/news/page/316/', 'https://www.whitehouse.gov/news/page/317/', 'https://www.whitehouse.gov/news/page/318/', 'https://www.whitehouse.gov/news/page/319/', 'https://www.whitehouse.gov/news/page/320/', 'https://www.whitehouse.gov/news/page/321/', 'https://www.whitehouse.gov/news/page/322/', 'https://www.whitehouse.gov/news/page/323/', 'https://www.whitehouse.gov/news/page/324/', 'https://www.whitehouse.gov/news/page/325/', 'https://www.whitehouse.gov/news/page/326/', 'https://www.whitehouse.gov/news/page/327/', 'https://www.whitehouse.gov/news/page/328/', 'https://www.whitehouse.gov/news/page/329/', 'https://www.whitehouse.gov/news/page/330/', 'https://www.whitehouse.gov/news/page/331/', 'https://www.whitehouse.gov/news/page/332/', 'https://www.whitehouse.gov/news/page/333/', 'https://www.whitehouse.gov/news/page/334/', 'https://www.whitehouse.gov/news/page/335/', 'https://www.whitehouse.gov/news/page/336/', 'https://www.whitehouse.gov/news/page/337/', 'https://www.whitehouse.gov/news/page/338/', 'https://www.whitehouse.gov/news/page/339/', 'https://www.whitehouse.gov/news/page/340/', 'https://www.whitehouse.gov/news/page/341/', 'https://www.whitehouse.gov/news/page/342/', 'https://www.whitehouse.gov/news/page/343/', 'https://www.whitehouse.gov/news/page/344/', 'https://www.whitehouse.gov/news/page/345/', 'https://www.whitehouse.gov/news/page/346/', 'https://www.whitehouse.gov/news/page/347/', 'https://www.whitehouse.gov/news/page/348/', 'https://www.whitehouse.gov/news/page/349/', 'https://www.whitehouse.gov/news/page/350/', 'https://www.whitehouse.gov/news/page/351/', 'https://www.whitehouse.gov/news/page/352/', 'https://www.whitehouse.gov/news/page/353/', 'https://www.whitehouse.gov/news/page/354/', 'https://www.whitehouse.gov/news/page/355/', 'https://www.whitehouse.gov/news/page/356/', 'https://www.whitehouse.gov/news/page/357/', 'https://www.whitehouse.gov/news/page/358/', 'https://www.whitehouse.gov/news/page/359/', 'https://www.whitehouse.gov/news/page/360/', 'https://www.whitehouse.gov/news/page/361/', 'https://www.whitehouse.gov/news/page/362/', 'https://www.whitehouse.gov/news/page/363/', 'https://www.whitehouse.gov/news/page/364/', 'https://www.whitehouse.gov/news/page/365/', 'https://www.whitehouse.gov/news/page/366/', 'https://www.whitehouse.gov/news/page/367/', 'https://www.whitehouse.gov/news/page/368/', 'https://www.whitehouse.gov/news/page/369/', 'https://www.whitehouse.gov/news/page/370/', 'https://www.whitehouse.gov/news/page/371/', 'https://www.whitehouse.gov/news/page/372/', 'https://www.whitehouse.gov/news/page/373/', 'https://www.whitehouse.gov/news/page/374/', 'https://www.whitehouse.gov/news/page/375/', 'https://www.whitehouse.gov/news/page/376/', 'https://www.whitehouse.gov/news/page/377/', 'https://www.whitehouse.gov/news/page/378/', 'https://www.whitehouse.gov/news/page/379/', 'https://www.whitehouse.gov/news/page/380/', 'https://www.whitehouse.gov/news/page/381/', 'https://www.whitehouse.gov/news/page/382/', 'https://www.whitehouse.gov/news/page/383/', 'https://www.whitehouse.gov/news/page/384/', 'https://www.whitehouse.gov/news/page/385/', 'https://www.whitehouse.gov/news/page/386/', 'https://www.whitehouse.gov/news/page/387/', 'https://www.whitehouse.gov/news/page/388/', 'https://www.whitehouse.gov/news/page/389/', 'https://www.whitehouse.gov/news/page/390/', 'https://www.whitehouse.gov/news/page/391/', 'https://www.whitehouse.gov/news/page/392/', 'https://www.whitehouse.gov/news/page/393/', 'https://www.whitehouse.gov/news/page/394/', 'https://www.whitehouse.gov/news/page/395/', 'https://www.whitehouse.gov/news/page/396/', 'https://www.whitehouse.gov/news/page/397/', 'https://www.whitehouse.gov/news/page/398/', 'https://www.whitehouse.gov/news/page/399/', 'https://www.whitehouse.gov/news/page/400/', 'https://www.whitehouse.gov/news/page/401/', 'https://www.whitehouse.gov/news/page/402/', 'https://www.whitehouse.gov/news/page/403/', 'https://www.whitehouse.gov/news/page/404/', 'https://www.whitehouse.gov/news/page/405/', 'https://www.whitehouse.gov/news/page/406/', 'https://www.whitehouse.gov/news/page/407/', 'https://www.whitehouse.gov/news/page/408/', 'https://www.whitehouse.gov/news/page/409/', 'https://www.whitehouse.gov/news/page/410/', 'https://www.whitehouse.gov/news/page/411/', 'https://www.whitehouse.gov/news/page/412/', 'https://www.whitehouse.gov/news/page/413/', 'https://www.whitehouse.gov/news/page/414/', 'https://www.whitehouse.gov/news/page/415/', 'https://www.whitehouse.gov/news/page/416/', 'https://www.whitehouse.gov/news/page/417/', 'https://www.whitehouse.gov/news/page/418/', 'https://www.whitehouse.gov/news/page/419/', 'https://www.whitehouse.gov/news/page/420/', 'https://www.whitehouse.gov/news/page/421/', 'https://www.whitehouse.gov/news/page/422/', 'https://www.whitehouse.gov/news/page/423/', 'https://www.whitehouse.gov/news/page/424/', 'https://www.whitehouse.gov/news/page/425/', 'https://www.whitehouse.gov/news/page/426/', 'https://www.whitehouse.gov/news/page/427/', 'https://www.whitehouse.gov/news/page/428/', 'https://www.whitehouse.gov/news/page/429/']
    url = page_list[i]
    print(f'------------------------{str(i)}-----------------------')
    s = requests.session()
    page = s.get(url).text
    soup = BeautifulSoup(page,'lxml')
    f = open(f'link/{str(i)}.txt', 'w')
    try:
        for i in range(1,11):
            links = soup.select(
                f'#main-content > div.page-results > div > article:nth-of-type({str(i)}) > div > h2 > a'
            )[0].get("href")

            f.write(links+'\n')
            print(f'{str(i)}成功----------')
            f.close()
    except IndexError:
    	pass

page_ten_link(428)
#获取所有链接
# for i in range(0,429):
#     page_ten_link(i)

# 整理所有链接到all_link.txt
# f0 = open('all_link.txt','w')
# for i in range(0,429):
#     f = open('link/{}.txt'.format(i),'r')
#     f0.write(f.read())
#     f.close()
# f0.close()

f0 = open('all_link.txt','r')
lines = eval(str(f0.readlines()).replace('\\n',''))
print(lines)



def get_html_and_txt(url,i):
    r = requests.get(url)
    content = r.text
    soup=BeautifulSoup(content,"lxml")
    if author_p := soup.find("p", attrs={"class": "author__name"}):
        author = author_p.get_text()
    else:
        author = ""
    try:
        type1 = soup.select('#main-content > div.page-header.page-header--small-title > div > p ')[0].get_text()
        type0 = type1.replace('				','').replace('			','')
    except IndexError:
        type0 = 'no type'
    try:
        date = soup.select('#main-content > div.page-header.page-header--small-title > div > div > p > time ')[0].get_text()
    except IndexError:
        date = 'no data'

    htmlname=url.split("/")[-2]
    a_dict = {
        "File_Name": htmlname,
        "TYPE": type0,
        "Title": htmlname.replace('-', ' '),
    }

    a_dict["Title_Url"] = url
    a_dict["Date"] = date
    a_dict["Author"] = author

    # -----------------------
    html_file = f"{htmlname}.html"
    html_path=os.path.join(HTML_DIR,html_file)
    with open(html_path,"w",encoding='utf-8') as f:
        f.write(content)
        f.close()
    with open(f'content_txt/{str(i)}.txt', 'w') as f1:
        f1.write(str(a_dict))


for i in range(4287):
    url = lines[i]
    get_html_and_txt(url,i)
    print(f'{str(i)}----------------------成功')

# get_html_and_txt('https://www.whitehouse.gov/briefings-statements/business-insider-us-economic-growth-2nd-quarter-gets-revised-higher-remains-strongest-since-2014/')

