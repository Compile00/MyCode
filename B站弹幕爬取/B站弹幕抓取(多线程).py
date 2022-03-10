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



def get_cid(bv):
    bv = bv.strip('BV1')
    url = f'https://api.bilibili.com/x/player/pagelist?bvid={bv}&jsonp=jsonp'
    res = requests.get(url)
    res_text = res.text
    res_dict = json.loads(res_text)
    cid = res_dict['data'][0]['cid']
    return cid


def Grab_barrage(date):
    # 伪装请求头
    headers = {
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "origin": "https://www.bilibili.com",
        # "referer": "https://www.bilibili.com/video/BV1Z5411Y7or?from=search&seid=8575656932289970537",
        "referer": f"https://www.bilibili.com/video/{bv}?t=441",
        #"cookie": "_uuid=0EBFC9C8-19C3-66CC-4C2B-6A5D8003261093748infoc; buvid3=4169BA78-DEBD-44E2-9780-B790212CCE76155837infoc; sid=ae7q4ujj; DedeUserID=501048197; DedeUserID__ckMd5=1d04317f8f8f1021; SESSDATA=e05321c1%2C1607514515%2C52633*61; bili_jct=98edef7bf9e5f2af6fb39b7f5140474a; CURRENT_FNVAL=16; rpdid=|(JJmlY|YukR0J'ulmumY~u~m; LIVE_BUVID=AUTO4315952457375679; CURRENT_QUALITY=80; bp_video_offset_501048197=417696779406748720; bp_t_offset_501048197=417696779406748720; PVID=2",
        "user-agent": random.choice(user_agent),
    }


    # 构造url访问   需要用到的参数
    params = {
        'type': 1,
        # 'oid': '128777652',
        # 'oid': cid,
        'oid': get_cid(bv),
        'date': date,
    }
    # 发送请求  获取响应
    response = requests.get(url, params=params, headers=headers)
    # print(response.encoding)   重新设置编码
    response.encoding = 'utf-8'
    # print(response.text)
    # 正则匹配提取数据
    comment = re.findall('<d p=".*?">(.*?)</d>', response.text)
    # 将每条弹幕数据写入txt
    with open('barrages.txt', 'a+', encoding='utf-8') as f:
        for con in comment:
            f.write(con + '\n')
    time.sleep(random.randint(1, 3))  # 休眠
    print("保存成功！文件已保存到当前工作目录下。")


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
    bv = 'BV1CP4y147NU'
    start = '20210720'
    end = '20210724'
    # 生成时间序列
    date_list = [x for x in pd.date_range(start, end).strftime('%Y-%m-%d')]
    count = 0
    # 调用主函数
    main()


# with open('barrages.txt') as f:
#     data = f.readlines()
#     print(f'弹幕数据：{len(data)}条')