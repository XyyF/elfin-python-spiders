#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import os
url = "http://tc.sinaimg.cn/maxwidth.800/tc.service.weibo.com/p3_pstatp_com/6da229b421faf86ca9ba406190b6f06e.jpg"
root = "./"
path = root + url.split('/')[-1]
if not os.path.exists(root):
    os.mkdir(root)
if not os.path.exists(path):
    r = requests.get(url)
    with open(path, 'wb') as f:
        f.write(r.content)
        f.close()
        print("文件保存成功")
else :
    print("文件已存在")