from bs4 import BeautifulSoup
import requests
import lxml
def what_titles(seachname):
	url = f'https://baike.baidu.com/item/{str(seachname)}'
	datao = {
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Accept-Encoding':'gzip, deflate, br',
	'Accept-Language':'zh-CN,zh;q=0.9',
	'Connection':'keep-alive',
	'Cookie':'BIDUPSID=5020404D7C66940BC964EBE921C86196; PSTM=1513171684; BDUSS=El-WDZuNjBlelpPaU83aWRqcnpuWFRFZDVFQ3oxeld3SkVmcFY5bEREOW9aSDVhQVFBQUFBJCQAAAAAAAAAAAEAAACZuCcLMDAzyP29o7~NAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGjXVlpo11ZaN; BAIDUID=2ACB8C6E67CD003A3F468487D9B72004:FG=1; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; H_PS_PSSID=; Hm_lvt_55b574651fcae74b0a9f1cf9c8d7c93a=1521796247,1522078863,1522196359,1522197720; pgv_pvi=4080627712; pgv_si=s4305604608; BK_SEARCHLOG=%7B%22key%22%3A%5B%22%E4%B9%8F%E5%96%84%E5%8F%AF%E9%99%88%22%5D%7D; Hm_lpvt_55b574651fcae74b0a9f1cf9c8d7c93a=1522199861; PSINO=7',
	'Host':'baike.baidu.com',
	'Upgrade-Insecure-Requests':'1',
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3298.4 Safari/537.36'
	}
	wb_data = requests.get(url,headers = datao,params=None,allow_redirects=False)
	soup = BeautifulSoup(wb_data.text,'lxml')
	titles = soup.select('body > div.body-wrapper > div.content-wrapper > div > div.main-content > div > h2')
	print(titles)
	#print(wb_data.text)
what_titles('%E7%8C%AA/147315')