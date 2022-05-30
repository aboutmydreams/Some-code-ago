import requests
from bs4 import BeautifulSoup
import time
import json
def get_coki(a,coki=None):#http://life.ccb.com/tran/WCCMainPlatV5?CCB_IBSVersion=V5&SERVLET_NAME=WCCMainPlatV5&isAjaxRequest=true&TXCODE=NYS101&CHOOSETYPE=1&REGION_CODE=360000&BILL_ITEM=05013
    url0 = 'http://www.ccb.com/tran/WCCMainPlatV5?CCB_IBSVersion=V5&SERVLET_NAME=WCCMainPlatV5&isAjaxRequest=true&TXCODE=NBQ001&Cookie_Id=f5ec1fe62cbcde9eYsVQFPplJWXMOG41ZbPV1523976805575iY7L1EOQT8IHeM5SUJiI074c8b4e5716132013953ebb3a9787b5&Usr_Id=&_=1523976801480'
    headers0 = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'Cookie': 'ccbdatard=1; cityName=%E5%8D%97%E6%98%8C%E5%B8%82; cityCode=360100; bankName=%E6%B1%9F%E8%A5%BF%E7%9C%81%E5%88%86%E8%A1%8C; bankCode=360000000; cityCodeFlag=0; cityCodeCustId=; billcitycode=360100; BIGipServerccvcc_jt_197.1_80_web_pool=1310917386.20480.0000; ccbsessionid=c8YU1VebwF1vEWC3eddcac01079-20180417202402; ticket=; cs_cid=; custName=; userType=; lastLoginTime=;',
        'Host': 'life.ccb.com',
        'Origin': 'http://life.ccb.com',
        'Pragma': 'no-cache',
        'Referer': 'http://life.ccb.com/tran/WCCMainB1L1?CCB_IBSVersion=V5&SERVLET_NAME=WCCMainB1L1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3386.1 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
        }
    response0 = requests.post(url0,headers=headers0)
    #print(requests.utils.dict_from_cookiejar(response0.cookies))
    tranCC = requests.utils.dict_from_cookiejar(response0.cookies)
    url = 'http://life.ccb.com/tran/WCCMainPlatV5?CCB_IBSVersion=V5&SERVLET_NAME=WCCMainPlatV5'
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
        'Cookie': f'{coki}',
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

    bd_session = requests.Session()
    what = bd_session.post(url,headers=headers,data=data)
    #print(type(what.cookies))
    cookii = requests.utils.dict_from_cookiejar(what.cookies)
    #print(cookii)
    #print(real_cookii)
    return str(
        'WCCTC='
        + str(cookii['WCCTC'])
        + '; tranCCBIBS1='
        + str(tranCC['tranCCBIBS1'])
        + '; ccbcustomid=dfb0525b50673a81cCq2SQCw86heIkM43Ctj1518080032515NfpKjxfBIyspYangTXhY747f853056f4e1dd6231aee0b06042ca; ccbdatard=1; cityName=%E5%8D%97%E6%98%8C%E5%B8%82; cityCode=360100; bankName=%E6%B1%9F%E8%A5%BF%E7%9C%81%E5%88%86%E8%A1%8C; bankCode=360000000; cityCodeFlag=0; cityCodeCustId=; billcitycode=360100; BIGipServerccvcc_jt_197.1_80_web_pool='
        + str(cookii['BIGipServerccvcc_jt_197.1_80_web_pool'])
        + '; ticket=; cs_cid=; custName=; userType=; lastLoginTime=; JSESSIONID='
        + str(cookii['JSESSIONID'])
        + '; INFO='
        + str(cookii['INFO'])
        + '; tranFAVOR='
        + str(cookii['tranFAVOR'])
    )
    # response = requests.post(url,headers=headers,data=data)
    # print(type(response.cookies))
    # print(requests.utils.dict_from_cookiejar(response.cookies))

# get_coki(5004118061)
#WCCTC=808713738_1457861684_373481128; tranCCBIBS1=FnBonIHgYz5qvxqmQRfrjhtzEsh0EzPqOPSqWh5qMPHrIxHmaUK0NxMznNSxTR2ieTDqWBCqyXarWREiPXAqfBZqIWJrTBl%2CTdYh3PM7rj; ccbcustomid=dfb0525b50673a81cCq2SQCw86heIkM43Ctj1518080032515NfpKjxfBIyspYangTXhY747f853056f4e1dd6231aee0b06042ca; ccbdatard=1; cityName=%E5%8D%97%E6%98%8C%E5%B8%82; cityCode=360100; bankName=%E6%B1%9F%E8%A5%BF%E7%9C%81%E5%88%86%E8%A1%8C; bankCode=360000000; cityCodeFlag=0; cityCodeCustId=; billcitycode=360100; BIGipServerccvcc_jt_197.1_80_web_pool=1310917386.20480.0000; ccbsessionid=c8YU1VebwF1vEWC3eddcac01079-20180417202402; ticket=; cs_cid=; custName=; userType=; lastLoginTime=; JSESSIONID=ZZ7TzgtnOS6vIyHA-wViG5OSrqC0Lhdnqq1VATlLM93rlMbR-8OA!-186547456; INFO=9a9v|WtX3V; tranFAVOR=TbtVoeusn9YyEaBEaPMydakEOPxyGa%2CEAPNyVaWEBP5y9aoE9Pyy2TfSuSc8DPTIfm
#WCCTC,tranCCBIBS1,ccbcustomid,ccbdatard=1; cityName=%E5%8D%97%E6%98%8C%E5%B8%82; cityCode=360100; bankName=%E6%B1%9F%E8%A5%BF%E7%9C%81%E5%88%86%E8%A1%8C; bankCode=360000000; cityCodeFlag=0; cityCodeCustId=; billcitycode=360100;ticket=; cs_cid=; custName=; userType=; lastLoginTime=; JSESSIONID,INFO,tranFAVOR