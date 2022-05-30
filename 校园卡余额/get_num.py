'''
目标：爬到所有数据且不封号，建立数据库，可以随时查询：输入学号或名字（人性化）
解决思路：1、伪装成一个普通用户，几秒查询一次，随后间隔时间发生细微变化，将
2、代理
3、用好多个账号
方案顺序：先写好一条可以爬到简化数据的，
（再写能够input的，学习框架）
'''
import requests,random
from bs4 import BeautifulSoup
import time
import life_coki
a = [1]

def get_count(a):#http://life.ccb.com/tran/WCCMainPlatV5?CCB_IBSVersion=V5&SERVLET_NAME=WCCMainPlatV5&isAjaxRequest=true&TXCODE=NYS101&CHOOSETYPE=1&REGION_CODE=360000&BILL_ITEM=05013
    url = 'http://life.ccb.com/tran/WCCMainPlatV5?CCB_IBSVersion=V5&SERVLET_NAME=WCCMainPlatV5'
    the_coki = life_coki.get_coki(1)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Length': '1114',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'life.ccb.com',
        'Origin': 'http://life.ccb.com',
        'Referer': 'http://life.ccb.com/tran/WCCMainB1L1?CCB_IBSVersion=V5&SERVLET_NAME=WCCMainB1L1',
        'Upgrade-Insecure-Requests': '1',
        'Cookie': f'{the_coki}',
    }

    data = {
        'BANK_COD': '360000',
        'BUTTON_IMG': '',
        'BUTTON_URL': '',
        'OPUN_COD': '360100',
        'MERCHANT': '05013|南昌大学|1740|0|请输入校园卡卡号|校园卡卡号||0|||0||360000000|||||1011111111|100010|11||',
        'SJ_CONTENT': '',
        'COMM': f'{a}',
        'Py_Mod': '',
        'SEQUENCE_CODE': '',
        'RE1CON': '',
        'RE2CON': '',
        'BUTTON_IMG': '',
        'BUTTON_URL': '',
        'SEQUENCE_NAME': '请选择',
        'REMARK1': '',
        'REMARK2': '',
        'PAGE1': '',
        'PAGE2': '',
        'TYPE1': '0',
        'DETAIL_FLAG': f'{a}',
        'TYPE2': '0',
        'BILL_NAME': '校园卡卡号',
        'BILL_COMM': '请输入校园卡卡号',
        'BILL_FLAG': '0',
        'TXCODE': 'NYS10A',
        'BILL_ITEM': '05013',
        'OPUN_NAME': '南昌市',
        'BANK_NAME': '江西省',
        'BIll_MERCHANT': '1740',
        'MERCHANT_NAME': '南昌大学',
        'AMT_FLAG': '1',
        'CUST_FALG': '',
        'BIll_CODE': '100010',
        'BILL_TYPE': '500',
        'BRAN_NO': '360000000',
        'PAY_TYPE': '11',
        'CTPPARAM': '',
        'BEGIN_TIME': '',
        'END_TIME': '',
        'HOLIDAY_BEGIN_TIME': '',
        'HOLIDAY_END_TIME': '',
        'history_0': '',
        'history_1': '',
        'history_2': '',
        'history_3': '',
        'history_4': '',
        'history_5': '',
        'history_6': '',
        'history_7': '',
        'history_8': '',
        'history_9': '',
    }

    response = requests.post(url,headers=headers,data=data)

    soup = BeautifulSoup(response.text,'lxml')
    name = soup.select('#jhform > div.form_box > table > tbody > tr:nth-of-type(4) > th:nth-of-type(1)')
    remaining_sum = soup.select('#jhform > div.form_box > table > tbody > tr:nth-of-type(4) > td:nth-of-type(1)')
    name0=str(name)
    if name1 := name0[5:-6]:
        remaining_sum0=str(remaining_sum)#字符串化 重要！！！
        remaining_sum1=remaining_sum0[5:-6]
        print(name1,remaining_sum1)
    else:
        textlong = len(response.text)
        #print(type(textlong))
        if textlong == 5832:
            print('不在查询时间内,或空号（没来报道 退学...）')
        else:
            print('存在某些问题，例如cookie过期',len(response.text))

    #print(type(remaining_sum0))#查看数据类型
    #print(response.status_code)
    #print(response.cookies)#有用
for i in range(5004118061,5004118062):
    time.sleep(random.randint(1,2))
    try:
        a.append(str(i))
        time.sleep(1)
        get_count(a[-1])

    except SyntaxError:
        raise
    except Exception as e:
        raise e
    # else:
    #     pass
    #     print('Flase')
    