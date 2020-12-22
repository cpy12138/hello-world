#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx_sdk
import base64
import os
import sys
import re
#luvcview:open camera to vedio
# 图片像素尺寸：最小 30*30 像素，最大 4096*4096 像素
os.system("fswebcam -S 10 --no-banner -r 1080x800 image.jpg")
# 加载图片,将图片转换为Base64格式
with open('image.jpg','rb') as f:
    img_Base64 = base64.b64encode(f.read())
    img_Base64 = bytes.decode(img_Base64)
f.close()

# 参数赋值
url = 'https://aiapi.jd.com/jdai/garbageImageSearch'
bodyStr = '{    "cityId":"310000",  "imgBase64":"%s"}'%img_Base64
params = { 
    'type' : 'json',
    'content' : 'json string',
    'appkey' : '7e9ad0497bd9e353119ac73335cbb2bb',
    'secretkey':'f8be422d899c7623cf0818a696942e33',
}

true = True
false = False
response = wx_sdk.wx_post_req( url, params, bodyStr=bodyStr )
dic = eval(response.text)
# 将字典中的garbage_info取出
garbage_info = dic.get('result').get('garbage_info')
# 
#for i in garbage_info:
#    print(i['confidence'])
    
# 按垃圾概率从大到小排序
sort = sorted(garbage_info, key=lambda a : a['confidence'], reverse=True)
print(sort[0])
#print(dic)
    
