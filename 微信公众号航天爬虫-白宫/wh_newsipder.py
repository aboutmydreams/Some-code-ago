import os
import requests
from bs4 import BeautifulSoup

HTML_DIR = "html"
TXT_PATH="whg_news.txt"
TYPEDIC={
    "presidential-action":"PRESIDENTIAL ACTIONS",
    "briefing-statement":"BRIEFINGS & STATEMENTS",
    "article":"ARTICLES"
}


def get_HTML_Text(url,code="utf-8"):
    r=requests.get(url)
    r.raise_for_status()
    r.encoding=code
    return r.text
aa = get_HTML_Text("https://www.whitehouse.gov/news/")
print(type(aa))



#输入html，生成字典再写入txt
def get_news(html):
    soup=BeautifulSoup(html,"html.parser")
    page_results_wrap=soup.find("div",attrs={"class":"page-results__wrap"})
    print(page_results_wrap)
    articles=page_results_wrap.find_all("article")
    for a in articles:
        a_dict={}
        a_type=a["class"][0]
        title_class=a_type+"__title"
        title_h=a.find("h2",attrs={"class":title_class})
        title_a=title_h.find("a")

        href=title_a.attrs["href"]
        title=title_a.get_text()

        a_time=a.find("time").get_text()

        a_dict["TYPE"]=TYPEDIC.get(a_type)
        a_dict["Title"] = title
        a_dict["Title_Url"] = href
        a_dict["Date"] = a_time

        a_html=get_HTML_Text(href)
        a_dict["Author"] = get_author(a_html).strip()

        htmlname=href.split("/")[-2]
        a_dict["File_Name"] = htmlname

        # -----------------------
        write_html(a_html,htmlname)
        add_news_to_txt(a_dict)


def get_author(html):
    soup=BeautifulSoup(html,"html.parser")
    author_p=soup.find("p",attrs={"class":"author__name"})
    if author_p:
        return author_p.get_text()
    else:
        return ""


def write_html(html,name):
    html_file=name+".html"
    html_path=os.path.join(HTML_DIR,html_file)
    with open(html_path,"w",encoding='utf-8') as f:
        f.write(html)


def start_up():
    if not os.path.exists(HTML_DIR):
        os.mkdir(HTML_DIR)

    with open(TXT_PATH,"w",encoding='utf-8') as f:
        pass


def add_news_to_txt(newsdic):
    with open(TXT_PATH, "a",encoding='utf-8') as f:
        for k in ["TYPE","Title","Title_Url","Date","Author","File_Name"]:
            f.write("[%s]: %s"%(k,newsdic[k]))
            f.write("\n")
        f.write("\n")


def get_pages_num(html):
    soup=BeautifulSoup(html,"html.parser")
    pagination=soup.find("div",attrs={"class":"pagination"})
    if pagination is None:
        return 10000
    pages=pagination.find_all("a",attrs={"class":"page-numbers"})
    max_page=2
    for page in pages:
        page_num=page.get_text()
        try:
            page_int=int(page_num)
            if page_int>max_page:
                max_page=page_int
        except Exception:
            pass
        # print(max_page)
    return max_page



def main():
    start_up()
    url="https://www.whitehouse.gov/news/"
    html=get_HTML_Text(url)
    get_news(html)
    pagenum=get_pages_num(html)
    # print(pagenum)
    n = 0
    for page in range(pagenum):
        n = n+1
        print(n)
        page_url=url+"page/%s/"%page
        try:
            page_html=get_HTML_Text(page_url)
        except Exception:
            break

        get_news(page_html)
        # if page>3:
        #     break

main()
# if __name__=="__main__":
#     main()
