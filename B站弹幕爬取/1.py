# -*- coding: UTF-8 -*-
"""
@File    ：spider.py
@Author  ：叶庭云
@CSDN    ：https://yetingyun.blog.csdn.net/
"""

import requests
import pandas as pd
import re
import time
import random
from concurrent.futures import ThreadPoolExecutor
import datetime

user_agent = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]
start_time = datetime.datetime.now()


def Grab_barrage(date):
    # 伪装请求头
    headers = {
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "origin": "https://www.bilibili.com",
        "referer": "https://www.bilibili.com/video/BV1Z5411Y7or?from=search&seid=8575656932289970537",
        "cookie": "buvid3=3C5A16E9-CCEC-49E3-9B69-D0CF2397A02F190948infoc; LIVE_BUVID=AUTO8915753855285096; rpdid=|(k|k)Jl)~ml0J'ul~)~l|J)R; CURRENT_FNVAL=80; blackside_state=1; _uuid=A2EE9A4F-4EF6-6C33-ED0E-599278D162DD81730infoc; fingerprint=fcf3d937afd3029dd8f3de9b3fae0a0f; buvid_fp=3C5A16E9-CCEC-49E3-9B69-D0CF2397A02F190948infoc; buvid_fp_plain=584CF95A-D71F-46AC-AB8F-40675987A5D5167625infoc; SESSDATA=e1b951fc,1642692388,ad256*71; bili_jct=ed7db20b2c50215e424992a8444a517c; DedeUserID=631786590; DedeUserID__ckMd5=769954c685713849; sid=i7wjnkhw; bfe_id=1bad38f44e358ca77469025e0405c4a6; CURRENT_QUALITY=64",
        "user-agent": random.choice(user_agent),
    }
    # 构造url访问   需要用到的参数
    params = {
        'type': 1,
        'oid': '210462922',
        'date': date
    }
    # 发送请求  获取响应
    response = requests.get(url, params=params, headers=headers)
    # print(response.encoding)   重新设置编码
    response.encoding = 'utf-8'
    # print(response.text)
    # 正则匹配提取数据
    comment = re.findall('<d p=".*?">(.*?)</d>', response.text)
    # 将每条弹幕数据写入txt
    with open('barrages.txt', 'a+') as f:
        for con in comment:
            f.write(con + '\n')
    time.sleep(random.randint(1, 3))  # 休眠


def main():
    # 开多线程爬取   提高爬取效率
    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(Grab_barrage, date_list)
    # 计算所用时间
    delta = (datetime.datetime.now() - start_time).total_seconds()
    print(f'用时：{delta}s')


if __name__ == '__main__':
    # 目标url
    url = "https://api.bilibili.com/x/v2/dm/history"
    start = '20200101'
    end = '20200806'
    # 生成时间序列
    date_list = [x for x in pd.date_range(start, end).strftime('%Y-%m-%d')]
    count = 0
    # 调用主函数
    main()


with open('barrages.txt') as f:
    data = f.readlines()
    print(f'弹幕数据：{len(data)}条')