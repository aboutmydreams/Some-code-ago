# coding:utf-8
import requests
url = 'http://120.26.6.172/get.php?source={}%20&param1=0&param2=1&json=1'.format('北京大学很大中国人民解放军但是的速度啊大大ad啊非官方地方')
response = requests.get(url)
response_list = eval(response.text)
better_key_list = []
for i,key in enumerate(response_list):
    test_list = []
    if i < 2:
        test_list.append(response_list[i+1])
        test_list.append(response_list[i+2])
    elif i == len(response_list)-2:
        test_list.append(response_list[i-1])
        test_list.append(response_list[i-2])
        test_list.append(response_list[i+1])
    elif i == len(response_list)-1:
        test_list.append(response_list[i-1])
        test_list.append(response_list[i-2])
    else:
        test_list.append(response_list[i-1])
        test_list.append(response_list[i-2])
        test_list.append(response_list[i+1])
        test_list.append(response_list[i+2])
    old_time = 0
    for i in test_list:
        near_key = i['t']
        if near_key.find(key['t'])!= -1:
            old_time = old_time + 1
        else:
            pass
    if old_time is 0:
        better_key_list.append(key)

print(better_key_list)