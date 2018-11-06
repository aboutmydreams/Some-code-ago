import urllib.request
url = "http://210.35.251.243/reader/redr_verify.php"
response = urllib.request.urlopen(url)
print(response.info())
print(type(response.info()))
aa = input('m')
print(aa)