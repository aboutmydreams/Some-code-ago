import requests,pytesseract
from io import BytesIO
import time,json,re
from PIL import Image
from bs4 import BeautifulSoup
# qwe = 1234
# aa = 'qwe'
# cc = eval(aa)
# print(cc)
#
# print(str(cc)+'hhh%s,,,'%aa)

def test(i):
    n = 1
    r = 0
    bd_session = requests.Session()
    url = 'http://passport2.chaoxing.com/num/code?'
    while n is not i:
        try:
            what = bd_session.get(url)
            img = Image.open(BytesIO(what.content))
            text=pytesseract.image_to_string(img)
            text=text.replace('o','0')
            text=text.replace('O','0')
            text=text.replace('Q','0')
            text=text.replace(' ','')
            text=text.replace('l','1')
            text=text.replace('s','8')
            text=text.replace('!','1')
            text=text.replace('i','1')
            text = re.sub("\D", "", text)#只保留数字
            print(text)
            int(text)
            n+=1
            if len(text) == 4:
                r+=1
            print(n)
        except ValueError:
            pass
            n+=1
            print('--',n)
            #img.show()
        except Exception as e:
            raise e
            #img.show()
            #unexpected EOF while parsing 没有验证函数参数是否有效
    print('准确率小于：',r/i)
test(100)