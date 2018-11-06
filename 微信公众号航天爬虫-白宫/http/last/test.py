#! -*- encoding:utf-8 -*-
import requests,re,json,time
f = open('wx-res.txt','r')
print (eval(str(f.readlines()).replace('\\n','')))